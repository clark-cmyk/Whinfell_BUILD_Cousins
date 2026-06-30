# /goal — Funds Flow Sponsorship Layer

**Project:** Whinfell Transmission Control  
**Track:** BUILD Cousins · Phase 2b  
**Date:** June 29, 2026  
**Ingest:** Option D (Hybrid) — **locked**  
**Implementation authority:** [Phase2_Flows_Implementation_Spec.md](../01_Strategy_Docs/Phase2_Flows_Implementation_Spec.md)

---

## Goal statement

Add a **Funds Flow Sponsorship** subsystem to each node cockpit so the operator can judge whether a node-level move is **sponsored by allocator flows** (% AUM), not price action alone — without displacing score, transmission, gate, or shock as primary authority.

**Gate:** Implementation spec v1.0 **desk-locked** → then PR-1 + PR-3a start.

---

## Success criteria

### Data / pipeline (L1 sidecar + L2 node block)

- [ ] `funds_flow_baskets` + `funds_flow_thresholds` in Master DD (PR-1)
- [ ] `data/flows/v1/latest_flows.json` written from `flows_{YYYYMMDD}_{HHMM}.csv` (PR-3a)
- [ ] Credit cross-section fallback patches 1D only when flows file absent (PR-3b)
- [ ] Each `node_cockpit.funds_flows` built by `funds_flows.py` with `degrade_mode` set correctly
- [ ] `% AUM` canonical; `flow_pct_aum_5d` = sum of last 5 daily % AUM (not average)
- [ ] `basket_role` (`primary` / `supporting` / `proxy`) + `asset_id` link to `canonical_assets`
- [ ] Verdict ∈ `{supportive, neutral, mixed, diverging}`; caps in `fallback_1d_credit` mode
- [ ] `confidence_delta` (−1/0/+1) applied to node tier — **not** composite score or gate
- [ ] Hydration bundle **v1.2.0** with optional `flows_sidecar` metadata block
- [ ] Tests: `test_funds_flows.py`, parser fixture from `WTM-Flows-Global.csv`

### UI (PR-4)

- [ ] `FundsFlowSponsorshipCard` in right rail; reads `cockpit.funds_flows` only
- [ ] Degrade banner verbatim: `5D flows unavailable — using 1D Credit cross-section fallback.`
- [ ] Credit + Breadth worked examples match spec §2.2–2.3
- [ ] Compare + fullscreen variants per implementation spec §2.4

### Export (PR-5)

- [ ] NODE COCKPIT block includes Funds Flow Verdict / 5D / Summary lines
- [ ] Omit 5D lines when `degrade_mode: fallback_1d_credit`

---

## Non-goals

- Flows as command-bar authority
- Heatmaps, gate override, browser CSV parse
- 5D synthesis from credit cross-section alone
- WhinSig code merge

---

## Definition of done

1. Spec [Phase2_Flows_Implementation_Spec.md](../01_Strategy_Docs/Phase2_Flows_Implementation_Spec.md) signed off (§7 checklist)
2. `pytest whinfell_pipeline/tests/test_funds_flows.py` PASS
3. Hydrate v1.2.0: `node_cockpits.credit.funds_flows` populated from flows fixture
4. TC card renders with degrade_notice when fallback active

---

## Authority hierarchy (locked)

```
1. Whinfell Score + Transmission + Gate + Shock
2. Node composite_score + directional / RV
3. funds_flows.verdict + interpretation (confirmation only)
```

---

## /roles (BUILD Cousins ownership)

| Role | PR ownership |
|------|----------------|
| **Blueprint** | Spec lock, Phase2 cockpit §9.1, WTM export copy |
| **Bridge** | PR-1 registry, PR-2 `funds_flows.py`, node_cockpits wire |
| **Integration Dynamo** | PR-3a parser, PR-3b fallback, batch_collect hook, normalize |
| **Clarity** | PR-4 `FundsFlowSponsorshipCard` |
| **Clark** | WTM-Flows Koyfin view expansion, desk drops `flows_*.csv` |
| **TempLibby** | Sign-off §7 review checklist |