#!/usr/bin/env python3
"""Analiza kawy (KC=F) i kakao (CC=F): reżim rynku, poziomy, czynniki fundamentalne, plan wejść
i kontrola wiszących zleceń z dziennika. Bez sieci, tylko pliki z repo, więc działa w Actions
(po każdym pobraniu cen) i u agenta po `git clone`.

Wejście: data/<coffee|cocoa>_{1d,1h,15m}.csv, data/latest.json, data/softy/* (fetch_softy.py),
         softy/kalendarz.csv, panel/projekt/agenci/paper_trading.md (zlecenia i kapitał).
Wynik:   data/softy/analiza.json i data/softy/analiza.md

Zasady księgi swing (agenci/ryzyko.md, sekcja 10a): ryzyko kawa 0,5%, kakao 0,25%; SL kawa 2× ATR D1,
kakao 2,5× ATR D1, w grze w zakresie min. 1× ATR D1 i 0,3× ATR D1 za granicą; TP1 = 2R, TP2 = 3R
(w zakresie TP1 = przeciwna granica, min. 1,5R po kosztach).

Dlaczego plan ma dwie nogi: limity liczone raz rano uciekały, gdy rynek zmieniał reżim (16.10 kawa
wybiła zakres 283-304). Dlatego dla każdego kierunku liczymy wejście z cofnięcia (limit, przed
poziomem) i wejście z kontynuacji (stop za ostatnim ekstremum), jako parę OCO, a limit odległy
o więcej niż MAX_LIMIT_ATR × ATR D1 oznaczamy jako mało realny.

Użycie: python3 softy/analiza.py [--kapital 10000000]
"""
import csv
import datetime as dt
import json
import math
import os
import re
import sys
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
SOFTY = os.path.join(DATA, "softy")
JOURNAL = os.path.join(ROOT, "panel", "projekt", "agenci", "paper_trading.md")
KALENDARZ = os.path.join(ROOT, "softy", "kalendarz.csv")
PL = ZoneInfo("Europe/Warsaw")
UTC = dt.timezone.utc

RYNKI = {
    "kawa": {"klucz": "coffee", "jedn": "c/lb", "usd_na_pkt": 375.0, "kontrakt": "KC (37 500 lb)",
             "ryzyko_proc": 0.5, "sl_atr": 2.0, "spread": 0.45, "krok_okragly": 10, "dziennik": ("Kawa",),
             "sesja_pl": "10:15-19:30", "zamkniecie_utc": (17, 30)},
    "kakao": {"klucz": "cocoa", "jedn": "USD/t", "usd_na_pkt": 10.0, "kontrakt": "CC (10 t)",
              "ryzyko_proc": 0.25, "sl_atr": 2.5, "spread": 18.0, "krok_okragly": 250, "dziennik": ("Kakao",),
              "sesja_pl": "10:45-19:30", "zamkniecie_utc": (17, 30)},
}
MAX_LIMIT_ATR = 0.75     # limit dalej niż tyle ATR D1 od ceny: w 1-2 sesje raczej się nie wypełni
FRONTRUN_ATR = 0.10      # limit stawiamy tyle ATR przed poziomem, żeby nie uciekł o kilka ticków
STOP_BUFOR_ATR = 0.10    # stop-entry tyle ATR za ekstremum
RANGE_SL_ATR = 0.30      # w zakresie SL tyle ATR za granicą


# ---------------------------------------------------------------- dane
def read_ohlc(name):
    f = os.path.join(DATA, name)
    if not os.path.exists(f):
        return []
    out = []
    for r in csv.DictReader(open(f)):
        try:
            out.append({"t": r.get("Datetime_UTC") or r.get("Date"), "o": float(r["Open"]), "h": float(r["High"]),
                        "l": float(r["Low"]), "c": float(r["Close"])})
        except (ValueError, KeyError, TypeError):
            continue
    return out


def read_close(name):
    f = os.path.join(SOFTY, name)
    if not os.path.exists(f):
        return []
    out = []
    for r in csv.DictReader(open(f)):
        try:
            out.append((r["Date"], float(r["Close"])))
        except (ValueError, KeyError):
            continue
    return out


def load_json(name, base=SOFTY):
    try:
        return json.load(open(os.path.join(base, name)))
    except Exception:
        return None


def num(v):
    try:
        return float(str(v).replace(" ", "").replace(" ", "").replace(",", "."))
    except Exception:
        return None


# ---------------------------------------------------------------- wskaźniki
def true_ranges(rows):
    return [max(r["h"] - r["l"], abs(r["h"] - p["c"]), abs(r["l"] - p["c"])) for p, r in zip(rows, rows[1:])]


def atr(rows, n=14):
    tr = true_ranges(rows)
    return sum(tr[-n:]) / min(n, len(tr)) if tr else None


def ema(vals, n):
    k, out = 2 / (n + 1), []
    for v in vals:
        out.append(v if not out else out[-1] + k * (v - out[-1]))
    return out


def adx(rows, n=14):
    if len(rows) < 2 * n + 2:
        return None, None, None
    pdm, mdm, tr = [], [], true_ranges(rows)
    for p, r in zip(rows, rows[1:]):
        up, dn = r["h"] - p["h"], p["l"] - r["l"]
        pdm.append(up if up > dn and up > 0 else 0.0)
        mdm.append(dn if dn > up and dn > 0 else 0.0)

    def wilder(x):
        s = [sum(x[:n])]
        for v in x[n:]:
            s.append(s[-1] - s[-1] / n + v)
        return s
    atr_s, p_s, m_s = wilder(tr), wilder(pdm), wilder(mdm)
    pdi = [100 * p / a if a else 0 for p, a in zip(p_s, atr_s)]
    mdi = [100 * m / a if a else 0 for m, a in zip(m_s, atr_s)]
    dx = [100 * abs(p - m) / (p + m) if p + m else 0 for p, m in zip(pdi, mdi)]
    adx_s = [sum(dx[:n]) / n]
    for v in dx[n:]:
        adx_s.append((adx_s[-1] * (n - 1) + v) / n)
    return adx_s[-1], pdi[-1], mdi[-1]


def swingi(rows, k=2):
    """Fraktale D1: szczyt/dołek wyższy/niższy od k świec po obu stronach."""
    hi, lo = [], []
    for i in range(k, len(rows) - k):
        win = rows[i - k:i + k + 1]
        if rows[i]["h"] == max(r["h"] for r in win):
            hi.append((rows[i]["t"][:10], rows[i]["h"]))
        if rows[i]["l"] == min(r["l"] for r in win):
            lo.append((rows[i]["t"][:10], rows[i]["l"]))
    return hi, lo


def klastry(punkty, tol):
    """Łączy poziomy bliższe niż tol; siła = liczba dotknięć, data = ostatnie dotknięcie."""
    out = []
    for d, v in sorted(punkty, key=lambda x: x[1]):
        if out and v - out[-1]["_min"] <= tol:
            c = out[-1]
            c["_vals"].append(v)
            c["_max"] = v
            c["sila"] += 1
            c["ostatnio"] = max(c["ostatnio"], d)
        else:
            out.append({"_vals": [v], "_min": v, "_max": v, "sila": 1, "ostatnio": d})
    for c in out:
        c["poziom"] = round(sum(c.pop("_vals")) / c["sila"], 2)
        c.pop("_max"); c.pop("_min")
    return out


# ---------------------------------------------------------------- sesja i kontekst
def zakonczone_d1(d1, cfg, now):
    """Ostatnia zakończona świeca D1 i ewentualnie bieżąca (sesja w trakcie)."""
    if not d1:
        return [], None
    last = d1[-1]
    h, m = cfg["zamkniecie_utc"]
    zamk = now.replace(hour=h, minute=m + 5 if m < 55 else m, second=0)
    if last["t"][:10] == now.date().isoformat() and now < zamk:
        return d1[:-1], last
    return d1, None


def atr_h1_sesja(h1, dni=5):
    """ATR H1 tylko ze świec sesji ICE (8-18 UTC), bo noc bez handlu zaniża średnią."""
    rows = [r for r in h1 if 8 <= int(r["t"][11:13]) <= 17]
    if len(rows) < 3:
        return None
    dates = sorted({r["t"][:10] for r in rows})[-dni:]
    rows = [r for r in rows if r["t"][:10] in dates]
    trs = [r["h"] - r["l"] for r in rows]
    return sum(trs) / len(trs)


def vwap_dnia(m15, date):
    rows = [r for r in m15 if r["t"][:10] == date]
    if not rows:
        return None
    tp = [(r["h"] + r["l"] + r["c"]) / 3 for r in rows]
    return sum(tp) / len(tp)


# ---------------------------------------------------------------- czynniki fundamentalne
def czynnik(nazwa, wynik, opis, dane=None):
    return {"czynnik": nazwa, "wynik": round(wynik, 2), "opis": opis, **({"dane": dane} if dane else {})}


def f_cot(rynek):
    f = os.path.join(SOFTY, "cot.csv")
    if not os.path.exists(f):
        return None
    rows = [r for r in csv.DictReader(open(f)) if r["rynek"] == rynek and r["mm_net"]]
    if len(rows) < 20:
        return None
    rows.sort(key=lambda r: r["data"])
    nets = [int(r["mm_net"]) for r in rows][-156:]
    net, d1w = nets[-1], nets[-1] - nets[-2]
    d4w = nets[-1] - nets[-5] if len(nets) >= 5 else 0
    pct = round(100 * sum(1 for x in nets if x <= net) / len(nets))
    if pct >= 90:
        w, op = -1.0, f"fundusze (managed money) net {net:+,} kontr., {pct}. percentyl 3 lat: tłoczno w longach, ryzyko likwidacji"
    elif pct <= 10:
        w, op = 1.0, f"fundusze net {net:+,}, {pct}. percentyl 3 lat: tłoczno w shortach, paliwo do squeeze"
    else:
        w = 0.5 if d4w > 0 else -0.5 if d4w < 0 else 0.0
        op = f"fundusze net {net:+,} ({pct}. percentyl 3 lat), zmiana 4 tyg. {d4w:+,}: pozycjonowanie bez skrajności, liczy się kierunek przepływu"
    return czynnik("COT", w, op, {"raport": rows[-1]["data"], "mm_net": net, "zmiana_1t": d1w, "zmiana_4t": d4w,
                                  "percentyl_3l": pct, "oi": num(rows[-1]["oi"])})


def f_pogoda(rynek, now):
    p = load_json("pogoda.json")
    if not p or rynek not in p.get("towary", {}):
        return None
    regs = p["towary"][rynek]
    sw = sum(r["waga"] for r in regs if r.get("proc_normy_30d") is not None) or 1
    p30 = sum(r["waga"] * r["proc_normy_30d"] for r in regs if r.get("proc_normy_30d") is not None) / sw
    sw16 = sum(r["waga"] for r in regs if r.get("proc_normy_16d") is not None) or 1
    p16 = sum(r["waga"] * r["proc_normy_16d"] for r in regs if r.get("proc_normy_16d") is not None) / sw16
    m, w, uw = now.month, 0.0, []
    if rynek == "kawa":
        bra = [r for r in regs if r["klucz"] in ("sul_de_minas", "cerrado", "mogiana")]
        tmin = min((r["tmin_prog_min"] for r in bra if r.get("tmin_prog_min") is not None), default=None)
        if m in (6, 7, 8) and tmin is not None and tmin <= 2:
            w += 2
            uw.append(f"ryzyko przymrozku w Minas (Tmin w prognozie {tmin:.1f}°C)")
        if m in (9, 10, 11):   # kwitnienie arabiki: deszcz decyduje o zbiorach 2027
            if p30 < 60 and p16 < 70:
                w += 1.5; uw.append("sucho w czasie kwitnienia i brak deszczu w prognozie")
            elif p16 < 60:
                w += 1; uw.append("prognoza 16 dni sucha w czasie kwitnienia")
            elif p16 > 110 and p30 > 80:
                w -= 1; uw.append("deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027")
        elif m in (12, 1, 2, 3):   # nalewanie ziarna
            if p30 < 60:
                w += 1; uw.append("sucho w czasie nalewania ziarna")
    else:
        if m in (10, 11, 12, 1, 2, 3):   # zbiory głównego sezonu + okres harmattanu
            if p30 < 60 and p16 < 70:
                w += 1; uw.append("sucho w Afryce Zach. w sezonie głównym (ryzyko dla zbiorów średnich)")
            elif p30 > 170:
                w += 0.5; uw.append("bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem")
            elif 85 <= p16 <= 130 and 85 <= p30 <= 130:
                w -= 0.5; uw.append("pogoda zbliżona do normy: wspiera podaż")
        else:   # sezon średni / kwitnienie
            if p30 < 60:
                w += 1; uw.append("sucho w czasie kwitnienia/zawiązywania strąków")
        ekw = next((r for r in regs if r["klucz"] == "los_rios"), None)
        if ekw and (ekw.get("proc_normy_30d") or 0) > 200:
            w += 0.5; uw.append("Ekwador bardzo mokro (powodzie)")
    op = f"opad 30 dni {p30:.0f}% normy, prognoza 16 dni {p16:.0f}% normy (średnia ważona regionów)"
    if uw:
        op += "; " + "; ".join(uw)
    return czynnik("Pogoda", w, op, {"proc_normy_30d": round(p30), "proc_normy_16d": round(p16),
                                     "aktualizacja": p.get("zaktualizowano_utc"),
                                     "regiony": {r["klucz"]: [r.get("proc_normy_30d"), r.get("proc_normy_16d")] for r in regs}})


def f_krzywa(rynek):
    k = load_json("krzywa.json")
    t = (k or {}).get("towary", {}).get(rynek)
    if not t or "spread_1_2_proc" not in t:
        return None
    s, s5 = t["spread_1_2_proc"], t.get("spread_1_2_proc_5d_temu")
    w = 1.0 if s > 2 else -1.0 if s < -2 else 0.0
    if s5 is not None and abs(s - s5) > 1:
        w += 0.5 if s > s5 else -0.5
    zm = f", 5 dni temu {s5:+.2f}%" if s5 is not None else ""
    nazwa = "backwardation (ciasno w bieżącej dostawie)" if s > 0 else "contango (zapasy wystarczają)"
    op = f"{t['kontrakty'][0]['symbol']} vs {t['kontrakty'][1]['symbol']}: {s:+.2f}%{zm}, {nazwa}"
    return czynnik("Krzywa", w, op, {"spread_proc": s, "spread_proc_5d": s5, "kontrakty": t["kontrakty"][:4]})


def f_zapasy(rynek):
    # automat (data/softy/zapasy_ice.csv) + wpisy agentów z newsów (softy/zapasy_reczne.csv); automat wygrywa w tym samym dniu
    rows = {}
    for f in (os.path.join(ROOT, "softy", "zapasy_reczne.csv"), os.path.join(SOFTY, "zapasy_ice.csv")):
        if os.path.exists(f):
            for r in csv.DictReader(open(f)):
                if r.get("rynek") == rynek and num(r.get("zapasy")):
                    rows[r["data"]] = r
    if not rows:
        return None
    rows = [rows[d] for d in sorted(rows)]
    if len(rows) < 2:
        if True:
            return czynnik("Zapasy ICE", 0, f"ostatni odczyt {rows[-1]['zapasy']} ({rows[-1]['data']}, {rows[-1]['zrodlo']}), za mało historii na trend",
                           {"ostatnie": rows[-1]})
        return None
    last = rows[-1]
    base = next((r for r in reversed(rows) if r["data"] <= (dt.date.fromisoformat(last["data"]) - dt.timedelta(days=28)).isoformat()), rows[0])
    zm = (num(last["zapasy"]) / num(base["zapasy"]) - 1) * 100
    w = 1.0 if zm < -5 else -1.0 if zm > 5 else 0.0
    op = f"{int(num(last['zapasy'])):,} ({last['data']}), zmiana od {base['data']}: {zm:+.1f}%" + (
        ": spadają, ciasno" if w > 0 else ": rosną, presja na bieżący kontrakt" if w < 0 else "")
    return czynnik("Zapasy ICE", w, op, {"ostatnie": last, "zmiana_proc": round(zm, 1), "od": base["data"]})


def f_fx(rynek):
    if rynek != "kawa":
        return None
    f = os.path.join(SOFTY, "fx_brl_1d.csv")
    if not os.path.exists(f):
        return None
    rows = list(csv.DictReader(open(f)))
    if len(rows) < 6:
        return None
    c, c5 = float(rows[-1]["Close"]), float(rows[-6]["Close"])
    zm = (c / c5 - 1) * 100
    w = 0.5 if zm < -1.5 else -0.5 if zm > 1.5 else 0.0
    op = f"USD/BRL {c:.3f}, 5 sesji {zm:+.1f}%" + (": real mocnieje, rolnicy mniej sprzedają" if w > 0 else
                                                   ": real słabnie, sprzedaż z Brazylii tańsza" if w < 0 else "")
    return czynnik("BRL", w, op, {"usdbrl": c, "zmiana_5d_proc": round(zm, 2)})


def f_sezon(klucz, now, dni=20):
    rows = read_close(f"{klucz}_dlugie_1d.csv")
    if len(rows) < 2000:
        return None
    by_year = {}
    for i, (d, c) in enumerate(rows):
        by_year.setdefault(d[:4], []).append(i)
    rets, doy = [], now.timetuple().tm_yday
    for y, idxs in by_year.items():
        if int(y) >= now.year:
            continue
        # pierwsza sesja tego roku o dniu roku >= dzisiejszego
        start = next((i for i in idxs if dt.date.fromisoformat(rows[i][0]).timetuple().tm_yday >= doy), None)
        if start is None or start + dni >= len(rows):
            continue
        rets.append((rows[start + dni][1] / rows[start][1] - 1) * 100)
    if len(rets) < 10:
        return None
    avg = sum(rets) / len(rets)
    med = sorted(rets)[len(rets) // 2]
    up = 100 * sum(1 for r in rets if r > 0) / len(rets)
    w = 0.5 if up >= 62 and med > 0 else -0.5 if up <= 38 and med < 0 else 0.0
    op = f"kolejne {dni} sesji od tej daty w {len(rets)} latach: mediana {med:+.1f}%, wzrost w {up:.0f}% lat"
    return czynnik("Sezonowość", w, op, {"lata": len(rets), "srednia_proc": round(avg, 2), "mediana_proc": round(med, 2),
                                         "proc_lat_wzrost": round(up)})


# ---------------------------------------------------------------- plan wejść
def okragle(v, krok):
    return round(round(v / krok) * krok, 2)


def plan_wejsc(rynek, cfg, cena, a, rez, lv, d1z, kapital):
    """Dwie nogi na kierunek (cofnięcie i kontynuacja) jako OCO, z wielkością wg ryzyko.md 10a."""
    spread = cfg["spread"]
    koszt = spread * 3   # spread + poślizg 2× spread
    ryz_usd = kapital * cfg["ryzyko_proc"] / 100
    pd_ = d1z[-1]
    zakres = rez["typ"] == "zakres"
    out = []

    def noga(kier, typ, wej, sl, uzas, tp1_lvl=None):
        r = abs(wej - sl)
        if r <= 0:
            return None
        s = 1 if kier == "LONG" else -1
        if zakres and tp1_lvl is not None and abs(tp1_lvl - wej) / r >= 1.5:
            tp1 = tp1_lvl - s * FRONTRUN_ATR * a
        else:
            tp1 = wej + s * 2 * r
        tp2 = wej + s * max(3 * r, abs(tp1 - wej) + 0.5 * a)
        rr = (abs(tp1 - wej) - koszt) / (r + koszt)
        dyst = (wej - cena) / a
        kontr = ryz_usd / ((r + koszt) * cfg["usd_na_pkt"])
        uw = []
        if typ == "limit" and abs(dyst) > MAX_LIMIT_ATR:
            uw.append(f"limit {abs(dyst):.2f}× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop")
        if typ == "stop" and abs(dyst) > 1.0:
            uw.append(f"stop {abs(dyst):.2f}× ATR D1 od ceny: daleko, do przeliczenia po sesji")
        przeszkoda = None
        for x in (lv["opory"] if s > 0 else lv["wsparcia"]):
            if (x["poziom"] - wej) * s > 0.2 * a and (tp1 - x["poziom"]) * s > 0 and x["sila"] >= 2:
                przeszkoda = x["poziom"]; break
        if przeszkoda:
            uw.append(f"silny poziom {przeszkoda} przed TP1: rozważyć częściowe wyjście przed nim")
        min_rr = 1.5 if zakres else 2.0
        if rr < min_rr - 0.05:
            uw.append(f"R:R po kosztach {rr:.2f} < {min_rr}: według ryzyko.md 10a nie składać")
        return {"kierunek": kier, "typ": typ, "wejscie": round(wej, 2), "sl": round(sl, 2), "tp1": round(tp1, 2),
                "tp2": round(tp2, 2), "r_pkt": round(r, 2), "r_atr": round(r / a, 2), "rr_tp1_netto": round(rr, 2),
                "odleglosc_atr": round(dyst, 2), "kontrakty": round(kontr, 1), "ryzyko_usd": round(ryz_usd),
                "uzasadnienie": uzas, "uwagi": uw}

    for kier in ("LONG", "SHORT"):
        s = 1 if kier == "LONG" else -1
        nogi = []
        if zakres:
            gr = rez["zakres_dol"] if s > 0 else rez["zakres_gora"]
            prz = rez["zakres_gora"] if s > 0 else rez["zakres_dol"]
            wej = gr + s * FRONTRUN_ATR * a
            sl = gr - s * max(RANGE_SL_ATR * a, a - abs(wej - gr))   # min. 1× ATR od wejścia i 0,3× ATR za granicą
            if abs(wej - sl) < a:
                sl = wej - s * a
            nogi.append(noga(kier, "limit", wej, sl, f"granica zakresu {gr:.2f} (10 sesji), TP1 przed przeciwną granicą", prz))
            # wybicie z zakresu w tę stronę: stop za przeciwną granicą
            wej_b = prz + s * STOP_BUFOR_ATR * a
            nogi.append(noga(kier, "stop", wej_b, wej_b - s * cfg["sl_atr"] * a,
                             f"wybicie zakresu za {prz:.2f}: zmiana reżimu, wejście z kontynuacji"))
        else:
            # cofnięcie: najbliższe sensowne wsparcie (long) / opór (short) między 0,3 a 1,5 ATR od ceny,
            # najlepiej wybity poziom zakresu albo EMA20
            kand = [x for x in (lv["wsparcia"] if s > 0 else lv["opory"]) if 0.3 * a <= abs(cena - x["poziom"]) <= 1.5 * a]
            kand += [{"poziom": rez["ema20"], "sila": 1, "zrodlo": "EMA20"}] if 0.3 * a <= (cena - rez["ema20"]) * s <= 1.5 * a else []
            if kand:
                best = max(kand, key=lambda x: (x["sila"], -abs(cena - x["poziom"])))
                poz = best["poziom"]
                wej = poz + s * FRONTRUN_ATR * a
                nogi.append(noga(kier, "limit", wej, wej - s * cfg["sl_atr"] * a,
                                 f"cofnięcie do {poz:.2f} ({best.get('zrodlo', 'swing D1, dotknięcia: ' + str(best['sila']))})"))
            ekstr = (max(pd_["h"], cena) if s > 0 else min(pd_["l"], cena))
            wej_b = ekstr + s * STOP_BUFOR_ATR * a
            nogi.append(noga(kier, "stop", wej_b, wej_b - s * cfg["sl_atr"] * a,
                             f"kontynuacja: przebicie {'szczytu' if s > 0 else 'dołka'} ostatniej sesji {ekstr:.2f}"))
        nogi = [n for n in nogi if n]
        zgodny = (rez["kierunek"] == kier) or zakres
        out.append({"kierunek": kier, "zgodny_z_rezimem": zgodny, "nogi": nogi,
                    "zasada": "obie nogi jako OCO; anulować, gdy D1 zamknie się za SL nogi limit; przeliczyć codziennie przed otwarciem ICE"})
    return out


def kontrola_zlecen(rynek, cfg, cena, a, ah1):
    if not os.path.exists(JOURNAL):
        return []
    out, hdr = [], None
    for line in open(JOURNAL):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        if hdr is None:
            hdr = cells
            continue
        r = dict(zip(hdr, cells))
        if not r.get("Instrument", "").startswith(cfg["dziennik"]) or not r.get("Status", "").startswith("oczekuje"):
            continue
        wej, sl = num(r.get("Wejście")), num(r.get("SL"))
        if wej is None:
            continue
        kier = r.get("Kierunek", "").upper()
        typ = "stop" if re.search(r"\bstop\b", r["Status"]) else "limit"
        dyst = (wej - cena) / a
        s = 1 if kier == "LONG" else -1
        if typ == "limit":
            # limit long czeka poniżej ceny, short powyżej
            if (wej - cena) * s > 0:
                ocena = "cena już za limitem: wypełni się od razu po otwarciu albo ma lukę"
            elif abs(dyst) > MAX_LIMIT_ATR:
                ocena = f"daleko ({abs(dyst):.2f}× ATR D1): mała szansa wypełnienia, rozważyć nogę stop albo przesunięcie"
            else:
                ocena = f"w zasięgu ({abs(dyst):.2f}× ATR D1, {abs(wej - cena) / ah1:.1f}× ATR H1)" if ah1 else f"w zasięgu ({abs(dyst):.2f}× ATR D1)"
        else:
            if (cena - wej) * s >= 0:
                ocena = "cena już za poziomem stop: wejście po cenie otwarcia (luka), sprawdzić R:R"
            elif abs(dyst) > 1.0:
                ocena = f"stop daleko ({abs(dyst):.2f}× ATR D1)"
            else:
                ocena = f"w zasięgu ({abs(dyst):.2f}× ATR D1)"
        if sl is not None and (cena - sl) * s <= 0:
            ocena = "cena już za SL: zlecenie nieaktualne"
        out.append({"nr": r.get("#"), "kierunek": kier, "typ": typ, "wejscie": wej, "sl": sl, "tp": r.get("TP"),
                    "odleglosc_atr_d1": round(dyst, 2), "ocena": ocena, "status": r["Status"][:120]})
    return out


def kapital_z_dziennika(domyslny=10_000_000):
    if not os.path.exists(JOURNAL):
        return domyslny
    found = re.findall(r"Kapitał\s+([\d\s ]{6,})\s*USD", open(JOURNAL).read())
    vals = [num(x) for x in found if num(x)]
    return vals[-1] if vals else domyslny


def kalendarz(now, dni=14):
    if not os.path.exists(KALENDARZ):
        return []
    out = []
    for r in csv.DictReader(open(KALENDARZ)):
        try:
            d = dt.date.fromisoformat(r["data"])
        except Exception:
            continue
        if now.date() <= d <= now.date() + dt.timedelta(days=dni):
            out.append(r)
    # zdarzenia cykliczne
    for i in range(dni + 1):
        d = now.date() + dt.timedelta(days=i)
        if d.weekday() == 4:
            out.append({"data": d.isoformat(), "godzina_pl": "21:30", "rynek": "oba", "wydarzenie": "CFTC COT (stan na wtorek)",
                        "waga": "średnia", "uwagi": "cykliczne"})
        if d.weekday() == 0:
            out.append({"data": d.isoformat(), "godzina_pl": "rano", "rynek": "kakao",
                        "wydarzenie": "przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów)",
                        "waga": "średnia-wysoka", "uwagi": "cykliczne"})
    return sorted(out, key=lambda r: (r["data"], r.get("godzina_pl", "")))


# ---------------------------------------------------------------- główna analiza
def analizuj(rynek, cfg, latest, now, kapital):
    k = cfg["klucz"]
    d1, h1, m15 = read_ohlc(f"{k}_1d.csv"), read_ohlc(f"{k}_1h.csv"), read_ohlc(f"{k}_15m.csv")
    if len(d1) < 60:
        return {"blad": "za mało świec D1"}
    d1z, biezaca = zakonczone_d1(d1, cfg, now)
    li = latest.get("instrumenty", {}).get(k, {})
    cena = li.get("cena") or (biezaca or d1z[-1])["c"]
    a = atr(d1z)
    ah1 = atr_h1_sesja(h1)
    closes = [r["c"] for r in d1z]
    e20, e50 = ema(closes, 20)[-1], ema(closes, 50)[-1]
    sma100 = sum(closes[-100:]) / min(100, len(closes))
    sma200 = sum(closes[-200:]) / min(200, len(closes))
    adx_v, pdi, mdi = adx(d1z)
    poprz = d1z[-21:-1]
    hi20, lo20 = max(r["h"] for r in poprz), min(r["l"] for r in poprz)
    # zakres roboczy: 10 sesji przed ostatnią (20 sesji bywa za szeroki, granice wychodzą 3 ATR od ceny)
    p10 = d1z[-11:-1]
    hi10, lo10 = max(r["h"] for r in p10), min(r["l"] for r in p10)
    last = d1z[-1]
    vol20 = math.sqrt(252) * (sum((math.log(b / a_) ) ** 2 for a_, b in zip(closes[-21:-1], closes[-20:])) / 20) ** 0.5 * 100

    # reżim
    f2 = lambda v: f"{v:.2f}"
    if last["c"] > hi10 or cena > hi10 + 0.25 * a:
        typ, kier, op = "wybicie_gora", "LONG", f"zamknięcie/cena nad szczytem 10 sesji {f2(hi10)}"
    elif last["c"] < lo10 or cena < lo10 - 0.25 * a:
        typ, kier, op = "wybicie_dol", "SHORT", f"zamknięcie/cena pod dołkiem 10 sesji {f2(lo10)}"
    elif adx_v and adx_v >= 22 and e20 > e50 and cena > e20:
        typ, kier, op = "trend_wzrostowy", "LONG", f"ADX {adx_v:.0f}, EMA20 > EMA50, cena nad EMA20"
    elif adx_v and adx_v >= 22 and e20 < e50 and cena < e20:
        typ, kier, op = "trend_spadkowy", "SHORT", f"ADX {adx_v:.0f}, EMA20 < EMA50, cena pod EMA20"
    else:
        typ, kier, op = "zakres", "NEUTRAL", f"ADX {adx_v or 0:.0f}, cena w zakresie 10 sesji {f2(lo10)}-{f2(hi10)}"
    # nieudane wybicie: ostatnia sesja wyszła za granicę, ale zamknęła się z powrotem w środku
    if last["h"] > hi10 and last["c"] <= hi10:
        op += f"; nieudane wybicie górą ({f2(last['h'])} > {f2(hi10)}, zamknięcie {f2(last['c'])}): uwaga na pułapkę albo drugie podejście"
    if last["l"] < lo10 and last["c"] >= lo10:
        op += f"; nieudane wybicie dołem ({f2(last['l'])} < {f2(lo10)}, zamknięcie {f2(last['c'])})"
    rez = {"typ": typ, "kierunek": kier, "opis": op, "adx": round(adx_v, 1) if adx_v else None,
           "di_plus": round(pdi, 1) if pdi else None, "di_minus": round(mdi, 1) if mdi else None,
           "ema20": round(e20, 2), "ema50": round(e50, 2), "sma100": round(sma100, 2), "sma200": round(sma200, 2),
           "zakres_gora": round(hi10, 2), "zakres_dol": round(lo10, 2),
           "zakres20_gora": round(hi20, 2), "zakres20_dol": round(lo20, 2),
           "pozycja_w_zakresie_proc": round(100 * (cena - lo10) / (hi10 - lo10)) if hi10 > lo10 else None,
           "zmiennosc_20d_roczna_proc": round(vol20, 1)}

    # poziomy
    hi, lo = swingi(d1z[-130:])
    pts = hi + lo + [(last["t"][:10], last["h"]), (last["t"][:10], last["l"])]
    kl = klastry(pts, 0.35 * a)
    P = (last["h"] + last["l"] + last["c"]) / 3
    piv = {"P": P, "R1": 2 * P - last["l"], "S1": 2 * P - last["h"], "R2": P + last["h"] - last["l"], "S2": P - (last["h"] - last["l"])}
    tyg = d1z[-5:]
    dodatkowe = [{"poziom": round(v, 2), "sila": 1, "zrodlo": n} for n, v in piv.items()]
    dodatkowe += [{"poziom": round(max(r["h"] for r in tyg), 2), "sila": 2, "zrodlo": "szczyt 5 sesji"},
                  {"poziom": round(min(r["l"] for r in tyg), 2), "sila": 2, "zrodlo": "dołek 5 sesji"}]
    krok = cfg["krok_okragly"]
    dodatkowe += [{"poziom": okragle(cena + i * krok, krok), "sila": 1, "zrodlo": "okrągły poziom"} for i in (-2, -1, 1, 2)]
    for x in kl:
        x["zrodlo"] = f"swing D1 ×{x['sila']}, ostatnio {x['ostatnio']}"
    wszystkie = kl + dodatkowe
    opory = sorted([x for x in wszystkie if x["poziom"] > cena + 0.05 * a], key=lambda x: x["poziom"])[:6]
    wsparcia = sorted([x for x in wszystkie if x["poziom"] < cena - 0.05 * a], key=lambda x: -x["poziom"])[:6]
    for x in opory + wsparcia:
        x["odleglosc_atr"] = round((x["poziom"] - cena) / a, 2)
    lv = {"opory": opory, "wsparcia": wsparcia, "pivoty": {k_: round(v, 2) for k_, v in piv.items()},
          "baza_pivotow": last["t"][:10]}

    # czynniki
    cz = [c for c in (f_cot(rynek), f_pogoda(rynek, now), f_krzywa(rynek), f_zapasy(rynek), f_fx(rynek), f_sezon(k, now)) if c]
    tech_w = {"wybicie_gora": 1.5, "trend_wzrostowy": 1.0, "wybicie_dol": -1.5, "trend_spadkowy": -1.0}.get(typ, 0.0)
    cz.insert(0, czynnik("Technika (reżim)", tech_w, op))
    suma = sum(c["wynik"] for c in cz)
    bias = "LONG" if suma >= 2 else "SHORT" if suma <= -2 else "NEUTRAL"
    pewnosc = max(1, min(5, int(round(abs(suma))) + (1 if bias != "NEUTRAL" else 0)))
    brak = [n for n, ok in (("COT", any(c["czynnik"] == "COT" for c in cz)), ("pogoda", any(c["czynnik"] == "Pogoda" for c in cz)),
                            ("krzywa", any(c["czynnik"] == "Krzywa" for c in cz)), ("zapasy ICE", any(c["czynnik"] == "Zapasy ICE" for c in cz)),
                            ("sezonowość", any(c["czynnik"] == "Sezonowość" for c in cz))) if not ok]

    plan = plan_wejsc(rynek, cfg, cena, a, rez, lv, d1z, kapital)
    dzis = biezaca or {}
    kontekst = {"cena": cena, "czas_notowania_utc": li.get("czas_notowania_utc"), "sesja_w_trakcie": biezaca is not None,
                "atr_d1": round(a, 2), "atr_h1_sesja": round(ah1, 2) if ah1 else None,
                "zakres_dzis_proc_atr": round(100 * (dzis["h"] - dzis["l"]) / a) if dzis else None,
                "vwap_dzis": round(vwap_dnia(m15, now.date().isoformat()), 2) if biezaca and vwap_dnia(m15, now.date().isoformat()) else None,
                "ostatnia_sesja": {"data": last["t"][:10], "o": last["o"], "h": last["h"], "l": last["l"], "c": last["c"]},
                "zmiana_5s_proc": round((closes[-1] / closes[-6] - 1) * 100, 2),
                "zmiana_20s_proc": round((closes[-1] / closes[-21] - 1) * 100, 2)}
    return {"jednostka": cfg["jedn"], "kontrakt": cfg["kontrakt"], "sesja_ice_pl": cfg["sesja_pl"], "kontekst": kontekst,
            "rezim": rez, "poziomy": lv, "czynniki": cz, "suma": round(suma, 2), "bias": bias, "pewnosc": pewnosc,
            "brak_danych": brak, "plan": plan, "zlecenia_w_dzienniku": kontrola_zlecen(rynek, cfg, cena, a, ah1)}


def alerty(res, poprz):
    """Co zmieniło się od poprzedniego przebiegu i co wymaga reakcji agenta; zmiany reżimu idą do rezim_log.csv."""
    out = []
    log = os.path.join(SOFTY, "rezim_log.csv")
    for rynek, r in res["rynki"].items():
        if "blad" in r:
            continue
        typ = r["rezim"]["typ"]
        stary = ((poprz or {}).get("rynki", {}).get(rynek) or {}).get("rezim", {}).get("typ")
        if stary and stary != typ:
            out.append({"rynek": rynek, "typ": "zmiana_rezimu", "opis": f"reżim {stary} → {typ}: przeliczyć plan i wiszące zlecenia"})
            nowy = not os.path.exists(log)
            with open(log, "a", newline="") as f:
                w = csv.writer(f)
                if nowy:
                    w.writerow(["czas_utc", "rynek", "z", "na", "cena", "opis"])
                w.writerow([res["wygenerowano_utc"], rynek, stary, typ, r["kontekst"]["cena"], r["rezim"]["opis"]])
        if "nieudane wybicie" in r["rezim"]["opis"]:
            out.append({"rynek": rynek, "typ": "nieudane_wybicie", "opis": r["rezim"]["opis"].split("; ", 1)[-1]})
        stary_bias = ((poprz or {}).get("rynki", {}).get(rynek) or {}).get("bias")
        if stary_bias and stary_bias != r["bias"]:
            out.append({"rynek": rynek, "typ": "zmiana_biasu", "opis": f"bias {stary_bias} → {r['bias']} ({r['pewnosc']}/5)"})
        for z in r["zlecenia_w_dzienniku"]:
            if not z["ocena"].startswith("w zasięgu"):
                out.append({"rynek": rynek, "typ": "zlecenie", "opis": f"#{z['nr']} {z['kierunek']} {z['typ']} {z['wejscie']}: {z['ocena']}"})
    return out


def fmt(v, jedn):
    if v is None:
        return "—"
    s = f"{v:,.0f}" if jedn == "USD/t" else f"{v:,.2f}"
    return s.replace(",", " ").replace(".", ",")


def markdown(res):
    L = [f"# Softy: kawa i kakao, analiza z {res['wygenerowano_pl']}", "",
         "Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.", ""]
    nazwy = {"kawa": "Kawa (Arabica KC)", "kakao": "Kakao (NY CC)"}
    for rynek, r in res["rynki"].items():
        if "blad" in r:
            L += [f"## {nazwy[rynek]}", "", f"Błąd: {r['blad']}", ""]
            continue
        j, k, z = r["jednostka"], r["kontekst"], r["rezim"]
        L += [f"## {nazwy[rynek]}: {r['bias']} {r['pewnosc']}/5 (suma {r['suma']:+.1f})", "",
              f"- Cena {fmt(k['cena'], j)} {j} ({k['czas_notowania_utc']} UTC){', sesja w trakcie' if k['sesja_w_trakcie'] else ''}. "
              f"ATR D1 {fmt(k['atr_d1'], j)}, ATR H1 (sesja) {fmt(k['atr_h1_sesja'], j)}. 5 sesji {k['zmiana_5s_proc']:+.1f}%, 20 sesji {k['zmiana_20s_proc']:+.1f}%.",
              f"- Reżim: **{z['typ'].replace('_', ' ')}** ({z['opis']}). Zakres 10 sesji {fmt(z['zakres_dol'], j)}–{fmt(z['zakres_gora'], j)} (20 sesji {fmt(z['zakres20_dol'], j)}–{fmt(z['zakres20_gora'], j)}), "
              f"EMA20 {fmt(z['ema20'], j)}, EMA50 {fmt(z['ema50'], j)}, SMA200 {fmt(z['sma200'], j)}.", ""]
        L += ["| Czynnik | Wynik | Opis |", "|---|---|---|"]
        L += [f"| {c['czynnik']} | {c['wynik']:+.1f} | {c['opis']} |" for c in r["czynniki"]]
        if r["brak_danych"]:
            L += ["", f"Brak danych: {', '.join(r['brak_danych'])} (patrz data/softy/status.json)."]
        L += ["", "Opory: " + ", ".join(f"{fmt(x['poziom'], j)} ({x['zrodlo']}, {x['odleglosc_atr']:+.2f} ATR)" for x in r["poziomy"]["opory"][:4]),
              "", "Wsparcia: " + ", ".join(f"{fmt(x['poziom'], j)} ({x['zrodlo']}, {x['odleglosc_atr']:+.2f} ATR)" for x in r["poziomy"]["wsparcia"][:4]), ""]
        L += ["| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |", "|---|---|---|---|---|---|---|---|---|"]
        for p in r["plan"]:
            for n in p["nogi"]:
                zg = "" if p["zgodny_z_rezimem"] else " (pod prąd)"
                L.append(f"| {n['kierunek']}{zg} | {n['typ']}: {n['uzasadnienie']} | {fmt(n['wejscie'], j)} | {fmt(n['sl'], j)} | "
                         f"{fmt(n['tp1'], j)} / {fmt(n['tp2'], j)} | {n['rr_tp1_netto']:.2f} | {n['odleglosc_atr']:+.2f} ATR | {n['kontrakty']:.0f} | {'; '.join(n['uwagi']) or 'ok'} |")
        if r["zlecenia_w_dzienniku"]:
            L += ["", "Wiszące zlecenia z dziennika:", ""]
            L += [f"- #{z_['nr']} {z_['kierunek']} {z_['typ']} {fmt(z_['wejscie'], j)} (SL {fmt(z_['sl'], j)}): {z_['ocena']}" for z_ in r["zlecenia_w_dzienniku"]]
        L.append("")
    if res.get("alerty"):
        L += ["## Alerty", ""] + [f"- {x['rynek']}: {x['opis']}" for x in res["alerty"]] + [""]
    if res["kalendarz"]:
        L += ["## Kalendarz (14 dni)", "", "| Data | Godz. PL | Rynek | Wydarzenie | Waga |", "|---|---|---|---|---|"]
        L += [f"| {e['data']} | {e.get('godzina_pl', '')} | {e.get('rynek', '')} | {e['wydarzenie']} | {e.get('waga', '')} |" for e in res["kalendarz"]]
    return "\n".join(L) + "\n"


def main():
    kapital = None
    if "--kapital" in sys.argv:
        kapital = float(sys.argv[sys.argv.index("--kapital") + 1])
    now = dt.datetime.now(UTC).replace(microsecond=0)
    latest = load_json("latest.json", DATA) or {}
    kapital = kapital or kapital_z_dziennika()
    res = {"wygenerowano_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
           "wygenerowano_pl": now.astimezone(PL).strftime("%Y-%m-%d %H:%M PL"),
           "kapital_usd": kapital, "parametry": {"MAX_LIMIT_ATR": MAX_LIMIT_ATR, "FRONTRUN_ATR": FRONTRUN_ATR,
                                                 "STOP_BUFOR_ATR": STOP_BUFOR_ATR, "RANGE_SL_ATR": RANGE_SL_ATR},
           "rynki": {}, "kalendarz": kalendarz(now), "status_danych": load_json("status.json")}
    for rynek, cfg in RYNKI.items():
        try:
            res["rynki"][rynek] = analizuj(rynek, cfg, latest, now, kapital)
        except Exception as e:
            res["rynki"][rynek] = {"blad": f"{type(e).__name__}: {e}"}
    os.makedirs(SOFTY, exist_ok=True)
    res["alerty"] = alerty(res, load_json("analiza.json"))
    json.dump(res, open(os.path.join(SOFTY, "analiza.json"), "w"), ensure_ascii=False, indent=1)
    open(os.path.join(SOFTY, "analiza.md"), "w").write(markdown(res))
    for rynek, r in res["rynki"].items():
        print(rynek, r.get("bias"), r.get("pewnosc"), r.get("rezim", {}).get("typ"), r.get("blad", ""))


if __name__ == "__main__":
    main()
