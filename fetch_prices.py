#!/usr/bin/env python3
"""Pobiera notowania z Yahoo Finance (yfinance) i zapisuje je do data/.

Wynik:
  data/latest.json          ostatnia cena, zmiana dzienna i czas notowania dla każdego instrumentu
  data/<klucz>_15m.csv      świece 15-minutowe (ostatnie ~10 dni)
  data/<klucz>_1h.csv       świece godzinowe (ostatnie ~60 dni)
  data/<klucz>_1d.csv       świece dzienne (ostatni rok)
  data/xauusd_*.csv, xagusd_*.csv   spot złota/srebra: świece futures przesunięte o bazę spot - futures
  data/spot_log.csv         każdy odczyt spotu (Swissquote / gold-api.com) z bazą względem futures
  data/status.json          kiedy działał skrypt i które pobrania się nie udały

Gdy pobranie instrumentu się nie uda, poprzednie pliki zostają bez zmian.
"""
import datetime as dt
import json
import os
import sys
import time
import urllib.request

import pandas as pd
import yfinance as yf

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")

# klucz -> (symbol Yahoo, opis). Spot/indeks to odpowiedniki cen CFD u brokerów.
TICKERS = {
    "nq":        ("NQ=F",     "Nasdaq 100 E-mini futures (CME)"),
    "ndx":       ("^NDX",     "Nasdaq 100 indeks (kasowy, ~US100 CFD)"),
    "gold":      ("GC=F",     "Złoto futures (COMEX)"),
    "silver":    ("SI=F",     "Srebro futures (COMEX)"),
    "wti":       ("CL=F",     "Ropa WTI futures (NYMEX)"),
    "ng":        ("NG=F",     "Gaz ziemny futures (NYMEX)"),
    "coffee":    ("KC=F",     "Kawa Arabica futures (ICE US)"),
    "cocoa":     ("CC=F",     "Kakao futures (ICE US)"),
    "dxy":       ("DX-Y.NYB", "Indeks dolara DXY"),
    "us10y":     ("^TNX",     "Rentowność US 10Y (x10)"),
    "vix":       ("^VIX",     "VIX"),
}

# Spot XAU/XAG: Yahoo go nie podaje, więc bierzemy bieżącą cenę z darmowych źródeł bez klucza
# (Swissquote, zapasowo gold-api.com), liczymy bazę spot - futures i przesuwamy o nią świece futures.
SPOT = {
    "xauusd": ("XAU", "gold",   "Złoto spot XAU/USD (jak XAUUSD w TradingView)"),
    "xagusd": ("XAG", "silver", "Srebro spot XAG/USD (jak XAGUSD w TradingView)"),
}
SPOT_LOG_KEEP = 2000   # wierszy w data/spot_log.csv (~3 tygodnie przy co 15 min)
BASIS_WINDOW = 8       # mediana bazy z ostatnich N odczytów (~2 h) wygładza opóźnienie futures z Yahoo

# interwał -> okres pobierany z Yahoo (limity Yahoo: 15m do 60 dni, 1h do 730 dni)
INTERVALS = {"15m": "10d", "1h": "60d", "1d": "1y"}


def history(symbol, interval, period, tries=2):
    last = None
    for i in range(tries):
        try:
            df = yf.Ticker(symbol).history(period=period, interval=interval, auto_adjust=False, prepost=True)
            if df is not None and not df.empty:
                return df
            last = "pusta odpowiedź"
        except Exception as e:  # yfinance zgłasza różne wyjątki przy limitach Yahoo
            last = f"{type(e).__name__}: {e}"
        time.sleep(3)
    raise RuntimeError(last)


def to_csv(df, path):
    df = df[["Open", "High", "Low", "Close", "Volume"]].copy()
    idx = df.index.tz_convert("UTC") if df.index.tz is not None else df.index
    df.index = idx.strftime("%Y-%m-%dT%H:%M:%SZ")
    df.index.name = "Datetime_UTC"
    df = df.dropna(subset=["Close"]).round(6)
    df.to_csv(path)
    return df


def http_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 claude-finance-data"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.load(r)


def spot_swissquote(metal):
    data = http_json(f"https://forex-data-feed.swissquote.com/public-quotes/bboquotes/instrument/{metal}/USD")
    best = None
    for platform in data:
        for prof in platform.get("spreadProfilePrices", []):
            bid, ask = float(prof["bid"]), float(prof["ask"])
            if bid > 0 and ask >= bid and (best is None or ask - bid < best[1] - best[0]):
                best = (bid, ask, platform.get("ts"))
    if best is None:
        raise RuntimeError("brak cen w odpowiedzi")
    bid, ask, ts = best
    when = dt.datetime.fromtimestamp(ts / 1000, dt.timezone.utc) if ts else dt.datetime.now(dt.timezone.utc)
    return {"cena": round((bid + ask) / 2, 4), "bid": bid, "ask": ask,
            "czas_notowania_utc": when.strftime("%Y-%m-%dT%H:%M:%SZ"), "zrodlo": "Swissquote (bid/ask)"}


def spot_goldapi(metal):
    data = http_json(f"https://api.gold-api.com/price/{metal}")
    price = float(data["price"])
    if price <= 0:
        raise RuntimeError("cena <= 0")
    return {"cena": price, "czas_notowania_utc": str(data.get("updatedAt", ""))[:19] + "Z", "zrodlo": "gold-api.com"}


def spot_quote(metal):
    errs = []
    for fn in (spot_swissquote, spot_goldapi):
        try:
            return fn(metal)
        except Exception as e:
            errs.append(f"{fn.__name__}: {type(e).__name__}: {e}"[:150])
    raise RuntimeError(" | ".join(errs))


def update_spot(latest, errors, now):
    """Dopisuje odczyt spotu do spot_log.csv i buduje <klucz>_{15m,1h,1d}.csv = świece futures + baza."""
    log_path = os.path.join(OUT, "spot_log.csv")
    try:
        log = pd.read_csv(log_path)
    except Exception:
        log = pd.DataFrame(columns=["Datetime_UTC", "klucz", "spot", "futures", "futures_czas_utc", "baza", "zrodlo"])
    for key, (metal, fut_key, desc) in SPOT.items():
        fut = latest["instrumenty"].get(fut_key)
        try:
            q = spot_quote(metal)
        except Exception as e:
            errors[f"{key}_spot"] = str(e)[:300]
            continue
        row = {"Datetime_UTC": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "klucz": key, "spot": q["cena"],
               "futures": fut["cena"] if fut else None, "futures_czas_utc": fut["czas_notowania_utc"] if fut else None,
               "baza": round(q["cena"] - fut["cena"], 4) if fut else None, "zrodlo": q["zrodlo"]}
        log = pd.concat([log, pd.DataFrame([row])], ignore_index=True)
        entry = {"symbol": f"{metal}/USD spot", "opis": desc, **q}
        recent = log[(log["klucz"] == key)]["baza"].dropna().astype(float).tail(BASIS_WINDOW)
        if fut and len(recent):
            basis = float(recent.median())
            entry["baza_vs_futures"] = round(basis, 3)
            entry["futures"] = fut["symbol"]
            for interval in INTERVALS:
                src = os.path.join(OUT, f"{fut_key}_{interval}.csv")
                try:
                    df = pd.read_csv(src, index_col="Datetime_UTC")
                    for c in ("Open", "High", "Low", "Close"):
                        df[c] = (df[c] + basis).round(4)
                    df.to_csv(os.path.join(OUT, f"{key}_{interval}.csv"))
                except Exception as e:
                    errors[f"{key}_{interval}"] = f"{type(e).__name__}: {e}"[:200]
            if "dzien" in fut:
                d = fut["dzien"]
                entry["dzien"] = {"data": d["data"], **{k: round(d[k] + basis, 4) for k in ("open", "high", "low")}}
                entry["dzien"]["high"] = max(entry["dzien"]["high"], q["cena"])
                entry["dzien"]["low"] = min(entry["dzien"]["low"], q["cena"])
            if "poprzednie_zamkniecie" in fut:
                pc = fut["poprzednie_zamkniecie"] + basis
                entry["poprzednie_zamkniecie"] = round(pc, 4)
                entry["zmiana_pct"] = round((q["cena"] / pc - 1) * 100, 3)
        latest["instrumenty"][key] = entry
    log.tail(SPOT_LOG_KEEP).to_csv(log_path, index=False)


def main():
    os.makedirs(OUT, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
    latest_path = os.path.join(OUT, "latest.json")
    try:
        latest = json.load(open(latest_path))
    except Exception:
        latest = {"instrumenty": {}}
    errors = {}

    for key, (sym, desc) in TICKERS.items():
        frames = {}
        for interval, period in INTERVALS.items():
            try:
                frames[interval] = to_csv(history(sym, interval, period), os.path.join(OUT, f"{key}_{interval}.csv"))
            except Exception as e:
                errors[f"{key}_{interval}"] = str(e)[:200]
        if "15m" not in frames and "1h" not in frames:
            continue
        intraday = frames.get("15m", frames.get("1h"))
        last_ts, last_row = intraday.index[-1], intraday.iloc[-1]
        entry = {"symbol": sym, "opis": desc, "cena": float(last_row["Close"]), "czas_notowania_utc": last_ts}
        daily = frames.get("1d")
        if daily is not None and len(daily) >= 2:
            # ostatnia świeca D1 to bieżąca (lub ostatnia) sesja, przedostatnia daje poprzednie zamknięcie
            pc = float(daily.iloc[-2]["Close"])
            entry["poprzednie_zamkniecie"] = pc
            entry["zmiana_pct"] = round((entry["cena"] / pc - 1) * 100, 3)
            today = daily.iloc[-1]
            entry["dzien"] = {"data": daily.index[-1][:10], "open": float(today["Open"]),
                              "high": float(today["High"]), "low": float(today["Low"])}
        latest["instrumenty"][key] = entry

    update_spot(latest, errors, now)

    latest["zrodlo"] = "Yahoo Finance przez yfinance; futures z opóźnieniem do ~10-15 min, ceny CFD u brokera mogą się różnić"
    latest["zaktualizowano_utc"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    json.dump(latest, open(latest_path, "w"), ensure_ascii=False, indent=1)
    json.dump({"uruchomiono_utc": latest["zaktualizowano_utc"], "bledy": errors},
              open(os.path.join(OUT, "status.json"), "w"), ensure_ascii=False, indent=1)

    ok = len(TICKERS) * len(INTERVALS) - len([k for k in errors if k.split("_")[0] in TICKERS])
    print(f"OK {ok}, błędy {len(errors)}")
    for k, v in errors.items():
        print(f"  {k}: {v}")
    # porażka całego przebiegu tylko gdy nic się nie pobrało
    sys.exit(1 if ok == 0 else 0)


if __name__ == "__main__":
    main()
