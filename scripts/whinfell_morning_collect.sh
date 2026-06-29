#!/usr/bin/env zsh
# Fast morning CSV collection — opens batch URLs, watches drop dir, runs pipeline.
# Usage: scripts/whinfell_morning_collect.sh [--open-only | --watch-only | --run-only]
set -euo pipefail

REPO="${REPO:-$HOME/Desktop/Whinfell_BUILD_Cousins}"
DROP="${DROP:-$HOME/Downloads/whinfell_drop}"
MODE="${1:-full}"

cd "$REPO"
mkdir -p "$DROP"

case "$MODE" in
  --open-only)
    python3 run_batch_collect.py open
    echo ""
    echo "Export each browser tab → $DROP"
    echo "Then: python3 run_batch_collect.py run"
    ;;
  --watch-only)
    python3 run_batch_collect.py watch --auto-run --timeout 900
    ;;
  --run-only)
    python3 run_batch_collect.py run --window today
    ;;
  --api-only)
    python3 run_batch_collect.py fetch-api
    python3 run_batch_collect.py run --window today
    ;;
  full|*)
    echo "=== Whinfell fast collect ==="
    echo "1) Opening batch saved-view URLs..."
    python3 run_batch_collect.py open
    echo ""
    echo "2) Export each tab to: $DROP"
    echo "   (8 exports — NOT 13 per-ticker loops)"
    echo ""
    echo "3) Watching drop dir (up to 15 min)..."
    python3 run_batch_collect.py watch --auto-run --timeout 900 || true
    echo ""
    echo "4) Final status:"
    python3 run_batch_collect.py status || true
    echo ""
    echo "If not ready: python3 run_batch_collect.py run"
    echo "Then: Transmission Control → Import Latest Hydration Bundle"
    ;;
esac