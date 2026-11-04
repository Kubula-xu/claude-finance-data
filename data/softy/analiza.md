# Softy: kawa i kakao, analiza z 2026-11-04 22:24 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 279,50 c/lb (2026-11-04T18:15:00Z UTC). ATR D1 11,41, ATR H1 (sesja) 3,65. 5 sesji -2.5%, 20 sesji -4.5%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 280.80). Zakres 10 sesji 280,80–317,90 (20 sesji 280,80–318,20), EMA20 294,22, EMA50 301,36, SMA200 304,41.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 280.80 |
| COT | +1.0 | fundusze net +20,104, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 130% normy, prognoza 16 dni 104% normy (średnia ważona regionów) |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +3.24%, 5 dni temu +5.52%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.477, 5 sesji +2.4%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.3%, wzrost w 58% lat |

Opory: 280,82 (P, +0.12 ATR), 284,13 (R1, +0.41 ATR), 285,32 (swing D1 ×3, ostatnio 2026-11-04, +0.51 ATR), 288,77 (R2, +0.81 ATR)

Wsparcia: 278,90 (swing D1 ×3, ostatnio 2026-11-04, -0.05 ATR), 277,50 (dołek 5 sesji, -0.18 ATR), 276,18 (S1, -0.29 ATR), 272,87 (S2, -0.58 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 269.77 (swing D1 ×2, ostatnio 2026-09-23) | 270,91 | 248,08 | 316,57 / 339,40 | 1.83 | -0.75 ATR | 6 | limit 0.75× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 285.32 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 285.45 | 286,59 | 263,76 | 332,25 / 355,08 | 1.83 | +0.62 ATR | 6 | silny poziom 297.35 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 285.32 (swing D1 ×3, ostatnio 2026-11-04) | 284,18 | 307,01 | 238,52 / 215,69 | 1.83 | +0.41 ATR | 6 | silny poziom 278.9 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 277.50 | 276,36 | 299,19 | 230,70 / 207,87 | 1.83 | -0.28 ATR | 6 | silny poziom 269.77 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.83 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): LONG 3/5 (suma +2.0)

- Cena 5 427 USD/t (2026-11-04T18:15:00Z UTC). ATR D1 199, ATR H1 (sesja) 72. 5 sesji -0.5%, 20 sesji -2.8%.
- Reżim: **zakres** (ADX 11, cena w zakresie 10 sesji 5343.00-5859.00; nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5427.00)). Zakres 10 sesji 5 343–5 859 (20 sesji 5 343–6 023), EMA20 5 560, EMA50 5 603, SMA200 4 589.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +0.0 | ADX 11, cena w zakresie 10 sesji 5343.00-5859.00; nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5427.00) |
| COT | +0.5 | fundusze net -10,940 (13. percentyl 3 lat), zmiana 4 tyg. +5,082: pozycjonowanie bez skrajności, liczy się kierunek przepływu |
| Pogoda | +1.0 | opad 30 dni 196% normy, prognoza 16 dni 192% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | +0.0 | CCZ26.NYB vs CCH27.NYB: -1.82%, 5 dni temu -1.95%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.2%, wzrost w 69% lat |

Opory: 5 443 (swing D1 ×3, ostatnio 2026-11-04, +0.08 ATR), 5 508 (R1, +0.41 ATR), 5 571 (swing D1 ×4, ostatnio 2026-11-02, +0.73 ATR), 5 589 (R2, +0.81 ATR)

Wsparcia: 5 391 (P, -0.18 ATR), 5 310 (S1, -0.59 ATR), 5 274 (dołek 5 sesji, -0.77 ATR), 5 250 (okrągły poziom, -0.89 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: granica zakresu 5343.00 (10 sesji), TP1 przed przeciwną granicą | 5 363 | 5 164 | 5 839 / 5 959 | 1.67 | -0.32 ATR | 10 | silny poziom 5442.67 przed TP1: rozważyć częściowe wyjście przed nim |
| LONG | stop: wybicie zakresu za 5859.00: zmiana reżimu, wejście z kontynuacji | 5 879 | 5 382 | 6 873 / 7 370 | 1.71 | +2.27 ATR | 5 | stop 2.27× ATR D1 od ceny: daleko, do przeliczenia po sesji |
| SHORT | limit: granica zakresu 5859.00 (10 sesji), TP1 przed przeciwną granicą | 5 839 | 6 038 | 5 363 / 5 243 | 1.67 | +2.07 ATR | 10 | limit 2.07× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop |
| SHORT | stop: wybicie zakresu za 5343.00: zmiana reżimu, wejście z kontynuacji | 5 323 | 5 820 | 4 329 / 3 832 | 1.71 | -0.52 ATR | 5 | silny poziom 5274.0 przed TP1: rozważyć częściowe wyjście przed nim |

## Alerty

- kawa: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia
- kakao: nieudane wybicie dołem (5274.00 < 5343.00, zamknięcie 5427.00)

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
