#!/usr/bin/env bash
# One-time setup — staged_raw/, manifests/, quarantine/ (Comet blueprint §1).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
STAGED="${STAGED_ROOT:-$ROOT/staged_raw}"
python3 run_csv_download.py init --staged-root "$STAGED"
mkdir -p "$ROOT/data/hydration"
echo "=== One-time setup complete ==="
echo "staged_root=$STAGED"
echo "hydration=$ROOT/data/hydration/latest.json"
echo "Next: save Koyfin/Barchart backup views (see 08_Deliverables/Comet_Browser_Operations_Blueprint.md)"