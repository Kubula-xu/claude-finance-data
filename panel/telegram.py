#!/usr/bin/env python3
"""Powiadomienia Telegram: sygnały, zlecenia, wejścia, zmiany SL, TP/zamknięcia i podsumowanie rynków.

Porównuje bieżący stan z ostatnio wysłanym (data/telegram_stan.json) i wysyła tylko różnice:
  - sygnały: zmiana kierunku/pewności agenta-koordynatora albo poziomów setupu (panel/projekt/dane/sygnaly.json),
  - dziennik: nowe zlecenie i zmiana statusu, SL lub TP (panel/projekt/agenci/paper_trading.md),
  - automat zleceń: wejście, SL na BE, TP1, TP2, SL, zamknięcie dnia, wygaśnięcie (data/wypelnienia.json),
  - podsumowanie rynków: rano (od 08:00 PL) i wieczorem (od 22:30 PL), pon.–pt.

Sekrety: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID. Bez nich skrypt tylko wypisuje wiadomości i nie zmienia stanu.
TELEGRAM_TRYB (domyślnie PAPER) trafia do nagłówka wiadomości; przy prawdziwym koncie ustaw REAL.
Pierwsze uruchomienie z sekretami zapamiętuje bieżący stan i wysyła jedną wiadomość powitalną z podsumowaniem.

Użycie: python3 panel/telegram.py               → zdarzenia (+ podsumowanie, jeśli pora)
        python3 panel/telegram.py podsumowanie  → podsumowanie od razu
        python3 panel/telegram.py test          → wiadomość testowa
        python3 panel/telegram.py --sucho       → tylko wypisz, nic nie wysyłaj ani nie zapisuj
"""
import datetime, html, json, os, sys, urllib.parse, urllib.request
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402

PL = ZoneInfo("Europe/Warsaw")
UTC = datetime.timezone.utc
STAN = f"{build.LIVE}/data/telegram_stan.json"
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "").strip()
CHAT = os.environ.get("TELEGRAM_CHAT_ID", "").strip()
TRYB = os.environ.get("TELEGRAM_TRYB", "PAPER").strip().upper() or "PAPER"
PANEL = "https://kubula-xu.github.io/claude-finance-data/"
STRZALKA = {"LONG": "🟢 LONG", "SHORT": "🔴 SHORT", "BRAK": "⚪ BRAK", "NEUTRAL": "⚪ NEUTRAL"}
AKTYWNE = ("oczekuje", "otwarta")
RANO, WIECZOR = datetime.time(8, 0), datetime.time(22, 30)


def e(x):
    return html.escape(str(x), quote=False)


def naglowek(ikona, tytul):
    return f"{ikona} <b>[{TRYB}] {e(tytul)}</b>"


def wczytaj(f, domyslne):
    try:
        return json.load(open(f))
    except (OSError, ValueError):
        return domyslne


def sygnaly():
    return wczytaj(f"{build.ROOT}/dane/sygnaly.json", {"instrumenty": []})


def ceny():
    return wczytaj(f"{build.LIVE}/data/latest.json", {"instrumenty": {}})["instrumenty"]


def fmt(v, dec=2):
    if v is None: return "–"
    return f"{v:,.{dec}f}".replace(",", " ").replace(".", ",")


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
    z = wczytaj(f"{build.LIVE}/data/wypelnienia.json", {"zlecenia": {}}).get("zlecenia", {})
    return {nr: {"stan": v.get("stan"), "zdarzenia": v.get("zdarzenia", [])} for nr, v in z.items()}


# ---------- wiadomości ----------

def opis_zlecenia(r):
    lin = [f"{e(r.get('Kierunek', ''))} · wejście {e(r.get('Wejście', ''))} · SL {e(r.get('SL', ''))} · TP {e(r.get('TP', ''))}"]
    if r.get("Ryzyko %"): lin.append(f"Ryzyko {e(r['Ryzyko %'])}%" + (f" · {e(r['Wielkość'])}" if r.get("Wielkość") else ""))
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
        tytul = f"Sygnał: {i.get('nazwa', k)}" if zmiana_kier else f"Setup zmieniony: {i.get('nazwa', k)}"
        lin = [naglowek("📡", tytul),
               f"{STRZALKA.get(n['kierunek'], e(n['kierunek']))} · pewność {e(n['pewnosc'])}/3"
               + (f" (było {e(s['kierunek'])} {e(s['pewnosc'])}/3)" if s and zmiana_kier else "")]
        if f.get("powod"): lin.append(e(f["powod"]))
        if n["kierunek"] not in (None, "BRAK") and st.get("wejscie") is not None:
            lin.append(f"Setup: {e(st.get('typ', ''))} {e(st.get('kierunek', ''))} {e(st['wejscie'])} · SL {e(st.get('sl'))}"
                       f" · TP {e(st.get('tp1'))} / {e(st.get('tp2'))}")
            if st.get("status"): lin.append(f"Status: {e(st['status'])}")
        out.append("\n".join(lin))
    return out


def wiadomosci_dziennika(stare, nowe):
    out = []
    rows = {r["#"]: r for r in build.journal() if r.get("#")}
    for nr, n in nowe.items():
        r, s = rows[nr], stare.get(nr)
        nazwa = f"#{nr} {r.get('Instrument', '')}"
        if s is None:
            if not n["status"].startswith(AKTYWNE): continue
            ikona, tyt = ("📥", "Nowe zlecenie") if n["status"].startswith("oczekuje") else ("✅", "Nowa pozycja")
            lin = [naglowek(ikona, f"{tyt} {nazwa}"), *opis_zlecenia(r), f"Status: {e(n['status'])}"]
            if r.get("Uwagi"): lin.append(f"<i>{e(r['Uwagi'][:300])}</i>")
            out.append("\n".join(lin))
            continue
        if s["status"] != n["status"]:
            st = n["status"]
            ikona = "🏁" if st.startswith("zamknięta") else "🚫" if st.startswith("anulowana") else "✅" if st.startswith("otwarta") else "🔄"
            lin = [naglowek(ikona, f"{nazwa}: {st}")]
            if st.startswith("zamknięta"):
                lin.append(f"Zamknięcie {e(r.get('Zamknięcie', '–'))} · wynik {e(r.get('Wynik (pkt)', '–'))} pkt · {e(r.get('Wynik (R)', '–'))} R")
            else:
                lin += opis_zlecenia(r)
            out.append("\n".join(lin))
        elif (s["sl"], s["tp"]) != (n["sl"], n["tp"]):
            lin = [naglowek("🛡", f"{nazwa}: zmiana poziomów")]
            if s["sl"] != n["sl"]: lin.append(f"SL {e(s['sl'])} → <b>{e(n['sl'])}</b>")
            if s["tp"] != n["tp"]: lin.append(f"TP {e(s['tp'])} → <b>{e(n['tp'])}</b>")
            out.append("\n".join(lin))
    return out


def ikona_zdarzenia(z):
    if " wejście " in z: return "✅"
    if " TP" in z: return "🎯"
    if "SL na BE" in z: return "🛡"
    if " BE " in z or z.endswith(" BE"): return "⚖️"
    if " SL " in z: return "🛑"
    if "zamknięcie dnia" in z: return "🏁"
    if "niewypełnione" in z: return "⌛"
    return "🔔"


def wiadomosci_automatu(stare, nowe):
    out = []
    auto = wczytaj(f"{build.LIVE}/data/wypelnienia.json", {"zlecenia": {}}).get("zlecenia", {})
    for nr, n in nowe.items():
        widziane = set((stare.get(nr) or {}).get("zdarzenia", []))
        for z in n["zdarzenia"]:
            if z in widziane: continue
            a = auto[nr]
            lin = [naglowek(ikona_zdarzenia(z), f"#{nr} {a.get('instrument', '')}"), e(z)]
            if a.get("stan") == "zamknięta" and z == n["zdarzenia"][-1] and a.get("wynik_pkt_zrealizowany") is not None:
                lin.append(f"Pozycja zamknięta · średnie wyjście {e(a.get('cena_wyjscia_srednia'))} · wynik {e(a['wynik_pkt_zrealizowany'])} pkt")
            elif a.get("stan") == "otwarta" and z == n["zdarzenia"][-1]:
                lin.append(f"Otwarte {int(round(a.get('pozostalo', 1) * 100))}% · SL teraz {e(a.get('sl_teraz'))}")
            lin.append("<i>automat na świecach 15m; potwierdź u brokera</i>")
            out.append("\n".join(lin))
    return out


def podsumowanie(tytul="Obserwowane rynki"):
    sig, cn = sygnaly(), ceny()
    lin = [naglowek("📊", f"{tytul} · {datetime.datetime.now(PL):%d.%m %H:%M} PL"), ""]
    for i in sig.get("instrumenty", []):
        c = cn.get(i["id"], {})
        f = i.get("final", {})
        zm = c.get("zmiana_pct")
        zm_txt = f"{'+' if (zm or 0) >= 0 else ''}{fmt(zm, 2)}%" if zm is not None else "–"
        kier = f.get("kierunek", "BRAK")
        lin.append(f"<b>{e(i.get('nazwa', i['id']))}</b> {fmt(c.get('cena'), i.get('dec', 2))} ({zm_txt}) · "
                   f"{STRZALKA.get(kier, e(kier))}" + (f" {e(f.get('pewnosc'))}/3" if kier not in ("BRAK", None) else ""))
    tlo = [f"{n} {fmt(cn[k].get('cena'), d)}" for k, n, d in (("dxy", "DXY", 2), ("us10y", "US10Y", 3), ("vix", "VIX", 2)) if k in cn]
    if tlo: lin += ["", "Tło: " + " · ".join(tlo)]
    akt = [r for r in build.journal() if r.get("Status", "").startswith(AKTYWNE)]
    auto = wczytaj(f"{build.LIVE}/data/wypelnienia.json", {"zlecenia": {}}).get("zlecenia", {})
    lin += ["", "<b>Zlecenia i pozycje</b>" if akt else "Brak aktywnych zleceń i pozycji."]
    for r in akt:
        stan = auto.get(r["#"], {}).get("stan") or r["Status"].split(" ")[0]
        lin.append(f"#{e(r['#'])} {e(r.get('Instrument', ''))} {e(r.get('Kierunek', ''))} {e(r.get('Wejście', ''))} · SL {e(r.get('SL', ''))} · {e(stan)}")
    lin += ["", f'<a href="{PANEL}">Panel</a>']
    return "\n".join(lin)


# ---------- wysyłka ----------

def wyslij(tekst):
    for i in range(0, len(tekst), 4000):
        dane = urllib.parse.urlencode({"chat_id": CHAT, "text": tekst[i:i + 4000], "parse_mode": "HTML",
                                       "disable_web_page_preview": "true"}).encode()
        with urllib.request.urlopen(f"https://api.telegram.org/bot{TOKEN}/sendMessage", dane, timeout=20) as r:
            if not json.load(r).get("ok"): raise RuntimeError("Telegram odrzucił wiadomość")


def pora_podsumowania(stan, teraz):
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

    if "test" in argv:
        out(naglowek("👋", "Test połączenia") + f"\nBot Claude Finance działa. {teraz:%d.%m %H:%M} PL")
        return
    if "podsumowanie" in argv:
        out(podsumowanie())
        return

    sig = sygnaly()
    nowe = {"sygnaly": migawka_sygnalow(sig), "dziennik": migawka_dziennika(), "automat": migawka_automatu()}
    stan = wczytaj(STAN, None)
    if stan is None:
        out(naglowek("👋", "Bot podłączony") + "\nOd teraz dostaniesz tu nowe sygnały, zlecenia, wejścia, zmiany SL, "
            "TP i zamknięcia oraz podsumowanie rynków rano i wieczorem.")
        out(podsumowanie())
        podsum = {"rano": teraz.date().isoformat()} if teraz.time() < WIECZOR else {"rano": teraz.date().isoformat(), "wieczor": teraz.date().isoformat()}
        stan = {**nowe, "podsumowanie": podsum}
    else:
        msgs = (wiadomosci_sygnalow(sig, stan.get("sygnaly", {}), nowe["sygnaly"])
                + wiadomosci_dziennika(stan.get("dziennik", {}), nowe["dziennik"])
                + wiadomosci_automatu(stan.get("automat", {}), nowe["automat"]))
        for m in msgs:
            out(m)
        stan.update(nowe)
        p = pora_podsumowania(stan.setdefault("podsumowanie", {}), teraz)
        if p:
            out(podsumowanie("Podsumowanie poranne" if p == "rano" else "Podsumowanie wieczorne"))
            stan["podsumowanie"][p] = teraz.date().isoformat()
        print(f"Wysłano {len(msgs) + bool(p)} wiadomości." if not sucho else f"Podgląd: {len(msgs) + bool(p)} wiadomości.")
    if not sucho:
        stan["zaktualizowano_utc"] = datetime.datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
        json.dump(stan, open(STAN, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1:])
