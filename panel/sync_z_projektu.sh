#!/usr/bin/env bash
# Kopiuje dziennik, sygnały, pivoty i raporty z folderu projektu do panel/projekt/ i wypycha je do repo.
# Push uruchamia workflow „Pulpit (GitHub Pages)”, który przebudowuje stronę.
# Użycie: panel/sync_z_projektu.sh ["opis zmiany"]
set -euo pipefail
SRC=${PROJEKT:-/mnt/project-files}
REPO=$(cd "$(dirname "$0")/.." && pwd)
DST="$REPO/panel/projekt"
mkdir -p "$DST/dane/d1_investing" "$DST/agenci" "$DST/raporty"
cp "$SRC/agenci/paper_trading.md" "$DST/agenci/"
cp "$SRC/dane/sygnaly.json" "$DST/dane/"
cp "$SRC"/dane/intraday_poziomy_*.csv "$DST/dane/" 2>/dev/null || true
cp "$SRC"/dane/d1_investing/*.csv "$SRC"/dane/d1_investing/README.md "$DST/dane/d1_investing/" 2>/dev/null || true
cp "$SRC"/raporty/*.html "$SRC"/raporty/*.md "$DST/raporty/" 2>/dev/null || true
cd "$REPO"
git add panel/projekt
git diff --cached --quiet && { echo "Bez zmian."; exit 0; }
printf '{"zsynchronizowano_utc": "%s"}\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$DST/sync.json"
git add panel/projekt
git commit -q -m "pulpit: ${1:-aktualizacja pozycji i raportów}"
for i in 1 2 3 4; do git pull -q --rebase origin main && git push -q origin HEAD:main && { echo "Wypchnięte."; exit 0; }; sleep $((2**i)); done
exit 1
