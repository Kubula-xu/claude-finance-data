# Softy: kawa i kakao, analiza z 2026-11-12 01:35 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): SHORT 3/5 (suma -2.5)

- Cena 265,45 c/lb (2026-11-11T18:15:00Z UTC). ATR D1 9,49, ATR H1 (sesja) 3,22. 5 sesji -5.1%, 20 sesji -10.9%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 270.80). Zakres 10 sesji 270,80–297,35 (20 sesji 270,80–318,20), EMA20 285,83, EMA50 296,27, SMA200 302,40.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 270.80 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 107% normy, prognoza 16 dni 118% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | -0.5 | KCZ26.NYB vs KCH27.NYB: +1.53%, 5 dni temu +4.12%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.583, 5 sesji +1.7%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.4%, wzrost w 58% lat |

Opory: 267,85 (R1, +0.25 ATR), 268,98 (swing D1 ×3, ostatnio 2026-11-11, +0.37 ATR), 270,25 (R2, +0.51 ATR), 279,60 (swing D1 ×2, ostatnio 2026-10-29, +1.49 ATR)

Wsparcia: 262,60 (S1, -0.30 ATR), 262,50 (swing D1 ×2, ostatnio 2026-11-11, -0.31 ATR), 262,15 (dołek 5 sesji, -0.35 ATR), 260,00 (okrągły poziom, -0.57 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 262.50 (swing D1 ×2, ostatnio 2026-11-11) | 263,45 | 244,46 | 301,42 / 320,41 | 1.80 | -0.21 ATR | 7 | silny poziom 268.98 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.80 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 267.40 | 268,35 | 249,36 | 306,32 / 325,31 | 1.80 | +0.31 ATR | 7 | silny poziom 279.6 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.80 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 268.98 (swing D1 ×3, ostatnio 2026-11-11) | 268,03 | 287,02 | 230,06 / 211,07 | 1.80 | +0.27 ATR | 7 | silny poziom 262.5 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.80 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 262.15 | 261,20 | 280,19 | 223,23 / 204,24 | 1.80 | -0.45 ATR | 7 | R:R po kosztach 1.80 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 2/5 (suma +1.5)

- Cena 5 061 USD/t (2026-11-11T18:15:00Z UTC). ATR D1 224, ATR H1 (sesja) 82. 5 sesji -7.2%, 20 sesji -11.8%.
- Reżim: **zakres** (ADX 19, cena w zakresie 10 sesji 4640.00-5614.00). Zakres 10 sesji 4 640–5 614 (20 sesji 4 640–6 023), EMA20 5 348, EMA50 5 499, SMA200 4 605.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 19, cena w zakresie 10 sesji 4640.00-5614.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 148% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.73%, 5 dni temu -1.77%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +6.1%, wzrost w 73% lat |

Opory: 5 086 (swing D1 ×4, ostatnio 2026-11-11, +0.11 ATR), 5 161 (R1, +0.45 ATR), 5 216 (swing D1 ×1, ostatnio 2026-07-16, +0.69 ATR), 5 250 (okrągły poziom, +0.84 ATR)

Wsparcia: 4 984 (P, -0.34 ATR), 4 970 (swing D1 ×2, ostatnio 2026-07-28, -0.40 ATR), 4 884 (S1, -0.79 ATR), 4 804 (swing D1 ×2, ostatnio 2026-11-11, -1.15 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 4640.00 (10 sesji), TP1 przed przeciwną granicą | 4 662 | 4 439 | 5 592 / 5 703 | 3.15 | -1.78 ATR | 9 | limit 1.78× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 5086.5 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5614.00: zmiana reżimu, wejście z kontynuacji | 5 636 | 5 077 | 6 755 / 7 314 | 1.74 | +2.57 ATR | 4 | stop 2.57× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5614.00 (10 sesji), TP1 przed przeciwną granicą | 5 592 | 5 815 | 4 662 / 4 551 | 3.15 | +2.37 ATR | 9 | limit 2.37× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 4970.5 przed TP1: rozważyć częściowe wyjście przed nim |
| SHORT | stop: wybicie zakresu za 4640.00: zmiana reżimu, wejście z kontynuacji | 4 618 | 5 177 | 3 499 / 2 940 | 1.74 | -1.98 ATR | 4 | stop 1.98× ATR D1 od ceny: daleko, do przeliczenia po sesji |

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
