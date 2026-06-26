# Whinfell Credit Confirmation Score — Full Calculation Logic

**Deliverable:** C1  
**Version:** 0.9 (Draft — Worked Example pending live panel data)  
**Owners:** Blueprint + Edge  
**Date:** June 26, 2026  
**Status:** In Progress — Self Review  
**Authoritative Source:** TempLibby / Arena (June 26, 2026)

---

## 1. Overview

The **Whinfell Credit Confirmation Score** is a 0–100 composite that measures whether credit and cross-asset conditions **confirm** or **impair** risk appetite. It is used to gate gross exposure and basis trade selection on the Transmission Map dashboard.

**Design principle:** Start neutral (50), add or subtract component weights based on signal direction, clamp to 0–100.

---

## 2. Weighting Table (Authoritative)

| # | Component | Weight | Bullish Condition | Bearish Condition |
|---|-----------|--------|-------------------|-------------------|
| 1 | HY spread trend (5D + 20D) | **25%** | HY spreads tightening on both windows | HY spreads widening on both windows |
| 2 | IG spread trend (5D + 20D) | **15%** | IG spreads tightening or stable | IG spreads widening persistently |
| 3 | HY minus IG differential | **10%** | Differential narrowing | Differential widening |
| 4 | HYG / LQD ratio | **10%** | Ratio rising | Ratio falling |
| 5 | Financials vs Defensives (XLF vs XLU/XLP) | **10%** | XLF outperforming defensives | XLF lagging defensives |
| 6 | 2s10s + 3m10y curve impulse | **10%** | Curve steepening for constructive/growth reasons | Inversion deepening or bear steepener |
| 7 | Equity breadth confirmation | **10%** | RTY + cyclicals participating meaningfully | Narrow megacap-led rally only |
| 8 | BTC / High-beta confirmation | **10%** | IBIT and high-beta assets confirming risk appetite | IBIT lagging or diverging sharply |

**Total weight:** 100%

---

## 3. Calculation Formula

### Step 1 — Base Score

```
Base Score = 50
```

### Step 2 — Score Each Component

For each of the 8 components, assign a **signal direction**:

| Signal | Points Applied |
|--------|----------------|
| **Clear Bullish** | +Full weight (e.g., +25 for Component 1) |
| **Clear Bearish** | −Full weight (e.g., −25 for Component 1) |
| **Mixed / Weak** | ±Half weight (e.g., +12.5 or −12.5 for Component 1) |
| **No readable signal** | 0 (see Missing Data Rules) |

```
Component Points = Weight × Direction Multiplier

Where Direction Multiplier = +1 (bullish), −1 (bearish), ±0.5 (mixed), or 0 (unavailable)
```

### Step 3 — Sum and Clamp

```
Raw Score = 50 + Σ(Component Points)
Final Score = CLAMP(Raw Score, 0, 100)
```

### Quick Reference Formula

```
Score = CLAMP( 50
  + HY_spread_pts      (±25 or ±12.5)
  + IG_spread_pts      (±15 or ±7.5)
  + HY_IG_diff_pts     (±10 or ±5)
  + HYG_LQD_ratio_pts  (±10 or ±5)
  + XLF_defensive_pts  (±10 or ±5)
  + Curve_impulse_pts  (±10 or ±5)
  + Breadth_pts        (±10 or ±5)
  + BTC_highbeta_pts   (±10 or ±5)
, 0, 100)
```

---

## 4. Data Sources

| Component | Primary Source | Series / Field | Notes |
|-----------|---------------|----------------|-------|
| HY spread trend | Koyfin | HY OAS or equivalent spread index — 5D change + 20D change | Tightening = spread level falling |
| IG spread trend | Koyfin | IG OAS or equivalent — 5D change + 20D change | Stable = within ~2 bp over 20D |
| HY minus IG differential | Koyfin / derived | HY OAS − IG OAS; compare 5D and 20D direction | Narrowing = differential shrinking |
| HYG / LQD ratio | Koyfin / Barchart | HYG price ÷ LQD price; track 5D direction | Rising ratio = risk-on credit |
| Financials vs Defensives | Koyfin / Barchart | XLF return vs blended XLU + XLP (or XLU alone) over 5D and 20D | Relative performance, not absolute |
| 2s10s + 3m10y curve impulse | Koyfin / FRED | 2s10s spread change + 3-month change in 10Y yield | Distinguish bull steepener vs bear steepener |
| Equity breadth | Koyfin / Barchart | RTY vs SPX (or QQQ) + cyclical sector participation | Meaningful = RTY keeping pace or leading |
| BTC / High-beta | Koyfin / Barchart | IBIT 5D% vs SPX; high-beta basket confirmation | Divergence = IBIT lagging on risk-on days |

> **C3 dependency:** Exact Koyfin ticker codes and Barchart series IDs will be documented in the Series & Ticker Master List (C3).

---

## 5. Missing Data Rules

| Situation | Rule |
|-----------|------|
| **20D% not directly available** | Use 1M% as proxy for 20D window. Note substitution in calculation log. |
| **5D% not available** | Use most recent 5 trading-day manual calc from daily closes. If impossible, score component as **Mixed (half weight)** and flag. |
| **Spread data delayed** | Fall back to HYG/LQD price-ratio direction as proxy for Components 1–3 only; score at **half weight** and flag as proxy. |
| **Single window conflicts** (5D bullish, 20D bearish) | Score as **Mixed (half weight)** in the direction of the 20D signal. |
| **Curve data unavailable** | Score Component 6 as **0**; do not impute. Note gap in log. |
| **Component entirely unavailable** | Assign **0 points**; do not redistribute weight. Final score reflects reduced confidence — note in interpretation. |

**Manual calc rule:** If ≥2 components are scored at 0 due to missing data, treat the overall reading as **low confidence** regardless of numeric score.

---

## 6. Component Scoring Guide (Desk Reference)

### Component 1 — HY Spread Trend (25%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+25)** | HY OAS down on both 5D and 20D |
| **Bearish (−25)** | HY OAS up on both 5D and 20D |
| **Mixed (±12.5)** | One window tightening, one widening; or flat 5D with meaningful 20D move |

### Component 2 — IG Spread Trend (15%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+15)** | IG OAS tightening or stable (≤2 bp change over 20D) |
| **Bearish (−15)** | IG OAS widening persistently (both windows) |
| **Mixed (±7.5)** | Stable 5D but widening 20D, or vice versa |

### Component 3 — HY minus IG Differential (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | Differential narrowing over 5D and 20D |
| **Bearish (−10)** | Differential widening over 5D and 20D |
| **Mixed (±5)** | Conflicting window direction |

### Component 4 — HYG / LQD Ratio (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | Ratio rising over 5D (HYG outperforming on relative basis) |
| **Bearish (−10)** | Ratio falling over 5D |
| **Mixed (±5)** | Flat or choppy; use 1M direction as tiebreaker |

### Component 5 — Financials vs Defensives (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | XLF outperforming XLU/XLP on 5D and 20D |
| **Bearish (−10)** | XLF lagging defensives on both windows |
| **Mixed (±5)** | Outperforming short-term, lagging longer-term |

### Component 6 — Curve Impulse (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | 2s10s steepening with growth/constructive context (not inflation panic) |
| **Bearish (−10)** | Inversion deepening or bear steepener (long-end selloff on growth fears) |
| **Mixed (±5)** | Steepening but driven by front-end cuts pricing; ambiguous context |

### Component 7 — Equity Breadth (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | RTY and cyclicals participating; breadth expanding |
| **Bearish (−10)** | Narrow megacap-led rally; RTY lagging |
| **Mixed (±5)** | RTY flat while SPX rallies |

### Component 8 — BTC / High-Beta (10%)

| Reading | Condition |
|---------|-----------|
| **Bullish (+10)** | IBIT confirming risk-on; high-beta assets aligned |
| **Bearish (−10)** | IBIT lagging or sharp divergence from equities |
| **Mixed (±5)** | IBIT flat while equities rally |

---

## 7. Score Interpretation Bands (Authoritative)

| Score | Color | Zone Name | Positioning Guidance |
|-------|-------|-----------|----------------------|
| **80–100** | Green | Strong Confirmation | Full gross allowed. Aggressive Client + Outright Basis |
| **65–79** | Amber | Constructive | Selective adds. Prefer Client Basis over Outright |
| **45–64** | Amber | Mixed / Fragile | Light gross. Fade weak follow-through |
| **25–44** | Red | Impaired | Reduce beta exposure. Favor hedges and relative value |
| **0–24** | Red | Hard Risk-Off | Defensive posture only |

### Current Dashboard Alignment

Live Comet dashboard (June 26, 2026): **Whinfell Score 58 / Amber — Mixed / Fragile**

---

## 8. Worked Example — Live Dashboard (June 26, 2026)

> **Status:** Pending live panel values from Comet workspace.  
> **Target outcome:** Reproduce **Score = 58** using today's visible inputs.

### Data Request (from Comet panels)

Please provide current values for:

| Panel | Fields Needed |
|-------|---------------|
| Credit ETFs | HYG 5D%, 1M% (20D proxy) |
| Credit ETFs | LQD 5D%, 1M% |
| Sector relative | XLF vs XLU/XLP relative performance (5D, 20D) |
| Spreads | HY OAS 5D + 20D direction; IG OAS 5D + 20D direction |
| Differential | HY−IG spread differential direction |
| Curve | 2s10s level + recent change; 3m10y change |
| Breadth | RTY vs SPX relative (5D) |
| High-beta | IBIT 5D% vs SPX 5D% |

### Calculation Worksheet (to be completed)

| Component | Weight | Signal | Points | Running Total |
|-----------|--------|--------|--------|---------------|
| Base | — | — | 50 | 50 |
| 1. HY spread trend | 25% | _TBD_ | _TBD_ | _TBD_ |
| 2. IG spread trend | 15% | _TBD_ | _TBD_ | _TBD_ |
| 3. HY−IG differential | 10% | _TBD_ | _TBD_ | _TBD_ |
| 4. HYG/LQD ratio | 10% | _TBD_ | _TBD_ | _TBD_ |
| 5. XLF vs defensives | 10% | _TBD_ | _TBD_ | _TBD_ |
| 6. Curve impulse | 10% | _TBD_ | _TBD_ | _TBD_ |
| 7. Equity breadth | 10% | _TBD_ | _TBD_ | _TBD_ |
| 8. BTC / high-beta | 10% | _TBD_ | _TBD_ | _TBD_ |
| **Final (clamped)** | | | | **Target: 58** |

---

## 9. Manual Calculation Checklist (~2 min)

1. Open Transmission Map / fallback sheet
2. Read each of the 8 component signals (bullish / bearish / mixed)
3. Start at **50**
4. Add or subtract weights per table (half weight for mixed)
5. Clamp to 0–100
6. Map score to interpretation band
7. Apply positioning guidance

---

## 10. Review Status

| Gate | Status | Date |
|------|--------|------|
| Self Review | Pending | — |
| Peer Review | Not started | — |
| Arena Review | Not started | — |
| TempLibby Sign-off | Not started | — |

---

*Sections 1–7 and 9 are complete. Section 8 will be finalized once live panel values are received from Comet workspace.*