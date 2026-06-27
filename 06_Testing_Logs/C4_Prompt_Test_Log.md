# C4 — Structured Prompt Testing Log

**Project:** Whinfell Transmission System  
**Lead:** Precision (BUILD Cousins)  
**Target:** Transmission Control v1.2 + WTM EXPORT v2.0  
**Date:** June 26, 2026  
**Status:** Sprint complete — structured test pass

---

## Test Scope

| # | Prompt / Layer | Test Focus |
|---|----------------|------------|
| A | WTM Transmission Read & Regime Classification | v2.0 export block · intake mapping |
| B | WTM Posture & Gross-Risk Recommendation | Gross % + posture parse |
| C | WTM Trade Evaluation & Ranking | Copy integrity · Inputs/Outputs |
| D | WTM Income Projection | Copy integrity · regime linkage text |
| E | WTM Divergence & Risk Compression | Copy integrity · action orientation |
| L2 | BTC Options Workflow | Gate block <50 · copy when allowed |
| L3 | BTC Calendar Arb Agent | Gate + spread fields in copy |

**Cross-cutting:** Round-trip handoff · gate reactions · tracer BTC bias · parser robustness

---

## Test Log Template

| Test ID | Date | Prompt | Input / Scenario | Expected | Actual | Pass |
|---------|------|--------|------------------|----------|--------|------|
| C4-001 | | | | | | |
| C4-002 | | | | | | |

---

## Executed Tests (June 26, 2026)

| Test ID | Scenario | Expected | Actual | Pass |
|---------|----------|----------|--------|------|
| C4-001 | Import WTM EXPORT v2.0 sample (Score 58, Stressed, Fragile Risk-On) | Intake populated; 7 fields parsed | Parser extracts score, state, regime, observation, gross rec, BTC bias, timestamp | **PASS** |
| C4-002 | Gross Risk Recommendation: `35% total, Light posture` | grossA=35, posture=light | Regex + posture map yields correct fields | **PASS** |
| C4-003 | BTC Bias: Confirming | highbeta d1 = up | BTC_BIAS_MAP → tracer horizon | **PASS** |
| C4-004 | BTC Bias: Dragging | highbeta d1 = down | Mapped correctly | **PASS** |
| C4-005 | Transmission State: Normal (capitalized) | transmissionState=normal | TX_PARSE handles label | **PASS** |
| C4-006 | Gate Score 45 | BLOCKED, BTC cards blocked | evaluateGate blocked=true | **PASS** |
| C4-007 | Gate Score 58 | Tight Risk Band, BTC enabled | tight=true, blocked=false | **PASS** |
| C4-008 | Gate Score 72 | Allowed | allowed key | **PASS** |
| C4-009 | Posture auto at score 58 | light | suggestPosture → light | **PASS** |
| C4-010 | Posture warning: Light + Blocked gate | Warning shown | postureGateMismatch true | **PASS** |
| C4-011 | Prompt A–E present in dashboard | 5 cards + Copy + I/O labels | PROMPTS array length 5, renderPrompts | **PASS** |
| C4-012 | Prompt A requires v2.0 block in canonical text | Export instruction in prompt body | Text includes WTM EXPORT v2.0 | **PASS** |
| C4-013 | L2/L3 copy disabled when blocked | disabled=true | btnCopy disabled when gate.blocked | **PASS** |
| C4-014 | Export includes v2.0 block | buildWtmExportV20 appended | Export function chains v2.0 | **PASS** |
| C4-015 | Round-trip: export → re-parse v2.0 block | Score/regime restored | extractWtmExportV20 + parseWtmExportV20 | **PASS** |
| C4-016 | Key Observation → handover when empty | handover prefilled | applyImportFields logic | **PASS** |
| C4-017 | Horizon line parse: Credit Confirmation | tracer credit row | Stage name regex parse | **PASS** |
| C4-018 | Invalid clipboard (no labels) | Toast: no fields | imported.length === 0 | **PASS** |
| C4-019 | Legacy v0 flat state migration | No crash, nested state | normalizeLegacyState | **PASS** |
| C4-020 | Shock Credit Widening → credit d1 down | Effects applied | SHOCKS.creditWidening effects | **PASS** |

---

## Findings & Recommendations

| # | Severity | Finding | Recommendation |
|---|----------|---------|----------------|
| 1 | Info | Prompt A taxonomy (Risk-On) differs from intake dropdown (Normal/Stressed) | Desk maps via Regime Tag; documented in Operator Guide |
| 2 | Info | Gross rec sets Book A only when total given | Desk splits A/B manually if needed — acceptable |
| 3 | Low | WTC-2.0 full state export not yet round-trip importable | Phase 2 import extension queued |
| 4 | Info | Live Perplexity responses vary in prose before export block | Parser prioritizes v2.0 block — robust |

**Overall:** Prompts A–E and L2/L3 are production-ready for desk use. v2.0 handoff is reliable for intake, gross risk, and BTC tracer seeding.

---

## Sign-Off

**Precision (Self Review):** PASS — June 26, 2026  
**Arena (Clarity Sentinel + Safeguard):** PASS — structured test coverage adequate for sprint ship