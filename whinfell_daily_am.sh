#!/bin/zsh
set -euo pipefail

cd ~/Desktop/Whinfell_BUILD_Cousins

python3 run_csv_download.py daily \
  --operator clark \
  --window today \
  --downloads ~/Downloads/whinfell_drop \
  --staged-root ./staged_raw \
  --hydrate-output data/hydration/latest.json

open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html
