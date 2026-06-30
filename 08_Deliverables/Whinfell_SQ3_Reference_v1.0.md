# SQ3 — China Policy Transmission Score

**Version:** 1.0  
**Date:** June 30, 2026  
**Status:** Production · locked weights  
**Authority:** `china_policy_track/sq3.py` (Python) · mirrored in Transmission Control (JavaScript)  
**Isolation:** SQ3 does **not** interact with Global Credit Confirmation Score (C1) logic

**Related:** [Desk User Manual v1.0](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Desk_User_Manual_v1.0.md) · [China Ladder v1.1](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/china_ladder.py)

---

## 1. What SQ3 is

**SQ3** is Whinfell’s **China Policy Transmission Score** — a single 0–100 number that answers:

> *Is China policy currently supporting or impairing global risk transmission — independent of the Global Whinfell Score?*

SQ3 sits on the **China track** of the dual-track console. Global Whinfell Score governs **BTC module access** (hard gate). SQ3 governs **China caution**, **dual-track impairment**, **mission-surface suffixes**, and the **China ladder handicap**.

| Track | Score | Primary question |
|-------|-------|----------------|
| **Global** | Whinfell Score (0–100) | Can we take new BTC risk? Is global transmission healthy? |
| **China** | SQ3 (0–100) | Is China policy transmission constructive, mixed, or impaired? |

Both scores appear in the command bar. Either can flag impairment even when the other looks fine — that asymmetry is intentional.

---

## 2. The three dimensions (inputs)

SQ3 is a **transparent weighted composite** of three desk-entered or pipeline-imported scalars:

| Dimension | Field (TC / bundle) | Range | Weight | Meaning |
|-----------|---------------------|-------|--------|---------|
| **Policy Strength** | `policy_strength` | 0–100 | **35%** | Hierarchy + force of central/provincial policy direction (fiscal, industrial, stabilization language) |
| **State Control Impulse** | `state_impulse_score` | **−100 to +100** | **35%** | Regulatory / intervention intensity — **positive = more state control** (typically impairs private-market transmission) |
| **Growth / Market Impulse** | `growth_impulse_score` | 0–100 | **30%** | Growth and market liquidity impulse (credit, PMI, turnover, property chain health) |

**Desk shorthand (shown in TC Explain drawer):**

> SQ3 = Policy STR. (35%) + State IMP. (35%) + Growth IMP. (30%)

### Where inputs come from

| Source | Path |
|--------|------|
| Manual entry | TC left rail → China Track · SQ3 (`#chinaPolicyStrength`, `#chinaStateImpulse`, `#chinaGrowthImpulse`) |
| Perplexity | `--- CHINA POLICY EXPORT v1.0 ---` text block |
| Koyfin CSV | `china_policy_{YYYYMMDD}_{HHMM}.csv` → Parquet → hydration `bundle.china` |
| WTM EXPORT | Lines `Policy Strength:`, `State Impulse Score:`, `Growth Impulse Score:` |

**Authoritative parser:** [`china_policy_track/data_parser.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/data_parser.py)  
**Example export:** [`sample_perplexity_export.txt`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/examples/sample_perplexity_export.txt)

---

## 3. How SQ3 is calculated

### Step 1 — Normalize each dimension to a 0–100 sub-scale

**Policy Strength** and **Growth Impulse** are already 0–100:

```
policy_normalized   = clamp(policy_strength, 0, 100)
growth_normalized   = clamp(growth_impulse_score, 0, 100)
```

**State Control Impulse** is signed (−100 … +100) and **inverted** so higher state control lowers the sub-score:

```
state_clamped       = clamp(state_impulse_score, -100, 100)
state_normalized    = (100 - state_clamped) / 2
```

| State impulse (raw) | Normalized sub-score | Desk read |
|--------------------|----------------------|-----------|
| +100 (max control) | 0 | Maximum impairment from state intervention |
| +38 | 31 | Elevated control — drags composite |
| 0 | 50 | Neutral |
| −100 (min control) | 100 | Minimum control friction |

### Step 2 — Apply fixed weights

```
policy_component  = 0.35 × policy_normalized
state_component   = 0.35 × state_normalized
growth_component  = 0.30 × growth_normalized
```

### Step 3 — Sum, round, clamp

```
SQ3_raw   = policy_component + state_component + growth_component
SQ3_score = round(clamp(SQ3_raw, 0, 100))
```

### Step 4 — Map to interpretation band

| SQ3 score | Band | Desk meaning |
|-----------|------|--------------|
| 0–49 | **Impaired** | China-led transmission broken — treat global BTC as hedge sleeve, not carry anchor |
| 50–64 | **Mixed / Fragile** | Choppy transmission — BTC beta unstable; basis trades client-sized only |
| 65–79 | **Constructive** | China policy supportive — cleaner BTC–credit coupling |
| 80–100 | **Strong** | Full policy alignment — tailwind to cyclicals |

**Code (Python — source of truth):** [`china_policy_track/sq3.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/sq3.py)  
**Tests:** [`china_policy_track/tests/test_sq3.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/tests/test_sq3.py)

---

## 4. Worked examples

### Example A — Perplexity sample (constructive mid-band)

**Inputs:** Policy 74 · State +38 · Growth 61

| Step | Value |
|------|-------|
| policy_normalized | 74 |
| state_normalized | (100 − 38) / 2 = **31** |
| growth_normalized | 61 |
| policy_component | 0.35 × 74 = 25.9 |
| state_component | 0.35 × 31 = 10.85 |
| growth_component | 0.30 × 61 = 18.3 |
| **SQ3** | round(55.05) = **55** → **Mixed / Fragile** |

*Interpretation:* Strong policy language (74) but elevated state control (+38) pulls the composite into the mid-50s — classic “policy strong, execution constrained” desk read.

### Example B — Neutral policy, zero impulses (production June 30)

**Inputs:** Policy 50 · State 0 · Growth 0

| Component | Calculation | Value |
|-----------|-------------|-------|
| Policy | 0.35 × 50 | 17.5 |
| State | 0.35 × 50 | 17.5 |
| Growth | 0.30 × 0 | 0.0 |
| **SQ3** | | **35** → **Impaired** |

*Interpretation:* Zero growth impulse dominates — even “middle” policy and state scores cannot lift SQ3 above the impairment line. This matches live hydration `bundle.china` when growth fields default to 0.

### Example C — What would clear impairment?

To reach **SQ3 ≥ 50** from Example B, you need roughly **+15 points** on the weighted sum — e.g. raise Growth Impulse to ~50 (adds 15 growth component points) **or** lower State Impulse toward −30 (raises state_normalized toward 65).

To reach **SQ3 ≥ 65** (constructive), typically need Policy ≥ ~65 **and** State Impulse ≤ ~+25 **and** Growth ≥ ~55 — desk heuristic, not a separate formula.

---

## 5. SQ3 on the China Ladder (second use)

SQ3 also acts as a **handicap multiplier** on the raw China ladder composite (five stage scores from horizon marks). This is separate from the SQ3 policy score itself but uses the **same SQ3 number**.

**Raw ladder score** = mean of five canonical stage composites (liquidity, credit, breadth, highbeta, basis) from China horizon marks.

**SQ3 handicap multipliers** ([`china_ladder.py`](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/china_ladder.py)):

| SQ3 score | Multiplier | Effect on raw ladder |
|-----------|------------|-------------------|
| ≥ 80 | 1.00 | No handicap |
| 65–79 | 0.95 | −5% |
| 50–64 | 0.80 | −20% |
| &lt; 50 | 0.60 | −40% |

```
final_china_score = round(raw_ladder_score × multiplier)
```

**TC display:** China ladder panel shows raw score, SQ3, multiplier, and **final adjusted** score with band (Strong / Constructive / Mixed / Impaired).

---

## 6. How Transmission Control uses SQ3

### 6.1 Command bar

- `cmdSq3Score` — e.g. *SQ3 policy 35*
- `cmdSq3Band` — interpretation band chip color (red/amber/green)

Computed live from intake fields via `calculateSq3()` — must match Python `calculate_sq3()` bit-for-bit on the same inputs.

### 6.2 Gate logic (dual-track)

**Global gate (Whinfell Score)** — hard BTC access:

| Whinfell | Gate |
|----------|------|
| &lt; 50 | **BLOCKED** — no new BTC risk |
| 50–64 | **Tight Risk** — 0.5× sizing |
| ≥ 65 + health ≥ 70 | **Allowed** |

**China overlay (SQ3)** — does **not** block BTC by itself when Global ≥ 50, but flags caution:

| SQ3 | TC behavior |
|-----|-------------|
| Not computed | Prompt to enter China dimensions or import CHINA POLICY EXPORT |
| &lt; 50 | **`chinaCaution = true`** · gate label becomes *Allowed · China Caution* or *Tight + China Caution* · dual-track impairment message |
| 50–64 | Monitor China transmission — unlock hints in gate drawer |
| ≥ 65 | Constructive China track — *Dual-track aligned* when Global also ≥ 65 |

**Critical rule:** Global &lt; 50 **always** blocks BTC regardless of SQ3. SQ3 &lt; 50 can impair the **combined** read when Global looks fine — e.g. Global 80 + SQ3 35 → BTC modules technically allowed but mission surfaces show **SQ3 constraint** suffixes.

### 6.3 Mission surfaces (all 5 nodes)

When SQ3 is Impaired / Mixed / Fragile, each mission tactical banner appends a muted suffix:

```
· SQ3 {score} constraint
```

Implemented in `buildMissionChinaSuffix()` — keeps China impairment visible on **Basis, Credit, Liquidity, Breadth, Highbeta** without polluting the primary RV lead sentence.

### 6.4 Coverage & impairment driver

- **Coverage checklist** — China ladder weakness feeds dictionary audit when SQ3 &lt; 65
- **`resolveImpairmentDriver()`** — when both Global &lt; 50 and SQ3 &lt; 50, names which track is *more* impaired (larger delta below 50)
- **Hydration audit** — `china.sq3_score`, `china.policy_strength`, etc. field-by-field in [hydration_log.json](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/data/hydration/hydration_log.json)

### 6.5 WTM EXPORT handoff

SQ3 ships in every locked export:

```
SQ3 Score: 35
SQ3 Band: Impaired
Policy Strength: 50
State Impulse Score: 0
Growth Impulse Score: 0
China Regime Tag: desk-auto
```

Specs: [WTM EXPORT v2.1](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.1_SPEC.md) · [v2.2](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/whinfell_pipeline/WTM_EXPORT_v2.2_SPEC.md)

---

## 7. Unique edge — why SQ3 exists

### 7.1 Dual-track independence

Most desks collapse China into a single global risk score. Whinfell **refuses to**:

- China policy transmission is a **separate stochastic process** from US credit/breadth/basis
- A strong Global Whinfell day (e.g. 80) can coexist with **impaired China SQ3** (e.g. 35) — the console surfaces both instead of averaging them away

### 7.2 Signed state-control dimension

The **State Impulse** axis (−100 … +100, inverted into the composite) encodes something standard “policy sentiment” scores miss:

> *Policy can be loud (high Policy Strength) while execution is clamped (high State Control) — mid-50s SQ3 is the designed output, not a bug.*

That maps to recurring desk experience: industrial policy acceleration + tight SOE/platform oversight = constructive headlines, impaired transmission.

### 7.3 Auditable, single-edit weights

All weights and bands live in one Python module (`sq3.py`). Changes require:

1. Edit `WEIGHT_*` or `INTERPRETATION_BANDS`
2. Run `china_policy_track/tests/test_sq3.py`
3. Verify TC JavaScript constants match (`SQ3_WEIGHT_POLICY`, etc.)

No hidden ML. No retraining. G-Quant can reproduce any session score from three integers.

### 7.4 Git-isolated from Global C1

SQ3 lives in `china_policy_track/` — **explicitly isolated** from Global Credit Confirmation Score ([C1 doc](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/04_Score_Calculation/Whinfell_Credit_Confirmation_Score_Logic.md)). China credit *ladder* stages use separate proxies (KHYB, CSI300, HSTECH); SQ3 does not double-count HY OAS confirmation.

### 7.5 Two-layer China read

| Layer | What it measures |
|-------|------------------|
| **SQ3 policy score** | Policy + state + growth **impulse** (slow-moving policy stance) |
| **China ladder + handicap** | **Tracer horizon marks** on five stages, discounted by SQ3 |

Operator sees: *“Policy impaired (SQ3 35) but liquidity stage horizon marks are improving”* — actionable tension, not a single blended number.

### 7.6 Agent-safe handoff

SQ3 + three components export in WTM EXPORT and `grok_payload`. TempLibby / Perplexity / G-Quant can reason on **the same integers** the UI shows — no screenshot OCR, no reinterpretation.

---

## 8. Operator checklist

| Step | Action |
|------|--------|
| 1 | Enter or import **Policy Strength**, **State Impulse**, **Growth Impulse** |
| 2 | Confirm **Computed SQ3** + band chip in China Track panel |
| 3 | Open **Explain** on SQ3 card — verify component story matches desk read |
| 4 | Check command bar — SQ3 line + gate label (*China Caution* if &lt; 50) |
| 5 | Walk one mission node — look for `· SQ3 N constraint` suffix when impaired |
| 6 | Review China ladder — raw vs **final (adj.)** after SQ3 handicap |
| 7 | On hydrate — confirm `bundle.china.sq3_score` matches TC (audit log) |

---

## 9. Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| SQ3 shows **—** | Missing any of three inputs | Enter all three or import CHINA POLICY EXPORT |
| SQ3 **35** with policy 50 / state 0 / growth 0 | Growth defaulting to 0 in CSV | Re-export China policy with growth fields populated |
| SQ3 differs after import vs manual | Bundle used `manual` source with sparse china block | Re-run AM chain with fresh `china_policy_*.csv` |
| Global green but all nodes show SQ3 suffix | SQ3 &lt; 50 or Mixed/Fragile band | Expected — dual-track impairment, not UI bug |
| Python vs TC score mismatch | Stale TC cache or edited weights in one layer only | Run `test_sq3.py`; verify JS weights match `sq3.py` |

---

## 10. Code & test links

| Asset | GitHub |
|-------|--------|
| SQ3 engine (Python) | [china_policy_track/sq3.py](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/sq3.py) |
| China ladder + handicap | [china_policy_track/china_ladder.py](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/china_ladder.py) |
| Unit tests | [china_policy_track/tests/test_sq3.py](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/china_policy_track/tests/test_sq3.py) |
| TC calculator | [Whinfell_Transmission_Control.html](https://github.com/clark-cmyk/Whinfell_BUILD_Cousins/blob/main/08_Deliverables/Whinfell_Transmission_Control.html) — `calculateSq3`, `deriveGate` |
| Live desk | [Pages preview](https://clark-cmyk.github.io/Whinfell_BUILD_Cousins/) |

**Raw (agents):** [sq3.py raw](https://raw.githubusercontent.com/clark-cmyk/Whinfell_BUILD_Cousins/main/china_policy_track/sq3.py)

---

*Whinfell SQ3 Reference v1.0 — for G-Quant, TempLibby, Comet, Perplexity, and desk operators.*