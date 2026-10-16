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
- `panel/wypelnienia.py` pilnuje zleceń z dziennika na świecach 15 min (po każdym pobraniu cen, wynik w `data/wypelnienia.json`): wejście po dotknięciu limitu w oknie handlu, SL na BE po +1R, 50% na TP1, reszta na TP2 albo SL, intraday zamknięcie o 22:30 PL. Strona nakłada ten wynik na dziennik.
- Agenci po zmianie pozycji lub nowym raporcie uruchamiają `panel/sync_z_projektu.sh "opis"`, który kopiuje pliki z folderu projektu i wypycha je do repo.

## Powiadomienia Telegram

`panel/telegram.py` wysyła na Telegram komunikaty w stylu desku funduszu: nowy lub zmieniony sygnał (`final` w `sygnaly.json`), nowe zlecenie i zmianę statusu, SL lub TP w dzienniku, zdarzenia automatu zleceń (wejście, SL na BE, TP1, TP2, SL, zamknięcie dnia, wygaśnięcie) oraz podsumowanie obserwowanych rynków rano (od 08:00 PL) i wieczorem (od 22:30 PL), pon.–pt. Uruchamia go workflow „Ceny Yahoo” co 15 min i workflow „Telegram” zaraz po synchronizacji plików agentów. Co już wysłano, zapisuje `data/telegram_stan.json`.

Konfiguracja (Settings → Secrets and variables → Actions):
- sekret `TELEGRAM_BOT_TOKEN`: token bota od @BotFather,
- sekret `TELEGRAM_CHAT_ID`: id czatu, do którego bot pisze,
- opcjonalnie zmienna `TELEGRAM_TRYB` (domyślnie `PAPER`, przy prawdziwym koncie `REAL`): trafia do nagłówka każdej wiadomości.

Polecenia w czacie z botem (odpowiada tylko na czat `TELEGRAM_CHAT_ID`; workflow „Telegram” odbiera je co 5 min, także w weekend, więc odpowiedź przychodzi z kilkuminutowym opóźnieniem):

| Polecenie | Odpowiedź |
|---|---|
| `/status` | kapitał, wynik od startu, liczba pozycji i zleceń, wynik niezrealizowany |
| `/pozycje` | otwarte pozycje i zlecenia z kursem, wynikiem w pkt, R i USD albo odległością do wejścia |
| `/sygnaly` | stanowisko komitetu i głosy agentów na każdym rynku |
| `/rynek <rynek>` | kurs, sesja, ATR, stanowisko i plan, np. `/rynek zloto`, `/rynek kawa` |
| `/rynki` | przegląd wszystkich rynków |
| `/raport` | skrót ostatniego raportu dla inwestorów |
| `/pomoc` | lista poleceń |

Test: Actions → „Telegram” → Run workflow → `test` albo `podsumowanie`. Podgląd odpowiedzi lokalnie: `python3 panel/telegram.py --sucho /rynek zloto`.

## Kawa i kakao (softy)

Osobna warstwa danych i analizy dla kawy (KC) i kakao (CC), bo na tych rynkach sama cena nie wystarcza.

- Workflow „Softy (kawa i kakao)” (`.github/workflows/softy.yml`, pn–pt 06:20 i 18:10 UTC, pt 20:00 UTC po COT, nd 21:00 UTC) uruchamia `softy/fetch_softy.py` i zapisuje do `data/softy/`:
  - `cot.csv`: CFTC Disaggregated, managed money / producenci / swap dealerzy / OI, ok. 4 lata,
  - `pogoda.json`: opad 30 dni wstecz i 16 dni prognozy jako % normy z 15 lat (Open-Meteo) dla regionów: Sul de Minas, Cerrado, Mogiana, Espírito Santo, Central Highlands (kawa); Soubré, Daloa, San-Pédro, Ashanti, Western North, Los Ríos (kakao),
  - `krzywa.json`: kolejne kontrakty (np. KCZ26/KCH27) i spread pierwszy–drugi (backwardation = ciasny rynek),
  - `fx_brl_1d.csv`, `fx_gbp_1d.csv`, `fx_eur_1d.csv`; `<coffee|cocoa>_dlugie_1d.csv` (od 2000 r., do sezonowości),
  - `zapasy_ice.csv`: zapasy certyfikowane z raportów ICE (best-effort); wpisy z newsów idą do `softy/zapasy_reczne.csv`,
  - `status.json`: co się udało, błędy i ostatni sukces każdego źródła.
- `softy/analiza.py` (bez sieci; liczy go też workflow „Ceny Yahoo” co 15 min) pisze `data/softy/analiza.json` i `analiza.md`: reżim rynku (zakres / trend / wybicie, nieudane wybicia), poziomy (swingi D1, pivoty, okrągłe), czynniki z jawnymi wagami (technika, COT, pogoda, krzywa, zapasy, BRL, sezonowość), plan wejść na oba kierunki jako pary OCO (limit z cofnięcia + stop z kontynuacji, wielkość wg ryzyko.md 10a), kontrolę wiszących zleceń z dziennika (odległość w ATR) i alerty (zmiana reżimu → `rezim_log.csv`).
- `softy/kalendarz.csv`: wydarzenia softów (FND, grind, CONAB, USDA, ICCO, Cecafé, zmiana czasu); COT w piątki i przybycia kakao w poniedziałki dopisują się same.
