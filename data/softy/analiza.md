# Softy: kawa i kakao, analiza z 2026-10-28 14:21 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -1.0)

- Cena 285,45 c/lb (2026-10-28T13:00:00Z UTC), sesja w trakcie. ATR D1 10,68, ATR H1 (sesja) 3,58. 5 sesji -5.6%, 20 sesji +1.5%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 290.30; nieudane wybicie dołem (289.05 < 290.30, zamknięcie 293.75)). Zakres 10 sesji 290,30–318,20 (20 sesji 281,80–318,20), EMA20 301,41, EMA50 305,61, SMA200 306,49.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 290.30; nieudane wybicie dołem (289.05 < 290.30, zamknięcie 293.75) |
| COT | +0.5 | fundusze net +22,337 (12. percentyl 3 lat), zmiana 4 tyg. +6,531: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | -1.0 | opad 30 dni 134% normy, prognoza 16 dni 155% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +1.0 | KCZ26.NYB vs KCH27.NYB: +4.50%, 5 dni temu +4.45%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.351, 5 sesji +6.5%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.8%, wzrost w 65% lat |

Opory: 286,90 (S1, +0.14 ATR), 289,05 (swing D1 ×1, ostatnio 2026-10-27, +0.34 ATR), 289,05 (dołek 5 sesji, +0.34 ATR), 295,90 (P, +0.98 ATR)

Wsparcia: 280,05 (S2, -0.51 ATR), 280,00 (okrągły poziom, -0.51 ATR), 278,40 (swing D1 ×1, ostatnio 2026-05-28, -0.66 ATR), 270,00 (okrągły poziom, -1.45 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 269.77 (swing D1 ×2, ostatnio 2026-09-23) | 270,84 | 249,49 | 313,54 / 334,89 | 1.82 | -1.37 ATR | 6 | limit 1.37× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 289.05 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 304.90 | 305,97 | 284,62 | 348,67 / 370,02 | 1.82 | +1.92 ATR | 6 | stop 1.92× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 297.85 (swing D1 ×3, ostatnio 2026-09-30) | 296,78 | 318,13 | 254,08 / 232,73 | 1.82 | +1.06 ATR | 6 | limit 1.06× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 285.45 | 284,38 | 305,73 | 241,68 / 220,33 | 1.82 | -0.10 ATR | 6 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 5 485 USD/t (2026-10-28T13:00:00Z UTC), sesja w trakcie. ATR D1 231, ATR H1 (sesja) 72. 5 sesji -3.9%, 20 sesji +3.1%.
- Reżim: **zakres** (ADX 11, cena w zakresie 10 sesji 5442.00-6023.00). Zakres 10 sesji 5 442–6 023 (20 sesji 5 051–6 023), EMA20 5 661, EMA50 5 647, SMA200 4 578.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 11, cena w zakresie 10 sesji 5442.00-6023.00 |
| COT | +0.5 | fundusze net -8,821 (19. percentyl 3 lat), zmiana 4 tyg. +7,585: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | +0.5 | opad 30 dni 163% normy, prognoza 16 dni 215% normy (średnia ważona regionów); Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.02%, 5 dni temu -1.69%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.5%, wzrost w 50% lat |

Opory: 5 548 (P, +0.27 ATR), 5 562 (swing D1 ×3, ostatnio 2026-10-19, +0.33 ATR), 5 651 (R1, +0.72 ATR), 5 656 (swing D1 ×2, ostatnio 2026-10-27, +0.74 ATR)

Wsparcia: 5 473 (S1, -0.05 ATR), 5 442 (dołek 5 sesji, -0.19 ATR), 5 433 (swing D1 ×3, ostatnio 2026-10-27, -0.22 ATR), 5 370 (S2, -0.50 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5442.00 (10 sesji), TP1 przed przeciwną granicą | 5 465 | 5 234 | 6 000 / 6 159 | 1.69 | -0.09 ATR | 9 | silny poziom 5561.67 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 6023.00: zmiana reżimu, wejście z kontynuacji | 6 046 | 5 468 | 7 203 / 7 781 | 1.74 | +2.43 ATR | 4 | stop 2.43× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 6023.00 (10 sesji), TP1 przed przeciwną granicą | 6 000 | 6 231 | 5 465 / 5 306 | 1.69 | +2.23 ATR | 9 | limit 2.23× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5442.00: zmiana reżimu, wejście z kontynuacji | 5 419 | 5 997 | 4 262 / 3 684 | 1.74 | -0.29 ATR | 4 | ok |

## Alerty

- kawa: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia
- kawa: nieudane wybicie dołem (289.05 < 290.30, zamknięcie 293.75)

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-10-28 | 19:00 | oba | FOMC (decyzja Fed; przez USD i nastrój ryzyka) | średnia |
| 2026-10-30 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-02 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-06 |  | oba | Okno rolowania indeksów towarowych (GSCI/BCOM roll grudzień → marzec |  5.-9. dzień roboczy listopada) |
| 2026-11-06 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-09 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
