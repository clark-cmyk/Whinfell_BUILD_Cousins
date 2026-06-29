#!/usr/bin/env bash
# Capture Barchart-only verification evidence to SCRATCH (plan verification plan).
set -euo pipefail

SCRATCH="${SCRATCH:-/var/folders/qn/gdsdhg9j3f77wk7fn889zbq40000gn/T/grok-goal-b053d4badfb2/implementer}"
REPO="${REPO:-$(cd "$(dirname "$0")/.." && pwd)}"

mkdir -p "$SCRATCH"
rm -f "$SCRATCH"/barchart_*

cd "$REPO"
rm -rf data/barchart/v1
mkdir -p data/barchart/v1

echo "=== capture start $(date -u +%Y-%m-%dT%H:%M:%SZ) repo=$REPO ===" >"$SCRATCH/barchart_evidence.txt"
echo "fetch_policy=file_only desk_path=whinfell_drop->staged_raw->ingest" | tee -a "$SCRATCH/barchart_evidence.txt"

# 1. Hydration x2
python3 run_batch_collect.py barchart-only 2>&1 | tee "$SCRATCH/barchart_hydration_1.log"
python3 run_batch_collect.py barchart-only 2>&1 | tee "$SCRATCH/barchart_hydration_2.log"

# 2. Outputs summary
{
  echo "=== outputs $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
  ls -l data/barchart/v1/
  python3 -c "
import json
from pathlib import Path
root = Path('data/barchart/v1')
for name in ['barchart_core_history','barchart_curve_history','barchart_spread_history','barchart_run_manifest']:
    d = json.loads((root / f'{name}.json').read_text())
    if name == 'barchart_run_manifest':
        print(name, 'approved', d['symbol_count_approved'], 'ok', d['symbol_count_ok'],
              'failed', d['symbol_count_failed'], 'outcomes', len(d['outcomes']))
    else:
        print(name, 'symbol_count', d['symbol_count'])
m = json.loads((root/'barchart_run_manifest.json').read_text())
print('fetch_modes', {k:v['fetch_mode'] for k,v in list(m.get('local_supplements',{}).items())[:5]})
btn = m['local_supplements'].get('BTN26', {})
btc = m['local_supplements'].get('^BTCUSD', {})
print('BTN26_supplement', btn)
print('BTC_supplement', btc)
core = json.loads((root/'barchart_core_history.json').read_text())
spread = json.loads((root/'barchart_spread_history.json').read_text())
if core['records']:
    print('sample_core_record', core['records'][0]['raw_symbol'], core['records'][0]['fetch_mode'])
if spread['records']:
    print('sample_spread_record', spread['records'][0]['raw_symbol'], spread['records'][0]['fetch_mode'])
"
} | tee "$SCRATCH/barchart_outputs.txt"

# 3. Normalize verify x2
: >"$SCRATCH/normalize_verify.log"
for run in 1 2; do
  echo "=== normalize verify run $run $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" >>"$SCRATCH/normalize_verify.log"
  python3 -c "
from whinfell_pipeline.barchart_hydration import normalize_barchart_symbol, classify_bucket
samples = [('^XRPUSD', None), ('GCN26', 'metals_curves'), ('_S_BF_ZBU6_ZBZ6_ZBH7', None)]
for sym, hint in samples:
    n = normalize_barchart_symbol(sym, group_hint=hint)
    print('raw', sym, 'bucket', classify_bucket(sym), 'canonical', n.get('canonical_id'),
          'instrument_class', n.get('instrument_class'), 'pricing_mode', n.get('pricing_mode'))
" >>"$SCRATCH/normalize_verify.log"
done

# 4. Tests x2
: >"$SCRATCH/barchart_tests.log"
for run in 1 2; do
  echo "=== test run $run $(date -u +%Y-%m-%dT%H:%M:%SZ) ===" >>"$SCRATCH/barchart_tests.log"
  python3 -m unittest \
    whinfell_pipeline.tests.test_batch_collect \
    whinfell_pipeline.tests.test_raw_csv_transform_2_2e \
    whinfell_pipeline.tests.test_data_dictionary \
    whinfell_pipeline.tests.test_barchart_hydration \
    -v >>"$SCRATCH/barchart_tests.log" 2>&1
  echo "exit=$?" >>"$SCRATCH/barchart_tests.log"
done

# 5. Evidence appendix
{
  echo ""
  echo "commands:"
  echo "  python3 run_batch_collect.py barchart-only (x2)"
  echo "  python3 -m unittest test_batch_collect test_raw_csv_transform_2_2e test_data_dictionary test_barchart_hydration (x2)"
  echo "koyfin_mentions_run1=$(grep -ci koyfin "$SCRATCH/barchart_hydration_1.log" || true)"
  echo "koyfin_mentions_run2=$(grep -ci koyfin "$SCRATCH/barchart_hydration_2.log" || true)"
  echo "symbol_lines_run1=$(grep -c '^symbol=' "$SCRATCH/barchart_hydration_1.log" || true)"
  echo "manifest_path=$REPO/data/barchart/v1/barchart_run_manifest.json"
  echo "--- manifest head ---"
  head -40 "$REPO/data/barchart/v1/barchart_run_manifest.json"
  echo "--- recorded ingest proof (unit tests in barchart_tests.log) ---"
  grep -E "test_ingest_recorded_|test_watchlist|test_api_path|test_live_api|test_hydrate_from" "$SCRATCH/barchart_tests.log" | tail -24
} >>"$SCRATCH/barchart_evidence.txt"

echo "capture_ok scratch=$SCRATCH"