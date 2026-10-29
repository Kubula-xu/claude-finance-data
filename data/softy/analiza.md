# Softy: kawa i kakao, analiza z 2026-10-29 09:47 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 2/5 (suma -1.5)

- Cena 286,35 c/lb (2026-10-28T17:15:00Z UTC). ATR D1 10,73, ATR H1 (sesja) 3,51. 5 sesji -9.3%, 20 sesji -1.4%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 289.05). Zakres 10 sesji 289,05–318,20 (20 sesji 283,30–318,20), EMA20 300,01, EMA50 304,87, SMA200 306,15.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 289.05 |
| COT | +0.5 | fundusze net +22,337 (12. percentyl 3 lat), zmiana 4 tyg. +6,531: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | -1.0 | opad 30 dni 134% normy, prognoza 16 dni 117% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +1.0 | KCZ26.NYB vs KCH27.NYB: +3.79%, 5 dni temu +4.45%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.349, 5 sesji +6.5%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.2%, wzrost w 62% lat |

Opory: 287,98 (P, +0.15 ATR), 291,92 (R1, +0.52 ATR), 294,55 (swing D1 ×2, ostatnio 2026-10-28, +0.76 ATR), 297,08 (R2, +1.00 ATR)

Wsparcia: 284,85 (swing D1 ×3, ostatnio 2026-10-28, -0.14 ATR), 284,05 (dołek 5 sesji, -0.21 ATR), 282,82 (S1, -0.33 ATR), 280,00 (okrągły poziom, -0.59 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 282.82 (S1) | 283,89 | 262,43 | 326,82 / 348,29 | 1.82 | -0.23 ATR | 6 | silny poziom 294.55 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 293.15 | 294,22 | 272,76 | 337,15 / 358,62 | 1.82 | +0.73 ATR | 6 | silny poziom 299.2 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 299.20 (swing D1 ×3, ostatnio 2026-09-30) | 298,13 | 319,59 | 255,20 / 233,73 | 1.82 | +1.10 ATR | 6 | limit 1.10× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 284.85 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 284.05 | 282,98 | 304,44 | 240,05 / 218,58 | 1.82 | -0.31 ATR | 6 | R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 5 462 USD/t (2026-10-28T17:15:00Z UTC). ATR D1 227, ATR H1 (sesja) 70. 5 sesji -6.6%, 20 sesji +1.7%.
- Reżim: **zakres** (ADX 11, cena w zakresie 10 sesji 5442.00-6023.00; nieudane wybicie dołem (5380.00 < 5442.00, zamknięcie 5456.00)). Zakres 10 sesji 5 442–6 023 (20 sesji 5 051–6 023), EMA20 5 642, EMA50 5 640, SMA200 4 578.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 11, cena w zakresie 10 sesji 5442.00-6023.00; nieudane wybicie dołem (5380.00 < 5442.00, zamknięcie 5456.00) |
| COT | +0.5 | fundusze net -8,821 (19. percentyl 3 lat), zmiana 4 tyg. +7,585: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | +0.5 | opad 30 dni 163% normy, prognoza 16 dni 239% normy (średnia ważona regionów); Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.01%, 5 dni temu -1.69%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.0%, wzrost w 50% lat |

Opory: 5 483 (P, +0.09 ATR), 5 562 (swing D1 ×3, ostatnio 2026-10-19, +0.44 ATR), 5 587 (R1, +0.55 ATR), 5 652 (swing D1 ×2, ostatnio 2026-10-28, +0.83 ATR)

Wsparcia: 5 412 (swing D1 ×3, ostatnio 2026-10-28, -0.22 ATR), 5 380 (dołek 5 sesji, -0.36 ATR), 5 353 (S1, -0.48 ATR), 5 250 (okrągły poziom, -0.93 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5442.00 (10 sesji), TP1 przed przeciwną granicą | 5 465 | 5 238 | 6 000 / 6 146 | 1.71 | +0.01 ATR | 9 | silny poziom 5561.67 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 6023.00: zmiana reżimu, wejście z kontynuacji | 6 046 | 5 478 | 7 181 / 7 749 | 1.74 | +2.57 ATR | 4 | stop 2.57× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 6023.00 (10 sesji), TP1 przed przeciwną granicą | 6 000 | 6 227 | 5 465 / 5 319 | 1.71 | +2.37 ATR | 9 | limit 2.37× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5442.00: zmiana reżimu, wejście z kontynuacji | 5 419 | 5 987 | 4 284 / 3 716 | 1.74 | -0.19 ATR | 4 | ok |

## Alerty

- kakao: nieudane wybicie dołem (5380.00 < 5442.00, zamknięcie 5456.00)

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-10-30 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-02 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-06 |  | oba | Okno rolowania indeksów towarowych (GSCI/BCOM roll grudzień → marzec |  5.-9. dzień roboczy listopada) |
| 2026-11-06 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-09 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-12 |  | kawa | Cecafé: eksport kawy z Brazylii za październik | średnia |
