# Comet Adapter Handoff Package

**From:** BUILD Cousins (Whinfell Pipeline)  
**Date:** June 27, 2026  
**Purpose:** Unblock Comet `run_csv_download.py` integration with staged CSV → adapter registry → Parquet → Transmission Control

---

## Package contents

```
Comet_Adapter_Handoff/
├── MANIFEST.md                          ← this file
├── staged_raw/README.md                 ← operator CSV folder spec
└── whinfell_pipeline/
    ├── __init__.py
    ├── version.py                       ← COMET_COLLECTOR_ID / VERSION constants
    ├── canonical.py                     ← CanonicalRecord, ValidationStatus
    ├── lineage.py                       ← sha256 lineage hashing
    ├── ingest.py                        ← CLI: --input, --staged, --init-staged
    ├── staged_csv.py                    ← CSV scan/validate/archive (2.2c)
    ├── adapters/
    │   ├── base.py                      ← SourceAdapter, AdapterResult
    │   ├── registry.py                  ← get_adapter_for_payload, parse_with_best_adapter
    │   ├── comet_collector.py           ← Comet envelope → Koyfin/Barchart delegate
    │   ├── koyfin_adapter.py            ← Global + China Policy (Koyfin)
    │   ├── barchart_adapter.py          ← Execution + China (Barchart)
    │   ├── transmission_control.py      ← registry dep (browser export bundles)
    │   └── legacy_parser.py             ← registry dep (WTM text exports)
    └── examples/
        ├── comet_koyfin_global.json     ← Comet envelope example (global)
        ├── comet_koyfin_china.json      ← Comet envelope example (china)
        ├── comet_barchart_btc.json      ← Comet envelope example (execution)
        └── staged/*.csv                 ← staged_raw CSV templates
```

---

## Comet collector contract

### Envelope (JSON — for live collector / non-CSV path)

```json
{
  "collector_version": "1.0.0",
  "collector_id": "comet-first-pass",
  "collected_at": "2026-06-27T14:00:00Z",
  "source_channel": "koyfin",
  "track": "global",
  "page_url": "https://app.koyfin.com/",
  "payload": { ... channel-specific fields ... }
}
```

| Field | Required | Notes |
|-------|----------|-------|
| `collector_version` | yes | Must be `1.0.0` (`version.COMET_COLLECTOR_VERSION`) |
| `collector_id` | yes | `comet-first-pass` (`version.COMET_COLLECTOR_ID`) |
| `source_channel` | yes | `koyfin` or `barchart` (routes in `comet_collector.py`) |
| `payload` | yes | Dict passed to delegate adapter |
| `track` | optional | `global`, `china_policy`, `execution` hint |
| `page_url` | optional | Stored as `_page_url` on payload |
| `collected_at` | optional | ISO timestamp → `timestamp` / `as_of` on payload |

### CSV staging path (Comet `run_csv_download.py` target)

Drop files into `staged_raw/` using Hive-style folders:

| Folder | Datasets |
|--------|----------|
| `source=barchart/dataset=futures_intraday/` | (+ futures_daily, options, greeks) |
| `source=koyfin/dataset=rates/` | (+ credit, equities) |
| `source=china_policy/` | CSV at source root |

**Filename:** `{dataset}_{YYYYMMDD}_{HHMM}.csv` or `{product}_{flavor}_{YYYYMMDD}.csv`

**Flow:** CSV row → flat dict with `source` + `_track_hint` → `parse_with_best_adapter()` → Parquet

See `examples/staged/*.csv` for header templates.

---

## Adapter registry order

```python
_DEFAULT_ADAPTERS = (
    TransmissionControlAdapter(),  # browser JSON bundles
    CometCollectorAdapter(),       # Comet envelope (collector_id / source_channel)
    KoyfinAdapter(),               # source=koyfin or global/china fields
    BarchartAdapter(),             # source=barchart or execution fields
    LegacyParserAdapter(),         # WTM EXPORT text
)
```

**Comet CSV integration:** After download, either:
1. Write CSV to `staged_raw/` and run `python3 -m whinfell_pipeline.ingest --staged`, or
2. Build Comet envelope JSON and run `python3 -m whinfell_pipeline.ingest --input file.json`

---

## Key payload fields

### Koyfin / Global (`track: global`)

| Field | Required |
|-------|----------|
| `observation_id` | recommended |
| `timestamp` | yes |
| `whinfell_score` | yes |
| `transmission_state` | yes |
| `regime_tag` | yes |
| `key_observation` | recommended |

### Barchart / Execution (`track: execution`)

| Field | Required |
|-------|----------|
| `timestamp` | yes |
| `near_month` or `basis_spread` | at least one |
| `far_month`, `ref_low`, `ref_mid`, `ref_high` | optional |

### China Policy (`source=china_policy` or Koyfin china track)

| Field | Required |
|-------|----------|
| `observation_id` | recommended |
| `timestamp` | yes |
| `policy_strength` | yes |
| `state_impulse_score`, `growth_impulse_score` | recommended |

---

## Operator commands (post-Comet CSV drop)

```bash
# Initialize staged folders (one-time)
python3 -m whinfell_pipeline.ingest --init-staged

# Ingest all pending CSVs → Parquet + archive
python3 -m whinfell_pipeline.ingest --staged

# Hydrate for Transmission Control
python3 -m whinfell_pipeline.hydrate -o hydration.json
```

---

## External dependency (not in this zip)

- `china_policy_track/` — China Policy observation parser (`parse_koyfin_barchart_export`)
- `whinfell_pipeline/global_track/` — Global Parquet write (ingest only; Comet can stop at JSON envelope)

For Comet CSV work, the critical integration surface is **`staged_csv.py` + `registry.py` + channel adapters**.

---

## Install / test in Cousins repo

Copy `whinfell_pipeline/` tree into repo root (merge with existing). From repo root:

```bash
python3 -m whinfell_pipeline.ingest --input whinfell_pipeline/examples/comet_koyfin_global.json
python3 -m unittest whinfell_pipeline.tests.test_staged_2_2c
```