# Whinfell Operator Dashboard — Setup Guide

**Deliverable:** C4.5 v1.1  
**Main file:** `Whinfell_Operator_Dashboard.html`  
**Version:** 1.1 (WTM Action Layer)  
**Lead:** Bridge (Edge, Precision support)

---

## Open Daily

```bash
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Operator_Dashboard.html
```

---

## C4.5 v1.1 — WTM Action Layer

| Zone | Content |
|------|---------|
| Left (~60%) | Koyfin status panel → Open Live Koyfin |
| Right (~40%) | Barchart status + **BTC Options (L2)** + **Calendar Arb (L3)** cards |
| WTM Intake | Score, Transmission State, Regime Tag, Gate Status (auto) |
| Bottom tabs | 5-Min Workflow · WTM Prompts A–E · Gross Risk |

---

## WTM Intake & Gate Logic

| Field | Source |
|-------|--------|
| Whinfell Score | Koyfin (0–100) |
| Transmission State | Normal / Stressed / Disorderly / Crisis |
| Regime Tag | Free text or preset (datalist) |
| Gate Status | **Auto-calculated** |

### Gate Rules

| Score | Gate Status | Banner | BTC Cards |
|-------|-------------|--------|-----------|
| **&lt; 50** | NO NEW BTC RISK | Red | Disabled |
| **50–64** | Tight Risk Band | Amber | Allowed — reduced sizing |
| **≥ 65** | Allowed | Green | Full access |

---

## BTC Cards (Right Pane — Barchart Area)

1. **BTC Options Workflow (WTM Layer 2)** — copy Layer 2 prompt
2. **BTC Calendar Arb Agent (WTM Layer 3)** — copy Layer 3 prompt

Both cards show **BLOCKED** or **ALLOWED** from gate status.

---

## WTM Prompts A–E

| Prompt | Title |
|--------|-------|
| A | WTM Transmission Read & Regime Classification |
| B | WTM Posture & Gross-Risk Recommendation |
| C | WTM Trade Evaluation & Ranking |
| D | WTM Income Projection from Current Book |
| E | WTM Divergence & Risk Compression |

Click **Copy** on any prompt → paste to agent.

---

## Persistence

**Save Settings** stores all fields to `localStorage` key `whinfell_operator_v1_1`. Migrates from v1/v2 automatically.