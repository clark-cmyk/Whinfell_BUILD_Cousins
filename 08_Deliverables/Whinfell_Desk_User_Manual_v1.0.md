# Whinfell Desk User Manual

**Version:** 1.0  
**Date:** June 30, 2026  
**Status:** Production  
**Build badge:** `2.2-HYDRATION-AUDIT-2026-06-30`  
**Authority:** Clark · BUILD Cousins · TempLibby (system owner)

---

## How to use this manual

This is the **single shareable desk manual** for operators, advisors, and browser agents. Each audience has a fast path below — you do not need to read the whole document.

| Audience | Role | Start here |
|----------|------|------------|
| **Wes** | Reviewer / stakeholder — no local setup | [§2 Desk preview (share link)](#2-desk-preview-share-link) |
| **Comet** | Supervised browser CSV collection | [§4 Comet collection runbook](#4-comet-collection-runbook) |
| **Perplexity** | Morning export + batch orchestration | [§5 Perplexity daily prompt](#5-perplexity-daily-prompt) |
| **G-Quant** | CS + quant advisor — lineage, fields, gates, **SQ3 math** | [§7 Data & quant reference](#7-data--quant-reference) · [SQ3 Reference](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_SQ3_Reference_v1.0.md) |
| **TempLibby** | Browser Grok operator assistant | [§8 Grok operator prompt](#8-grok-operator-prompt) |
| **Clark** | Desk owner — full daily chain + publish | [§3 Clark daily workflow](#3-clark-daily-workflow) |

### Live desk (no install)

| Resource | Link |
|----------|------|
| **Transmission Control (auto-hydrated)** | [clark-cmyk.github.io/Whinfell_BUILD_Cousins](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) |
| Latest hydration bundle (JSON) | [latest.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/latest.json) |
| Field-by-field audit log (JSON) | [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) |
| GitHub repo | [github.com/clark-cmyk/Whinfell_BUILD_Cousins](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins) |

### Document index (deep dives)

| Document | View on GitHub | Raw (for agents) |
|----------|----------------|------------------|
| **This manual** | [Whinfell_Desk_User_Manual_v1.0.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Desk_User_Manual_v1.0.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Desk_User_Manual_v1.0.md) |
| Expanded operator guide v1.5 | [Whinfell_Expanded_Operators_Guide_v1.5.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Expanded_Operators_Guide_v1.5.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Expanded_Operators_Guide_v1.5.md) |
| Comet browser blueprint | [Comet_Browser_Operations_Blueprint.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Comet_Browser_Operations_Blueprint.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Comet_Browser_Operations_Blueprint.md) |
| Perplexity + Comet collection | [Perplexity_Comet_Collection_Instructions.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Perplexity_Comet_Collection_Instructions.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Perplexity_Comet_Collection_Instructions.md) |
| Perplexity full collect prompt | [Perplexity_Full_Collection_Prompt.txt](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Perplexity_Full_Collection_Prompt.txt) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Perplexity_Full_Collection_Prompt.txt) |
| Clark simple data update | [Whinfell_Data_Update_Simple_Guide.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Data_Update_Simple_Guide.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Data_Update_Simple_Guide.md) |
| Desk validation log | [Desk_Feedback_Log.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Desk_Feedback_Log.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Desk_Feedback_Log.md) |
| UI audit spec | [whinfell_ui_audit_chunked.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/whinfell_ui_audit_chunked.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/whinfell_ui_audit_chunked.md) |
| Grok operator prompt | [Whinfell_Grok_Operator_Prompt.txt](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Grok_Operator_Prompt.txt) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Grok_Operator_Prompt.txt) |
| Quick reference card v1.5 | [Whinfell_Quick_Reference_Card_v1.5.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Quick_Reference_Card_v1.5.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Quick_Reference_Card_v1.5.md) |
| Comet shortcuts | [Comet_Shortcuts_WTM.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Comet_Shortcuts_WTM.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Comet_Shortcuts_WTM.md) |
| Credit score logic (C1) | [Whinfell_Credit_Confirmation_Score_Logic.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/04_Score_Calculation/Whinfell_Credit_Confirmation_Score_Logic.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/04_Score_Calculation/Whinfell_Credit_Confirmation_Score_Logic.md) |
| Interim node score weights | [Phase2_Interim_Node_Score_Weights.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/04_Score_Calculation/Phase2_Interim_Node_Score_Weights.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/04_Score_Calculation/Phase2_Interim_Node_Score_Weights.md) |
| Master data dictionary | [data_dictionary.yaml](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/data_dictionary.yaml) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/whinfell_pipeline/data_dictionary.yaml) |
| WTM EXPORT v2.1 spec | [WTM_EXPORT_v2.1_SPEC.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.1_SPEC.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/whinfell_pipeline/WTM_EXPORT_v2.1_SPEC.md) |
| WTM EXPORT v2.2 spec | [WTM_EXPORT_v2.2_SPEC.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.2_SPEC.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/whinfell_pipeline/WTM_EXPORT_v2.2_SPEC.md) |
| Transmission Control (source) | [Whinfell_Transmission_Control.html](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Transmission_Control.html) | — (use Pages desk URL above) |
| **SQ3 reference (full)** | [Whinfell_SQ3_Reference_v1.0.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_SQ3_Reference_v1.0.md) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_SQ3_Reference_v1.0.md) |
| SQ3 engine (Python) | [china_policy_track/sq3.py](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/sq3.py) | [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/china_policy_track/sq3.py) |

**Clark Mac local paths** (not web links): project root `~/Desktop/Whinfell_BUILD_Cousins/`, CSV drop `~/Downloads/whinfell_drop/`.

---

## 1. What Transmission Control is

**Transmission Control (TC)** is the Whinfell operator console — a single HTML desk for regime read, gate enforcement, node mission surfaces, relative-value quartiles, funds-flow sponsorship, and WTM export handoff.

| Layer | Tool | Role |
|-------|------|------|
| Research | Perplexity (Prompts A–E) | Regime narrative, sizing, trade eval |
| Execution & state | Transmission Control | Intake, gates, tracer, 5 node cockpits |
| Live charts | Koyfin + Barchart (browser tabs) | Rates, credit, breadth, futures, basis |
| Data pipeline | [`run_csv_download.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/run_csv_download.py) | Normalize → stage → Parquet → hydrate |
| Field audit | [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) | Field-by-field populate trace |

**No auto-trading.** Agents collect and explain; Clark approves risk and sizing.

### Five transmission nodes

| Node | Mission read focus | Primary RV series |
|------|-------------------|-------------------|
| Liquidity | Rates & funding | US 2s10s spread |
| Credit | HY confirmation | HY OAS proxy |
| Breadth | Participation | IWM / SPY |
| Highbeta | BTC beta transmission | IBIT vs QQQ |
| Basis | Calendar / term structure | Basis vs ref band |

### Gate rules (non-negotiable)

| Whinfell Score | Gate | BTC calendar arb | Size posture |
|----------------|------|------------------|--------------|
| &lt; 50 | NO NEW BTC RISK | **Blocked** | Defensive / flat |
| 50–64 | Tight Risk Band | Reduced (0.5×) | Light gross |
| ≥ 65 | Allowed | Full access subject to health | Selective → full |

**China SQ3 &lt; 50** flags dual-track impairment — gate chip shows **China Caution** on all nodes.

### SQ3 at a glance

**SQ3** = China Policy Transmission Score (0–100), separate from Global Whinfell Score.

```
SQ3 = Policy STR. (35%) + State IMP. (35%) + Growth IMP. (30%)
```

| Input | Range | Notes |
|-------|-------|-------|
| Policy Strength | 0–100 | Force of policy hierarchy |
| State Impulse | −100 … +100 | **+ = more state control** (inverted in formula) |
| Growth Impulse | 0–100 | Growth / market liquidity impulse |

| SQ3 | Band | Gate impact |
|-----|------|-------------|
| &lt; 50 | Impaired | **China Caution** on all mission nodes |
| 50–64 | Mixed / Fragile | Monitor; client-sized BTC/basis |
| ≥ 65 | Constructive+ | Dual-track alignment possible |

**Full math, worked examples, China ladder handicap, and unique edge:** [Whinfell_SQ3_Reference_v1.0.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_SQ3_Reference_v1.0.md)

---

## 2. Desk preview (share link)

**For Wes, Lovable, and any reviewer who should not touch Clark's machine.**

### Access (private — GitHub login required)

The desk repo is **private**. Reviewers need:

1. A **GitHub account**
2. **Read** collaborator access (Clark invites you)
3. **GitHub Pro** on Clark's account (enables private Pages)

**Setup guide (Clark):** [Desk_Preview_Private_Access_Setup.md](Desk_Preview_Private_Access_Setup.md)

### URL (auto-hydrated — no import step)

Use the URL shown in the repo **Settings → Pages** after Clark enables private Pages (may match `https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/` once re-deployed).

Sign in to GitHub first, then open the link. Transmission Control auto-loads the co-hosted hydration bundle — no file picker, no git, no terminal.

### What reviewers should see

1. Command bar: Whinfell Score, transmission state, SQ3, gate, freshness
2. Five node cockpits with mission tactical banners
3. Focus mode: RV chart + horizon evidence table
4. Header **Explain** drawer → **Hydration field log** (field-by-field audit)
5. Build badge: `2.2-HYDRATION-AUDIT-2026-06-30`

### What to tell stakeholders

> Clark will invite you to the private GitHub repo. Accept the invite, sign in to GitHub, then open the desk link from Clark. Transmission Control loads with today's hydration bundle. Click **Explain** in the header for the field-by-field hydration log. No local setup required.

### When Clark updates the preview

After the morning chain:

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
bash scripts/publish_desk_preview.sh
```

GitHub Actions redeploys in ~1–2 minutes. Same URL, new data.

**Note:** [latest.json on Pages](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/latest.json) is **public**. Do not publish if bundle contents must stay private.

---

## 3. Clark daily workflow

### Morning (recommended — one script)

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
./whinfell_daily_am.sh
```

This runs:

1. `normalize_whinfell_drop.sh` on `~/Downloads/whinfell_drop`
2. `run_csv_download.py daily` (48h window, overwrite)
3. Writes [latest.json](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/latest.json) + [hydration_log.json](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/hydration_log.json) (local; published to Pages after `publish_desk_preview.sh`)
4. Opens Transmission Control locally

**Or one-click:** double-click `Whinfell_Daily_AM.command` on Desktop.  
**Script:** [whinfell_daily_am.sh](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_daily_am.sh)

### After hydrate — three checks in TC

| # | Action | Pass criteria |
|---|--------|---------------|
| 1 | Confirm import status chip | `Imported … · Fresh` (local file) or auto-hydrate on Pages |
| 2 | Open **Explain** → Hydration field log | `33/33 required OK` · quality ≥ 45 · session `ok` |
| 3 | Walk nodes in Focus mode | Mission banner + RV chart populated |

### Tracer (hybrid 2.2b)

- Import surfaces **Suggestions Pending** — horizon matrix **never auto-fills**
- **Accept** writes marks · **Dismiss** clears suggestions only
- Manual edits flip command bar to **Override** until re-import

### End of session

1. Update handover / watch items  
2. **Save State**  
3. Optional: [`publish_desk_preview.sh`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/scripts/publish_desk_preview.sh) for team preview URL

### Manual chain (if debugging)

```bash
bash scripts/normalize_whinfell_drop.sh ~/Downloads/whinfell_drop
python3 run_csv_download.py daily \
  --operator cwt \
  --window 48h \
  --downloads ~/Downloads/whinfell_drop \
  --staged-root ./staged_raw \
  --hydrate-output data/hydration/latest.json \
  --overwrite
python3 -m whinfell_pipeline.hydrate -o data/hydration/latest.json
```

---

## 4. Comet collection runbook

**Supervised mode only.** Comet exports CSVs; Clark runs the pipeline and approves risk.

### Rules

| DO | DON'T |
|----|-------|
| Export **8 saved screens** to `~/Downloads/whinfell_drop` | Loop tickers one-by-one |
| Use exact saved view names below | Rename files by hand |
| Report filename + row count after each export | Parse CSV contents or guess scores |
| Ask Clark before terminal commands | Execute trades or change risk limits |

### The 8 daily exports

**Koyfin (4)**

| Saved view | Canonical filename |
|------------|-------------------|
| WTM-Rates-Credit | `rates_YYYYMMDD_HHMM.csv` |
| WTM-Equities-Breadth | `equities_YYYYMMDD_HHMM.csv` |
| WTM-Credit-Confirmation | `credit_YYYYMMDD_HHMM.csv` |
| WTM-China-Policy | `china_policy_YYYYMMDD_HHMM.csv` |

**Barchart (3 required + 1 optional)**

| Saved screen | Canonical filename |
|--------------|-------------------|
| WTM-Futures-Intraday | `futures_intraday_YYYYMMDD_HHMM.csv` |
| WTM-Futures-Daily | `futures_daily_YYYYMMDD_HHMM.csv` |
| WTM-BTC-Basis | `btc_basis_YYYYMMDD.csv` |
| WTM-Flows-Global (optional) | `flows_YYYYMMDD_HHMM.csv` |

**Export path:** always `~/Downloads/whinfell_drop` — not Downloads root.

### Comet supervised prompt (paste at shift start)

```
You are the Whinfell desk collection assistant (supervised mode).

RULES:
- Do NOT execute trades or change risk limits.
- Do NOT skip validation. Report quarantined files.
- Ask Clark to confirm before running terminal commands.
- After each CSV export, state: source, dataset, filename, row count.

MORNING SEQUENCE:
1. Open Koyfin: WTM-Rates-Credit, WTM-Equities-Breadth, WTM-Credit-Confirmation, WTM-China-Policy.
2. Export each CSV to ~/Downloads/whinfell_drop
3. Open Barchart: WTM-Futures-Intraday, WTM-Futures-Daily, WTM-BTC-Basis.
4. Export each CSV to whinfell_drop.
5. Tell Clark: "Exports complete — ready for Whinfell Daily AM."

Clark runs ./whinfell_daily_am.sh. You do NOT import into Transmission Control unless asked.
```

### Comet shortcuts (optional)

| Trigger | Action |
|---------|--------|
| `wtm control` | Open Transmission Control HTML |
| `wtm morning` | Run morning sequence above |
| `wtm daily csv` | Remind Clark to run `whinfell_daily_am.sh` |

Full blueprint: [Comet_Browser_Operations_Blueprint.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Comet_Browser_Operations_Blueprint.md) · shortcuts: [Comet_Shortcuts_WTM.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Comet_Shortcuts_WTM.md)

---

## 5. Perplexity daily prompt

Paste each morning:

```
Whinfell morning collect — supervised, no improvisation.

1. Export these 8 Koyfin/Barchart saved views as CSV to ~/Downloads/whinfell_drop:
   - WTM-Rates-Credit, WTM-Equities-Breadth, WTM-Credit-Confirmation, WTM-China-Policy
   - WTM-Futures-Intraday, WTM-Futures-Daily, WTM-BTC-Basis
   - (optional) WTM-Flows-Global

2. Do NOT rename files. Do NOT parse CSV contents. Do NOT guess Whinfell scores.

3. Report back:
   - Each filename + approximate row count
   - Any export that failed or landed outside whinfell_drop

4. Tell Clark: "Ready for Whinfell Daily AM" — Clark runs the Mac pipeline.

You do NOT import into Transmission Control. You do NOT trade.
```

**After Clark runs AM:** confirm [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) shows `tc_session_level: ok`.

Deep collection spec: [Perplexity_Comet_Collection_Instructions.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Perplexity_Comet_Collection_Instructions.md) · full prompt: [Perplexity_Full_Collection_Prompt.txt](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Perplexity_Full_Collection_Prompt.txt)

---

## 6. Transmission Control — operator tour

### Open locally

```bash
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html
```

Or use the [Pages desk URL](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) (§2) for zero-setup review.

### Layout (Phase 2.2)

| Zone | What it shows |
|------|---------------|
| **Header** | Regime summary · import status · theme toggle · **Explain** drawer |
| **Command bar** | Whinfell Score · transmission health · SQ3 · gate · freshness |
| **Left rail** | Global + China intake · provenance · operator guide |
| **Center** | Flipchart / Focus / Compare · mission read · RV chart |
| **Right rail** | BTC L2/L3 modules · operator precision · Grok export |

### Keyboard / flipchart

| Key | Action |
|-----|--------|
| `←` `→` | Previous / next node |
| `1`–`5` | Jump to node |
| `f` | Toggle Focus mode |
| `c` | Toggle Compare mode |
| `?` | Shift+click node tab for flipchart help |

### Coverage checklist (data quality rail)

| Pill | Meaning |
|------|---------|
| History ✓ | RV quartiles loaded from hydration |
| Flows ✓/◐/✕ | Funds-flow sponsorship status |
| Signals ✓/◐/✕ | Derived component_inputs readiness |
| Per-node pills | Combined flows + signals for that node |

Click any pill → **Data dictionary audit** with remediation codes (`DD-MISS`, `DD-DERIV`, etc.).

### Hydration field log (production audit)

**Explain** drawer → **Hydration field log**

Every field maps: `bundle path → TC UI target → status → value → notes`

| Status | Meaning |
|--------|---------|
| `ok` | Populated — production ready |
| `partial` | Fallback path (e.g. credit horizon-net, horizon_fallback components) |
| `empty` | Required field missing — investigate pipeline |
| `optional_empty` | Optional field blank (e.g. `gate_status` — TC derives gate) |

Standalone file: [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) (GitHub: [blob](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/hydration_log.json) · [raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/data/hydration/hydration_log.json))

---

## 7. Data & quant reference

**For G-Quant (CS + quant advisor).**  
**SQ3 deep dive:** [Whinfell_SQ3_Reference_v1.0.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_SQ3_Reference_v1.0.md) (calculation, bands, dual-track gate, unique edge).

### Hydration bundle schema (v1.2.0)

| Block | Contents |
|-------|----------|
| `global` | Whinfell score, transmission, regime, key observation, L3 refs |
| `china` | Policy strength, state/growth impulse, SQ3, regime tag |
| `execution` | BTC bias, calendar spread legs, ref low/mid/high |
| `node_cockpits` | Per-node composite, rv_basis, funds_flows, directional, relative_value |
| `suggested_tracer` | Heuristic horizon marks — **confirm_required** (never auto-applied) |
| `flows_sidecar` | WTM-Flows ingest metadata + basket health |
| `ingest_provenance` | Staged file routes (ARCH-1) |
| `hydration_audit` | Field-by-field populate log + remediation |
| `wtm_export_v22` | Locked handoff block for downstream agents |

### Lineage & provenance

| Field | Use |
|-------|-----|
| `snapshot_id` | Bundle identity (e.g. `global-2026-06-30-raw2wtm-01`) |
| `lineage_hash` | sha256 over core payload — **confirm re-import by hash, not file mtime** |
| `as_of` | Data timestamp for freshness chip |
| `freshness_status` | `fresh` (&lt;4h) · `aging` (4–24h) · `stale` (&gt;24h) |

### RV basis structure

```
node_cockpits.{node}.rv_basis
  ├── active_series_id    # e.g. hy_oas_proxy
  ├── active_horizon      # default 3m
  ├── richness_label      # cheap | fair | rich | extreme
  └── series.{id}.horizons.{1m|3m|6m|12m|3y}
        ├── current_value
        ├── percentile, quartile
        └── n_observations
```

History sources: Koyfin wide exports → [`rv_history.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/rv_history.py) → Barchart curve/spread JSON → dated series fixture.

### Credit node — intentional design

Credit **does not** use weighted `component_inputs` (authoritative doc: [Whinfell_Credit_Confirmation_Score_Logic.md](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/04_Score_Calculation/Whinfell_Credit_Confirmation_Score_Logic.md)). It uses:

- `rv_basis` on HY OAS proxy (quartile-rich mission read)
- `composite_score_source: horizon_net_fallback` from tracer horizon net
- Audit status: `partial` — **not** a pipeline failure

### Composite score sources

| `composite_score_source` | Meaning |
|--------------------------|---------|
| `weighted_components` | C1-weighted live RV components (liquidity, breadth, highbeta, basis) |
| `horizon_net_fallback` | Tracer net when components insufficient (credit always; others when &lt;2 live) |

### Funds flow sponsorship

- Normalized: `flow_pct_aum` per ETF basket per node
- `flows_status`: `ok` · `partial` · `fallback_1d` · `unavailable`
- Global flows file: `WTM-Flows-Global.csv` → `flows_sidecar.as_of` — refresh when stale

### Known partial states (June 30 production)

| Item | Status | Action |
|------|--------|--------|
| Liquidity 10Y / DXY components | `horizon_fallback` | Map RV history keys when series available |
| Flows as-of | May lag 1 day | Re-export `WTM-Flows-Global.csv` |
| Barchart options/greeks collect | Often `collect_exit=1` noise | Does not block hydrate; core Koyfin + basis paths OK |
| `gate_status` in parquet | Often empty | TC derives from score + transmission |

### Machine registry

[`data_dictionary.yaml`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/data_dictionary.yaml) — locked naming, ingest routes, node weights, funds baskets. Export specs: [v2.1](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.1_SPEC.md) · [v2.2](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.2_SPEC.md)

---

## 8. Grok operator prompt

**For TempLibby (Browser Grok).** Paste as system/context wrapper, then attach `grok_payload` from TC **Copy Grok prompt** or **Export Pipeline Bundle**.

```
You are supporting the Whinfell Transmission Control operator console.

Return your answer in this exact order:

SECTION 1 — PLAIN ENGLISH
Regime setup, BTC calendar arb allowed/constrained/blocked, main risk, next steps.
Direct, practical, non-technical where possible.

SECTION 2 — TOOL MAP
Map into: Whinfell Score, Transmission State, Regime Tag, Gate State, Execution Intent,
Operator Confidence, Shock Probability/Horizon, Basis Regime Label, Layer 3 action, Key Observation.

SECTION 3 — UI CHECK
Does the UI help or hurt? Recommend clarity, gate visibility, operator safety only.
Rewrite confusing helper text in simpler desk English if needed.

SECTION 4 — OPERATOR ACTION
One line: EXECUTE / WATCH / BLOCKED — size posture + main reason.

SECTION 5 — WTM EXPORT
--- WTM EXPORT ---
Whinfell Score: <value>
Transmission State: <value>
Regime Tag: <value>
Key Observation: <value>

RULES:
- Plain English before tool language.
- Score < 50 → BTC calendar arb BLOCKED.
- Tight Risk → client structures only, reduced size.
- Flag confusing or inconsistent tool state.
- Reference hydration_audit summary if grok_payload includes it.
```

Full prompt file: [Whinfell_Grok_Operator_Prompt.txt](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/08_Deliverables/Whinfell_Grok_Operator_Prompt.txt)

---

## 9. Troubleshooting

| Symptom | Check | Fix |
|---------|-------|-----|
| TC shows "Hydration required" | No bundle in session | Import [latest.json](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/latest.json) or use [Pages URL](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) |
| Field log shows `empty` on required field | [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) remediation | Re-run AM chain; check quarantine `.meta.json` |
| Flows ✕ on all nodes | `flows_sidecar.flows_status` | Stage `flows_*.csv`; re-export WTM-Flows-Global |
| RV chart empty | `rv_horizon_count` in audit | Re-run barchart history; verify Koyfin exports staged |
| `collect_exit=1` in daily manifest | Barchart options/greeks noise | OK if hydrate_exit=0; core paths still populate |
| Import blocked (downgrade guard) | Incoming quality &lt; current session | Shift+click Import to force, or dismiss stale session |
| Pages 404 | Repo visibility / Actions source | Repo public · Pages source = GitHub Actions |
| Wes sees stale data | Pages not republished | Run [publish_desk_preview.sh](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/scripts/publish_desk_preview.sh) |

### Quarantine diagnosis

```bash
ls staged_raw/quarantine/$(date +%Y%m%d)/
# Read sidecar:
cat staged_raw/quarantine/.../*.meta.json
```

---

## 10. File map (quick reference)

| Resource | Local (Clark Mac) | Web link |
|----------|-------------------|----------|
| Operator console | `~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html` | [Pages desk](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) · [source](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Transmission_Control.html) |
| Hydration bundle | `data/hydration/latest.json` | [Pages JSON](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/latest.json) · [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/latest.json) |
| Hydration audit log | `data/hydration/hydration_log.json` | [Pages JSON](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json) · [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/data/hydration/hydration_log.json) |
| CSV drop folder | `~/Downloads/whinfell_drop/` | — (local only) |
| Staged ingest | `staged_raw/` | [GitHub tree](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/tree/main/staged_raw) (manifests only; CSVs gitignored) |
| Data dictionary | `whinfell_pipeline/data_dictionary.yaml` | [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/data_dictionary.yaml) |
| Publish to Pages | `scripts/publish_desk_preview.sh` | [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/scripts/publish_desk_preview.sh) |
| Morning chain | `whinfell_daily_am.sh` | [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_daily_am.sh) |
| Daily CSV pipeline | `run_csv_download.py` | [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/run_csv_download.py) |
| Desk URLs (Comet) | `whinfell_pipeline/desk_urls.yaml` | [GitHub](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/desk_urls.yaml) |

---

## 11. Support & ownership

| Role | Contact / tool |
|------|----------------|
| System owner | TempLibby |
| Desk owner | Clark |
| Build / pipeline | BUILD Cousins |
| Collection agents | Comet · Perplexity (supervised) |
| Quant review | G-Quant |
| Stakeholder preview | Wes → [Pages desk URL](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) (§2) |

**Ship status (June 30, 2026):** Phase 2.2 mission surfaces (5/5) · hydration field audit · GitHub Pages desk preview · ARCH-1 ingest routing · production session `ok` at quality 90.

---

*Whinfell Desk User Manual v1.0 — share freely with Comet, Perplexity, Wes, G-Quant, and TempLibby.*