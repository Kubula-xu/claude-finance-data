# claude-finance-data

Darmowy kanał cen dla projektu „Bot tradingowy giełda”. GitHub Actions co 15 minut (niedziela–piątek) uruchamia `fetch_prices.py`, który pobiera notowania z Yahoo Finance (yfinance) i commituje je do `data/`. Bez kluczy API i bez kredytów Claude.

## Pliki w `data/`

| Plik | Zawartość |
|---|---|
| `latest.json` | ostatnia cena, poprzednie zamknięcie, zmiana %, OHLC dnia i czas notowania (UTC) dla każdego instrumentu |
| `<klucz>_15m.csv` | świece 15 min, ~10 dni |
| `<klucz>_1h.csv` | świece 1 h, ~60 dni |
| `<klucz>_1d.csv` | świece dzienne, 1 rok |
| `status.json` | czas ostatniego przebiegu i lista nieudanych pobrań |

CSV: `Datetime_UTC,Open,High,Low,Close,Volume`, od najstarszego.

Klucze: `nq` (NQ=F), `ndx` (^NDX), `gold` (GC=F), `silver` (SI=F), `wti` (CL=F), `ng` (NG=F), `coffee` (KC=F), `cocoa` (CC=F), `dxy` (DX-Y.NYB), `us10y` (^TNX), `vix` (^VIX).

## Uwagi

- Futures z Yahoo mają opóźnienie do ~10–15 min; GitHub dodatkowo potrafi opóźnić start harmonogramu. Zawsze sprawdzaj `czas_notowania_utc`.
- Ceny CFD u brokera różnią się od futures (rollover, spread). Indeks ^NDX jest bliżej US100 CFD; Yahoo nie podaje spotu XAU/XAG (XAUUSD=X zwraca pustą odpowiedź).
- Ręczne odświeżenie: zakładka Actions → „Ceny Yahoo” → Run workflow.
