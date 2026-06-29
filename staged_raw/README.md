# staged_raw — Operator CSV staging (Comet runbook)

Drop collector CSV exports here before pipeline ingest. **Comet copies** from `~/Downloads` — originals are never moved. Processed files archive to `archived/` under each dataset folder after `collect` / `ingest --staged`.

## Layout

```
staged_raw/
├── manifests/              ← stage_manifest__*.json, daily_manifest__*.json
├── quarantine/YYYYMMDD/    ← bad filenames or header failures
├── source=barchart/
│   ├── dataset=futures_intraday/
│   ├── dataset=futures_daily/
│   ├── dataset=options/
│   └── dataset=greeks/
├── source=koyfin/
│   ├── dataset=rates/
│   ├── dataset=credit/
│   └── dataset=equities/
└── source=china_policy/
```

## Naming (required)

- `{dataset}_{YYYYMMDD}_{HHMM}.csv` — e.g. `rates_20260627_1400.csv`
- `{product}_{flavor}_{YYYYMMDD}.csv` — e.g. `btc_basis_20260627.csv`

Each staged CSV gets a sidecar `{filename}.csv.meta.json` (operator, sha256, source, dataset).

## Daily chain (Comet runbook)

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins

# One command
python3 run_csv_download.py daily \
  --operator desk \
  --window 24h \
  --hydrate-output data/hydration/latest.json

# Or step-by-step
python3 run_csv_download.py init
python3 run_csv_download.py stage --operator desk --window today
python3 run_csv_download.py collect
python3 run_csv_download.py hydrate --hydrate-output data/hydration/latest.json
```

Then **Import Latest Hydration Bundle** in Transmission Control (`data/hydration/latest.json`).

See `08_Deliverables/Comet_Browser_Operations_Blueprint.md` for Koyfin/Barchart backup view names and Comet shortcuts.

## Alternate ingest (unchanged)

```bash
python3 -m whinfell_pipeline.ingest --init-staged
python3 -m whinfell_pipeline.ingest --staged
python3 -m whinfell_pipeline.hydrate -o data/hydration/latest.json
```