# /arena — Funds Flow Ingest Strategy Debate

**Date:** June 29, 2026  
**Facilitator:** BUILD Cousins  
**Question:** How should Whinfell ingest ETF flow data for the Funds Flow Sponsorship layer?  
**Resolution:** **Option D (Hybrid) accepted** — see [Phase2_Flows_Implementation_Spec.md](../01_Strategy_Docs/Phase2_Flows_Implementation_Spec.md)  
**Authority:** [Phase2_Funds_Flow_Sponsorship_Design.md](../01_Strategy_Docs/Phase2_Funds_Flow_Sponsorship_Design.md)

---

## Arena context

| Fact | Evidence |
|------|----------|
| Staged `credit_*.csv` today is **WTM observation** rows | `observation_id,timestamp,whinfell_score,...` — no flow columns after 2.2e transform |
| Raw credit cross-section **does** have flows | `Fund Flows/Periodic (D)` + `AUM` per ticker (millions USD) in quarantine WhinPump exports |
| **WTM-Flows-Global.csv already exists on desk** | `~/Downloads/whinfell_drop` — **quarantined** (wrong filename) |
| WTM-Flows format is ideal for 5D | Dated rows: `{TICKER} Flow (D)` + `{TICKER} AUM` — 750+ sessions |
| Current WTM-Flows ticker set is **incomplete** | SPY, HYG, LQD, JAAA, BKLN, MCHI only — missing IBIT, IWM, IEF, TLT, SHY, QQQ, RSP, BITO, GBTC |
| Design requires **5D cumulative % AUM** | Cross-section alone cannot compute 5D without a history store |

**Desk pain today:** Clark dropped `WTM-Flows-Global.csv` twice (Jun 29) → quarantine with reason: `filename must match flows_{YYYYMMDD}_{HHMM}.csv`.

---

## What each persona needs

| Persona | Priority |
|---------|----------|
| **Clark (operator)** | Minimal extra clicks; no new rename surprises |
| **TempLibby (desk lead)** | Institutional signal quality; 5D persistence; no noisy 1D-only reads |
| **Bridge (pipeline)** | One parser path; deterministic `% AUM`; sidecar → hydrate |
| **Integration Dynamo** | Fits `collection_manifest.yaml` + normalize_rules; no WhinSig merge |
| **Clarity (UI)** | All 5 node baskets populated or graceful `enabled: false` |

---

## Option A — Dedicated `WTM-Flows` export (BUILD recommendation)

**What:** Add optional batch export #15 — Koyfin saved view **WTM-Flows** with dated `Flow (D)` + `AUM` for **all basket ETFs** (~18 tickers).

**Operator action:**
1. Open saved view WTM-Flows (historical table, Date column)
2. Export CSV → `whinfell_drop/`
3. Normalize → `flows_{YYYYMMDD}_{HHMM}.csv`

**Pipeline:** `flows_ingest.py` → `data/flows/v1/latest_flows.json` → `funds_flows.py` on hydrate.

| Pros | Cons |
|------|------|
| Single authoritative time-series for 5D + 20D persistence | +2 clicks/day (optional, not in required 8) |
| Matches existing desk artifact (`WTM-Flows-Global.csv`) | Clark must expand Koyfin view tickers |
| `% AUM` = `Flow(D) / AUM × 100` (same units — millions) | New normalize rule + manifest entry |
| Clean separation from WTM observation transform | View maintenance when baskets change |

**Evidence:** Quarantine file header:
```
Date, SPY Flow (D), HYG Flow (D), ..., SPY AUM, HYG AUM, ...
```

---

## Option B — Parse flows from `WTM-Credit-Confirmation` only

**What:** Extend credit ingest to read `Fund Flows/Periodic (D)` + `AUM` from raw cross-section before WTM row transform.

| Pros | Cons |
|------|------|
| Zero extra exports — credit already in required batch | **No dated history** in staged path → **no 5D cumulative** |
| Rich credit ETF coverage (HYG, LQD, IBIT, GBTC in WhinPump) | Credit file often transformed to observation-only |
| Fast MVP for Credit node only | Breadth / Liquidity / Basis nodes lack ETFs |
| | Column name differs from WhinSig (`Fund Flows/Periodic (D)` vs `Flow (D)`) |
| | Conflicts with 2.2e “last row = observation” contract |

**Verdict:** Useful as **1D fallback** for Credit node only — **insufficient as primary** for sponsorship layer (design requires 5D).

---

## Option C — Mine `WTM-Rates-Credit` wide timeseries (`rates_*.csv`)

**What:** Parse `BIL Flow (D)`, `HYG Flow (D)`, etc. from optional Koyfin daily wide export.

| Pros | Cons |
|------|------|
| Some flow columns already in wide rates file | Partial coverage — not all basket ETFs |
| Date column supports 5D if file ingested daily | Massive column noise (prices + vol + corr) |
| No new saved view if rates optional export runs | Rates export is **optional** — flows absent on many days |
| | Parser complexity; fragile column detection |

**Verdict:** **Supplement only** — do not anchor sponsorship on optional rates export.

---

## Option D — Hybrid primary + fallback (implementation pattern)

**What:**  
1. **Primary:** Option A (`flows_*.csv` time-series)  
2. **Fallback:** Option B cross-section `Fund Flows/Periodic (D)` when flows file missing  
3. **Fallback limits:** 1D `% AUM` only; set `horizon_display: 1d`; verdict cap at `neutral`/`mixed`; `interpretation.summary` notes “5D unavailable”

| Pros | Cons |
|------|------|
| Best signal when flows file present | Two code paths to test |
| Cockpit never hard-fails | Operator may not notice degraded mode |
| Matches progressive-fill philosophy | Must not fake 5D from single snapshot |

**Verdict:** **Recommended implementation shape** — primary A, degrade to B.

---

## Option E — WhinSig `flows_merger.py` integration

**What:** Call or port WhinSig merger from `~/Desktop/dashboards/whinsig/`.

| Pros | Cons |
|------|------|
| Proven Flow (D) detection | Cross-repo dependency; outside Whinfell BUILD scope |
| | Different output shape; not node-basket aware |
| | Playbook explicitly says “not Whinfell basis pipeline” |

**Verdict:** **Borrow patterns, not code** — replicate column detection in `funds_flows.py`.

---

## Comparison matrix

| Criterion | A WTM-Flows | B Credit only | C Rates wide | D Hybrid | E WhinSig |
|-----------|-------------|---------------|--------------|----------|-----------|
| 5D cumulative | ✅ | ❌ | ⚠️ partial | ✅ | ✅ |
| All 5 node baskets | ✅ (if view built) | ❌ credit-heavy | ❌ | ✅/⚠️ | ⚠️ |
| Extra daily clicks | +2 optional | 0 | 0 | +2 optional | N/A |
| Pipeline complexity | Low | Medium | High | Medium | High |
| Already on desk | ✅ (quarantined) | ✅ (raw quarantine) | ✅ (quarantine) | ✅ | Separate repo |
| Matches Master DD | ✅ clean | ⚠️ | ⚠️ | ✅ | ❌ |

---

## BUILD Cousins recommendation (for team vote)

### Adopt **Option D** with **Option A as primary**

1. **Immediate (PR-3a):** Register `flows_{YYYYMMDD}_{HHMM}.csv` in Master DD + `normalize_whinfell_drop.sh` mapping from `WTM-Flows-Global.csv` / `WTM-Flows*.csv`.
2. **Clark (one-time):** Expand Koyfin **WTM-Flows** saved view to full basket ticker list (see design doc § baskets).
3. **Optional enrichment:** Add `koyfin_flows` to `collection_manifest.yaml` — `optional: true`, priority 15, **not** in `required_batch_ids`.
4. **Fallback:** Cross-section `Fund Flows/Periodic (D)` from raw credit quarantine path → Credit node 1D only when `flows_*.csv` absent.
5. **Do not** block daily 8-click chain on flows file — sponsorship degrades to `enabled: false` or 1D-limited.

### Reject as primary

- **Option B alone** — fails 5D requirement  
- **Option E** — scope creep  

---

## Decisions needed from team

| # | Question | Options | BUILD default |
|---|----------|---------|---------------|
| **Q1** | Primary ingest path? | A only · D hybrid · B credit-only | **D hybrid** |
| **Q2** | Add flows to daily Comet `/plan`? | Required (+2 clicks) · Optional enrichment · Manual weekly | **Optional enrichment** |
| **Q3** | Rename contract for desk? | `flows_{YYYYMMDD}_{HHMM}.csv` · `wtm_flows_{YYYYMMDD}.csv` | **`flows_{YYYYMMDD}_{HHMM}.csv`** |
| **Q4** | Who expands Koyfin WTM-Flows view? | Clark · Perplexity · BUILD spec only | **Clark + BUILD ticker list** |
| **Q5** | Unit assumption locked? | Flow & AUM both millions USD → `% AUM = flow/aum×100` | **Yes — verify on HYG row** |

### Q5 sanity check (from quarantine `WTM-Flows-Global.csv`, 2023-06-29)

```
HYG Flow (D) = -678.90    HYG AUM = 14505.42
→ % AUM ≈ -4.68% daily   (large move — likely millions USD flow / millions AUM)
```

Desk should confirm this matches Koyfin display semantics before locking thresholds.

---

## Immediate unblock (no debate required)

```bash
# Rename desk drop before stage (until normalize script updated)
mv ~/Downloads/whinfell_drop/WTM-Flows-Global.csv \
   ~/Downloads/whinfell_drop/flows_$(date +%Y%m%d)_$(date +%H%M).csv
```

Or add to `normalize_whinfell_drop.sh`:
```
WTM-Flows-Global.csv → flows_{YYYYMMDD}_{HHMM}.csv
WTM-Flows*.csv       → flows_{YYYYMMDD}_{HHMM}.csv
```

---

## Vote template (paste in desk channel)

```
Funds Flow Ingest — Arena vote
Q1 Primary:  [ ] A only  [ ] D hybrid ✓  [ ] B only
Q2 Daily plan: [ ] Required  [ ] Optional ✓  [ ] Weekly manual
Q3 Filename:   [ ] flows_{date}_{time} ✓  [ ] wtm_flows_{date}
Q4 View owner: [ ] Clark ✓  [ ] Perplexity  [ ] BUILD only
Q5 Units:      [ ] millions/millions ✓  [ ] needs desk check

Clark / TempLibby: reply with choices by EOD or default BUILD recommendations apply.
```