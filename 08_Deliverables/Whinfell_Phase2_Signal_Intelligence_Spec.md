# Whinfell Transmission Control — Phase 2 Signal Intelligence Spec

**Version:** 2.0 (Refined)  
**Date:** June 26, 2026  
**Status:** Draft implemented — P2a + P2b  
**File:** `08_Deliverables/Whinfell_Transmission_Control.html`

---

## Objective

Elevate Transmission Control from execution layer to **Signal Intelligence & Decision Support** — human-in-the-loop, no live feeds.

---

## In Scope (Phase 2)

| Area | Delivered |
|------|-----------|
| Signal Tracer enhancements | Health score, snapshots, chain viz, configurable shocks |
| Lightweight looping | Re-evaluate macro, Scenario Loop (session-only) |
| BTC opportunity scanning | Reference-band rules on L3 card |
| Data model v3 | Named snapshots (cap 12), WTC-2.0 export |
| Gate + tracer integration | Informational health on gate banner |

## Out of Scope

- Live Koyfin/Barchart feeds
- Auto-execution
- Multi-user shared state
- Portfolio optimization

---

## 1. Signal Tracer

### Health Score (0–100, derived)

- Ladder net scores: 40%
- Whinfell Score: 35%
- Chain coherence: 25%
- **Never persisted** — computed on render/export

### Named Snapshots (max 12)

```javascript
{ id, name, savedAt, scoreBand, regimeTag, intake, tracer, posture }
```

Save / Load / Delete / Compare against current state.

### Enhanced Chain

- Weakest link highlighted
- Arrow weight by adjacent divergence
- Directional arrows for ±1 deltas

### Configurable Shocks

- Intensity: **mild** (1d only) / **full**
- Per-stage enable toggles
- Stored in `tracer.shockConfig`

---

## 2. Lightweight Looping

| Mode | Trigger | Behavior |
|------|---------|----------|
| **Re-evaluate** | User click | Refresh matrix → re-apply shock → recalc health |
| **Scenario Loop** | User click | 2–3 intake what-ifs, side-by-side gate + health (session-only) |

No background polling or auto-alerts.

---

## 3. BTC L3 Opportunity Scan

Manual reference bands:

| Field | Use |
|-------|-----|
| refLow / refMid / refHigh | Operator-entered historical range |
| basisSpread | Current spread |

**Scan** → Rich / Fair / Cheap + direction hint. Label: manual-reference score.

---

## 4. Data Model v3

```javascript
{
  version: 3,
  intake, grossRisk, research, tracer, btcL3, urls, meta,
  snapshots: [],
  scenarioLoop: { variants, lastResults }  // ephemeral
}
```

**Export:** `WTC-2.0` + `WTM EXPORT v2.0` research block.

---

## 5. Arena Sign-Off (Sprint Self-Review)

| Role | Result |
|------|--------|
| Blueprint | PASS — layer separation maintained |
| Edge | PASS — BTC scan rule-based only |
| Safeguard | PASS — gate score-driven; health advisory |
| Bridge | PASS — schema v3 + export bump |
| Clarity | PASS — tracer tab information hierarchy |
| Spark | PASS — user-triggered looping only |
| Hammer | PASS — ship-ready draft |

---

## Known Gaps (Post-Sprint)

- WTC-2.0 full export not yet import-parseable (snapshots, shock config)
- Scenario Loop uses current tracer for all variants (intake-only what-if)
- Horizon auto-fill deferred to future phase

**Next:** Desk feedback → TempLibby sign-off → Phase 2 production badge