# Softy: kawa i kakao, analiza z 2026-11-22 21:26 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 273,35 c/lb (2026-11-20T18:00:00Z UTC). ATR D1 8,84, ATR H1 (sesja) 3,49. 5 sesji -1.9%, 20 sesji -11.1%.
- Reżim: **zakres** (ADX 16, cena w zakresie 10 sesji 266.70-288.30). Zakres 10 sesji 266,70–288,30 (20 sesji 266,70–314,90), EMA20 283,12, EMA50 292,47, SMA200 300,75.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 16, cena w zakresie 10 sesji 266.70-288.30 |
| COT | +1.0 | fundusze net +9,023, 1. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 101% normy, prognoza 16 dni 141% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +0.0 | KCZ26.NYB vs KCH27.NYB: +1.73%, 5 dni temu +2.07%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.934, 5 sesji +5.2%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +4.2%, wzrost w 54% lat |

Opory: 276,83 (R1, +0.39 ATR), 277,15 (swing D1 ×2, ostatnio 2026-11-20, +0.43 ATR), 280,00 (okrągły poziom, +0.75 ATR), 280,32 (R2, +0.79 ATR)

Wsparcia: 272,42 (P, -0.11 ATR), 269,80 (swing D1 ×1, ostatnio 2026-06-22, -0.40 ATR), 268,93 (S1, -0.50 ATR), 268,15 (swing D1 ×3, ostatnio 2026-11-20, -0.59 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 266.70 (10 sesji), TP1 przed przeciwną granicą | 267,58 | 258,75 | 287,42 / 294,09 | 1.81 | -0.65 ATR | 14 | silny poziom 277.15 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 288.30: zmiana reżimu, wejście z kontynuacji | 289,18 | 271,51 | 324,53 / 342,20 | 1.79 | +1.79 ATR | 7 | stop 1.79× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 288.30 (10 sesji), TP1 przed przeciwną granicą | 287,42 | 296,25 | 267,58 / 260,91 | 1.81 | +1.59 ATR | 14 | limit 1.59× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 268.15 przed TP1: rozważyć częściowe wyjście przed nim |
| SHORT | stop: wybicie zakresu za 266.70: zmiana reżimu, wejście z kontynuacji | 265,82 | 283,49 | 230,47 / 212,80 | 1.79 | -0.85 ATR | 7 | ok |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.5)

- Cena 5 150 USD/t (2026-11-20T18:15:00Z UTC). ATR D1 236, ATR H1 (sesja) 82. 5 sesji +0.6%, 20 sesji -7.9%.
- Reżim: **trend spadkowy** (ADX 22, EMA20 < EMA50, cena pod EMA20; nieudane wybicie górą (5393.00 > 5287.00, zamknięcie 5150.00): uwaga na pułapkę albo drugie podejście). Zakres 10 sesji 4 640–5 287 (20 sesji 4 640–5 687), EMA20 5 188, EMA50 5 383, SMA200 4 634.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.0 | ADX 22, EMA20 < EMA50, cena pod EMA20; nieudane wybicie górą (5393.00 > 5287.00, zamknięcie 5150.00): uwaga na pułapkę albo drugie podejście |
| COT | +1.0 | fundusze net -19,213, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 209% normy, prognoza 16 dni 95% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.72%, 5 dni temu -2.65%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.8%, wzrost w 65% lat |

Opory: 5 206 (swing D1 ×2, ostatnio 2026-11-16, +0.24 ATR), 5 222 (P, +0.31 ATR), 5 321 (R1, +0.72 ATR), 5 393 (szczyt 5 sesji, +1.03 ATR)

Wsparcia: 5 096 (swing D1 ×4, ostatnio 2026-11-20, -0.23 ATR), 5 052 (S1, -0.42 ATR), 5 000 (okrągły poziom, -0.63 ATR), 4 970 (swing D1 ×2, ostatnio 2026-07-28, -0.76 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4970.50 (swing D1 ×2, ostatnio 2026-07-28) | 4 994 | 4 403 | 6 177 / 6 768 | 1.75 | -0.66 ATR | 4 | silny poziom 5206.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5393.00 | 5 417 | 4 825 | 6 599 / 7 190 | 1.75 | +1.13 ATR | 4 | stop 1.13× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 5416.33 (swing D1 ×3, ostatnio 2026-11-20) | 5 393 | 5 984 | 4 210 / 3 619 | 1.75 | +1.03 ATR | 4 | limit 1.03× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5096.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 5124.00 | 5 100 | 5 692 | 3 918 / 3 327 | 1.75 | -0.21 ATR | 4 | silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |

## Alerty

- kakao: nieudane wybicie górą (5393.00 > 5287.00, zamknięcie 5150.00): uwaga na pułapkę albo drugie podejście

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-23 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-27 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-30 |  | kakao | ICCO Quarterly Bulletin of Cocoa Statistics (rewizja bilansu 2025/26 i 2026/27) | średnia |
| 2026-11-30 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-12-04 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
