#!/usr/bin/env python3
"""Buduje statyczny pulpit Claude Finance dla GitHub Pages.

Wejście (wszystko w repo):
  panel/projekt/dane/sygnaly.json          sygnały i setupy agentów
  panel/projekt/agenci/paper_trading.md    dziennik paper tradingu (pozycje)
  panel/projekt/raporty/*.html|md          raporty PR dla inwestorów
  panel/projekt/dane/intraday_poziomy_*.csv pivoty dnia
  data/                                    ceny z fetch_prices.py

Użycie: python3 panel/build.py [katalog_wyjściowy]   (domyślnie _site)
Wynik: index.html, panel.json, pozycje.json
"""
import csv, json, os, sys, datetime
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "projekt")
D1 = f"{ROOT}/dane/d1_investing"
LIVE = os.path.dirname(HERE)   # katalog repo z data/

def load_csv(name):
    key = name.rsplit(".", 1)[0]
    f = f"{LIVE}/data/{key}_1d.csv"
    if os.path.exists(f):   # świeże świece dzienne z Yahoo (fetch_prices.py)
        rows = [dict(date=r["Datetime_UTC"][:10], o=float(r["Open"]), h=float(r["High"]), l=float(r["Low"]), c=float(r["Close"]))
                for r in csv.DictReader(open(f)) if r["Close"]]
        return rows[-130:]
    with open(f"{D1}/{name}") as f:
        rows = [dict(date=r["Date"], o=float(r["Open"]), h=float(r["High"]), l=float(r["Low"]), c=float(r["Close"]))
                for r in csv.DictReader(f)]
    return sorted(rows, key=lambda r: r["date"])

def atr14(rows):
    trs = [max(r["h"]-r["l"], abs(r["h"]-p["c"]), abs(r["l"]-p["c"])) for p, r in zip(rows, rows[1:])]
    return sum(trs[-14:]) / min(14, len(trs)) if trs else None

def journal():
    out, hdr = [], None
    for line in open(f"{ROOT}/agenci/paper_trading.md"):
        if not line.startswith("|"): continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "): continue
        if hdr is None: hdr = cells; continue
        out.append(dict(zip(hdr, cells)))
    return out

PIV = {"US100":"nq","Zloto":"gold","Srebro":"silver","WTI":"wti","NatGas":"ng","Kakao":"cocoa","Kawa":"coffee"}

def pivots():
    out = {}
    import glob
    files = sorted(glob.glob(f"{ROOT}/dane/intraday_poziomy_*.csv"))
    if not files: return out, None
    for r in csv.DictReader(open(files[-1])):
        k = PIV.get(r["instrument"])
        if k: out[k] = {c: (float(v) if c not in ("instrument","baza_dnia","ATR_H1_zrodlo") else v) for c, v in r.items() if v != ""}
    return out, os.path.basename(files[-1])

def num(v):
    try: return float(str(v).replace(" ", "").replace(",", "."))
    except: return None

def sizing(ins, kapital):
    s, k = ins["setup"], ins.get("kontrakt")
    if not k or not s.get("ryzyko_pct") or s.get("sl") is None: return None
    risk = kapital * s["ryzyko_pct"] / 100
    dist = abs(s["wejscie"] - s["sl"]) + (s.get("koszt") or 0)
    units = risk / (dist * k["usd_na_jedn_cfd"])
    contracts = risk / (dist * k["usd_na_jedn_ceny"])
    return {"ryzyko_usd": round(risk), "jednostki_cfd": round(units, 2), "kontrakty": round(contracts, 2),
            "nominal_usd": round(units * s["wejscie"] * k["usd_na_jedn_cfd"])}

ALIAS = {"US100": "nq", "Nasdaq 100": "nq", "Złoto": "gold", "Srebro": "silver", "Ropa WTI": "wti", "WTI": "wti",
         "Gaz ziemny": "ng", "Złoto (XAUUSD spot)": "gold", "Złoto (XAUUSD)": "gold", "NatGas": "ng", "Kawa US": "coffee", "Kakao US": "cocoa"}

def journal_sized(rows, sig):
    by = {i["id"]: i for i in sig["instrumenty"]}
    kap = sig.get("kapital", 0)
    for r in rows:
        ins = by.get(ALIAS.get(r.get("Instrument", "")))
        e, sl, rp = num(r.get("Wejście")), num(r.get("SL")), num(r.get("Ryzyko %"))
        r["_id"] = ins["id"] if ins else None
        if ins and e and sl and rp and e != sl:
            k = ins["kontrakt"]; risk = kap * rp / 100; dist = abs(e - sl)
            r["_ryzyko_usd"] = round(risk)
            r["_kontrakty"] = round(risk / (dist * k["usd_na_jedn_ceny"]), 2)
            r["_jednostki"] = round(risk / (dist * k["usd_na_jedn_cfd"]), 2)
            r["_jedn"] = k["jedn_cfd"]
            R = num(r.get("Wynik (R)"))
            r["_wynik_usd"] = None
            if r.get("Status", "").startswith("zamknięta"):   # wynik zrealizowany tylko dla zamkniętych
                import re
                m = re.match(r"\s*([\d\s]+[\d])", r.get("Wielkość", ""))
                cl = num(r.get("Zamknięcie"))
                d = 1 if r.get("Kierunek", "").upper() == "LONG" else -1
                if m and cl is not None:
                    r["_wynik_usd"] = round(d * (cl - e) * float(m.group(1).replace(" ", "")) * k["usd_na_jedn_cfd"])
                elif R is not None:
                    r["_wynik_usd"] = round(R * risk)
    return rows

ALLOWED = {"h1", "h2", "h3", "p", "ul", "ol", "li", "b", "strong", "em", "i", "q", "blockquote", "br", "table", "thead", "tbody", "tr", "th", "td", "small", "span", "time", "section", "header", "footer", "div"}

def sanitize(html_text):
    """Raport PR → bezpieczny podzbiór HTML (bez stylów, skryptów, linków i atrybutów)."""
    from html.parser import HTMLParser
    from html import escape
    out, skip = [], []
    class P(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag in ("style", "script", "title", "head"): skip.append(tag); return
            if not skip and tag in ALLOWED: out.append(f"<{tag}>")
        def handle_endtag(self, tag):
            if skip and tag == skip[-1]: skip.pop(); return
            if not skip and tag in ALLOWED and tag != "br": out.append(f"</{tag}>")
        def handle_data(self, data):
            if not skip: out.append(escape(data))
    P(convert_charrefs=True).feed(html_text)
    return "".join(out)

def reports():
    import glob, re
    out = []
    files = glob.glob(f"{ROOT}/raporty/**/*.md", recursive=True) + glob.glob(f"{ROOT}/raporty/**/*.html", recursive=True)
    for f in sorted(files, key=os.path.basename, reverse=True)[:10]:
        txt = open(f).read()
        if f.endswith(".html"):
            m = re.search(r"<title>(.*?)</title>", txt, re.S)
            title = m.group(1).strip() if m else os.path.basename(f)
            body = sanitize(txt)
        else:
            title = next((l.lstrip("# ").strip() for l in txt.splitlines() if l.startswith("#")), os.path.basename(f))
            body = None
        out.append({"plik": os.path.relpath(f, ROOT), "tytul": title, "html": body, "tekst": None if body else txt[:6000],
                    "zmieniono": datetime.datetime.fromtimestamp(os.path.getmtime(f), datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
    return out

SPOT_KEY = {"gold": "xauusd", "silver": "xagusd"}   # spot z repo (Swissquote); świece spot = futures + baza
SPOT_OFFSET = {"gold": 24.5}   # zapas, gdy w repo brak spotu: XAUUSD ≈ GC=F − 24,5 USD

def fetch_live():
    if not os.path.exists(LIVE + "/data/latest.json"): return None
    latest = json.load(open(LIVE + "/data/latest.json"))
    h1 = {}
    for k in ("nq", "gold", "silver", "wti", "ng", "coffee", "cocoa", "xauusd", "xagusd"):
        f = f"{LIVE}/data/{k}_1h.csv"
        if os.path.exists(f):
            rows = list(csv.DictReader(open(f)))[-72:]
            h1[k] = [dict(t=r["Datetime_UTC"], o=float(r["Open"]), h=float(r["High"]), l=float(r["Low"]), c=float(r["Close"])) for r in rows if r["Close"]]
    status = json.load(open(LIVE + "/data/status.json")) if os.path.exists(LIVE + "/data/status.json") else {}
    return {"latest": latest, "h1": h1, "status": status}

SWING = {"coffee", "cocoa"}

def po_terminie(r, k):
    """Pozycja intraday otwarta przed dzisiejszą sesją: zasada zamknięcia do 22:30 PL już minęła."""
    if k in SWING: return False
    try:
        d = datetime.date.fromisoformat(r.get("Data otwarcia (UTC)", "")[:10])
    except ValueError:
        return False
    from zoneinfo import ZoneInfo
    cutoff = datetime.datetime.combine(d, datetime.time(22, 30), ZoneInfo("Europe/Warsaw"))
    return datetime.datetime.now(datetime.timezone.utc) > cutoff + datetime.timedelta(minutes=30)

def open_positions(rows, sig, live):
    import re
    by = {i["id"]: i for i in sig["instrumenty"]}
    out = []
    if not live: return out
    L = live["latest"].get("instrumenty", {})
    for r in rows:
        if not r.get("Status", "").startswith("otwarta"): continue
        k = r.get("_id"); ins = by.get(k)
        m = re.match(r"\s*([\d\s]+[\d])", r.get("Wielkość", ""))
        if not ins or not m or k not in L: continue
        units = float(m.group(1).replace(" ", ""))
        e, sl = num(r["Wejście"]), num(r["SL"])
        tp = [num(x) for x in r.get("TP", "").split("/")]
        spot = "spot" in r.get("Instrument", "")
        sk = SPOT_KEY.get(k) if spot else None
        if sk and sk in L:
            src, off, cur, h1key = L[sk], 0, L[sk]["cena"], sk
        else:
            off = SPOT_OFFSET.get(k, 0) if spot else 0
            src, cur, h1key = L[k], L[k]["cena"] - off, k
        d = 1 if r["Kierunek"].upper() == "LONG" else -1
        u = ins["kontrakt"]["usd_na_jedn_cfd"]
        pnl = d * (cur - e) * units * u
        risk = abs(e - sl) * units * u
        out.append({"nr": r["#"], "po_terminie": po_terminie(r, k), "id": k, "nazwa": ins["nazwa"], "instrument": r["Instrument"], "kierunek": r["Kierunek"].upper(),
                    "wejscie": e, "sl": sl, "tp1": tp[0] if tp else None, "tp2": tp[1] if len(tp) > 1 else None,
                    "jednostki": units, "usd_na_jedn": u, "jedn": ins["kontrakt"]["jedn_cfd"], "cena": round(cur, 4), "cena_futures": L[k]["cena"], "h1_key": h1key,
                    "spot_offset": off, "symbol": src["symbol"], "zrodlo": src.get("zrodlo", "Yahoo Finance"), "czas": src["czas_notowania_utc"],
                    "pnl_usd": round(pnl), "ryzyko_usd": round(risk), "r": round(pnl / risk, 2) if risk else None,
                    "status": r["Status"], "uwagi": r.get("Uwagi", "")})
    return out

def build():
    sig = json.load(open(f"{ROOT}/dane/sygnaly.json"))
    readme = open(f"{LIVE}/README.md").read()
    kap = sig.get("kapital", 0)
    piv, pivfile = pivots()
    for ins in sig["instrumenty"]:
        ins["wielkosc"] = sizing(ins, kap)
        ins["pivoty"] = piv.get(ins["id"])
        rows = load_csv(ins["csv"])
        ins["ohlc"] = rows
        ins["atr_obliczony"] = round(atr14(rows), 4)
    live = fetch_live()
    dz = journal_sized(journal(), sig)
    return {
        "live": {"zaktualizowano_utc": live["latest"].get("zaktualizowano_utc"), "ceny": {k: {kk: v.get(kk) for kk in ("symbol", "cena", "czas_notowania_utc", "zmiana_pct", "dzien")} for k, v in live["latest"].get("instrumenty", {}).items()}, "h1": live["h1"], "bledy": live["status"].get("bledy", {})} if live else None,
        "pozycje": open_positions(dz, sig, live),
        "zbudowano": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "zrodlo_danych": "Yahoo Finance (kontrakty futures, świece dzienne z repo claude-finance-data)",
        "readme": readme,
        "sygnaly": sig,
        "dziennik": dz,
        "pivoty_plik": pivfile,
        "dziennik_sync": (json.load(open(f"{ROOT}/sync.json")).get("zsynchronizowano_utc") if os.path.exists(f"{ROOT}/sync.json") else None),
        "raporty": reports(),
    }

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(LIVE, "_site")
    os.makedirs(out, exist_ok=True)
    data = build()
    js = json.dumps(data, ensure_ascii=False)
    open(f"{out}/panel.json", "w").write(js)
    json.dump({"zbudowano": data["zbudowano"], "pozycje": data["pozycje"]}, open(f"{out}/pozycje.json", "w"), ensure_ascii=False, indent=1)
    html = open(os.path.join(HERE, "szablon.html")).read().replace("__PANEL_DATA__", js.replace("</", "<\\/"))
    open(f"{out}/index.html", "w").write(html)
    open(f"{out}/.nojekyll", "w").close()
    print(f"{out}: panel.json {len(js)} B, {len(data['pozycje'])} otwartych pozycji, {len(data['dziennik'])} wpisów w dzienniku")
