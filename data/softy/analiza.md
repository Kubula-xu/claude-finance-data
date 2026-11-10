# Softy: kawa i kakao, analiza z 2026-11-10 17:33 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 2/5 (suma -1.5)

- Cena 266,45 c/lb (2026-11-10T16:00:00Z UTC), sesja w trakcie. ATR D1 10,14, ATR H1 (sesja) 3,51. 5 sesji -6.3%, 20 sesji -5.8%.
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

Opory: 267,87 (S2, +0.14 ATR), 270,73 (S1, +0.42 ATR), 270,78 (swing D1 ×3, ostatnio 2026-11-09, +0.43 ATR), 272,80 (dołek 5 sesji, +0.63 ATR)

Wsparcia: 262,85 (swing D1 ×1, ostatnio 2026-05-19, -0.36 ATR), 260,00 (okrągły poziom, -0.64 ATR), 250,00 (okrągły poziom, -1.62 ATR), 242,70 (swing D1 ×1, ostatnio 2026-06-09, -2.34 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 262.85 (swing D1 ×1, ostatnio 2026-05-19) | 263,86 | 243,59 | 304,42 / 324,70 | 1.81 | -0.26 ATR | 6 | silny poziom 270.78 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 280.60 | 281,61 | 261,34 | 322,17 / 342,45 | 1.81 | +1.50 ATR | 6 | stop 1.50× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 270.78 (swing D1 ×3, ostatnio 2026-11-09) | 269,77 | 290,04 | 229,21 / 208,93 | 1.81 | +0.33 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 266.45 | 265,44 | 285,71 | 224,88 / 204,60 | 1.81 | -0.10 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 4 864 USD/t (2026-11-10T16:00:00Z UTC), sesja w trakcie. ATR D1 209, ATR H1 (sesja) 83. 5 sesji -7.9%, 20 sesji -11.8%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 5072.00). Zakres 10 sesji 5 072–5 622 (20 sesji 5 072–6 023), EMA20 5 445, EMA50 5 548, SMA200 4 600.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 5072.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 199% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.45%, 5 dni temu -1.85%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.5%, wzrost w 65% lat |

Opory: 4 912 (S1, +0.23 ATR), 4 973 (swing D1 ×3, ostatnio 2026-11-09, +0.52 ATR), 4 978 (dołek 5 sesji, +0.55 ATR), 5 000 (okrągły poziom, +0.65 ATR)

Wsparcia: 4 821 (S2, -0.21 ATR), 4 800 (swing D1 ×1, ostatnio 2026-06-29, -0.31 ATR), 4 632 (swing D1 ×1, ostatnio 2026-05-11, -1.11 ATR), 4 500 (okrągły poziom, -1.74 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4800.00 (swing D1 ×1, ostatnio 2026-06-29) | 4 821 | 4 298 | 5 866 / 6 389 | 1.72 | -0.21 ATR | 4 | silny poziom 4973.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5227.00 | 5 248 | 4 725 | 6 293 / 6 816 | 1.72 | +1.84 ATR | 4 | stop 1.84× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 4973.00 (swing D1 ×3, ostatnio 2026-11-09) | 4 952 | 5 475 | 3 907 / 3 384 | 1.72 | +0.42 ATR | 4 | R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 4864.00 | 4 843 | 5 366 | 3 798 / 3 275 | 1.72 | -0.10 ATR | 4 | R:R po kosztach 1.72 < 2.0: według ryzyko.md 10a nie składać |

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
