#!/usr/bin/env python3
"""Pobiera notowania z Yahoo Finance (yfinance) i zapisuje je do data/.

Wynik:
  data/latest.json          ostatnia cena, zmiana dzienna i czas notowania dla każdego instrumentu
  data/<klucz>_15m.csv      świece 15-minutowe (ostatnie ~10 dni)
  data/<klucz>_1h.csv       świece godzinowe (ostatnie ~60 dni)
  data/<klucz>_1d.csv       świece dzienne (ostatni rok)
  data/status.json          kiedy działał skrypt i które pobrania się nie udały

Gdy pobranie instrumentu się nie uda, poprzednie pliki zostają bez zmian.
"""
import datetime as dt
import json
import os
import sys
import time

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

    latest["zrodlo"] = "Yahoo Finance przez yfinance; futures z opóźnieniem do ~10-15 min, ceny CFD u brokera mogą się różnić"
    latest["zaktualizowano_utc"] = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    json.dump(latest, open(latest_path, "w"), ensure_ascii=False, indent=1)
    json.dump({"uruchomiono_utc": latest["zaktualizowano_utc"], "bledy": errors},
              open(os.path.join(OUT, "status.json"), "w"), ensure_ascii=False, indent=1)

    ok = len(TICKERS) * len(INTERVALS) - len(errors)
    print(f"OK {ok}, błędy {len(errors)}")
    for k, v in errors.items():
        print(f"  {k}: {v}")
    # porażka całego przebiegu tylko gdy nic się nie pobrało
    sys.exit(1 if ok == 0 else 0)


if __name__ == "__main__":
    main()
