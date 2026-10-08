# claude-finance-data

Darmowy kanał cen dla projektu „Bot tradingowy giełda”. GitHub Actions co 15 minut (niedziela–piątek) uruchamia `fetch_prices.py`, który pobiera notowania z Yahoo Finance (yfinance) i commituje je do `data/`. Bez kluczy API i bez kredytów Claude.

## Pliki w `data/`

| Plik | Zawartość |
|---|---|
| `latest.json` | ostatnia cena, poprzednie zamknięcie, zmiana %, OHLC dnia i czas notowania (UTC) dla każdego instrumentu |
| `<klucz>_15m.csv` | świece 15 min, ~10 dni |
| `<klucz>_1h.csv` | świece 1 h, ~60 dni |
| `<klucz>_1d.csv` | świece dzienne, 1 rok |
| `spot_log.csv` | każdy odczyt spotu XAU/XAG z bazą względem futures |
| `status.json` | czas ostatniego przebiegu i lista nieudanych pobrań |

CSV: `Datetime_UTC,Open,High,Low,Close,Volume`, od najstarszego.

Klucze: `nq` (NQ=F), `ndx` (^NDX), `gold` (GC=F), `silver` (SI=F), `wti` (CL=F), `ng` (NG=F), `coffee` (KC=F), `cocoa` (CC=F), `dxy` (DX-Y.NYB), `us10y` (^TNX), `vix` (^VIX).

Spot: `xauusd` (złoto XAU/USD) i `xagusd` (srebro XAG/USD), czyli to samo co XAUUSD/XAGUSD w TradingView. Bieżąca cena (bid/ask) pochodzi z darmowego kanału Swissquote (zapasowo gold-api.com), bez klucza. Świece `xauusd_*.csv` i `xagusd_*.csv` to świece futures GC=F/SI=F przesunięte o bazę spot − futures (mediana z ostatnich ~2 h odczytów, w `latest.json` pole `baza_vs_futures`). Ostatnie świece są więc dokładne do kilku dolarów, a starsze przybliżone (baza zmienia się powoli, skacze przy rolowaniu kontraktu).

## Uwagi

- Futures z Yahoo mają opóźnienie do ~10–15 min; GitHub dodatkowo potrafi opóźnić start harmonogramu. Zawsze sprawdzaj `czas_notowania_utc`.
- Ceny CFD u brokera różnią się od futures (rollover, spread). Indeks ^NDX jest bliżej US100 CFD; Spot XAU/XAG bierzemy spoza Yahoo (patrz wyżej), bo XAUUSD=X zwraca pustą odpowiedź.
- Ręczne odświeżenie: zakładka Actions → „Ceny Yahoo” → Run workflow.

## Pulpit Claude Finance (GitHub Pages)

Strona: https://kubula-xu.github.io/claude-finance-data/

Workflow „Pulpit (GitHub Pages)” buduje ją po każdym pobraniu cen i po każdej zmianie w `panel/`. Strona w przeglądarce co 3 minuty dociąga `data/latest.json` i przelicza wynik otwartych pozycji.

- `panel/build.py` składa `index.html`, `panel.json` i `pozycje.json` (otwarte pozycje z wynikiem).
- `panel/szablon.html` to szablon strony.
- `panel/projekt/` to kopia plików agentów: `agenci/paper_trading.md` (dziennik i pozycje), `dane/sygnaly.json`, `dane/intraday_poziomy_*.csv`, `raporty/`.
- Agenci po zmianie pozycji lub nowym raporcie uruchamiają `panel/sync_z_projektu.sh "opis"`, który kopiuje pliki z folderu projektu i wypycha je do repo.
