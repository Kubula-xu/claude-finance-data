# Softy: kawa i kakao, analiza z 2026-11-05 17:51 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 277,85 c/lb (2026-11-05T16:30:00Z UTC), sesja w trakcie. ATR D1 11,42, ATR H1 (sesja) 3,66. 5 sesji -2.4%, 20 sesji -4.4%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 280.80). Zakres 10 sesji 280,80–317,90 (20 sesji 280,80–318,20), EMA20 294,25, EMA50 301,37, SMA200 304,41.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 280.80 |
| COT | +1.0 | fundusze net +20,104, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 121% normy, prognoza 16 dni 93% normy (średnia ważona regionów) |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +3.35%, 5 dni temu +5.52%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.460, 5 sesji +2.1%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.5%, wzrost w 54% lat |

Opory: 278,87 (swing D1 ×3, ostatnio 2026-11-04, +0.09 ATR), 280,87 (P, +0.26 ATR), 284,33 (R1, +0.57 ATR), 285,32 (swing D1 ×3, ostatnio 2026-11-04, +0.65 ATR)

Wsparcia: 276,28 (S1, -0.14 ATR), 272,82 (S2, -0.44 ATR), 270,00 (okrągły poziom, -0.69 ATR), 269,77 (swing D1 ×2, ostatnio 2026-09-23, -0.71 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 269.77 (swing D1 ×2, ostatnio 2026-09-23) | 270,91 | 248,07 | 316,60 / 339,44 | 1.83 | -0.61 ATR | 6 | silny poziom 278.87 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 285.45 | 286,59 | 263,75 | 332,28 / 355,12 | 1.83 | +0.77 ATR | 6 | R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 285.32 (swing D1 ×3, ostatnio 2026-11-04) | 284,18 | 307,02 | 238,49 / 215,65 | 1.83 | +0.55 ATR | 6 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 277.40 | 276,26 | 299,10 | 230,57 / 207,73 | 1.83 | -0.14 ATR | 6 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): LONG 3/5 (suma +2.0)

- Cena 5 315 USD/t (2026-11-05T16:30:00Z UTC), sesja w trakcie. ATR D1 199, ATR H1 (sesja) 78. 5 sesji +0.0%, 20 sesji -2.3%.
- Reżim: **zakres** (ADX 11, cena w zakresie 10 sesji 5343.00-5859.00; nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5456.00)). Zakres 10 sesji 5 343–5 859 (20 sesji 5 343–6 023), EMA20 5 563, EMA50 5 604, SMA200 4 589.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 11, cena w zakresie 10 sesji 5343.00-5859.00; nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5456.00) |
| COT | +0.5 | fundusze net -10,940 (13. percentyl 3 lat), zmiana 4 tyg. +5,082: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | +1.0 | opad 30 dni 203% normy, prognoza 16 dni 185% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | +0.0 | CCZ26.NYB vs CCH27.NYB: -1.88%, 5 dni temu -1.95%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +4.4%, wzrost w 73% lat |

Opory: 5 329 (S1, +0.07 ATR), 5 401 (P, +0.43 ATR), 5 443 (swing D1 ×3, ostatnio 2026-11-04, +0.64 ATR), 5 500 (okrągły poziom, +0.93 ATR)

Wsparcia: 5 274 (dołek 5 sesji, -0.21 ATR), 5 245 (swing D1 ×2, ostatnio 2026-11-04, -0.35 ATR), 5 203 (S2, -0.57 ATR), 5 087 (swing D1 ×3, ostatnio 2026-10-01, -1.15 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5343.00 (10 sesji), TP1 przed przeciwną granicą | 5 363 | 5 164 | 5 839 / 5 959 | 1.67 | +0.24 ATR | 10 | silny poziom 5442.67 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5859.00: zmiana reżimu, wejście z kontynuacji | 5 879 | 5 382 | 6 873 / 7 370 | 1.71 | +2.84 ATR | 5 | stop 2.84× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5859.00 (10 sesji), TP1 przed przeciwną granicą | 5 839 | 6 038 | 5 363 / 5 243 | 1.67 | +2.64 ATR | 10 | limit 2.64× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5343.00: zmiana reżimu, wejście z kontynuacji | 5 323 | 5 820 | 4 329 / 3 832 | 1.71 | +0.04 ATR | 5 | silny poziom 5274.0 przed TP1: rozważyć częściowe wyjście przed nim |

## Alerty

- kakao: nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5456.00)

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
