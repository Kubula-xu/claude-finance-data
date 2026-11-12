# Softy: kawa i kakao, analiza z 2026-11-12 13:42 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): SHORT 3/5 (suma -2.5)

- Cena 269,35 c/lb (2026-11-12T12:15:00Z UTC), sesja w trakcie. ATR D1 9,19, ATR H1 (sesja) 3,10. 5 sesji -3.8%, 20 sesji -9.8%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 270.80). Zakres 10 sesji 270,80–297,35 (20 sesji 270,80–318,20), EMA20 286,17, EMA50 296,41, SMA200 302,42.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 270.80 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 107% normy, prognoza 16 dni 118% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | -0.5 | KCZ26.NYB vs KCH27.NYB: +1.53%, 5 dni temu +4.12%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.583, 5 sesji +1.7%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.4%, wzrost w 58% lat |

Opory: 271,67 (R1, +0.25 ATR), 271,95 (swing D1 ×1, ostatnio 2026-11-11, +0.28 ATR), 274,33 (R2, +0.54 ATR), 279,60 (swing D1 ×2, ostatnio 2026-10-29, +1.11 ATR)

Wsparcia: 268,82 (swing D1 ×3, ostatnio 2026-11-11, -0.06 ATR), 266,90 (dołek 5 sesji, -0.27 ATR), 266,62 (S1, -0.30 ATR), 264,23 (S2, -0.56 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 264.23 (S2) | 265,15 | 246,76 | 301,92 / 320,31 | 1.79 | -0.46 ATR | 7 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.79 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 271.95 | 272,87 | 254,48 | 309,64 / 328,03 | 1.79 | +0.38 ATR | 7 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.79 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 279.60 (swing D1 ×2, ostatnio 2026-10-29) | 278,68 | 297,07 | 241,91 / 223,52 | 1.79 | +1.01 ATR | 7 | limit 1.01× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 268.82 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.79 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 266.90 | 265,98 | 284,37 | 229,21 / 210,82 | 1.79 | -0.37 ATR | 7 | R:R po kosztach 1.79 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 2/5 (suma +1.5)

- Cena 5 060 USD/t (2026-11-12T12:15:00Z UTC), sesja w trakcie. ATR D1 219, ATR H1 (sesja) 80. 5 sesji -10.1%, 20 sesji -14.4%.
- Reżim: **zakres** (ADX 20, cena w zakresie 10 sesji 4640.00-5614.00). Zakres 10 sesji 4 640–5 614 (20 sesji 4 640–6 023), EMA20 5 333, EMA50 5 493, SMA200 4 604.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 20, cena w zakresie 10 sesji 4640.00-5614.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 148% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.73%, 5 dni temu -1.77%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +6.1%, wzrost w 73% lat |

Opory: 5 087 (swing D1 ×3, ostatnio 2026-10-01, +0.12 ATR), 5 115 (R2, +0.25 ATR), 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.71 ATR), 5 250 (okrągły poziom, +0.87 ATR)

Wsparcia: 5 011 (R1, -0.22 ATR), 4 962 (swing D1 ×3, ostatnio 2026-11-11, -0.45 ATR), 4 842 (P, -1.00 ATR), 4 800 (swing D1 ×1, ostatnio 2026-06-29, -1.19 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 4640.00 (10 sesji), TP1 przed przeciwną granicą | 4 662 | 4 443 | 5 592 / 5 702 | 3.21 | -1.82 ATR | 9 | limit 1.82× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5614.00: zmiana reżimu, wejście z kontynuacji | 5 636 | 5 089 | 6 730 / 7 277 | 1.73 | +2.63 ATR | 4 | stop 2.63× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5614.00 (10 sesji), TP1 przed przeciwną granicą | 5 592 | 5 811 | 4 662 / 4 552 | 3.21 | +2.43 ATR | 9 | limit 2.43× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 4962.33 przed TP1: rozważyć częściowe wyjście przed nim |
| SHORT | stop: wybicie zakresu za 4640.00: zmiana reżimu, wejście z kontynuacji | 4 618 | 5 165 | 3 524 / 2 977 | 1.73 | -2.02 ATR | 4 | stop 2.02× ATR D1 od ceny: daleko, do przeliczenia po sesji |

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
