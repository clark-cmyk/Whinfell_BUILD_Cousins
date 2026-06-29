#!/bin/zsh
set -euo pipefail

cd "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"

echo "=== Whinfell EOD Handoff ==="
echo "operator=clark mode=eod"
echo ""

echo "Refreshing hydration bundle (latest Parquet → JSON)…"
python3 run_csv_download.py hydrate \
  --hydrate-output data/hydration/latest.json

echo ""
echo "EOD checklist:"
echo "  1. Transmission Control → update Handover / Watch Items"
echo "  2. Save State"
echo "  3. Confirm gate + gross risk for next session"
echo ""
echo "Hydration bundle: data/hydration/latest.json"

open "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html"
open "/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins/data/hydration"