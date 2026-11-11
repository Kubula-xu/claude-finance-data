# Softy: kawa i kakao, analiza z 2026-11-11 15:35 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): SHORT 3/5 (suma -2.0)

- Cena 262,70 c/lb (2026-11-11T14:00:00Z UTC), sesja w trakcie. ATR D1 9,83, ATR H1 (sesja) 3,22. 5 sesji -4.4%, 20 sesji -7.3%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 272.80). Zakres 10 sesji 272,80–304,90 (20 sesji 272,80–318,20), EMA20 287,98, EMA50 297,53, SMA200 302,91.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 272.80 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 113% normy, prognoza 16 dni 124% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | -0.5 | KCZ26.NYB vs KCH27.NYB: +1.87%, 5 dni temu +4.12%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | +0.0 | USD/BRL 5.565, 5 sesji +1.4% |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.3%, wzrost w 50% lat |

Opory: 267,57 (S2, +0.50 ATR), 269,48 (S1, +0.69 ATR), 270,00 (okrągły poziom, +0.74 ATR), 270,12 (swing D1 ×3, ostatnio 2026-11-10, +0.76 ATR)

Wsparcia: 250,00 (okrągły poziom, -1.29 ATR), 242,70 (swing D1 ×1, ostatnio 2026-06-09, -2.04 ATR), 240,00 (okrągły poziom, -2.31 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 250.00 (okrągły poziom) | 250,98 | 231,33 | 290,28 / 309,93 | 1.81 | -1.19 ATR | 6 | limit 1.19× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 270.12 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 275.95 | 276,93 | 257,28 | 316,23 / 335,88 | 1.81 | +1.45 ATR | 6 | stop 1.45× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 270.12 (swing D1 ×3, ostatnio 2026-11-10) | 269,14 | 288,79 | 229,84 / 210,19 | 1.81 | +0.66 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 262.70 | 261,72 | 281,37 | 222,42 / 202,77 | 1.81 | -0.10 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 5 033 USD/t (2026-11-11T14:00:00Z UTC), sesja w trakcie. ATR D1 220, ATR H1 (sesja) 83. 5 sesji -12.4%, 20 sesji -17.3%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 4978.00). Zakres 10 sesji 4 978–5 622 (20 sesji 4 978–6 023), EMA20 5 378, EMA50 5 516, SMA200 4 602.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 4978.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 207% normy, prognoza 16 dni 161% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.68%, 5 dni temu -1.77%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.8%, wzrost w 69% lat |

Opory: 5 075 (R2, +0.19 ATR), 5 087 (swing D1 ×3, ostatnio 2026-10-01, +0.25 ATR), 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.83 ATR), 5 250 (okrągły poziom, +0.98 ATR)

Wsparcia: 4 961 (swing D1 ×3, ostatnio 2026-11-10, -0.33 ATR), 4 909 (R1, -0.56 ATR), 4 800 (swing D1 ×1, ostatnio 2026-06-29, -1.06 ATR), 4 774 (P, -1.17 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4960.67 (swing D1 ×3, ostatnio 2026-11-10) | 4 983 | 4 432 | 6 085 / 6 636 | 1.73 | -0.23 ATR | 4 | silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 5033.00 | 5 055 | 4 504 | 6 157 / 6 708 | 1.73 | +0.10 ATR | 4 | silny poziom 5428.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 5216.00 (swing D1 ×1, ostatnio 2026-07-16) | 5 194 | 5 745 | 4 092 / 3 541 | 1.73 | +0.73 ATR | 4 | silny poziom 4960.67 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 4640.00 | 4 618 | 5 169 | 3 516 / 2 965 | 1.73 | -1.88 ATR | 4 | stop 1.88× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |

## Alerty

- kawa: bias NEUTRAL → SHORT (3/5)

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
