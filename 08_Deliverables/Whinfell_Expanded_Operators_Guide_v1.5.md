# Whinfell Expanded Operator's Guide v1.5

**Version:** 1.5  
**Date:** June 30, 2026  
**Authority:** TempLibby, Template Team · BUILD Cousins  
**Status:** Production — Mission Surfaces + ARCH-1 Routing  
**Primary file:** `Whinfell_Transmission_Control.html` (build badge `2.2-UI-2026-06-30`)  
**Quick ref:** `Whinfell_Quick_Reference_Card_v1.4.docx`  
**Runbook entry:** `run_csv_download.py`  
**Desk validation log:** `08_Deliverables/Desk_Feedback_Log.md`

---

## 1. System Architecture

| Layer | Tool | Role |
|-------|------|------|
| **Research & Analysis** | Perplexity (Prompts A–E) | Regime read, sizing, trade eval, income, divergence |
| **Execution & State** | Transmission Control (HTML) | Intake, gates, gross risk, tracer, node cockpits |
| **Live Data** | Koyfin + Barchart (browser tabs) | Transmission map, futures/basis, RV history |
| **CSV Collector** | Comet + `run_csv_download.py` | Normalize → stage → Parquet → hydration |
| **Ingest Router (ARCH-1)** | `whinfell_pipeline/source_router.py` | Dictionary-driven file classification |

**No iframes.** Control surface opens live data in dedicated tabs.

---

## 2. Open Commands

```bash
# Primary execution layer (Phase 2.2 UI + mission surfaces)
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html

# Quick Reference Card (print at desk)
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Quick_Reference_Card_v1.4.docx

# Desk feedback log (mission-surface validation)
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Desk_Feedback_Log.md
```

---

## 3. Daily CSV Chain (Primary Path — 48h)

**One command (recommended):**

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
bash scripts/normalize_whinfell_drop.sh ~/Downloads/whinfell_drop
python3 run_csv_download.py daily \
  --operator cwt \
  --window 48h \
  --downloads ~/Downloads/whinfell_drop \
  --staged-root ./staged_raw \
  --hydrate-output data/hydration/latest.json \
  --overwrite
```

Then in Transmission Control: **Import** `data/hydration/latest.json` → confirm import using **`lineage_hash`** (not file timestamp) → review **Suggested Tracer** → **Accept** or **Dismiss** → **Save State**.

**Morning shortcut:** `./whinfell_daily_am.sh` or `python3 Whinfell_Daily_Launcher.py` (normalize + 48h + overwrite)

### Pre-stage rename (required for native Barchart/Koyfin names)

`scripts/normalize_whinfell_drop.sh` reads rules from `whinfell_pipeline/data_dictionary.yaml` → `file_naming_conventions.normalize_rules`.

**WTM desk exports (auto-renamed):** `WTM-Flows*.csv`, `WTM-Global-Rates.csv`, `WTM-Equities-Breath.csv`, `WTM-Credit-Confirmation*.csv`, `WTM-China-Policy.csv`, etc.

**Barchart native exports (v1.5 — auto-renamed):**

| Vendor pattern | Canonical filename |
|----------------|-------------------|
| `*_daily_historical-data-*` | `futures_daily_{YYYYMMDD}_{HHMM}.csv` |
| `*_daily-nearby_historical-data-*` | `futures_daily_{YYYYMMDD}_{HHMM}.csv` |
| `futures-spreads-*` | `btc_basis_{YYYYMMDD}.csv` |
| `*-volatility-greeks-*` | `greeks_{YYYYMMDD}_{HHMM}.csv` |
| `*-options-*` | `options_{YYYYMMDD}_{HHMM}.csv` |

Run normalize **before** stage. Files that still quarantine after rename usually fail header/transform validation — check `.meta.json` in `staged_raw/quarantine/`.

### Staged folder contract (`staged_raw/`)

| Folder | Datasets |
|--------|----------|
| `source=koyfin/dataset=rates/` | + `credit`, `equities`, `flows` |
| `source=barchart/dataset=futures_intraday/` | + `futures_daily`, `options`, `greeks` |
| `source=china_policy/` | CSV at source root |

**Filename patterns (required after normalize):**

- `{dataset}_{YYYYMMDD}_{HHMM}.csv`
- `{product}_{flavor}_{YYYYMMDD}.csv` — e.g. `btc_basis_20260630.csv`

### Sidecars, quarantine, manifests

| Artifact | Location | Purpose |
|----------|----------|---------|
| `.meta.json` | Next to each staged CSV | sha256, source/dataset, **`route`** block (ARCH-1) |
| `quarantine/` | `staged_raw/quarantine/YYYYMMDD/` | Filename or header/transform failures |
| `stage_manifest__*.json` | `staged_raw/manifests/` | Stage run audit trail |
| `daily_manifest__*.json` | `staged_raw/manifests/` | Full daily chain result |

---

## 4. Transmission Control — Mission Surfaces (5/5)

All five node cockpits ship the **mission-surface** operator console pattern:

| Node | Tactical eyebrow | Primary RV series |
|------|------------------|-------------------|
| Basis | Basis mission read | Basis vs ref band |
| Credit | Credit mission read | HY OAS proxy |
| Liquidity | Liquidity mission read | US 2s10s spread |
| Breadth | Breadth mission read | IWM / SPY participation |
| Highbeta | High-beta mission read | IBIT vs QQQ beta spread |

**Each node shows:**

1. **Tactical banner** — RV richness + expression eligibility + gate cap (0.5× when Tight)
2. **SQ3 suffix** — separate line when China impaired (not embedded in lead sentence)
3. **Implication chip row** — band/composite fallback · RV posture · flows · gate
4. **Full diagnostics** — expandable disclosure (signal · directional · RV · flows · gate)

**Focus mode:** RV chart + horizon evidence table. Credit may show **spot-fallback** table when a single bps reading applies across lookbacks.

**Phase 2.2 UI (`2.2-UI-2026-06-30`):**

- Three-zone top bar (identity · status · actions)
- Primary KPI band with signal detail **drawer** (replaces per-card WHY links)
- Panel zone labels: Ladders · Data quality · Workflow · Mission read · Implications
- Metadata demoted to drawer tech block

Desk validation checklist: `08_Deliverables/Desk_Feedback_Log.md`

---

## 5. ARCH-1 Ingest Routing

**Module:** `whinfell_pipeline/source_router.py`  
**Entry point:** `route_ingest(path)` → `RouteResult`

Classifies CSVs using `data_dictionary.yaml` → `source_systems` detect rules. Delegates to existing parsers (`raw_csv_transform`, `crypto_sleeve`). Stage writes `route` metadata into `.meta.json` sidecars.

**RV quartile history:** `whinfell_pipeline/rv_history.py` merges:

1. Koyfin wide exports (SOFR, HYG/LQD, correlations) — live when staged
2. Barchart spread/curve JSON sidecars
3. Dated series fixture fallback

---

## 6. Daily Workflow

| Step | Action |
|------|--------|
| 1 | Export CSVs from Koyfin / Barchart / China into **Downloads/whinfell_drop** |
| 2 | `bash scripts/normalize_whinfell_drop.sh ~/Downloads/whinfell_drop` |
| 3 | `python3 run_csv_download.py daily --window 48h --overwrite` |
| 4 | **Import** `data/hydration/latest.json` — confirm **`lineage_hash`** |
| 5 | Walk each node cockpit — mission banner + Focus mode |
| 6 | **Accept** or **Dismiss** Suggested Tracer · **Save State** |

---

## 7. Gate Rules

| Score | Gate | BTC Access | Banner |
|-------|------|------------|--------|
| &lt; 50 | NO NEW BTC RISK | Blocked | Red |
| 50–64 | Tight Risk Band | Reduced sizing (0.5×) | Amber |
| ≥ 65 | Allowed | Full access | Green |

**Posture ladder:** Full (80+) · Selective (65–79) · Light (50–64) · Defensive (&lt;50) · Flat

---

## 8. Hybrid Signal Tracer (2.2b)

- Import surfaces **Suggestions Pending** — matrix never auto-fills until **Accept**
- **Dismiss** clears suggestions only
- Manual edits set command bar **Override**

---

## 9. WTM EXPORT v2.2

Hydration bundles ship `node_cockpits`, `cockpit_context`, and embedded WTM EXPORT v2.2 blocks.  
Perplexity **v2.1** import remains valid for research-only handoff.

---

## 10. Troubleshooting

| Symptom | Check |
|---------|-------|
| File quarantined after normalize | `.meta.json` errors · run `route_ingest` classification · header shape |
| Native Barchart still skipped | Re-run `normalize_whinfell_drop.sh` — v1.5 rules cover daily/options/greeks/spreads |
| Flows unavailable on nodes | Confirm `flows_{YYYYMMDD}_{HHMM}.csv` staged · `flows_status: ok` in bundle |
| Mission banner hidden | Node needs `rv_basis` hydration · re-import bundle |
| Composite fallback chip | Expected when `composite_score_source: horizon_net_fallback` |
| Stale freshness | Re-run 48h chain · confirm `lineage_hash` changed |

---

## 11. Support

| Role | Contact |
|------|---------|
| System owner | TempLibby |
| Build support | BUILD Cousins (Bridge) |
| CSV collector | Comet runbook · `run_csv_download.py` |

**Ship:** Phase 2.2 mission surfaces (5/5) · UI refactor · ARCH-1 router · Barchart normalize expansion · June 30, 2026