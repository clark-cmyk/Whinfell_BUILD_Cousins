#!/usr/bin/env bash
# Morning daily chain — Comet Browser Operations Blueprint.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
OPERATOR="${OPERATOR:-desk}"
WINDOW="${WINDOW:-today}"
HYDRATE_OUT="${HYDRATE_OUT:-$ROOT/data/hydration/latest.json}"
DOWNLOADS="${DOWNLOADS:-$HOME/Downloads}"

echo "=== Whinfell morning daily chain ==="
echo "operator=$OPERATOR window=$WINDOW downloads=$DOWNLOADS"
python3 run_csv_download.py daily \
  --downloads "$DOWNLOADS" \
  --operator "$OPERATOR" \
  --window "$WINDOW" \
  --hydrate-output "$HYDRATE_OUT"
echo ""
echo "Next: open Transmission Control → Import Latest Hydration Bundle"
echo "File: $HYDRATE_OUT"