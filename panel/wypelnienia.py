#!/usr/bin/env python3
"""Pilnuje zleceń z dziennika na świecach 15 min, bez udziału Claude.

Dla każdego wiersza dziennika ze statusem „oczekuje…” albo „otwarta…”:
  - wejście: pierwsza świeca 15m w oknie handlu, której zakres obejmuje cenę limitu,
  - po +1R SL przesuwa się na wejście (BE),
  - TP1 zamyka 50%, TP2 resztę,
  - SL zamyka całość (gdy świeca dotyka SL i TP naraz, liczymy SL),
  - intraday: zamknięcie po ostatniej cenie przed 22:30 PL; niewypełnione zlecenie wygasa.
Złoto i srebro „spot” liczone na świecach xauusd/xagusd (futures przesunięte o bazę, więc przybliżone).

Użycie: python3 panel/wypelnienia.py   → zapisuje data/wypelnienia.json
Ten sam wynik nakłada panel/build.py na dziennik przy budowie strony.
"""
import csv, datetime, json, os, re, sys
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402

PL = ZoneInfo("Europe/Warsaw")
UTC = datetime.timezone.utc
SWING = build.SWING
# Okna nowych wejść (czas PL) z ryzyko.md, sekcja 4; używane, gdy zlecenie nie podaje własnych.
OKNA = {"gold": ["09:00-12:00", "14:00-20:00"], "silver": ["09:00-12:00", "14:00-20:00"],
        "wti": ["09:00-12:00", "15:00-20:30"], "ng": ["15:00-20:30"], "nq": ["15:45-21:30"]}
ZAMKNIECIE = datetime.time(22, 30)


def candles(key):
    f = f"{build.LIVE}/data/{key}_15m.csv"
    if not os.path.exists(f): return []
    out = []
    for r in csv.DictReader(open(f)):
        if not r["Close"]: continue
        t = datetime.datetime.fromisoformat(r["Datetime_UTC"].replace("Z", "+00:00"))
        out.append((t, float(r["High"]), float(r["Low"]), float(r["Close"])))
    return out


def okna(row, k):
    txt = f"{row.get('Status', '')} {row.get('Uwagi', '')}"
    m = re.search(r"okn[ao][^|]*", txt)
    pary = re.findall(r"(\d{1,2}:\d{2})\s*[–-]\s*(\d{1,2}:\d{2})", m.group(0)) if m else []
    if not pary: pary = [tuple(o.split("-")) for o in OKNA.get(k, [])]
    return [(datetime.time.fromisoformat(a.zfill(5)), datetime.time.fromisoformat(b.zfill(5))) for a, b in pary]


def termin_swing(row, start):
    m = re.search(r"do (\d{1,2})\.(\d{1,2})", row.get("Status", ""))
    if not m: return start + datetime.timedelta(days=14)
    d = datetime.date(start.year, int(m.group(2)), int(m.group(1)))
    return datetime.datetime.combine(d, datetime.time(23, 59), PL)


def symuluj(row, k):
    e, sl, = build.num(row.get("Wejście")), build.num(row.get("SL"))
    tps = [build.num(x) for x in row.get("TP", "").split("/") if build.num(x) is not None]
    if None in (e, sl) or not tps: return None
    try:
        start = datetime.datetime.fromisoformat(row["Data otwarcia (UTC)"].strip()).replace(tzinfo=UTC)
    except ValueError:
        return None
    swing = k in SWING
    spot = "spot" in row.get("Instrument", "")
    key = {"gold": "xauusd", "silver": "xagusd"}.get(k, k) if spot else k
    cs = [c for c in candles(key) if c[0] >= start]
    d = 1 if row.get("Kierunek", "").upper() == "LONG" else -1
    tp1, tp2 = tps[0], tps[-1]
    risk = abs(e - sl)
    if swing:
        koniec_wejsc = koniec = termin_swing(row, start)
    else:
        dzien = start.astimezone(PL).date()
        koniec = datetime.datetime.combine(dzien, ZAMKNIECIE, PL)
        koniec_wejsc = koniec
        ok = okna(row, k)
    res = {"nr": row["#"], "instrument": row["Instrument"], "kierunek": d, "klucz_cen": key, "zdarzenia": [],
           "stan": "oczekuje", "pozostalo": 1.0, "sl_teraz": sl}
    fill = None
    for i, (t, h, l, c) in enumerate(cs):
        if t >= koniec_wejsc: break
        if not swing:
            lt = t.astimezone(PL).time()
            if not any(a <= lt < b for a, b in ok): continue
        if l <= e <= h:
            fill = i
            res["stan"], res["czas_wejscia"] = "otwarta", t.strftime("%Y-%m-%dT%H:%MZ")
            res["zdarzenia"].append(f"{t.astimezone(PL):%d.%m %H:%M} PL wejście {e:g}")
            break
    if fill is None:
        now = datetime.datetime.now(UTC)
        if now >= koniec_wejsc:
            res["stan"] = "wygasło"
            res["zdarzenia"].append("zlecenie niewypełnione, termin minął")
        return res
    cur_sl, left, be, realized = sl, 1.0, False, 0.0   # realized w jednostkach ceny × część pozycji
    exits = []
    for j, (t, h, l, c) in enumerate(cs[fill:]):
        tpl = f"{t.astimezone(PL):%d.%m %H:%M} PL"
        if not swing and t >= koniec:
            break
        hit_sl = (l <= cur_sl) if d == 1 else (h >= cur_sl)
        if hit_sl:
            exits.append((cur_sl, left)); realized += d * (cur_sl - e) * left; left = 0
            res["zdarzenia"].append(f"{tpl} {'BE' if be else 'SL'} {cur_sl:g}")
            break
        if j == 0: continue   # w świecy wejścia liczymy tylko SL
        best = h if d == 1 else l
        if left == 1.0 and d * (best - tp1) >= 0 and tp1 != tp2:
            exits.append((tp1, 0.5)); realized += d * (tp1 - e) * 0.5; left = 0.5
            res["zdarzenia"].append(f"{tpl} TP1 {tp1:g}, zamknięte 50%")
        if d * (best - tp2) >= 0:
            exits.append((tp2, left)); realized += d * (tp2 - e) * left; left = 0
            res["zdarzenia"].append(f"{tpl} TP2 {tp2:g}")
            break
        if not be and d * (best - e) >= risk:
            be, cur_sl = True, e
            res["zdarzenia"].append(f"{tpl} +1R, SL na BE {e:g}")
    if left > 0 and not swing and datetime.datetime.now(UTC) >= koniec:
        last = [x for x in cs[fill:] if x[0] < koniec]
        px = last[-1][3] if last else e
        exits.append((px, left)); realized += d * (px - e) * left; left = 0
        res["zdarzenia"].append(f"22:30 PL zamknięcie dnia po {px:g}")
    res["pozostalo"], res["sl_teraz"] = left, cur_sl
    if exits:
        done = sum(p for _, p in exits)
        res["cena_wyjscia_srednia"] = round(sum(px * p for px, p in exits) / done, 4)
        res["wynik_pkt_zrealizowany"] = round(realized, 4)   # na całą pozycję (część × punkty)
    if left == 0: res["stan"] = "zamknięta"
    return res


def licz():
    out = {}
    for r in build.journal():
        st = r.get("Status", "")
        if not st.startswith(("oczekuje", "otwarta")): continue
        k = build.ALIAS.get(r.get("Instrument", ""))
        if not k: continue
        s = symuluj(r, k)
        if s: out[r["#"]] = s
    return out


if __name__ == "__main__":
    res = {"zaktualizowano_utc": datetime.datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "opis": "Automatyczne pilnowanie zleceń z dziennika na świecach 15m (panel/wypelnienia.py)", "zlecenia": licz()}
    json.dump(res, open(f"{build.LIVE}/data/wypelnienia.json", "w"), ensure_ascii=False, indent=1)
    for nr, z in res["zlecenia"].items():
        print(nr, z["instrument"], z["stan"], "; ".join(z["zdarzenia"]))
