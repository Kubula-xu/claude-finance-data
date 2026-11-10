# Softy: kawa i kakao, analiza z 2026-11-10 02:29 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma +0.5)

- Cena 266,70 c/lb (2026-11-09T18:15:00Z UTC). ATR D1 10,54, ATR H1 (sesja) 3,61. 5 sesji -8.7%, 20 sesji -8.2%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 276.00). Zakres 10 sesji 276,00–304,90 (20 sesji 276,00–318,20), EMA20 289,06, EMA50 298,33, SMA200 303,30.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 276.00 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 115% normy, prognoza 16 dni 90% normy (średnia ważona regionów) |
| Krzywa | +1.0 | KCZ26.NYB vs KCH27.NYB: +2.38%, 5 dni temu +3.14%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | +0.0 | USD/BRL 5.503, 5 sesji +1.3% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana -1.1%, wzrost w 46% lat |

Opory: 268,73 (swing D1 ×3, ostatnio 2026-11-09, +0.19 ATR), 268,78 (P, +0.20 ATR), 270,92 (R1, +0.40 ATR), 273,00 (swing D1 ×1, ostatnio 2026-11-09, +0.60 ATR)

Wsparcia: 264,57 (S1, -0.20 ATR), 262,85 (swing D1 ×1, ostatnio 2026-05-19, -0.37 ATR), 262,43 (S2, -0.41 ATR), 260,00 (okrągły poziom, -0.64 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 262.85 (swing D1 ×1, ostatnio 2026-05-19) | 263,90 | 242,83 | 306,05 / 327,12 | 1.82 | -0.27 ATR | 6 | silny poziom 268.73 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 273.00 | 274,05 | 252,98 | 316,20 / 337,27 | 1.82 | +0.70 ATR | 6 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 279.60 (swing D1 ×2, ostatnio 2026-10-29) | 278,55 | 299,62 | 236,40 / 215,33 | 1.82 | +1.12 ATR | 6 | limit 1.12× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 266.65 | 265,60 | 286,67 | 223,45 / 202,38 | 1.82 | -0.10 ATR | 6 | R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 2/5 (suma +1.5)

- Cena 5 113 USD/t (2026-11-09T18:15:00Z UTC). ATR D1 209, ATR H1 (sesja) 80. 5 sesji -5.9%, 20 sesji -9.9%.
- Reżim: **zakres** (ADX 14, cena w zakresie 10 sesji 5072.00-5622.00). Zakres 10 sesji 5 072–5 622 (20 sesji 5 072–6 023), EMA20 5 455, EMA50 5 552, SMA200 4 601.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 14, cena w zakresie 10 sesji 5072.00-5622.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 164% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.21%, 5 dni temu -1.92%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.5%, wzrost w 65% lat |

Opory: 5 183 (P, +0.33 ATR), 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.49 ATR), 5 250 (okrągły poziom, +0.66 ATR), 5 273 (R1, +0.77 ATR)

Wsparcia: 5 089 (swing D1 ×4, ostatnio 2026-11-09, -0.12 ATR), 5 072 (dołek 5 sesji, -0.20 ATR), 5 023 (S1, -0.43 ATR), 4 970 (swing D1 ×2, ostatnio 2026-07-28, -0.68 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5072.00 (10 sesji), TP1 przed przeciwną granicą | 5 093 | 4 884 | 5 601 / 5 720 | 1.73 | -0.10 ATR | 10 | silny poziom 5428.0 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5622.00: zmiana reżimu, wejście z kontynuacji | 5 643 | 5 120 | 6 689 / 7 211 | 1.72 | +2.53 ATR | 4 | stop 2.53× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5622.00 (10 sesji), TP1 przed przeciwną granicą | 5 601 | 5 810 | 5 093 / 4 974 | 1.73 | +2.33 ATR | 10 | limit 2.33× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5072.00: zmiana reżimu, wejście z kontynuacji | 5 051 | 5 574 | 4 005 / 3 483 | 1.72 | -0.30 ATR | 4 | silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim |

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-12 |  | kawa | Cecafé: eksport kawy z Brazylii za październik | średnia |
| 2026-11-13 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-16 |  | kakao | First Notice Day kakao XII (CCZ26) wg reguły ICE (10 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-16 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-19 |  | kawa | First Notice Day kawy XII (KCZ26) wg reguły ICE (7 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-20 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-23 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
