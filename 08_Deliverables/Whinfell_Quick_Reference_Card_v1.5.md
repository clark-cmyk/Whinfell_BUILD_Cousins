# Whinfell Quick Reference Card v1.5

**Date:** June 30, 2026 · **Badge:** `2.2-UI-2026-06-30` · **Mission surfaces:** 5/5  
**Print companion:** `Whinfell_Quick_Reference_Card_v1.4.docx` (layout) · **This file:** content authority v1.5

---

## Morning chain (48h — preferred)

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
python3 Whinfell_Daily_Launcher.py
```

**CLI equivalent:**

```bash
bash scripts/normalize_whinfell_drop.sh ~/Downloads/whinfell_drop
python3 run_csv_download.py daily --window 48h --overwrite \
  --hydrate-output data/hydration/latest.json
```

**Then in Transmission Control:** Import `data/hydration/latest.json` → confirm **`lineage_hash`** → Accept tracer → Save State.

---

## Open at desk

| Item | Command |
|------|---------|
| Transmission Control | `open 08_Deliverables/Whinfell_Transmission_Control.html` |
| Operator Guide v1.5 | `open 08_Deliverables/Whinfell_Expanded_Operators_Guide_v1.5.md` |
| Desk feedback log | `open 08_Deliverables/Desk_Feedback_Log.md` |
| WTM-Import-Core criteria | `open 08_Deliverables/ARCH-3_WTM_Import_Core_Criteria.md` |

---

## Five node cockpits (mission surfaces)

| Node | Focus |
|------|-------|
| **Basis** | Calendar rich/cheap · RV quartile · gate |
| **Credit** | HY spread RV · flows sponsorship · SQ3 suffix |
| **Liquidity** | 2s10s · duration flows · rates gate |
| **Breadth** | IWM/SPY participation · equity flows |
| **Highbeta** | IBIT vs QQQ beta spread · BTC bias |

**UI zones:** Header (gate + score) · KPI band · Signal drawer (**Explain**)

---

## Normalize before stage

Native vendor names → canonical via `data_dictionary.yaml` `normalize_rules`:

- `koyfin_2026-MM-DD.csv` → `rates_*`
- `koyfin_wtm-import-core*` → `credit_*` (**WTM-Import-Core**)
- `WTM-Flows*.csv` → `flows_*`
- Barchart `*_daily_historical*` → `futures_daily_*`
- Delete browser dupes: `filename (1).csv`

---

## Hydration confirm

| Field | Expect |
|-------|--------|
| `lineage_hash` | `sha256:…` — authority for session |
| `freshness_status` | `fresh` |
| `node_cockpits` | 5 nodes |
| `flows_sidecar.flows_status` | `ok` (when WTM-Flows staged) |
| `ingest_provenance` | staged route summary (ARCH-1 M3) |

```bash
python3 -m whinfell_pipeline.desk_operator_confirm
```

---

## WTM EXPORT v2.2

Each **NODE COCKPIT** block includes funds-flow lines (PR-5):

- Funds Flow Verdict / 1D / 5D / Breadth / Summary

Copy from TC or hydration `wtm_export_v22` for Perplexity handoff.

---

## Clark: WTM-Import-Core (ARCH-3)

1. Create watchlist **`WTM-Import-Core`** — 16 tickers per criteria doc  
2. Export CSV to `~/Downloads/whinfell_drop`  
3. Run morning chain → verify `route: koyfin_snapshot_csv`  
4. Sign off per `ARCH-3_WTM_Import_Core_Criteria.md`

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Quarantine filename | Run `normalize_whinfell_drop.sh` first |
| Quarantine headers | Use WTM snapshot export (`Ticker` + `Last Price`), not raw wide dump |
| Import blocked | Confirm `lineage_hash` upgrade; use force only if intentional |
| Flows unavailable | Stage `WTM-Flows*.csv` in same 48h window |

---

*v1.5 adds: mission surfaces · 48h AM chain · ARCH-3 criteria · ingest provenance · PR-5 export lines*