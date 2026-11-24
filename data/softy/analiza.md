# Softy: kawa i kakao, analiza z 2026-11-24 17:09 PL

Automat (softy/analiza.py). Bias to suma czynników z jawnymi wagami, nie wyrocznia: agent softów weryfikuje go newsami.

## Kawa (Arabica KC): NEUTRAL 1/5 (suma -1.0)

- Cena 262,95 c/lb (2026-11-24T15:45:00Z UTC), sesja w trakcie. ATR D1 7,54, ATR H1 (sesja) 3,16. 5 sesji -2.3%, 20 sesji -8.8%.
- Reżim: **wybicie dol** (zamknięcie/cena pod dołkiem 10 sesji 266.70). Zakres 10 sesji 266,70–288,30 (20 sesji 266,70–304,90), EMA20 282,42, EMA50 291,82, SMA200 300,64.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | -1.5 | zamknięcie/cena pod dołkiem 10 sesji 266.70 |
| COT | +1.0 | fundusze net +9,023, 1. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | -1.0 | opad 30 dni 100% normy, prognoza 16 dni 194% normy (średnia ważona regionów); deszcze kwitnienia dopisują: dobre perspektywy zbiorów 2027 |
| Krzywa | +1.0 | KCZ26.NYB vs KCH27.NYB: +2.82%, 5 dni temu +2.06%, backwardation (ciasno w bieżącej dostawie) |
| Zapasy ICE | +0.0 | 239,748 (2026-10-21), zmiana od 2026-10-13: -2.9% |
| BRL | -0.5 | USD/BRL 5.929, 5 sesji +2.5%: real słabnie, sprzedaż z Brazylii tańsza |
| Sezonowość | +0.0 | kolejne 20 sesji od tej daty w 26 latach: mediana +4.9%, wzrost w 58% lat |

Opory: 266,70 (swing D1 ×1, ostatnio 2026-11-12, +0.50 ATR), 269,77 (swing D1 ×2, ostatnio 2026-09-23, +0.90 ATR), 270,00 (okrągły poziom, +0.93 ATR), 273,05 (dołek 5 sesji, +1.34 ATR)

Wsparcia: 250,00 (okrągły poziom, -1.72 ATR), 242,70 (swing D1 ×1, ostatnio 2026-06-09, -2.68 ATR), 240,00 (okrągły poziom, -3.04 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG (pod prąd) | stop: kontynuacja: przebicie szczytu ostatniej sesji 274.90 | 275,65 | 260,57 | 305,83 / 320,91 | 1.75 | +1.68 ATR | 9 | stop 1.68× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | limit: cofnięcie do 269.77 (swing D1 ×2, ostatnio 2026-09-23) | 269,02 | 284,10 | 238,84 / 223,76 | 1.75 | +0.80 ATR | 9 | limit 0.80× ATR D1 od ceny: w 1-2 sesje mało realny, liczy się noga stop; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT | stop: kontynuacja: przebicie dołka ostatniej sesji 262.95 | 262,20 | 277,28 | 232,02 / 216,94 | 1.75 | -0.10 ATR | 9 | R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |

## Kakao (NY CC): LONG 5/5 (suma +4.0)

- Cena 5 417 USD/t (2026-11-24T15:45:00Z UTC), sesja w trakcie. ATR D1 233, ATR H1 (sesja) 88. 5 sesji +2.9%, 20 sesji -5.5%.
- Reżim: **wybicie gora** (zamknięcie/cena nad szczytem 10 sesji 5250.00; nieudane wybicie górą (5252.00 > 5250.00, zamknięcie 5186.00): uwaga na pułapkę albo drugie podejście). Zakres 10 sesji 4 640–5 250 (20 sesji 4 640–5 622), EMA20 5 186, EMA50 5 375, SMA200 4 639.

| Czynnik | Wynik | Opis |
|---|---|---|
| Technika (reżim) | +1.5 | zamknięcie/cena nad szczytem 10 sesji 5250.00; nieudane wybicie górą (5252.00 > 5250.00, zamknięcie 5186.00): uwaga na pułapkę albo drugie podejście |
| COT | +1.0 | fundusze net -19,213, 2. percentyl 3 lat: pozycja funduszy najniższa od lat, mało do likwidacji, paliwo do odbicia/squeeze |
| Pogoda | +1.0 | opad 30 dni 219% normy, prognoza 16 dni 126% normy (średnia ważona regionów); bardzo mokro: ryzyko czarnej zgnilizy strąków i problemy z suszeniem; Ekwador bardzo mokro (powodzie) |
| Krzywa | +0.0 | CCZ26.NYB vs CCH27.NYB: -1.70%, 5 dni temu -2.65%, contango (zapasy wystarczają) |
| Zapasy ICE | +0.0 | 3,635,354 (2026-10-21), zmiana od 2026-10-13: +1.6% |
| Sezonowość | +0.5 | kolejne 20 sesji od tej daty w 26 latach: mediana +2.2%, wzrost w 65% lat |

Opory: 5 571 (swing D1 ×4, ostatnio 2026-11-02, +0.66 ATR), 5 732 (swing D1 ×3, ostatnio 2026-09-28, +1.35 ATR), 5 750 (okrągły poziom, +1.43 ATR), 5 916 (swing D1 ×4, ostatnio 2026-10-20, +2.14 ATR)

Wsparcia: 5 338 (R2, -0.34 ATR), 5 262 (R1, -0.66 ATR), 5 252 (szczyt 5 sesji, -0.71 ATR), 5 250 (okrągły poziom, -0.72 ATR)

| Kierunek | Noga | Wejście | SL | TP1 / TP2 | R:R netto | Od ceny | Kontrakty | Uwagi |
|---|---|---|---|---|---|---|---|---|
| LONG | limit: cofnięcie do 5221.67 (swing D1 ×3, ostatnio 2026-11-23) | 5 245 | 4 661 | 6 412 / 6 996 | 1.75 | -0.74 ATR | 4 | silny poziom 5571.25 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| LONG | stop: kontynuacja: przebicie szczytu ostatniej sesji 5417.00 | 5 440 | 4 857 | 6 607 / 7 191 | 1.75 | +0.10 ATR | 4 | silny poziom 5571.25 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | limit: cofnięcie do 5571.25 (swing D1 ×4, ostatnio 2026-11-02) | 5 548 | 6 131 | 4 381 / 3 797 | 1.75 | +0.56 ATR | 4 | silny poziom 5252.0 przed TP1: rozważyć częściowe wyjście przed nim; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |
| SHORT (pod prąd) | stop: kontynuacja: przebicie dołka ostatniej sesji 5090.00 | 5 067 | 5 650 | 3 900 / 3 316 | 1.75 | -1.50 ATR | 4 | stop 1.50× ATR D1 od ceny: daleko, do przeliczenia po sesji; R:R po kosztach 1.75 < 2.0: według ryzyko.md 10a nie składać |

## Alerty

- kawa: reżim zakres → wybicie_dol: przeliczyć plan i wiszące zlecenia
- kakao: reżim zakres → wybicie_gora: przeliczyć plan i wiszące zlecenia
- kakao: nieudane wybicie górą (5252.00 > 5250.00, zamknięcie 5186.00): uwaga na pułapkę albo drugie podejście

## Kalendarz (14 dni)

| Data | Godz. PL | Rynek | Wydarzenie | Waga |
|---|---|---|---|---|
| 2026-11-27 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-11-30 |  | kakao | ICCO Quarterly Bulletin of Cocoa Statistics (rewizja bilansu 2025/26 i 2026/27) | średnia |
| 2026-11-30 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
| 2026-12-04 | 21:30 | oba | CFTC COT (stan na wtorek) | średnia |
| 2026-12-07 | rano | kakao | przybycia kakao do portów CIV (Reuters/Bloomberg, szacunki eksporterów) | średnia-wysoka |
