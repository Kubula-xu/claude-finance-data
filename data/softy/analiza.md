# Softy: kawa i kakao, analiza z 2026-11-24 18:57 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 262,95 c/lb (2026-11-24T15:45:00Z UTC). ATR D1 7,87, ATR H1 (sesja) 3,16. 5 sesji -8.2%, 20 sesji -10.5%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 266.70). Zakres 10 sesji 266,70–288,30 (20 sesji 266,70–304,90), EMA20 280,56, EMA50 290,68, SMA200 300,46.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 266.70 |
| COT | +1.0 | fundusze net +9,023, 1. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 100% normy, prognoza 16 dni 207% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +1.5 | KCZ26.NYB vs KCH27.NYB: +3.73%, 5 dni temu +1.88%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.904, 5 sesji +2.1%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +4.9%, wzrost w 58% lat |

Opory: 263,82 (P, +0.11 ATR), 265,88 (R1, +0.37 ATR), 266,73 (swing D1 ×2, ostatnio 2026-11-24, +0.48 ATR), 268,82 (R2, +0.75 ATR)

Wsparcia: 261,75 (swing D1 ×1, ostatnio 2026-11-24, -0.15 ATR), 261,75 (dołek 5 sesji, -0.15 ATR), 260,88 (S1, -0.26 ATR), 258,82 (S2, -0.52 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 258.82 (S2) | 259,61 | 243,87 | 291,08 / 306,81 | 1.76 | -0.42 ATR | 8 | silny poziom 266.73 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.76 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 266.75 | 267,54 | 251,80 | 299,01 / 314,74 | 1.76 | +0.58 ATR | 8 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.76 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 266.73 (swing D1 ×2, ostatnio 2026-11-24) | 265,94 | 281,68 | 234,47 / 218,74 | 1.76 | +0.38 ATR | 8 | silny poziom 261.75 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.76 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 261.75 | 260,96 | 276,70 | 229,49 / 213,76 | 1.76 | -0.25 ATR | 8 | R:R po kosztach 1.76 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): LONG 3/5 (suma +2.5)

- Cena 5 417 USD/t (2026-11-24T15:45:00Z UTC). ATR D1 240, ATR H1 (sesja) 88. 5 sesji +7.7%, 20 sesji -2.9%.
- Reżim: **wybicie gora** (zamknięcie/cena nad szczytem 10 sesji 5252.00). Zakres 10 sesji 4 640–5 252 (20 sesji 4 640–5 622), EMA20 5 208, EMA50 5 376, SMA200 4 646.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +1.5 | zamknięcie/cena nad szczytem 10 sesji 5252.00 |
| COT | +1.0 | fundusze net -19,213, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 219% normy, prognoza 16 dni 121% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.5 | CCZ26.NYB vs CCH27.NYB: -4.26%, 5 dni temu -2.68%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.2%, wzrost w 65% lat |

Opory: 5 446 (swing D1 ×3, ostatnio 2026-11-24, +0.12 ATR), 5 481 (szczyt 5 sesji, +0.27 ATR), 5 509 (R1, +0.38 ATR), 5 571 (swing D1 ×4, ostatnio 2026-11-02, +0.64 ATR)

Wsparcia: 5 389 (P, -0.12 ATR), 5 297 (S1, -0.50 ATR), 5 250 (okrągły poziom, -0.69 ATR), 5 227 (swing D1 ×3, ostatnio 2026-11-24, -0.79 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: cofnięcie do 5227.33 (swing D1 ×3, ostatnio 2026-11-24) | 5 251 | 4 650 | 6 453 / 7 054 | 1.75 | -0.69 ATR | 4 | silny poziom 5445.67 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| LONG | stop: kontynuacja: przebicie szczytu ostatniej sesji 5481.00 | 5 505 | 4 904 | 6 707 / 7 308 | 1.75 | +0.37 ATR | 4 | silny poziom 5571.25 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | limit: cofnięcie do 5571.25 (swing D1 ×4, ostatnio 2026-11-02) | 5 547 | 6 148 | 4 345 / 3 745 | 1.75 | +0.54 ATR | 4 | silny poziom 5227.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | stop: kontynuacja: przebicie dołka ostatniej sesji 5269.00 | 5 245 | 5 846 | 4 043 / 3 442 | 1.75 | -0.72 ATR | 4 | silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-27 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-30 |  | kakao | ICCO Quarterly Bulletin of Cocoa Statistics (rewizja bilansu 2025/26 i 2026/27) | średnia |
| 2026-11-30 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-12-04 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-12-07 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
