# Softy: kawa i kakao, analiza z 2026-11-09 18:50 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma +0.5)

- Cena 267,35 c/lb (2026-11-09T17:15:00Z UTC). ATR D1 10,50, ATR H1 (sesja) 3,60. 5 sesji -8.5%, 20 sesji -8.0%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 276.00). Zakres 10 sesji 276,00–304,90 (20 sesji 276,00–318,20), EMA20 289,13, EMA50 298,35, SMA200 303,30.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 276.00 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 114% normy, prognoza 16 dni 81% normy (średnia ważona regionów) |
| Krzywa | +1.0 | KCZ26.NYB vs KCH27.NYB: +2.56%, 5 dni temu +3.14%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | +0.0 | USD/BRL 5.515, 5 sesji +1.5% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana -0.8%, wzrost w 46% lat |

Opory: 268,88 (swing D1 ×3, ostatnio 2026-11-09, +0.15 ATR), 269,15 (P, +0.17 ATR), 271,20 (R1, +0.37 ATR), 273,00 (swing D1 ×1, ostatnio 2026-11-09, +0.54 ATR)

Wsparcia: 265,30 (S1, -0.20 ATR), 263,25 (S2, -0.39 ATR), 262,85 (swing D1 ×1, ostatnio 2026-05-19, -0.43 ATR), 260,00 (okrągły poziom, -0.70 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 263.25 (S2) | 264,30 | 243,29 | 306,31 / 327,32 | 1.82 | -0.29 ATR | 6 | silny poziom 268.88 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 273.00 | 274,05 | 253,04 | 316,06 / 337,07 | 1.82 | +0.64 ATR | 6 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 279.60 (swing D1 ×2, ostatnio 2026-10-29) | 278,55 | 299,56 | 236,54 / 215,53 | 1.82 | +1.07 ATR | 6 | limit 1.07× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 267.10 | 266,05 | 287,06 | 224,04 / 203,03 | 1.82 | -0.12 ATR | 6 | R:R po kosztach 1.82 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 2/5 (suma +1.5)

- Cena 5 126 USD/t (2026-11-09T17:15:00Z UTC). ATR D1 209, ATR H1 (sesja) 80. 5 sesji -5.7%, 20 sesji -9.7%.
- Reżim: **zakres** (ADX 14, cena w zakresie 10 sesji 5072.00-5622.00). Zakres 10 sesji 5 072–5 622 (20 sesji 5 072–6 023), EMA20 5 457, EMA50 5 553, SMA200 4 601.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 14, cena w zakresie 10 sesji 5072.00-5622.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 194% normy, prognoza 16 dni 186% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.22%, 5 dni temu -1.92%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.5%, wzrost w 69% lat |

Opory: 5 187 (P, +0.29 ATR), 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.43 ATR), 5 282 (R1, +0.74 ATR), 5 343 (swing D1 ×1, ostatnio 2026-11-09, +1.04 ATR)

Wsparcia: 5 089 (swing D1 ×4, ostatnio 2026-11-09, -0.18 ATR), 5 072 (dołek 5 sesji, -0.26 ATR), 5 032 (S1, -0.45 ATR), 5 000 (okrągły poziom, -0.60 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5072.00 (10 sesji), TP1 przed przeciwną granicą | 5 093 | 4 884 | 5 601 / 5 720 | 1.73 | -0.16 ATR | 10 | silny poziom 5428.0 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5622.00: zmiana reżimu, wejście z kontynuacji | 5 643 | 5 120 | 6 689 / 7 211 | 1.72 | +2.47 ATR | 4 | stop 2.47× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5622.00 (10 sesji), TP1 przed przeciwną granicą | 5 601 | 5 810 | 5 093 / 4 974 | 1.73 | +2.27 ATR | 10 | limit 2.27× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5072.00: zmiana reżimu, wejście z kontynuacji | 5 051 | 5 574 | 4 005 / 3 483 | 1.72 | -0.36 ATR | 4 | silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim |

## Alerty

- kawa: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia
- kawa: bias LONG → NEUTRAL (1/5)

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-09 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-12 |  | kawa | Cecafé: eksport kawy z Brazylii za październik | średnia |
| 2026-11-13 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-16 |  | kakao | First Notice Day kakao XII (CCZ26) wg reguły ICE (10 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-16 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-11-19 |  | kawa | First Notice Day kawy XII (KCZ26) wg reguły ICE (7 dni rob. przed 1. dniem rob. miesiąca) | średnia |
| 2026-11-20 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-23 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
