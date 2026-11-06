# Softy: kawa i kakao, analiza z 2026-11-06 11:24 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 2/5 (suma -1.5)

- Cena 277,25 c/lb (2026-11-06T10:00:00Z UTC), sesja w trakcie. ATR D1 10,81, ATR H1 (sesja) 3,53. 5 sesji -2.9%, 20 sesji -4.1%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 277.40). Zakres 10 sesji 277,40–315,50 (20 sesji 277,40–318,20), EMA20 292,62, EMA50 300,42, SMA200 304,06.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 277.40 |
| COT | +1.0 | fundusze net +20,104, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 121% normy, prognoza 16 dni 120% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +3.01%, 5 dni temu +5.52%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.487, 5 sesji +2.6%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.4%, wzrost w 54% lat |

Opory: 279,32 (P, +0.19 ATR), 282,23 (R1, +0.46 ATR), 282,90 (swing D1 ×3, ostatnio 2026-11-05, +0.52 ATR), 287,00 (swing D1 ×1, ostatnio 2026-05-11, +0.90 ATR)

Wsparcia: 276,40 (dołek 5 sesji, -0.08 ATR), 274,23 (S1, -0.28 ATR), 271,32 (S2, -0.55 ATR), 270,00 (okrągły poziom, -0.67 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 269.77 (swing D1 ×2, ostatnio 2026-09-23) | 270,85 | 249,22 | 314,11 / 335,74 | 1.82 | -0.59 ATR | 6 | silny poziom 282.9 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 284.40 | 285,48 | 263,85 | 328,74 / 350,37 | 1.82 | +0.76 ATR | 6 | R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 282.90 (swing D1 ×3, ostatnio 2026-11-05) | 281,82 | 303,45 | 238,56 / 216,93 | 1.82 | +0.42 ATR | 6 | silny poziom 276.4 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 276.40 | 275,32 | 296,95 | 232,06 / 210,43 | 1.82 | -0.18 ATR | 6 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma -0.5)

- Cena 5 137 USD/t (2026-11-06T10:00:00Z UTC), sesja w trakcie. ATR D1 204, ATR H1 (sesja) 78. 5 sesji -5.0%, 20 sesji -8.5%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 5274.00). Zakres 10 sesji 5 274–5 830 (20 sesji 5 274–6 023), EMA20 5 527, EMA50 5 587, SMA200 4 593.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 5274.00 |
| COT | +0.5 | fundusze net -10,940 (13. percentyl 3 lat), zmiana 4 tyg. +5,082: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | +1.0 | opad 30 dni 203% normy, prognoza 16 dni 152% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.14%, 5 dni temu -1.95%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +6.1%, wzrost w 73% lat |

Opory: 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.39 ATR), 5 253 (P, +0.57 ATR), 5 362 (R1, +1.10 ATR), 5 430 (swing D1 ×3, ostatnio 2026-11-05, +1.43 ATR)

Wsparcia: 5 087 (swing D1 ×3, ostatnio 2026-10-01, -0.24 ATR), 5 071 (S1, -0.32 ATR), 5 000 (okrągły poziom, -0.67 ATR), 4 970 (swing D1 ×2, ostatnio 2026-07-28, -0.82 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4970.50 (swing D1 ×2, ostatnio 2026-07-28) | 4 991 | 4 480 | 6 012 / 6 523 | 1.71 | -0.72 ATR | 5 | silny poziom 5430.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.71 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5434.00 | 5 454 | 4 944 | 6 476 / 6 987 | 1.71 | +1.55 ATR | 5 | stop 1.55× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.71 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 5430.00 (swing D1 ×3, ostatnio 2026-11-05) | 5 410 | 5 920 | 4 388 / 3 877 | 1.71 | +1.33 ATR | 5 | limit 1.33× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.71 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 5137.00 | 5 117 | 5 627 | 4 095 / 3 584 | 1.71 | -0.10 ATR | 5 | silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.71 < 2.0: według ryzyko.md 10a nie składać |

## Alerty

- kawa: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia
- kakao: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-06 |  | oba | Okno rolowania indeksów towarowych (GSCI/BCOM roll grudzień → marzec |  5.-9. dzień roboczy listopada) |
| 2026-11-06 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-09 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-12 |  | kawa | Cecafé: eksport kawy z Brazylii za październik | średnia |
| 2026-11-13 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-16 |  | kakao | First Notice Day kakao XII (CCZ26) wg reguły ICE (10 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-16 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-19 |  | kawa | First Notice Day kawy XII (KCZ26) wg reguły ICE (7 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-20 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
