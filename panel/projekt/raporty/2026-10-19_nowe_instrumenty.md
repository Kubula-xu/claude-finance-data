# Nowe instrumenty dla Claude Finance: propozycja dyrektora

19.10.2026. Odpowiedź na pytanie Kuby, na czym firma może operować poza obecnymi siedmioma rynkami (US100, złoto, srebro, NatGas, WTI, kawa, kakao; CFD w XTB).

**Uwaga do liczb:** korelacje, ATR i spready poniżej to typowe wartości z ostatnich lat i z cennika XTB, nie policzone dziś z danych (środowisko nie łączy się z Yahoo). Przed dodaniem rynku trzeba je przeliczyć na danych z repo i sprawdzić spread na platformie.

## Czego brakuje w obecnym portfelu

- **Dwie mocne grupy korelacji:** metale (złoto + srebro, korelacja ok. 0,8) i energia (WTI + NatGas, słabiej). Dokładanie kolejnego rynku do tych grup niewiele daje, bo limit grupy (0,75%) i tak tnie ryzyko.
- **Jeden rynek akcji, tylko USA i tylko tech.** Brak ekspozycji na Europę, przemysł i Chiny.
- **Brak walut**, choć agent makro już śledzi DXY i rentowność 10Y (klucze `dxy`, `us10y` w repo).
- **Handel intraday zaczyna się w praktyce po 14:30 PL** (US100, energia, NatGas). Rano firma prawie nie ma czego grać poza złotem.

## Kandydaci

| Rynek (symbol XTB) | Dane w repo (Yahoo) | Korelacja z portfelem | Zmienność dzienna | Spread / SL | Do której księgi | Ocena |
|---|---|---|---|---|---|---|
| **Miedź (COPPER)** | HG=F | niska z US100, umiarkowana ze złotem (ok. 0,3–0,4) | 1,5–2% | ok. 2–4% | intraday (sesja COMEX) | **start nr 1** |
| **DAX (DE40)** | ^GDAXI | wysoka z US100 (ok. 0,6–0,7), ale inne godziny | ok. 1% | ok. 1% | intraday 09:00–17:30 PL | **start nr 2** |
| **EUR/USD (EURUSD)** | EURUSD=X | ujemna z DXY, umiarkowana ze złotem | ok. 0,5% | < 2% | intraday | dobry, ale wymaga zmiany limitu nominału |
| **USD/JPY (USDJPY)** | JPY=X | silna z rentownościami USA | ok. 0,6–0,8% | < 2% | intraday | jak EURUSD |
| **S&P 500 (US500)** | ^GSPC | bardzo wysoka z US100 (ok. 0,9) | ok. 1% | ok. 1% | intraday | **odradzam**: dubel US100 |
| **Ropa Brent (OIL)** | BZ=F | bardzo wysoka z WTI (ok. 0,95) | 1,5–2% | ok. 2–3% | intraday | **odradzam**: dubel WTI |
| **Platyna (PLATINUM)** | PL=F | wysoka ze złotem i srebrem | 1,5–2% | 3–6% | intraday | odradzam na start: grupa metali już pełna |
| **Cukier (SUGAR)** | SB=F | niska z resztą, trochę z ropą (etanol) | 1,5–2% | 5–10% | swing, agent softów | dobry trzeci soft |
| **Pszenica / kukurydza (WHEAT, CORN)** | ZW=F, ZC=F | niska | 1,5–2% | 5–10% | swing | później; potrzebują raportów USDA i pogody |
| **WIG20 (W20)** | brak dobrego darmowego feedu H1 | umiarkowana z DAX | ok. 1–1,5% | wyższy, płynność CFD słabsza | intraday | odradzam: dane i płynność |

## Dlaczego miedź na start

- **Prawdziwa dywersyfikacja:** napędzają ją Chiny, przemysł i podaż z kopalń (Chile, Peru, Kongo), a nie technologia USA ani inflacja jak złoto. To nowy czynnik w portfelu, a nie kolejna kopia istniejącego.
- **Pasuje do agentów bez nowej infrastruktury:** technika liczy ją tak jak WTI (ATR H1, poziomy), makro już patrzy na dolara i PMI, a sentyment ma do czytania newsy o Chinach i zapasach LME/COMEX.
- **Dane za darmo:** HG=F w yfinance, wystarczy dodać klucz `copper` do `fetch_prices.py` w repo.
- **Zmienność i spread** są w zakresie, który ryzyko już akceptuje dla WTI (spread kilka procent SL, ruch 1,5–2% dziennie).
- **Grupa korelacji:** proponuję nową grupę „metale przemysłowe”, a nie dopisanie do złota i srebra, ale z zastrzeżeniem, że ryzyko sprawdzi to na danych z 60 dni H1.

## Dlaczego DAX jako drugi

- Wypełnia **ranek**: sesja Xetra 09:00–17:30 PL, najmocniejszy ruch 09:00–11:00, gdy dziś firma stoi.
- Spread ok. 1 pkt przy ATR H1 kilkadziesiąt punktów, czyli jeden z najtańszych rynków u XTB.
- Minus: korelacja z US100. Proponuję wspólną grupę „akcje” z limitem 0,75%, a w praktyce zamykanie DAX-a przed 15:30 PL, żeby nie trzymać obu naraz.

## Waluty: dobre, ale z jedną zmianą w zasadach

EUR/USD i USD/JPY mają najmniejsze spready i świetne dane, a agent makro już rozumie ich czynniki. Problem jest w limitach: przy ruchu ok. 0,5% dziennie SL to kilkadziesiąt pipsów, więc pozycja z ryzykiem 50 000 USD ma nominał ok. 15–20 mln USD, czyli powyżej limitu 150% kapitału na pozycję (ryzyko.md, sekcja 2). Żeby grać waluty, trzeba albo podnieść limit nominału dla FX (np. do 250%), albo grać je z ryzykiem 0,25%. To decyzja Kuby i agenta ryzyka, dlatego waluty proponuję dopiero jako trzeci krok.

## Plan wdrożenia (proponowany)

1. Dodać do `fetch_prices.py` w repo klucze `copper` (HG=F) i `dax` (^GDAXI), żeby zebrały się świece 15m/1h.
2. Ryzyko przelicza ATR H1, spread vs SL i korelacje z obecnymi rynkami na 60 dniach H1 i dopisuje wiersze do tabeli w ryzyko.md (sekcja 3) oraz godziny handlu.
3. Przez tydzień agenci głosują na nowych rynkach bez transakcji (tylko glosy.csv), żeby skutecznosc.py miał ich ocenę.
4. Jeśli trafność nie jest gorsza niż na obecnych rynkach, wchodzą do paper tradingu z ryzykiem 0,25% przez pierwszy tydzień.
5. Później: decyzja o walutach (limit nominału) i o cukrze w księdze softów.
