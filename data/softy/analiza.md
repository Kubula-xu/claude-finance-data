# Softy: kawa i kakao, analiza z 2026-11-10 16:02 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 2/5 (suma -1.5)

- Cena 266,70 c/lb (2026-11-09T18:15:00Z UTC). ATR D1 10,14, ATR H1 (sesja) 3,60. 5 sesji -6.3%, 20 sesji -5.8%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 276.00). Zakres 10 sesji 276,00–304,90 (20 sesji 276,00–318,20), EMA20 289,72, EMA50 298,60, SMA200 303,33.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 276.00 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 115% normy, prognoza 16 dni 156% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +2.40%, 5 dni temu +3.76%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.591, 5 sesji +2.8%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana -1.1%, wzrost w 46% lat |

Opory: 267,87 (S2, +0.12 ATR), 270,73 (S1, +0.40 ATR), 270,78 (swing D1 ×3, ostatnio 2026-11-09, +0.40 ATR), 272,80 (dołek 5 sesji, +0.60 ATR)

Wsparcia: 262,85 (swing D1 ×1, ostatnio 2026-05-19, -0.38 ATR), 260,00 (okrągły poziom, -0.66 ATR), 250,00 (okrągły poziom, -1.65 ATR), 242,70 (swing D1 ×1, ostatnio 2026-06-09, -2.37 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 262.85 (swing D1 ×1, ostatnio 2026-05-19) | 263,86 | 243,59 | 304,42 / 324,70 | 1.81 | -0.28 ATR | 6 | silny poziom 270.78 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 280.60 | 281,61 | 261,34 | 322,17 / 342,45 | 1.81 | +1.47 ATR | 6 | stop 1.47× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 270.78 (swing D1 ×3, ostatnio 2026-11-09) | 269,77 | 290,04 | 229,21 / 208,93 | 1.81 | +0.30 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 266.70 | 265,69 | 285,96 | 225,13 / 204,85 | 1.81 | -0.10 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 5 113 USD/t (2026-11-09T18:15:00Z UTC). ATR D1 209, ATR H1 (sesja) 80. 5 sesji -7.9%, 20 sesji -11.8%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 5072.00). Zakres 10 sesji 5 072–5 622 (20 sesji 5 072–6 023), EMA20 5 445, EMA50 5 548, SMA200 4 600.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 5072.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 199% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.45%, 5 dni temu -1.85%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.5%, wzrost w 65% lat |

Opory: 5 161 (R1, +0.23 ATR), 5 222 (swing D1 ×2, ostatnio 2026-11-09, +0.52 ATR), 5 250 (okrągły poziom, +0.66 ATR), 5 319 (R2, +0.98 ATR)

Wsparcia: 5 087 (swing D1 ×3, ostatnio 2026-10-01, -0.12 ATR), 5 070 (P, -0.21 ATR), 4 978 (dołek 5 sesji, -0.65 ATR), 4 973 (swing D1 ×3, ostatnio 2026-11-09, -0.67 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4973.00 (swing D1 ×3, ostatnio 2026-11-09) | 4 994 | 4 471 | 6 039 / 6 562 | 1.72 | -0.57 ATR | 4 | silny poziom 5221.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5227.00 | 5 248 | 4 725 | 6 293 / 6 816 | 1.72 | +0.65 ATR | 4 | silny poziom 5428.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 5221.50 (swing D1 ×2, ostatnio 2026-11-09) | 5 201 | 5 723 | 4 155 / 3 633 | 1.72 | +0.42 ATR | 4 | silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 4978.00 | 4 957 | 5 480 | 3 912 / 3 389 | 1.72 | -0.75 ATR | 4 | R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |

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
