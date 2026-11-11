# Softy: kawa i kakao, analiza z 2026-11-11 09:51 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -0.5)

- Cena 266,75 c/lb (2026-11-10T18:15:00Z UTC). ATR D1 9,83, ATR H1 (sesja) 3,49. 5 sesji -4.4%, 20 sesji -7.3%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 272.80). Zakres 10 sesji 272,80–304,90 (20 sesji 272,80–318,20), EMA20 287,98, EMA50 297,53, SMA200 302,91.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 272.80 |
| COT | +1.0 | fundusze net +14,732, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +0.0 | opad 30 dni 115% normy, prognoza 16 dni 90% normy (średnia ważona regionów) |
| Krzywa | +0.5 | KCZ26.NYB vs KCH27.NYB: +2.04%, 5 dni temu +3.76%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.580, 5 sesji +2.6%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +1.3%, wzrost w 50% lat |

Opory: 267,57 (S2, +0.08 ATR), 269,48 (S1, +0.28 ATR), 270,12 (swing D1 ×3, ostatnio 2026-11-10, +0.34 ATR), 270,80 (dołek 5 sesji, +0.41 ATR)

Wsparcia: 262,85 (swing D1 ×1, ostatnio 2026-05-19, -0.40 ATR), 260,00 (okrągły poziom, -0.69 ATR), 250,00 (okrągły poziom, -1.70 ATR), 242,70 (swing D1 ×1, ostatnio 2026-06-09, -2.45 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 262.85 (swing D1 ×1, ostatnio 2026-05-19) | 263,83 | 244,18 | 303,13 / 322,78 | 1.81 | -0.30 ATR | 6 | silny poziom 270.12 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 275.95 | 276,93 | 257,28 | 316,23 / 335,88 | 1.81 | +1.04 ATR | 6 | stop 1.04× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 270.12 (swing D1 ×3, ostatnio 2026-11-10) | 269,14 | 288,79 | 229,84 / 210,19 | 1.81 | +0.24 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 266.75 | 265,77 | 285,42 | 226,47 / 206,82 | 1.81 | -0.10 ATR | 6 | R:R po kosztach 1.81 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): NEUTRAL 1/5 (suma +0.0)

- Cena 4 852 USD/t (2026-11-10T18:15:00Z UTC). ATR D1 220, ATR H1 (sesja) 83. 5 sesji -12.4%, 20 sesji -17.3%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 4978.00). Zakres 10 sesji 4 978–5 622 (20 sesji 4 978–6 023), EMA20 5 378, EMA50 5 516, SMA200 4 602.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 4978.00 |
| COT | +1.0 | fundusze net -12,253, 9. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 200% normy, prognoza 16 dni 188% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | -1.0 | CCZ26.NYB vs CCH27.NYB: -2.64%, 5 dni temu -1.85%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +5.8%, wzrost w 69% lat |

Opory: 4 909 (R1, +0.26 ATR), 4 961 (swing D1 ×3, ostatnio 2026-11-10, +0.49 ATR), 5 000 (okrągły poziom, +0.67 ATR), 5 075 (R2, +1.01 ATR)

Wsparcia: 4 800 (swing D1 ×1, ostatnio 2026-06-29, -0.24 ATR), 4 774 (P, -0.35 ATR), 4 640 (dołek 5 sesji, -0.96 ATR), 4 636 (swing D1 ×2, ostatnio 2026-11-10, -0.98 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | limit: cofnięcie do 4640.00 (dołek 5 sesji) | 4 662 | 4 111 | 5 764 / 6 315 | 1.73 | -0.86 ATR | 4 | limit 0.86× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; silny poziom 4960.67 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 4941.00 | 4 963 | 4 412 | 6 065 / 6 616 | 1.73 | +0.50 ATR | 4 | silny poziom 5087.33 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 4960.67 (swing D1 ×3, ostatnio 2026-11-10) | 4 939 | 5 490 | 3 836 / 3 285 | 1.73 | +0.39 ATR | 4 | silny poziom 4640.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 4640.00 | 4 618 | 5 169 | 3 516 / 2 965 | 1.73 | -1.06 ATR | 4 | stop 1.06× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.73 < 2.0: według ryzyko.md 10a nie składać |

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
