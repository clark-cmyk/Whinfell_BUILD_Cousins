# Comet Browser Operations Blueprint

**Version:** 1.0  
**Date:** June 27, 2026  
**From:** Comet + BUILD Cousins Integration  
**For:** Desk operators · supervised Comet use · Clark oversight

---

## Purpose

Low-friction, **supervised** daily workflow: browser exports → `run_csv_download.py` → Transmission Control hydration. Comet assists collection; **Clark approves** each step. No auto-trading.

**Agent instructions (Perplexity + Comet):** `08_Deliverables/Perplexity_Comet_Collection_Instructions.md`  
**Fast collect tool:** `python3 run_batch_collect.py` · wired URLs in `whinfell_pipeline/desk_urls.yaml`

---

## One-Time Setup Checklist

| # | Task | Command / Action | Done |
|---|------|------------------|------|
| 1 | Initialize staged folders | `python3 run_csv_download.py init` or `scripts/init_daily_csv.sh` | ☐ |
| 2 | Save Koyfin backup views (see §2) | Koyfin → Save View → name exactly as listed | ☐ |
| 3 | Save Barchart backup views (see §3) | Barchart → Save Screen → name exactly as listed | ☐ |
| 4 | Set Comet memorized shortcuts (see §4) | Comet → Shortcuts → add 6 entries | ☐ |
| 5 | Bookmark Transmission Control | `open 08_Deliverables/Whinfell_Transmission_Control.html` | ☐ |
| 6 | Set default hydration path in Transmission Control URLs | Paste `data/hydration/latest.json` note in handover | ☐ |
| 7 | Run test daily chain once | `python3 run_csv_download.py daily --operator desk --window 24h` | ☐ |
| 8 | Import test bundle in Transmission Control | **Import Latest Hydration Bundle** → verify Pipeline badge | ☐ |
| 9 | Print Quick Reference v1.4 | `08_Deliverables/Whinfell_Quick_Reference_Card_v1.4.docx` | ☐ |

---

## 1. Daily Chain (5 Minutes)

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
python3 run_csv_download.py daily \
  --operator desk \
  --window today \
  --hydrate-output data/hydration/latest.json
```

**Then in Transmission Control:**

1. Click **Import Latest Hydration Bundle**
2. Select `data/hydration/latest.json`
3. Confirm status chip: `Imported … · Fresh/Aging · snap_…`
4. Review command bar **Pipeline** badge + freshness dot
5. **Accept** or **Dismiss** Suggested Tracer (matrix never auto-fills)
6. **Save State**

**Shortcut:** `scripts/morning_daily.sh`

---

## 2. Koyfin Backup Views (save once)

Create and **Save View** with these exact names. Export CSV after morning read.

| View Name | Panels / Series | CSV filename (Comet export) |
|-----------|-----------------|----------------------------|
| **WTM-Rates-Credit** | HY OAS, IG OAS, 2s10s (`T10Y2Y`), 10Y (`DGS10`) | `rates_YYYYMMDD_HHMM.csv` |
| **WTM-Equities-Breadth** | `IWM` vs `SPY`, `XLI`, `XLF` vs `XLU` | `equities_YYYYMMDD_HHMM.csv` |
| **WTM-Credit-Confirmation** | `HYG`, `LQD`, HYG/LQD ratio trend | `credit_YYYYMMDD_HHMM.csv` |
| **WTM-China-Policy** | Policy strength, state/growth impulse fields | `china_policy_YYYYMMDD_HHMM.csv` |

**Export path:** Koyfin → Export CSV → lands in `~/Downloads` → `run_csv_download.py stage` copies to `staged_raw/source=koyfin/dataset={rates|credit|equities}/`.

**Fallback:** If OAS panels unavailable, use `HYG`/`LQD` ETF returns per `07_Reference_Materials/Whinfell_Series_Ticker_Master_List.md`.

---

## 3. Barchart Backup Views (save once)

| View Name | Symbols | CSV filename |
|-----------|---------|--------------|
| **WTM-Futures-Intraday** | `BTC1!`, `ES1!`, `CL1!`, `IBIT` | `futures_intraday_YYYYMMDD_HHMM.csv` |
| **WTM-Futures-Daily** | Front-month `BTC`, `ES`, `CL` daily | `futures_daily_YYYYMMDD_HHMM.csv` |
| **WTM-BTC-Basis** | Near/far month, basis spread, ref low/mid/high | `btc_basis_YYYYMMDD.csv` (product_flavor pattern) |
| **WTM-Options-Greeks** | BTC options chain summary (desk L2) | `options_YYYYMMDD_HHMM.csv` |

**Export path:** Barchart → Download CSV → `~/Downloads` → staged to `staged_raw/source=barchart/dataset={futures_intraday|futures_daily|options|greeks}/`.

---

## 4. Comet Memorized Shortcuts

Add in Comet → **Shortcuts** (voice or typed trigger → action):

| Shortcut Name | Trigger Phrase | Action |
|---------------|----------------|--------|
| **Open Transmission Control** | `wtm control` | Open `Whinfell_Transmission_Control.html` |
| **Open Koyfin Rates** | `wtm koyfin rates` | Open saved view **WTM-Rates-Credit** |
| **Open Barchart Futures** | `wtm barchart futures` | Open saved view **WTM-Futures-Intraday** |
| **Run Daily CSV Chain** | `wtm daily csv` | Terminal: `cd ~/Desktop/Whinfell_BUILD_Cousins && python3 run_csv_download.py daily --operator desk --window today` |
| **Import Hydration** | `wtm hydrate import` | Remind: click **Import Latest Hydration Bundle** → `data/hydration/latest.json` |
| **Morning Checklist** | `wtm morning` | Paste Saved Prompts Utility Block (§6) |

---

## 5. Supervised Comet Control Prompt (for Clark)

Paste into Comet at shift start. **Supervised mode — confirm each step before proceeding.**

```
You are the Whinfell desk collection assistant (supervised mode).

RULES:
- Do NOT execute trades or change risk limits.
- Do NOT skip validation. Quarantined files must be reported.
- Ask Clark to confirm before running terminal commands.
- After each CSV export, state: source, dataset, filename, row count.

MORNING SEQUENCE:
1. Open Koyfin backup views: WTM-Rates-Credit, WTM-Equities-Breadth, WTM-Credit-Confirmation, WTM-China-Policy.
2. Export each as CSV to Downloads using naming: {dataset}_{YYYYMMDD}_{HHMM}.csv
3. Open Barchart backup views: WTM-Futures-Intraday, WTM-BTC-Basis.
4. Export each as CSV to Downloads.
5. Ask Clark: "Ready to run daily chain?" — on approval, run:
   cd ~/Desktop/Whinfell_BUILD_Cousins && python3 run_csv_download.py daily --operator desk --window today --hydrate-output data/hydration/latest.json
6. Report: files_staged, files_quarantined, collect_exit, hydrate_output path.
7. Remind Clark: Transmission Control → Import Latest Hydration Bundle → Accept/Dismiss tracer → Save State.

If any file is quarantined, show errors from staged_raw/quarantine/ and staged_raw/manifests/stage_manifest__*.json.
```

---

## 6. Saved Prompts Utility Block

Copy into Comet or Perplexity as needed.

```
--- WTM SAVED PROMPTS UTILITY BLOCK ---
Desk: Whinfell Transmission Control · Phase 2.2
Authority: Pipeline hydration + hybrid tracer (confirm_required)

PROMPT A — Transmission Read:
"Classify current regime from Whinfell Score, transmission state, and key observation. End with WTM EXPORT v2.1 block."

PROMPT B — Gross Risk:
"Given Whinfell Score {score} and gate {gate}, recommend total gross % and posture ladder step."

PROMPT C — Trade Ranking:
"Rank candidate trades by alignment with transmission map and gate band."

PROMPT D — Income Projection:
"Project session/week P&L outlook from current book and regime."

PROMPT E — Divergence:
"Where does live tape diverge from WTM read? Flag compression risks."

HYDRATION REMINDER:
After run_csv_download.py daily → Import Latest Hydration Bundle (data/hydration/latest.json) → Accept tracer suggestions only if confirmed.
--- END UTILITY BLOCK ---
```

---

## 7. Manifest & Quarantine Reference

| Artifact | Path |
|----------|------|
| Stage manifest | `staged_raw/manifests/stage_manifest__*.json` |
| Daily manifest | `staged_raw/manifests/daily_manifest__*.json` |
| Quarantine | `staged_raw/quarantine/YYYYMMDD/` |
| Sidecar meta | `{staged_file}.csv.meta.json` |
| Hydration bundle | `data/hydration/latest.json` |

---

## 8. Escalation

| Issue | Action |
|-------|--------|
| Quarantined CSV | Check filename pattern + headers in `staged_raw/README.md` |
| `collect_exit=1` | Re-stage exports; check `daily_manifest__*.json` |
| Stale freshness | Re-run daily chain; re-import bundle |
| Comet shortcut fails | Use manual commands from Quick Reference v1.4 |

**Owner:** TempLibby · **Build:** BUILD Cousins (Bridge)