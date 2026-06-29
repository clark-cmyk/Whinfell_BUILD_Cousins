#!/bin/zsh
# Barchart-only first-pass hydration — all approved symbols, no Koyfin.
PROJECT="/Users/clarksonwthornburgh/Desktop/Whinfell_BUILD_Cousins"
LOG="$HOME/Desktop/whinfell_barchart_hydration.log"
cd "$PROJECT" || exit 1
{
  echo "=== Whinfell Barchart Hydration $(date) ==="
  /usr/bin/python3 run_batch_collect.py barchart-only
  echo "exit=$?"
} 2>&1 | tee -a "$LOG"
read "?Press Enter to close..."