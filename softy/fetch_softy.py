#!/usr/bin/env python3
"""Dane fundamentalne dla kawy (Arabica KC) i kakao (NY CC). Uruchamia go GitHub Actions (workflow „Softy”).

Środowisko Claude nie łączy się z CFTC, ICE, Open-Meteo ani Yahoo, więc wszystko pobiera się tutaj
i trafia do data/softy/. Każde źródło jest niezależne: gdy jedno padnie, reszta się zapisuje, a błąd
ląduje w data/softy/status.json. Poprzednie pliki zostają wtedy bez zmian.

Wynik (data/softy/):
  cot.csv              CFTC Disaggregated (futures only), tygodniowo: managed money, producenci, OI (ok. 4 lata)
  pogoda.json          regiony upraw: opad 30 dni wstecz i 16 dni prognozy vs norma 15 lat, Tmin/Tmax
  pogoda_norma.json    norma opadu i Tmin dla dnia roku (z archiwum Open-Meteo, odświeżana co 90 dni)
  krzywa.json          ceny kolejnych kontraktów (KCZ26, KCH27…), spread pierwszy-drugi w %
  fx_brl_1d.csv, fx_gbp_1d.csv, fx_eur_1d.csv   USD/BRL, GBP/USD, EUR/USD (rok, D1)
  coffee_dlugie_1d.csv, cocoa_dlugie_1d.csv     zamknięcia D1 od 2000 r. (sezonowość; odświeżane co tydzień)
  zapasy_ice.csv       zapasy certyfikowane ICE (worki kawy / tony kakao), dzień po dniu, gdy uda się pobrać raport
  ice/                 ostatnie surowe raporty ICE (.xls), do ręcznego wglądu
  status.json          czas przebiegu, błędy i co się udało

Użycie: python softy/fetch_softy.py [cot|pogoda|krzywa|fx|dlugie|ice ...]   (bez argumentów: wszystko)
"""
import csv
import datetime as dt
import io
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "softy")
UA = {"User-Agent": "Mozilla/5.0 claude-finance-data (softy)"}
NOW = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)

# Kody CFTC: Coffee C (ICE US) 083731, Cocoa (ICE US) 073732
COT_KODY = {"083731": "kawa", "073732": "kakao"}

# Regiony upraw: (klucz, opis, lat, lon, waga w indeksie towaru). Wagi ~ udział w podaży, która dziś rusza cenę.
REGIONY = {
    "kawa": [
        ("sul_de_minas", "Sul de Minas, MG (arabika)", -21.55, -45.43, 0.30),
        ("cerrado", "Cerrado Mineiro, MG (arabika)", -18.94, -46.99, 0.20),
        ("mogiana", "Mogiana, SP (arabika)", -20.54, -47.40, 0.15),
        ("espirito_santo", "Espírito Santo (konilon/robusta)", -19.39, -40.07, 0.15),
        ("wietnam", "Central Highlands, Wietnam (robusta)", 12.67, 108.04, 0.20),
    ],
    "kakao": [
        ("soubre", "Soubré, Wybrzeże Kości Słoniowej", 5.79, -6.61, 0.30),
        ("daloa", "Daloa, Wybrzeże Kości Słoniowej", 6.88, -6.45, 0.20),
        ("san_pedro", "San-Pédro, Wybrzeże Kości Słoniowej", 4.75, -6.64, 0.10),
        ("ashanti", "Ashanti, Ghana", 6.69, -1.62, 0.15),
        ("western_north", "Western North, Ghana", 6.21, -2.49, 0.10),
        ("los_rios", "Los Ríos, Ekwador", -1.80, -79.53, 0.15),
    ],
}
NORMA_LATA = 15
NORMA_WAZNA_DNI = 90

# Kontrakty: obie giełdy mają miesiące H K N U Z
MIESIACE = {3: "H", 5: "K", 7: "N", 9: "U", 12: "Z"}
KRZYWA = {"kawa": "KC", "kakao": "CC"}
FX = {"brl": "BRL=X", "gbp": "GBPUSD=X", "eur": "EURUSD=X"}
DLUGIE = {"coffee": "KC=F", "cocoa": "CC=F"}

# Raporty ICE z zapasami certyfikowanymi (publiczne .xls, publikowane po sesji)
ICE_URL = {
    "kawa": "https://www.ice.com/publicdocs/futures_us_reports/coffee/coffee_cert_stock_{d}.xls",
    "kakao": "https://www.ice.com/publicdocs/futures_us_reports/cocoa/cocoa_cert_stock_{d}.xls",
}

status = {"uruchomiono_utc": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"), "bledy": {}, "ok": {}}


def get(url, tries=3, timeout=40):
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
                return r.read()
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{type(last).__name__}: {last}")


def get_json(url, **kw):
    return json.loads(get(url, **kw))


def path(name):
    return os.path.join(OUT, name)


def file_age_days(name):
    p = path(name)
    if not os.path.exists(p):
        return None
    try:
        meta = json.load(open(p)) if name.endswith(".json") else None
        ts = meta.get("zaktualizowano_utc") if isinstance(meta, dict) else None
    except Exception:
        ts = None
    if ts:
        return (NOW - dt.datetime.fromisoformat(ts.replace("Z", "+00:00"))).days
    return (NOW.timestamp() - os.path.getmtime(p)) / 86400


def pick(row, *patterns):
    """Wartość z wiersza CFTC po wzorcu nazwy pola (nazwy różnią się między API a plikami zip)."""
    for pat in patterns:
        for k, v in row.items():
            if re.fullmatch(pat, k.strip().lower()):
                return v
    return None


def to_int(v):
    try:
        return int(float(str(v).replace(",", "").strip()))
    except Exception:
        return None


# ---------------------------------------------------------------- COT
def cot_rows_socrata():
    kody = ",".join(f"'{k}'" for k in COT_KODY)
    od = (NOW - dt.timedelta(days=4 * 366)).strftime("%Y-%m-%dT00:00:00")
    q = {"$where": f"cftc_contract_market_code in({kody}) AND report_date_as_yyyy_mm_dd >= '{od}'",
         "$order": "report_date_as_yyyy_mm_dd", "$limit": "5000"}
    url = "https://publicreporting.cftc.gov/resource/72hh-3qpy.json?" + urllib.parse.urlencode(q)
    return get_json(url)


def cot_rows_zip():
    rows = []
    for year in range(NOW.year - 4, NOW.year + 1):
        try:
            raw = get(f"https://www.cftc.gov/files/dea/history/fut_disagg_txt_{year}.zip", timeout=90)
        except Exception as e:
            status["bledy"][f"cot_zip_{year}"] = str(e)[:200]
            continue
        z = zipfile.ZipFile(io.BytesIO(raw))
        for name in z.namelist():
            text = z.read(name).decode("latin-1")
            for r in csv.DictReader(io.StringIO(text)):
                code = (pick(r, r"cftc_contract_market_code") or "").strip()
                if code in COT_KODY:
                    rows.append(r)
    return rows


def cot():
    try:
        rows, src = cot_rows_socrata(), "publicreporting.cftc.gov (72hh-3qpy)"
        if not rows:
            raise RuntimeError("pusta odpowiedź")
    except Exception as e:
        status["bledy"]["cot_api"] = str(e)[:200]
        rows, src = cot_rows_zip(), "cftc.gov fut_disagg_txt_<rok>.zip"
    out = {}
    for r in rows:
        code = (pick(r, r"cftc_contract_market_code") or "").strip()
        data = str(pick(r, r"report_date_as_yyyy_mm_dd", r"report_date_as_yyyy-mm-dd") or "")[:10]
        if code not in COT_KODY or not data:
            continue
        rec = {
            "data": data, "rynek": COT_KODY[code],
            "mm_long": to_int(pick(r, r"m_money_positions_long_all?")),
            "mm_short": to_int(pick(r, r"m_money_positions_short_all?")),
            "mm_spread": to_int(pick(r, r"m_money_positions_spread_all?", r"m_money_positions_spread")),
            "prod_long": to_int(pick(r, r"prod_merc_positions_long_all?", r"prod_merc_positions_long")),
            "prod_short": to_int(pick(r, r"prod_merc_positions_short_all?", r"prod_merc_positions_short")),
            "swap_long": to_int(pick(r, r"swap_positions_long_all?")),
            "swap_short": to_int(pick(r, r"swap__?positions_short_all?")),
            "oi": to_int(pick(r, r"open_interest_all")),
        }
        if rec["mm_long"] is None or rec["mm_short"] is None:
            continue
        rec["mm_net"] = rec["mm_long"] - rec["mm_short"]
        out[(rec["rynek"], data)] = rec
    if not out:
        raise RuntimeError("brak wierszy COT dla kawy i kakao")
    cols = ["data", "rynek", "mm_long", "mm_short", "mm_net", "mm_spread", "prod_long", "prod_short",
            "swap_long", "swap_short", "oi"]
    with open(path("cot.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for k in sorted(out, key=lambda k: (k[1], k[0])):
            w.writerow({c: out[k].get(c) for c in cols})
    ost = max(k[1] for k in out)
    return f"{len(out)} wierszy, ostatni raport {ost}, źródło {src}"


# ---------------------------------------------------------------- pogoda
def norma():
    """Średni opad i Tmin dla każdego dnia roku (okno ±15 dni) z archiwum Open-Meteo, osobno dla regionu."""
    age = file_age_days("pogoda_norma.json")
    if age is not None and age < NORMA_WAZNA_DNI:
        return json.load(open(path("pogoda_norma.json")))
    end = dt.date(NOW.year - 1, 12, 31)
    start = dt.date(end.year - NORMA_LATA + 1, 1, 1)
    res = {"zaktualizowano_utc": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"), "okres": f"{start}..{end}",
           "opis": "opad_mm[d] i tmin[d] = średnia z lat dla dnia roku d (1-366), wygładzona oknem ±15 dni",
           "regiony": {}}
    for towar, regs in REGIONY.items():
        for key, _, lat, lon, _ in regs:
            url = ("https://archive-api.open-meteo.com/v1/archive?" + urllib.parse.urlencode({
                "latitude": lat, "longitude": lon, "start_date": start.isoformat(), "end_date": end.isoformat(),
                "daily": "precipitation_sum,temperature_2m_min", "timezone": "UTC"}))
            d = get_json(url, timeout=120)["daily"]
            sums, tmins, cnt = [0.0] * 367, [0.0] * 367, [0] * 367
            for t, p, tn in zip(d["time"], d["precipitation_sum"], d["temperature_2m_min"]):
                if p is None or tn is None:
                    continue
                doy = dt.date.fromisoformat(t).timetuple().tm_yday
                sums[doy] += p
                tmins[doy] += tn
                cnt[doy] += 1
            raw_p = [sums[i] / cnt[i] if cnt[i] else None for i in range(367)]
            raw_t = [tmins[i] / cnt[i] if cnt[i] else None for i in range(367)]
            sm_p, sm_t = [None] * 367, [None] * 367
            for i in range(1, 367):
                win = [((i - 1 + o) % 366) + 1 for o in range(-15, 16)]
                vp = [raw_p[j] for j in win if raw_p[j] is not None]
                vt = [raw_t[j] for j in win if raw_t[j] is not None]
                sm_p[i] = round(sum(vp) / len(vp), 3) if vp else None
                sm_t[i] = round(sum(vt) / len(vt), 2) if vt else None
            res["regiony"][key] = {"opad_mm": sm_p, "tmin": sm_t}
            time.sleep(1)
    json.dump(res, open(path("pogoda_norma.json"), "w"))
    return res


def pogoda():
    nor = norma()["regiony"]
    res = {"zaktualizowano_utc": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "zrodlo": "Open-Meteo (prognoza: model best_match; norma: archiwum ERA5, 15 lat)", "towary": {}}
    today = NOW.date()
    for towar, regs in REGIONY.items():
        lst = []
        for key, opis, lat, lon, waga in regs:
            url = ("https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode({
                "latitude": lat, "longitude": lon, "past_days": 30, "forecast_days": 16, "timezone": "UTC",
                "daily": "precipitation_sum,temperature_2m_max,temperature_2m_min"}))
            d = get_json(url)["daily"]
            n = nor.get(key, {}).get("opad_mm") or [None] * 367
            past, fut, norm_past, norm_fut, tmin_f, tmax_f = 0.0, 0.0, 0.0, 0.0, [], []
            dni = []
            for t, p, tx, tn in zip(d["time"], d["precipitation_sum"], d["temperature_2m_max"], d["temperature_2m_min"]):
                day = dt.date.fromisoformat(t)
                nv = n[day.timetuple().tm_yday] or 0.0
                p = p or 0.0
                if day < today:
                    past += p
                    norm_past += nv
                else:
                    fut += p
                    norm_fut += nv
                    if tn is not None:
                        tmin_f.append(tn)
                    if tx is not None:
                        tmax_f.append(tx)
                dni.append({"d": t, "opad": round(p, 1), "tmax": tx, "tmin": tn})
            lst.append({
                "klucz": key, "opis": opis, "lat": lat, "lon": lon, "waga": waga,
                "opad_30d_mm": round(past, 1), "norma_30d_mm": round(norm_past, 1),
                "proc_normy_30d": round(100 * past / norm_past) if norm_past > 1 else None,
                "opad_prog_16d_mm": round(fut, 1), "norma_16d_mm": round(norm_fut, 1),
                "proc_normy_16d": round(100 * fut / norm_fut) if norm_fut > 1 else None,
                "tmin_prog_min": min(tmin_f) if tmin_f else None, "tmax_prog_max": max(tmax_f) if tmax_f else None,
                "dni": dni,
            })
            time.sleep(0.5)
        res["towary"][towar] = lst
    json.dump(res, open(path("pogoda.json"), "w"), ensure_ascii=False, indent=1)
    return f"{sum(len(v) for v in res['towary'].values())} regionów"


# ---------------------------------------------------------------- Yahoo: krzywa, FX, długie serie
def yf_hist(sym, **kw):
    import yfinance as yf
    last = None
    for _ in range(2):
        try:
            df = yf.Ticker(sym).history(auto_adjust=False, **kw)
            if df is not None and not df.empty:
                return df.dropna(subset=["Close"])
            last = "pusta odpowiedź"
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(3)
    raise RuntimeError(last)


def kontrakty(root, n=4):
    out, y, m = [], NOW.year, NOW.month
    while len(out) < n:
        m += 1
        if m > 12:
            m, y = 1, y + 1
        if m in MIESIACE:
            out.append((f"{root}{MIESIACE[m]}{str(y)[2:]}.NYB", f"{y}-{m:02d}"))
    # bieżący miesiąc też bywa jeszcze notowany (np. Z w grudniu przed wygaśnięciem)
    if NOW.month in MIESIACE:
        out.insert(0, (f"{root}{MIESIACE[NOW.month]}{str(NOW.year)[2:]}.NYB", f"{NOW.year}-{NOW.month:02d}"))
    return out


def krzywa():
    res = {"zaktualizowano_utc": NOW.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "opis": "spread_1_2_proc = (pierwszy/drugi - 1)*100; dodatni = backwardation (ciasny rynek bieżący)",
           "towary": {}}
    for towar, root in KRZYWA.items():
        lst = []
        for sym, mies in kontrakty(root):
            try:
                df = yf_hist(sym, period="10d", interval="1d")
                lst.append({"symbol": sym, "miesiac": mies, "cena": round(float(df["Close"].iloc[-1]), 2),
                            "data": df.index[-1].strftime("%Y-%m-%d"),
                            "cena_5d_temu": round(float(df["Close"].iloc[0]), 2)})
            except Exception as e:
                status["bledy"][f"krzywa_{sym}"] = str(e)[:150]
        lst = [x for x in lst if x["data"] >= (NOW.date() - dt.timedelta(days=7)).isoformat()]
        t = {"kontrakty": lst}
        if len(lst) >= 2:
            t["spread_1_2_proc"] = round((lst[0]["cena"] / lst[1]["cena"] - 1) * 100, 2)
            t["spread_1_2_proc_5d_temu"] = round((lst[0]["cena_5d_temu"] / lst[1]["cena_5d_temu"] - 1) * 100, 2)
        res["towary"][towar] = t
    if not any(t["kontrakty"] for t in res["towary"].values()):
        raise RuntimeError("żaden kontrakt nie zwrócił ceny")
    json.dump(res, open(path("krzywa.json"), "w"), ensure_ascii=False, indent=1)
    return ", ".join(f"{k}: {len(v['kontrakty'])} kontr." for k, v in res["towary"].items())


def zapisz_d1(df, name, cols=("Open", "High", "Low", "Close")):
    with open(path(name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Date", *cols])
        for idx, r in df.iterrows():
            w.writerow([idx.strftime("%Y-%m-%d"), *[round(float(r[c]), 6) for c in cols]])


def fx():
    done = []
    for k, sym in FX.items():
        try:
            zapisz_d1(yf_hist(sym, period="1y", interval="1d"), f"fx_{k}_1d.csv")
            done.append(k)
        except Exception as e:
            status["bledy"][f"fx_{k}"] = str(e)[:150]
    if not done:
        raise RuntimeError("brak kursów")
    return ", ".join(done)


def dlugie():
    done = []
    for k, sym in DLUGIE.items():
        name = f"{k}_dlugie_1d.csv"
        age = file_age_days(name)
        if age is not None and age < 6:
            done.append(f"{k} (świeże)")
            continue
        try:
            zapisz_d1(yf_hist(sym, period="max", interval="1d"), name, cols=("Close",))
            done.append(k)
        except Exception as e:
            status["bledy"][f"dlugie_{k}"] = str(e)[:150]
    return ", ".join(done)


# ---------------------------------------------------------------- ICE: zapasy certyfikowane
def parse_ice(raw, towar):
    """Szuka w raporcie wiersza z sumą zapasów. Format arkusza bywa różny, więc heurystyka:
    pierwszy wiersz z 'total' (bez 'pending'/'transit'), największa liczba w tym wierszu."""
    import pandas as pd
    sheets = pd.read_excel(io.BytesIO(raw), sheet_name=None, header=None)
    best = None
    for _, df in sheets.items():
        for _, row in df.iterrows():
            cells = [c for c in row.tolist() if str(c) != "nan"]
            txt = " ".join(str(c) for c in cells).lower()
            if "total" not in txt or any(w in txt for w in ("pending", "transit", "grading")):
                continue
            nums = [float(c) for c in cells if isinstance(c, (int, float)) and float(c) > 0]
            if not nums:
                continue
            val = max(nums)
            if best is None or val > best[0]:
                best = (val, txt[:120])
    if best is None:
        raise RuntimeError("nie znalazłem wiersza 'total' w raporcie")
    return best


def ice():
    os.makedirs(path("ice"), exist_ok=True)
    plik = path("zapasy_ice.csv")
    rows = list(csv.DictReader(open(plik))) if os.path.exists(plik) else []
    have = {(r["data"], r["rynek"]) for r in rows}
    done = []
    for towar, tpl in ICE_URL.items():
        for back in range(0, 7):
            d = NOW.date() - dt.timedelta(days=back)
            if d.weekday() >= 5 or (d.isoformat(), towar) in have:
                continue
            url = tpl.format(d=d.strftime("%Y%m%d"))
            try:
                raw = get(url, tries=1, timeout=30)
            except Exception:
                continue
            open(path(f"ice/{towar}_ostatni.xls"), "wb").write(raw)
            try:
                val, txt = parse_ice(raw, towar)
                rows.append({"data": d.isoformat(), "rynek": towar, "zapasy": int(val),
                             "jednostka": "worki 60 kg" if towar == "kawa" else "worki/tony wg raportu ICE",
                             "zrodlo": "ICE xls (automat)", "uwagi": txt.replace(",", " ")})
                done.append(f"{towar} {d}")
            except Exception as e:
                status["bledy"][f"ice_parse_{towar}"] = str(e)[:150]
            break
    rows.sort(key=lambda r: (r["data"], r["rynek"]))
    with open(plik, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["data", "rynek", "zapasy", "jednostka", "zrodlo", "uwagi"])
        w.writeheader()
        w.writerows(rows)
    if not done:
        raise RuntimeError("nie pobrano nowego raportu ICE (adres mógł się zmienić albo raport jeszcze nie wyszedł)")
    return ", ".join(done)


ZADANIA = {"cot": cot, "pogoda": pogoda, "krzywa": krzywa, "fx": fx, "dlugie": dlugie, "ice": ice}


def main():
    os.makedirs(OUT, exist_ok=True)
    wybor = sys.argv[1:] or list(ZADANIA)
    st_path = path("status.json")
    try:
        prev = json.load(open(st_path))
    except Exception:
        prev = {}
    for name in wybor:
        try:
            status["ok"][name] = ZADANIA[name]()
            print(f"OK {name}: {status['ok'][name]}")
        except Exception as e:
            status["bledy"][name] = f"{type(e).__name__}: {e}"[:300]
            print(f"BŁĄD {name}: {status['bledy'][name]}")
    # zachowaj informację o ostatnim udanym przebiegu każdego źródła
    ost = prev.get("ostatni_sukces_utc", {})
    for name in status["ok"]:
        ost[name] = status["uruchomiono_utc"]
    status["ostatni_sukces_utc"] = ost
    json.dump(status, open(st_path, "w"), ensure_ascii=False, indent=1)
    sys.exit(0 if status["ok"] else 1)


if __name__ == "__main__":
    main()
