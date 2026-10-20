# Softy: kawa i kakao, analiza z 2026-10-20 10:45 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): LONG 4/5 (suma +3.0)

- Cena 313,35 c/lb (2026-10-20T08:25:00Z UTC), sesja w trakcie. ATR D1 10,64, ATR H1 (sesja) 3,61. 5 sesji +8.6%, 20 sesji +14.2%.
- Reżim: **wybicie gora** (zamknięcie/cena nad szczytem 10 sesji 311.30). Zakres 10 sesji 283,50–311,30 (20 sesji 269,75–311,30), EMA20 297,78, EMA50 305,35, SMA200 308,26.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +1.5 | zamknięcie/cena nad szczytem 10 sesji 311.30 |
| COT | +1.0 | fundusze net +15,270, 3. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 155% normy, prognoza 16 dni 118% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +1.5 | KCZ26.NYB vs KCH27.NYB: +4.45%, 5 dni temu +2.56%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,852 (2026-10-19), zmiana od 2026-10-13: -2.8% |
| BRL | +0.0 | USD/BRL 5.047, 5 sesji +1.3% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana -0.9%, wzrost w 42% lat |

Opory: 315,52 (swing D1 ×2, ostatnio 2026-09-08, +0.20 ATR), 317,75 (szczyt 5 sesji, +0.41 ATR), 319,00 (swing D1 ×5, ostatnio 2026-10-19, +0.53 ATR), 320,00 (okrągły poziom, +0.63 ATR)

Wsparcia: 312,15 (P, -0.11 ATR), 308,20 (swing D1 ×3, ostatnio 2026-10-07, -0.48 ATR), 306,55 (S1, -0.64 ATR), 301,50 (swing D1 ×2, ostatnio 2026-10-19, -1.11 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: cofnięcie do 308.20 (swing D1 ×3, ostatnio 2026-10-07) | 309,26 | 287,99 | 351,81 / 373,08 | 1.82 | -0.38 ATR | 6 | silny poziom 315.52 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG | stop: kontynuacja: przebicie szczytu ostatniej sesji 317.75 | 318,81 | 297,54 | 361,36 / 382,63 | 1.82 | +0.51 ATR | 6 | R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | limit: cofnięcie do 319.00 (swing D1 ×5, ostatnio 2026-10-19) | 317,94 | 339,21 | 275,39 / 254,12 | 1.82 | +0.43 ATR | 6 | silny poziom 308.2 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | stop: kontynuacja: przebicie dołka ostatniej sesji 303.00 | 301,94 | 323,21 | 259,39 / 238,12 | 1.82 | -1.07 ATR | 6 | stop 1.07× ATR D1 od ceny: daleko, do przeliczenia po sesji; silny poziom 297.85 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

Wiszące zlecenia z dziennika:

- #49 LONG limit 310,00 (SL 302,20): w zasięgu (0.31× ATR D1, 0.9× ATR H1)

## Kakao (NY CC): NEUTRAL 2/5 (suma +1.5)

- Cena 5 695 USD/t (2026-10-19T17:15:00Z UTC). ATR D1 276, ATR H1 (sesja) 76. 5 sesji +0.2%, 20 sesji +6.3%.
- Reżim: **zakres** (ADX 14, cena w zakresie 10 sesji 5431.00-6023.00). Zakres 10 sesji 5 431–6 023 (20 sesji 5 051–6 023), EMA20 5 687, EMA50 5 649, SMA200 4 585.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 14, cena w zakresie 10 sesji 5431.00-6023.00 |
| COT | +1.0 | fundusze net -11,921, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.5 | opad 30 dni 158% normy, prognoza 16 dni 213% normy (średnia ważona regionów); Ekwador bardzo mokro (powodzie) |
| Krzywa | +0.0 | CCZ26.NYB vs CCH27.NYB: -1.69%, 5 dni temu -2.01%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,606,396 (2026-10-19), zmiana od 2026-10-13: +0.8% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.5%, wzrost w 62% lat |

Opory: 5 729 (swing D1 ×4, ostatnio 2026-10-19, +0.12 ATR), 5 740 (R1, +0.16 ATR), 5 793 (R2, +0.36 ATR), 5 921 (swing D1 ×3, ostatnio 2026-10-05, +0.82 ATR)

Wsparcia: 5 665 (P, -0.11 ATR), 5 612 (S1, -0.30 ATR), 5 590 (dołek 5 sesji, -0.38 ATR), 5 562 (swing D1 ×3, ostatnio 2026-10-19, -0.48 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5431.00 (10 sesji), TP1 przed przeciwną granicą | 5 459 | 5 183 | 5 995 / 6 286 | 1.46 | -0.86 ATR | 8 | limit 0.86× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5728.75 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 6023.00: zmiana reżimu, wejście z kontynuacji | 6 051 | 5 361 | 7 429 / 8 118 | 1.78 | +1.29 ATR | 3 | stop 1.29× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 6023.00 (10 sesji), TP1 przed przeciwną granicą | 5 995 | 6 271 | 5 459 / 5 168 | 1.46 | +1.09 ATR | 8 | limit 1.09× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5590.0 przed TP1: rozważyć częściowe wyjście przed nim |
| SHORT | stop: wybicie zakresu za 5431.00: zmiana reżimu, wejście z kontynuacji | 5 403 | 6 093 | 4 025 / 3 336 | 1.78 | -1.06 ATR | 3 | stop 1.06× ATR D1 od ceny: daleko, do przeliczenia po sesji |

Wiszące zlecenia z dziennika:

- #50 LONG limit 5 610 (SL 5 470): w zasięgu (0.31× ATR D1, 1.1× ATR H1)

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-10-23 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-10-26 |  | oba | Tydzień przesunięcia czasu (PL zimowy, USA letni do 1.11): ICE US softs otwierają o godzinę wcześniej czasu PL (kawa 09:15, kakao 09:45) | wysoka |
| 2026-10-26 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-10-28 | 19:00 | oba | FOMC (decyzja Fed; przez USD i nastrój ryzyka) | średnia |
| 2026-10-30 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-02 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
