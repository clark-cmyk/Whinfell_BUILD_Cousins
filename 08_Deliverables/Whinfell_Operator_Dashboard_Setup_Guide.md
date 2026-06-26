# Whinfell Operator Dashboard — Setup Guide

**Deliverable:** C4.5  
**Main file:** `Whinfell_Operator_Dashboard.html`  
**Version:** 1.0 (No-iframe Control Surface — Signed Off June 26, 2026)  
**Lead:** Bridge (Edge, Forge Master, Clarity)

---

## Open Daily (Desk Command)

```bash
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Operator_Dashboard.html
```

Or double-click the file in Finder. Bookmark in Chrome/Edge for one-click access.

---

## What This Is

**Control surface** for Whinfell desk operations — no embedded iframes:

| Zone | Width | Content |
|------|-------|---------|
| Left | ~60% | Koyfin status panel → **Open Live Koyfin** |
| Right | ~40% | Barchart status panel → **Open Live Barchart** |
| Bottom | Full | Prompts · 5-min workflow · Gross Risk |

**Workflow:** Open this dashboard → click **Open Live Koyfin** + **Open Live Barchart** (dedicated tabs) → read data in those tabs, run prompts and update risk here.

---

## First-Time Setup (~2 min)

1. Paste **Koyfin Whinfell workspace URL** in the URL Settings bar  
2. Paste **Barchart futures/basis URL** in the right field  
3. Click **Save Settings** (persists in browser localStorage)  
4. Click **Open Live Koyfin** and **Open Live Barchart** — arrange side-by-side or on second monitor  
5. Keep all three windows open during the session

---

## 5-Minute Morning Workflow

| Min | Action |
|-----|--------|
| 1 | Open Live Koyfin → Transmission State + Whinfell Score |
| 2 | Scan Liquidity, Rates, Credit Confirmation (Koyfin tab) |
| 3 | Open Live Barchart → Futures Leadership + Basis Edge |
| 4 | Copy Prompts ① + ② to agent (bottom panel) |
| 5 | Update Gross Risk + posture (bottom panel) |

**Daily Rule:** Update Gross Risk after morning review and after any material trade.

---

## Bottom Panel Tabs

- **5-Min Morning Workflow** — checklist  
- **Saved Agentic Prompts (6)** — copy-paste  
- **Gross Risk Controls** — Book A/B, score, handover  
- **Quick Tickers** — C3 master list shortcuts  
- **Setup Help** — detailed instructions

---

## Architecture Note

v1.0 uses a **no-iframe control surface**. Koyfin and Barchart block embedding; live sites open in dedicated browser tabs. This dashboard holds URLs, timestamps, workflow, prompts, and risk controls — always functional.

---

## References

- `08_Deliverables/C3_Whinfell_Series_Ticker_Master_List.md`
- `08_Deliverables/C1_Whinfell_Credit_Confirmation_Score_Logic.md`
- `08_Deliverables/C2_Whinfell_Credit_Score_Fallback.xlsx`