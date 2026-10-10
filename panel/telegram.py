#!/usr/bin/env python3
"""Bot Telegram Claude Finance: komunikaty desku transakcyjnego i polecenia.

Komunikaty (porównanie z ostatnio wysłanym stanem w data/telegram_stan.json, wysyłane tylko różnice):
  - rekomendacje komitetu: zmiana kierunku/przekonania albo poziomów setupu (panel/projekt/dane/sygnaly.json),
  - dziennik: nowe zlecenie i zmiana statusu, SL lub TP (panel/projekt/agenci/paper_trading.md),
  - automat zleceń: wejście, SL na BE, TP1, TP2, SL, zamknięcie sesji, wygaśnięcie (data/wypelnienia.json),
  - przegląd rynków: rano (od 08:00 PL) i wieczorem (od 22:30 PL), pon.–pt.

Polecenia (tylko z czatu TELEGRAM_CHAT_ID; odbiór przez getUpdates, przesunięcie w data/telegram_komendy.json):
  /status /pozycje /sygnaly /rynek <instrument> /rynki /raport /pomoc

Sekrety: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID. Bez nich skrypt tylko wypisuje wiadomości i nie zmienia stanu.
TELEGRAM_TRYB (domyślnie PAPER) trafia do nagłówka wiadomości; przy prawdziwym koncie ustaw REAL.
Pierwsze uruchomienie z sekretami zapamiętuje bieżący stan i wysyła jedną wiadomość powitalną z przeglądem rynków.

Użycie: python3 panel/telegram.py                    → komunikaty (+ przegląd, jeśli pora)
        python3 panel/telegram.py komendy            → odpowiedz na polecenia z czatu
        python3 panel/telegram.py podsumowanie       → przegląd rynków od razu
        python3 panel/telegram.py test               → wiadomość testowa
        python3 panel/telegram.py --sucho [...]      → tylko wypisz, nic nie wysyłaj ani nie zapisuj
        python3 panel/telegram.py --sucho /rynek zloto → podgląd odpowiedzi na polecenie
"""
import datetime, glob, html, json, os, re, sys, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402

PL = ZoneInfo("Europe/Warsaw")
UTC = datetime.timezone.utc
STAN = f"{build.LIVE}/data/telegram_stan.json"
KOMENDY = f"{build.LIVE}/data/telegram_komendy.json"
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
TRYB = os.environ.get("TELEGRAM_TRYB", "PAPER").strip().upper() or "PAPER"
RACHUNEK = "rachunek rzeczywisty" if TRYB == "REAL" else "rachunek modelowy"
PANEL = "https://kubula-xu.github.io/claude-finance-data/"
KIER = {"LONG": "▲ LONG", "SHORT": "▼ SHORT", "BRAK": "■ brak pozycji", "NEUTRAL": "■ neutralnie"}
AKTYWNE = ("oczekuje", "otwarta")
RANO, WIECZOR = datetime.time(8, 0), datetime.time(22, 30)
ZASTRZEZENIE = "<i>Materiał wewnętrzny Claude Finance. Nie stanowi rekomendacji inwestycyjnej.</i>"


def e(x):
    return html.escape(str(x), quote=False)


def naglowek(dzial, tytul):
    return f"<b>CLAUDE FINANCE</b> │ {e(dzial)} │ {TRYB}\n<b>{e(tytul)}</b>"


def wczytaj(f, domyslne):
    try:
        return json.load(open(f))
    except (OSError, ValueError):
        return domyslne


def sygnaly():
    return wczytaj(f"{build.ROOT}/dane/sygnaly.json", {"instrumenty": []})


def ceny():
    return wczytaj(f"{build.LIVE}/data/latest.json", {"instrumenty": {}})["instrumenty"]


def automat():
    return wczytaj(f"{build.LIVE}/data/wypelnienia.json", {"zlecenia": {}}).get("zlecenia", {})


def fmt(v, dec=2):
    if v is None: return "–"
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


def zn(v, dec=2):
    return ("+" if v >= 0 else "−") + fmt(abs(v), dec)


# ---------- migawki stanu ----------

def migawka_sygnalow(sig):
    out = {}
    for i in sig.get("instrumenty", []):
        f, s = i.get("final", {}), i.get("setup", {})
        out[i["id"]] = {"kierunek": f.get("kierunek"), "pewnosc": f.get("pewnosc"),
                        "setup": [s.get("kierunek"), s.get("wejscie"), s.get("sl"), s.get("tp1"), s.get("tp2")]}
    return out


def migawka_dziennika():
    return {r["#"]: {"status": r.get("Status", ""), "sl": r.get("SL", ""), "tp": r.get("TP", "")}
            for r in build.journal() if r.get("#")}


def migawka_automatu():
    return {nr: {"stan": v.get("stan"), "zdarzenia": v.get("zdarzenia", [])} for nr, v in automat().items()}


# ---------- komunikaty ----------

def parametry(r):
    lin = [f"Kierunek: {KIER.get(r.get('Kierunek', '').upper(), e(r.get('Kierunek', '')))}",
           f"Wejście: {e(r.get('Wejście', ''))} · Stop: {e(r.get('SL', ''))} · Cele: {e(r.get('TP', ''))}"]
    if r.get("Ryzyko %"):
        lin.append(f"Ryzyko: {e(r['Ryzyko %'])}% kapitału" + (f" · Wolumen: {e(r['Wielkość'])}" if r.get("Wielkość") else ""))
    return lin


def wiadomosci_sygnalow(sig, stare, nowe):
    out = []
    by = {i["id"]: i for i in sig.get("instrumenty", [])}
    for k, n in nowe.items():
        s = stare.get(k)
        if s == n or s is None and n["kierunek"] in (None, "BRAK"): continue
        i, f, st = by[k], by[k].get("final", {}), by[k].get("setup", {})
        zmiana_kier = s is None or (s["kierunek"], s["pewnosc"]) != (n["kierunek"], n["pewnosc"])
        if not zmiana_kier and n["kierunek"] in (None, "BRAK"): continue   # setup bez sygnału nie jest wiadomością
        nazwa = i.get("nazwa", k)
        tytul = f"Rekomendacja: {nazwa}" if zmiana_kier else f"Aktualizacja planu transakcji: {nazwa}"
        lin = [naglowek("Komitet inwestycyjny", tytul), "",
               f"Stanowisko: <b>{KIER.get(n['kierunek'], e(n['kierunek']))}</b> · przekonanie {e(n['pewnosc'])}/3"
               + (f" (poprzednio {KIER.get(s['kierunek'], e(s['kierunek']))}, {e(s['pewnosc'])}/3)" if s and zmiana_kier else "")]
        if f.get("powod"): lin.append(f"Teza: {e(f['powod'])}")
        if n["kierunek"] not in (None, "BRAK") and st.get("wejscie") is not None:
            lin += ["", f"Plan: zlecenie {e(st.get('typ', ''))} {e(st.get('kierunek', ''))} {e(st['wejscie'])}",
                    f"Stop: {e(st.get('sl'))} · Cele: {e(st.get('tp1'))} / {e(st.get('tp2'))}"
                    + (f" · Ryzyko: {fmt(st['ryzyko_pct'], 2)}%" if st.get("ryzyko_pct") else "")]
            if st.get("status"): lin.append(f"Status: {e(st['status'])}")
        out.append("\n".join(lin))
    return out


def wiadomosci_dziennika(stare, nowe):
    out = []
    rows = {r["#"]: r for r in build.journal() if r.get("#")}
    for nr, n in nowe.items():
        r, s = rows[nr], stare.get(nr)
        nazwa = f"{r.get('Instrument', '')} (#{nr})"
        if s is None:
            if not n["status"].startswith(AKTYWNE): continue
            tyt = "Złożenie zlecenia" if n["status"].startswith("oczekuje") else "Otwarcie pozycji"
            lin = [naglowek("Desk transakcyjny", f"{tyt}: {nazwa}"), "", *parametry(r), f"Status: {e(n['status'])}"]
            if r.get("Uwagi"): lin += ["", f"<i>{e(r['Uwagi'][:300])}</i>"]
            out.append("\n".join(lin))
            continue
        if s["status"] != n["status"]:
            st = n["status"]
            if st.startswith("zamknięta"):
                lin = [naglowek("Desk transakcyjny", f"Zamknięcie pozycji: {nazwa}"), "",
                       f"Sposób: {e(st)}",
                       f"Cena zamknięcia: {e(r.get('Zamknięcie', '–'))} · Wynik: {e(r.get('Wynik (pkt)', '–'))} pkt / {e(r.get('Wynik (R)', '–'))} R"]
            elif st.startswith("anulowana"):
                lin = [naglowek("Desk transakcyjny", f"Anulowanie zlecenia: {nazwa}"), "", f"Powód: {e(st)}"]
            else:
                tyt = "Otwarcie pozycji" if st.startswith("otwarta") else "Zmiana statusu"
                lin = [naglowek("Desk transakcyjny", f"{tyt}: {nazwa}"), "", *parametry(r), f"Status: {e(st)}"]
            out.append("\n".join(lin))
        elif (s["sl"], s["tp"]) != (n["sl"], n["tp"]):
            lin = [naglowek("Zarządzanie ryzykiem", f"Korekta poziomów: {nazwa}"), ""]
            if s["sl"] != n["sl"]: lin.append(f"Stop: {e(s['sl'])} → <b>{e(n['sl'])}</b>")
            if s["tp"] != n["tp"]: lin.append(f"Cele: {e(s['tp'])} → <b>{e(n['tp'])}</b>")
            out.append("\n".join(lin))
    return out


def opis_zdarzenia(z):
    """Zdarzenie automatu → (dział, tytuł, czas, cena)."""
    m = re.match(r"(\d{2}\.\d{2} \d{2}:\d{2} PL|\d{2}:\d{2} PL)\s*(.*)", z)
    czas, rest = (m.group(1), m.group(2)) if m else ("", z)
    ceny_ = re.findall(r"\d+(?:\.\d+)?", rest.replace("+1R", "").replace("TP1", "").replace("TP2", "").replace("50%", ""))
    cena = ceny_[-1] if ceny_ else None
    if rest.startswith("wejście"): return "Desk transakcyjny", "Otwarcie pozycji (realizacja limitu)", czas, cena
    if rest.startswith("TP1"): return "Desk transakcyjny", "Częściowa realizacja zysku (TP1, 50% pozycji)", czas, cena
    if rest.startswith("TP2"): return "Desk transakcyjny", "Realizacja celu końcowego (TP2)", czas, cena
    if "SL na BE" in rest: return "Zarządzanie ryzykiem", "Stop przeniesiony na cenę wejścia", czas, cena
    if rest.startswith("BE"): return "Zarządzanie ryzykiem", "Zamknięcie na stopie zabezpieczającym (bez straty)", czas, cena
    if rest.startswith("SL"): return "Zarządzanie ryzykiem", "Stop loss wykonany", czas, cena
    if "zamknięcie dnia" in rest: return "Desk transakcyjny", "Zamknięcie pozycji na koniec sesji", czas, cena
    if "niewypełnione" in rest: return "Desk transakcyjny", "Zlecenie wygasło bez realizacji", czas, None
    return "Desk transakcyjny", rest, czas, cena


def wiadomosci_automatu(stare, nowe):
    out = []
    auto = automat()
    for nr, n in nowe.items():
        widziane = set((stare.get(nr) or {}).get("zdarzenia", []))
        for z in n["zdarzenia"]:
            if z in widziane: continue
            a = auto[nr]
            dzial, tytul, czas, cena = opis_zdarzenia(z)
            lin = [naglowek(dzial, f"{tytul}: {a.get('instrument', '')} (#{nr})"), ""]
            if cena: lin.append(f"Cena: {e(cena)}" + (f" · Czas: {e(czas)}" if czas else ""))
            elif czas: lin.append(f"Czas: {e(czas)}")
            if z == n["zdarzenia"][-1]:
                if a.get("stan") == "zamknięta" and a.get("wynik_pkt_zrealizowany") is not None:
                    lin.append(f"Pozycja zamknięta w całości · średnia cena wyjścia {fmt(a.get('cena_wyjscia_srednia'), 2)} · "
                               f"wynik {zn(a['wynik_pkt_zrealizowany'], 2)} pkt")
                elif a.get("stan") == "otwarta":
                    lin.append(f"Pozostaje otwarte: {int(round(a.get('pozostalo', 1) * 100))}% · stop {fmt(a.get('sl_teraz'), 2)}")
            lin.append("<i>Wykonanie wg automatu na świecach 15 min; do potwierdzenia u brokera.</i>")
            out.append("\n".join(lin))
    return out


def aktywne():
    return [r for r in build.journal() if r.get("Status", "").startswith(AKTYWNE)]


def przeglad(tytul="Przegląd rynków"):
    sig, cn = sygnaly(), ceny()
    lin = [naglowek("Research", f"{tytul} · {datetime.datetime.now(PL):%d.%m %H:%M}"), ""]
    for i in sig.get("instrumenty", []):
        c = cn.get(i["id"], {})
        f = i.get("final", {})
        zm = c.get("zmiana_pct")
        kier = f.get("kierunek", "BRAK")
        lin.append(f"<b>{e(i.get('nazwa', i['id']))}</b> {fmt(c.get('cena'), i.get('dec', 2))}"
                   f" ({zn(zm) + '%' if zm is not None else '–'}) · {KIER.get(kier, e(kier))}"
                   + (f" {e(f.get('pewnosc'))}/3" if kier not in ("BRAK", None) else ""))
    tlo = [f"{n} {fmt(cn[k].get('cena'), d)}" for k, n, d in (("dxy", "DXY", 2), ("us10y", "US10Y", 3), ("vix", "VIX", 2)) if k in cn]
    if tlo: lin += ["", "Otoczenie: " + " · ".join(tlo)]
    akt, auto = aktywne(), automat()
    lin += ["", "<b>Ekspozycja</b>" if akt else "Brak otwartych pozycji i zleceń oczekujących."]
    for r in akt:
        stan = auto.get(r["#"], {}).get("stan") or r["Status"].split(" ")[0]
        lin.append(f"#{e(r['#'])} {e(r.get('Instrument', ''))} {e(r.get('Kierunek', ''))} {e(r.get('Wejście', ''))} · stop {e(r.get('SL', ''))} · {e(stan)}")
    lin += ["", f'<a href="{PANEL}">Panel</a> · /pomoc', ZASTRZEZENIE]
    return "\n".join(lin)


# ---------- polecenia ----------

ALIASY = {"nq": "nq", "nasdaq": "nq", "us100": "nq", "ndx": "nq", "gold": "gold", "zloto": "gold", "złoto": "gold",
          "xauusd": "gold", "silver": "silver", "srebro": "silver", "xagusd": "silver", "wti": "wti", "ropa": "wti",
          "oil": "wti", "ng": "ng", "gaz": "ng", "natgas": "ng", "coffee": "coffee", "kawa": "coffee",
          "cocoa": "cocoa", "kakao": "cocoa"}
POLECENIA = [("status", "Stan rachunku i ekspozycji"), ("pozycje", "Otwarte pozycje i zlecenia z wynikiem"),
             ("sygnaly", "Stanowisko komitetu na każdym rynku"), ("rynek", "Szczegóły rynku, np. /rynek zloto"),
             ("rynki", "Przegląd wszystkich rynków"), ("raport", "Ostatni raport dla inwestorów"),
             ("pomoc", "Lista poleceń")]


def kapital():
    txt = open(f"{build.ROOT}/agenci/paper_trading.md").read()
    m = re.findall(r"kapitał (\d[\d  ]*\d) USD", txt)
    return float(m[-1].replace(" ", "").replace(" ", "")) if m else sygnaly().get("kapital")


def wycena(r):
    """Bieżąca wycena otwartej pozycji: (cena, pkt, R, USD) albo None."""
    k = build.ALIAS.get(r.get("Instrument", ""))
    a = automat().get(r["#"], {})
    klucz = a.get("klucz_cen") or ({"gold": "xauusd", "silver": "xagusd"}.get(k, k) if "spot" in r.get("Instrument", "") else k)
    c = ceny().get(klucz, {}).get("cena")
    e_, sl = build.num(r.get("Wejście")), build.num(r.get("SL"))
    if c is None or e_ is None or sl is None or e_ == sl: return None
    d = 1 if r.get("Kierunek", "").upper() == "LONG" else -1
    pkt = d * (c - e_)
    usd = None
    m = re.match(r"\s*([\d\s]+[\d])", r.get("Wielkość", ""))
    ins = {i["id"]: i for i in sygnaly().get("instrumenty", [])}.get(k)
    if m and ins and ins.get("kontrakt"):
        usd = pkt * float(m.group(1).replace(" ", "")) * ins["kontrakt"]["usd_na_jedn_cfd"] * a.get("pozostalo", 1.0)
    return c, pkt, pkt / abs(e_ - sl), usd


def cmd_status(_):
    kap, start = kapital(), sygnaly().get("kapital")
    akt, auto = aktywne(), automat()
    otw = [r for r in akt if (auto.get(r["#"], {}).get("stan") or r["Status"]) .startswith("otwarta")]
    lin = [naglowek("Raport zarządczy", "Stan rachunku"), "",
           f"Rachunek: {RACHUNEK}",
           f"Kapitał (ostatnie zamknięcie): <b>{fmt(kap, 0)} USD</b>"
           + (f" ({zn((kap - start) / start * 100)}% od startu)" if kap and start else ""),
           f"Pozycje otwarte: {len(otw)} · zlecenia oczekujące: {len(akt) - len(otw)}"]
    niezr = [w[3] for w in (wycena(r) for r in otw) if w and w[3] is not None]
    if niezr: lin.append(f"Wynik niezrealizowany: {zn(sum(niezr), 0)} USD")
    lt = wczytaj(f"{build.LIVE}/data/latest.json", {}).get("zaktualizowano_utc")
    if lt:
        t = datetime.datetime.fromisoformat(lt.replace("Z", "+00:00")).astimezone(PL)
        lin.append(f"Notowania z: {t:%d.%m %H:%M} PL")
    lin += ["", "Szczegóły: /pozycje · /sygnaly · /rynki"]
    return "\n".join(lin)


def cmd_pozycje(_):
    akt, auto = aktywne(), automat()
    lin = [naglowek("Desk transakcyjny", "Pozycje i zlecenia"), ""]
    if not akt: lin.append("Brak otwartych pozycji i zleceń oczekujących.")
    for r in akt:
        a = auto.get(r["#"], {})
        stan = a.get("stan") or r["Status"].split(" ")[0]
        lin.append(f"<b>#{e(r['#'])} {e(r.get('Instrument', ''))}</b> · {KIER.get(r.get('Kierunek', '').upper(), e(r.get('Kierunek', '')))} · {e(stan)}")
        sl = r.get("SL", "") if a.get("sl_teraz") in (None, build.num(r.get("SL"))) else fmt(a["sl_teraz"], 2)
        lin.append(f"Wejście {e(r.get('Wejście', ''))} · stop {e(sl)} · cele {e(r.get('TP', ''))}")
        w = wycena(r)
        if w and stan == "otwarta":
            lin.append(f"Kurs {fmt(w[0], 2)} · {zn(w[1])} pkt · {zn(w[2])} R" + (f" · {zn(w[3], 0)} USD" if w[3] is not None else ""))
        elif w:
            lin.append(f"Kurs {fmt(w[0], 2)} · do wejścia {fmt(abs(w[1]), 2)} pkt · ważność: {e(r['Status'])}")
        lin.append("")
    return "\n".join(lin).rstrip()


def cmd_sygnaly(_):
    sig = sygnaly()
    lin = [naglowek("Komitet inwestycyjny", "Stanowisko na rynkach"), ""]
    for i in sig.get("instrumenty", []):
        f = i.get("final", {})
        kier = f.get("kierunek", "BRAK")
        glosy = " · ".join(f"{a} {v[0]} {v[1]}" for a, v in i.get("agenci", {}).items())
        lin.append(f"<b>{e(i.get('nazwa', i['id']))}</b>: {KIER.get(kier, e(kier))}" + (f" {e(f.get('pewnosc'))}/3" if kier != "BRAK" else ""))
        if f.get("powod"): lin.append(e(f["powod"]))
        if glosy: lin.append(f"<i>Głosy: {e(glosy)}</i>")
        lin.append("")
    if sig.get("aktualizacja"): lin.append(f"Stan na: {e(sig['aktualizacja'].replace('T', ' ')[:16])} UTC")
    return "\n".join(lin)


def cmd_rynek(arg):
    k = ALIASY.get(arg.strip().lower())
    if not k:
        return "Wskaż rynek, np. /rynek zloto. Dostępne: nasdaq, zloto, srebro, ropa, gaz, kawa, kakao."
    i = {x["id"]: x for x in sygnaly().get("instrumenty", [])}.get(k, {"id": k})
    cn = ceny()
    c, f, st = cn.get(k, {}), i.get("final", {}), i.get("setup", {})
    dec = i.get("dec", 2)
    lin = [naglowek("Research", f"{i.get('nazwa', k)} · {i.get('ticker_tv', c.get('symbol', ''))}"), ""]
    if c:
        d = c.get("dzien", {})
        lin.append(f"Kurs: <b>{fmt(c.get('cena'), dec)}</b> ({zn(c.get('zmiana_pct') or 0)}%)")
        lin.append(f"Sesja: O {fmt(d.get('open'), dec)} · H {fmt(d.get('high'), dec)} · L {fmt(d.get('low'), dec)}")
        if c.get("czas_notowania_utc"):
            t = datetime.datetime.fromisoformat(c["czas_notowania_utc"].replace("Z", "+00:00")).astimezone(PL)
            lin.append(f"Notowanie: {t:%d.%m %H:%M} PL ({e(c.get('symbol', ''))})")
    sp = {"gold": "xauusd", "silver": "xagusd"}.get(k)
    if sp and sp in cn: lin.append(f"Spot: {fmt(cn[sp].get('cena'), dec)}")
    if i.get("atr"): lin.append(f"ATR D1: {fmt(i['atr'], dec)}")
    kier = f.get("kierunek", "BRAK")
    lin += ["", f"Stanowisko komitetu: <b>{KIER.get(kier, e(kier))}</b>" + (f" · przekonanie {e(f.get('pewnosc'))}/3" if kier != "BRAK" else "")]
    if f.get("powod"): lin.append(f"Teza: {e(f['powod'])}")
    if i.get("agenci"): lin.append("Głosy: " + " · ".join(f"{e(a)} {e(v[0])} {e(v[1])}" for a, v in i["agenci"].items()))
    if st.get("wejscie") is not None and kier != "BRAK":
        lin.append(f"Plan: {e(st.get('typ', ''))} {e(st.get('kierunek', ''))} {e(st['wejscie'])} · stop {e(st.get('sl'))} · cele {e(st.get('tp1'))} / {e(st.get('tp2'))}")
        if st.get("status"): lin.append(f"Status: {e(st['status'])}")
    return "\n".join(lin)


def cmd_raport(_):
    pliki = sorted(f for f in glob.glob(f"{build.ROOT}/raporty/*.html") if re.match(r"\d{4}-\d{2}-\d{2}_raport", os.path.basename(f)))
    if not pliki: return "Brak raportów."
    t = open(pliki[-1]).read()
    t = re.sub(r"<(style|script|head)[^>]*>.*?</\1>", "", t, flags=re.S)
    linie = [html.unescape(x).strip() for x in re.sub(r"<[^>]+>", "\n", t).split("\n")]
    linie = [x for x in linie if x]
    tytul = linie[2] if len(linie) > 2 else os.path.basename(pliki[-1])
    akapity = [x for x in linie if len(x) > 120][:3]
    lin = [naglowek("Relacje inwestorskie", tytul), "", e(linie[0]) if linie else "", ""]
    lin += [e(a) for a in akapity]
    lin += ["", f'<a href="{PANEL}">Pełny raport w panelu</a>', ZASTRZEZENIE]
    return "\n\n".join(x for x in lin if x)


def cmd_pomoc(_):
    return "\n".join([naglowek("Obsługa", "Dostępne polecenia"), ""]
                     + [f"/{c} — {e(o)}" for c, o in POLECENIA]
                     + ["", "Komunikaty o zleceniach, wejściach, stopach i celach przychodzą automatycznie. "
                        "Polecenia są obsługiwane w cyklu kilkuminutowym."])


OBSLUGA = {"status": cmd_status, "pozycje": cmd_pozycje, "sygnaly": cmd_sygnaly, "sygnały": cmd_sygnaly,
           "rynek": cmd_rynek, "rynki": lambda _: przeglad(), "raport": cmd_raport, "pomoc": cmd_pomoc,
           "help": cmd_pomoc, "start": cmd_pomoc}


def odpowiedz(tekst):
    m = re.match(r"/(\w+)(?:@\w+)?\s*(.*)", tekst.strip(), flags=re.S)
    if not m: return None
    f = OBSLUGA.get(m.group(1).lower())
    if not f: return "Nieznane polecenie. Lista poleceń: /pomoc"
    try:
        return f(m.group(2))
    except Exception as ex:  # odpowiedź zamiast ciszy, gdy brakuje danych
        return f"Nie udało się przygotować odpowiedzi ({e(type(ex).__name__)}). Spróbuj ponownie później."


# ---------- Telegram API ----------

def api(metoda, **pola):
    dane = urllib.parse.urlencode(pola).encode()
    with urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/{metoda}", dane, timeout=30) as r:
        w = json.load(r)
    if not w.get("ok"): raise RuntimeError(f"Telegram odrzucił {metoda}")
    return w["result"]


def wyslij(tekst):
    for i in range(0, len(tekst), 4000):
        api("sendMessage", chat_id=CHAT, text=tekst[i:i + 4000], parse_mode="HTML", disable_web_page_preview="true")


def obsluz_komendy():
    st = wczytaj(KOMENDY, {})
    if not st.get("menu"):
        api("setMyCommands", commands=json.dumps([{"command": c, "description": o} for c, o in POLECENIA], ensure_ascii=False))
        st["menu"] = True
    upd = api("getUpdates", offset=st.get("offset", 0), timeout=0, allowed_updates='["message"]')
    n = 0
    for u in upd:
        st["offset"] = u["update_id"] + 1
        msg = u.get("message") or {}
        if str(msg.get("chat", {}).get("id")) != CHAT: continue   # tylko czat właściciela
        odp = odpowiedz(msg.get("text", ""))
        if odp:
            wyslij(odp)
            n += 1
    json.dump(st, open(KOMENDY, "w"), ensure_ascii=False, indent=1)   # bez znacznika czasu: commit tylko po nowych wiadomościach
    print(f"Polecenia: {len(upd)} wiadomości, {n} odpowiedzi.")


def pora_przegladu(stan, teraz):
    if teraz.weekday() >= 5: return None
    dzis = teraz.date().isoformat()
    if teraz.time() >= WIECZOR and stan.get("wieczor") != dzis: return "wieczor"
    if RANO <= teraz.time() < WIECZOR and stan.get("rano") != dzis: return "rano"
    return None


def main(argv):
    sucho = "--sucho" in argv or not (TOKEN and CHAT)
    if not (TOKEN and CHAT) and "--sucho" not in argv:
        print("Brak TELEGRAM_BOT_TOKEN / TELEGRAM_CHAT_ID: tylko podgląd, stan bez zmian.")
    out = (lambda t: print(t, "\n---")) if sucho else wyslij
    teraz = datetime.datetime.now(PL)
    arg = [a for a in argv if a != "--sucho"]

    if arg and arg[0].startswith("/"):
        out(odpowiedz(" ".join(arg)))
        return
    if "komendy" in arg:
        if not sucho: obsluz_komendy()
        return
    if "test" in arg:
        out(naglowek("Obsługa", "Test połączenia") + f"\nKanał komunikacji działa poprawnie. {teraz:%d.%m %H:%M} PL")
        return
    if "podsumowanie" in arg:
        out(przeglad())
        return

    sig = sygnaly()
    nowe = {"sygnaly": migawka_sygnalow(sig), "dziennik": migawka_dziennika(), "automat": migawka_automatu()}
    stan = wczytaj(STAN, None)
    if stan is None:
        out(naglowek("Obsługa", "Kanał komunikacji uruchomiony") + "\n\nBędziemy tu przekazywać rekomendacje komitetu, "
            "zlecenia, realizacje, zmiany stopów i celów oraz przegląd rynków rano i wieczorem. Lista poleceń: /pomoc")
        out(przeglad())
        podsum = {"rano": teraz.date().isoformat()} if teraz.time() < WIECZOR else {"rano": teraz.date().isoformat(), "wieczor": teraz.date().isoformat()}
        stan = {**nowe, "podsumowanie": podsum}
    else:
        msgs = (wiadomosci_sygnalow(sig, stan.get("sygnaly", {}), nowe["sygnaly"])
                + wiadomosci_dziennika(stan.get("dziennik", {}), nowe["dziennik"])
                + wiadomosci_automatu(stan.get("automat", {}), nowe["automat"]))
        for m in msgs:
            out(m)
        stan.update(nowe)
        p = pora_przegladu(stan.setdefault("podsumowanie", {}), teraz)
        if p:
            out(przeglad("Przegląd poranny" if p == "rano" else "Przegląd wieczorny"))
            stan["podsumowanie"][p] = teraz.date().isoformat()
        print(f"Wysłano {len(msgs) + bool(p)} wiadomości." if not sucho else f"Podgląd: {len(msgs) + bool(p)} wiadomości.")
    if not sucho:
        stan["zaktualizowano_utc"] = datetime.datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        json.dump(stan, open(STAN, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
