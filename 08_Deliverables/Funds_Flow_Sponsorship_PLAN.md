# /plan — Funds Flow Sponsorship Implementation

**Project:** Whinfell Transmission Control  
**Design authority:** `01_Strategy_Docs/Phase2_Funds_Flow_Sponsorship_Design.md`  
**Date:** June 29, 2026

---

## Phase placement

| Slice | Phase | Deliverable |
|-------|-------|-------------|
| **2b-data** | PR-1 → PR-3 | Registry + builder + Koyfin ingest |
| **2b-ui** | PR-4 → PR-5 | `FundsFlowSponsorshipCard` + export lines |

Blocked by: node cockpit hydration v1.1.0 (✅ shipped `cdd677a`).  
Parallel with: ARCH-1 component routing (independent workstream).

---

## STEP 0 — Confirm design lock

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
# Read authority
open 01_Strategy_Docs/Phase2_Funds_Flow_Sponsorship_Design.md
open 08_Deliverables/Funds_Flow_Sponsorship_GOAL.md
```

Desk confirms: flows = confirmation layer only; `% AUM` canonical.

---

## STEP 1 — Master DD registry (PR-1)

**Owner:** Bridge

1. Add `funds_flow_baskets` + `funds_flow_thresholds` to `data_dictionary.yaml`
2. Add `canonical_assets` for: `shy`, `ief`, `tlt`, `bil`, `iwm`, `rsp`, `ibit`, `bito`, `gbtc` (as needed)
3. Column map: `{TICKER} Flow (D)`, `{TICKER} AUM`, `{TICKER} Flow % AUM (D)`
4. Helpers: `funds_flow_basket_for_node()`, `funds_flow_thresholds()`
5. Tests: `test_funds_flow_baskets_locked`

**Exit:** `test_data_dictionary.py` PASS with basket count = 5 nodes

---

## STEP 2 — Pipeline builder (PR-2)

**Owner:** Bridge

1. Create `whinfell_pipeline/funds_flows.py`
   - `compute_etf_row()` — 1D/5D % AUM, persistence_score
   - `compute_aggregate()` — weighted mean, breadth, concentration
   - `assign_verdict()` — flow-only + divergence overlay vs node directional/RV
   - `build_interpretation()` — summary, caution_line, change_mind_trigger
   - `build_funds_flows(node_id, flow_inputs, node_cockpit, as_of)`
2. Wire into `node_cockpits.build_node_cockpit()` → attach `funds_flows`
3. Bump `HYDRATION_BUNDLE_VERSION` → `1.2.0` when block present
4. Apply `confidence_delta` to node `confidence` tier (clamp low/medium/high)

**Exit:** `test_funds_flows.py` PASS · hydrate bundle includes `funds_flows` on all nodes

---

## STEP 3 — Koyfin flow ingest (PR-3)

**Owner:** Integration Dynamo

1. Audit `WTM-Credit-Confirmation` export for `Flow (D)` / `AUM` columns (desk sample)
2. Extend `raw_csv_transform` or adapter to emit `data/flows/v1/latest_flows.json` sidecar
3. Optional: add `WTM-Flows` to `collection_manifest.yaml` if credit export insufficient
4. Hydrate reads sidecar → `flow_inputs` dict keyed by ticker

**Desk action:** Export one credit CSV with flow columns → drop in `whinfell_drop` → verify sidecar

**Exit:** Real `flow_pct_aum_1d` non-null for HYG in hydration bundle

---

## STEP 4 — TC UI component (PR-4)

**Owner:** Clarity + Bridge

1. Implement `FundsFlowSponsorshipCard` in Transmission Control node cockpit rail
2. Layout: header → verdict badge → aggregate line → ETF rows (max 5) → interpretation
3. CSS: tabular-nums, right-align, muted palette, 150ms fade on node flip
4. Compare mode: stack cards per compared node
5. Full-screen Why: expand interpretation + change-mind trigger

**Placement:** Right rail, below driver checklist / trigger map

**Exit:** Headless or manual verify — card visible on Credit node with fixture bundle

---

## STEP 5 — Export + docs (PR-5)

**Owner:** Blueprint

1. Add optional flow lines to `build_node_cockpit_export_block()`:
   - `Funds Flow Verdict:`
   - `Funds Flow 5D:`
   - `Funds Flow Summary:`
2. Update `Phase2_Node_Cockpit_Data_Model.md` §9 MVP checklist
3. Update `BUILD_TODO_List.md` · `Progress_Log.md`
4. Update `Whinfell_Phased_Development_Plan_v1.0.md` Phase 2b bullet

---

## STEP 6 — Verify & report

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
python3 -m pytest whinfell_pipeline/tests/test_funds_flows.py whinfell_pipeline/tests/test_node_cockpits.py -q
python3 -m whinfell_pipeline.hydrate -o /tmp/hydration_test.json
# Inspect: node_cockpits.credit.funds_flows
```

**Report template for TempLibby:**

```
Funds Flow Sponsorship — status
  registry: 5/5 node baskets locked
  pipeline: funds_flows.py wired / degrade path tested
  ingest: [credit export | WTM-Flows | fixture-only]
  UI: FundsFlowSponsorshipCard [rail | pending]
  tests: N PASS
  open: [threshold tuning | dedicated export | desk confirm]
```

---

## PR dependency graph

```
PR-1 (registry)
  ├── PR-2 (builder) ── PR-4 (UI)
  └── PR-3 (ingest)  ──┘
         └── PR-5 (export/docs)
```

---

## Comet / desk collection note

Flow columns may already exist on Koyfin saved views (WhinSig pattern: `IBIT Flow (D)`). For Whinfell MVP:

1. Confirm which WTM export includes `% AUM` or `Flow (D)` + `AUM`
2. If missing, add **WTM-Flows** saved view to Comet shortcuts (optional enrichment — not blocking PR-1/2)

Do **not** parse flows in the browser. Pipeline only.