# /goal — Funds Flow Sponsorship Layer

**Project:** Whinfell Transmission Control  
**Track:** BUILD Cousins · Phase 2b  
**Date:** June 29, 2026

---

## Goal statement

Add a **Funds Flow Sponsorship** subsystem to each node cockpit so the operator can judge whether a node-level move is **sponsored by allocator flows** (% AUM), not price action alone — without displacing score, transmission, gate, or shock as primary authority.

---

## Success criteria

### Data / pipeline

- [ ] `funds_flow_baskets` registered in Master DD with ETF mapping for all 5 nodes
- [ ] Each `node_cockpit` in hydration bundle includes `funds_flows` block when Koyfin flow inputs present
- [ ] `% AUM` is canonical; 1D and 5D cumulative computed deterministically
- [ ] Verdict ∈ `{supportive, neutral, mixed, diverging}` with stable thresholds in YAML
- [ ] `confidence_delta` (−1/0/+1) applied to node conviction — **not** composite score or gate
- [ ] Graceful degrade: `funds_flows.enabled: false` when inputs missing; cockpit still valid
- [ ] Unit tests cover aggregate, verdict, divergence overlay, and per-node baskets

### UI (Phase 2 cockpit rail)

- [ ] `FundsFlowSponsorshipCard` renders in **right rail** below driver checklist
- [ ] Operator answers in <2s: sponsorship? persistent? confirms or contradicts?
- [ ] Visual treatment: institutional, calm, tabular nums, no heatmaps
- [ ] Compare mode: one compact card per node, synchronized horizon
- [ ] Full-screen “Here’s Why”: sponsorship section subordinate to node rationale

### Export / round-trip

- [ ] Flow verdict + 5D aggregate exportable in WTM block (v2.2 addendum or v2.3)
- [ ] Rationale / change-mind text derives from same deterministic logic as UI

---

## Non-goals (this goal)

- Flows as top-level command-bar authority
- Flashing alerts, oversized charts, or global flow heatmap
- Options flow or futures flow (ETF % AUM only for MVP)
- Replacing WhinSig — may reuse column patterns, not merge codebases
- Auto-trading or gate override from flow signals

---

## Definition of done

1. `python3 -m pytest whinfell_pipeline/tests/test_funds_flows.py` PASS  
2. Hydrate produces `node_cockpits.*.funds_flows` with real credit-export flow columns (or fixture)  
3. TC renders card in node cockpit view with verdict + 3–5 ETF rows  
4. BUILD TODO + Progress Log updated; design doc locked at v1.0  

---

## Authority hierarchy (locked)

```
1. Whinfell Score + Transmission + Gate + Shock   ← primary
2. Node composite_score + directional / RV        ← node verdict
3. funds_flows.verdict + interpretation           ← confirmation only
```