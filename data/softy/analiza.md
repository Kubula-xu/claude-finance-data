# Softy: kawa i kakao, analiza z 2026-11-11 02:47 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 266,75 c/lb (2026-11-10T18:15:00Z UTC). ATR D1 10,05, ATR H1 (sesja) 3,49. 5 sesji -6.1%, 20 sesji -8.9%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 272.80). Zakres 10 sesji 272,80–304,90 (20 sesji 272,80–318,20), EMA20 287,53, EMA50 297,35, SMA200 302,88.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 272.80 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 115% normy, prognoza 16 dni 90% normy (średnia ważona regionów) |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +2.04%, 5 dni temu +3.76%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.580, 5 sesji +2.6%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.3%, wzrost w 50% lat |

Opory: 268,73 (R1, +0.20 ATR), 269,52 (swing D1 ×3, ostatnio 2026-11-10, +0.28 ATR), 270,72 (R2, +0.40 ATR), 279,60 (swing D1 ×2, ostatnio 2026-10-29, +1.28 ATR)

Wsparcia: 265,30 (dołek 5 sesji, -0.14 ATR), 265,03 (S1, -0.17 ATR), 264,07 (swing D1 ×2, ostatnio 2026-11-10, -0.27 ATR), 263,32 (S2, -0.34 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 263.32 (S2) | 264,33 | 244,22 | 304,53 / 324,63 | 1.81 | -0.24 ATR | 6 | silny poziom 269.52 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 269.00 | 270,01 | 249,90 | 310,21 / 330,31 | 1.81 | +0.32 ATR | 6 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 279.60 (swing D1 ×2, ostatnio 2026-10-29) | 278,59 | 298,70 | 238,39 / 218,29 | 1.81 | +1.18 ATR | 6 | limit 1.18× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 265.3 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 265.30 | 264,29 | 284,40 | 224,09 / 203,99 | 1.81 | -0.24 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 4 852 USD/t (2026-11-10T18:15:00Z UTC). ATR D1 215, ATR H1 (sesja) 83. 5 sesji -10.4%, 20 sesji -15.4%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 4978.00). Zakres 10 sesji 4 978–5 622 (20 sesji 4 978–6 023), EMA20 5 388, EMA50 5 521, SMA200 4 602.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 4978.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 188% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.64%, 5 dni temu -1.85%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.8%, wzrost w 69% lat |

Opory: 4 891 (P, +0.18 ATR), 4 970 (swing D1 ×2, ostatnio 2026-07-28, +0.55 ATR), 5 000 (okrągły poziom, +0.69 ATR), 5 014 (R1, +0.75 ATR)

Wsparcia: 4 784 (swing D1 ×2, ostatnio 2026-11-10, -0.32 ATR), 4 768 (dołek 5 sesji, -0.39 ATR), 4 729 (S1, -0.57 ATR), 4 632 (swing D1 ×1, ostatnio 2026-05-11, -1.02 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4784.00 (swing D1 ×2, ostatnio 2026-11-10) | 4 805 | 4 269 | 5 879 / 6 416 | 1.73 | -0.22 ATR | 4 | silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5053.00 | 5 074 | 4 538 | 6 148 / 6 685 | 1.73 | +1.04 ATR | 4 | stop 1.04× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 5078.75 (swing D1 ×4, ostatnio 2026-11-10) | 5 057 | 5 594 | 3 983 / 3 446 | 1.73 | +0.96 ATR | 4 | limit 0.96× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 4784.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 4768.00 | 4 747 | 5 283 | 3 673 / 3 136 | 1.73 | -0.49 ATR | 4 | R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |

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
