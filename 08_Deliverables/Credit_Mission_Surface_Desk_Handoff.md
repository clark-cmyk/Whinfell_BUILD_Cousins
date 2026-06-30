# Credit Mission-Surface — Desk Handoff Note

**Build:** `2.2-MISSION-2026-06-29` · **Console:** `Whinfell_Transmission_Control.html`  
**Audience:** Operators already using the Basis mission-surface · **Status:** v1 accepted — desk testing before Liquidity

---

## Open Credit — what to check first

Same cockpit shell as Basis; eyebrow reads **“Credit mission read.”**

| Zone | What you should see |
|------|---------------------|
| **Tactical lead** (`#basisTacticalSentence`) | One RV + gate sentence — **not** the raw band. Example: *“HY OAS proxy is cheap vs history; long spread is allowed, but only at 0.5× under Tight Risk.”* |
| **Tactical suffix** (muted line below, when material) | Short SQ3 constraint only — e.g. *“· SQ3 35 constraint”*. **Not** in the lead line. |
| **Summary strip** | Primary reading in **bps** (HY OAS proxy), stance row (Q · percentile · n), preferred expression + size cap |
| **Implication rail** | Compact chips — see validation below |
| **RV chart** | Generic quartile bars (no Basis-style ref bands) |
| **Shared (unchanged)** | Hydration & Coverage banner · gate decision sentence · post-import checklist · funds-flow card in diagnostics drawer |

---

## Validate key behaviors

### Composite fallback (empty `component_inputs`)

Credit often runs on **horizon-net fallback**, not C1-weighted components.

- **Rail:** **Composite fallback** chip appears **instead of** the band chip (e.g. not “Blocked”).
- **Full diagnostics → Signal:** Chip reads **horizon-net fallback**; copy states composite is from horizon-net fallback, not C1-weighted components.
- **Do not treat** an empty component list as “score complete.”

### Signal band vs RV tension

Fixture can show band **Blocked** while RV reads **cheap** and posture **long spread**.

- **Tactical lead must follow RV + gate**, not the band.
- Band context lives in diagnostics, not the mission lead.

### Gate: Tight Risk + China caution

With Whinfell ~50 and impaired/mixed SQ3 (China inputs populated):

- **Rail gate chip:** **Tight + China Caution** (not generic “Tight Risk” alone).
- **Gate block (diagnostics drawer):** Full gate decision sentence with China ladder / SQ3 and Credit RV sizing language.
- **Tactical suffix:** SQ3 constraint line when SQ3 band is impaired, fragile, or mixed.
- **China constraint** is carried by the **gate chip + gate sentence**; the lead line stays RV-focused.

### Weakest link

When Credit is transmission weakest link:

- **Weakest link** chip appears on the **implication rail only** — not in the tactical banner.
- Node rail tab should also show weakest indicator (existing behavior).

### Flows sponsorship

With flows `ok` in bundle: **Supportive** (or neutral) flows chip; funds-flow card inside **Full diagnostics**.

---

## v1 limitations (desk awareness)

1. **Mission-surface nodes:** Credit and Basis only — Liquidity, Breadth, High Beta still use the legacy expanded decision rail.
2. **Shared DOM/CSS:** Tactical banner IDs/classes still use `basis-*` prefix; content switches per node.
3. **No pipeline change:** Scoring, hydration, and `horizon_net_fallback` logic unchanged — presentation only.
4. **Credit chart:** No calendar ref bands; HY OAS uses **higher_is_cheaper** richness semantics.
5. **Composite score:** Until ARCH-1 live components ship, Credit composite may stay on horizon-net fallback even when RV/flows look constructive.
6. **Badge frozen** at `2.2-MISSION-2026-06-29` for this release.

---

## Recommended first test cases

Use **Import Latest Hydration Bundle** with `whinfell_pipeline/examples/cockpit_hydration_snippet.json` (or desk `data/hydration/latest.json` after morning chain).

| # | Test | Expected on Credit |
|---|------|-------------------|
| 1 | Import bundle → select **Credit** | Mission banner visible; reading ~**339 bps**; RV **cheap** / Q4 |
| 2 | Implication rail | Chips: **Composite fallback** · **Long spread** · **Supportive** · **Tight + China Caution** · **Weakest link** |
| 3 | Tactical lead vs band | Lead mentions **cheap** + **long spread** + **0.5×**; does **not** open with “Blocked” |
| 4 | Full diagnostics | Signal shows **horizon-net fallback**; funds-flow card present; gate sentence populated |
| 5 | China / SQ3 suffix | Set Policy 50 / State 0 / Growth 0 (or import bundle with SQ3 ~35) → suffix line appears; gate chip stays **Tight + China Caution** |
| 6 | Contrast Basis | Switch to Basis — mission shell matches; eyebrow **Basis mission read**; band chip (not Composite fallback) |
| 7 | Contrast Liquidity | Switch to Liquidity — **no** mission tactical banner; legacy diagnostic cards in right rail |

**Pass criteria for desk sign-off:** Tests 1–4 pass on the hydration fixture; 5–7 confirm node-specific behavior and no regression on Basis.

---

## Pause point

Node development **pauses** after this handoff. Collect desk notes in `Desk_Feedback_Log.md` before extending mission-surface to Liquidity.

**Open console:**
```bash
open ~/Desktop/Whinfell_BUILD_Cousins/08_Deliverables/Whinfell_Transmission_Control.html
```

**Import test bundle:**
```bash
# After morning chain, or use snippet directly:
# whinfell_pipeline/examples/cockpit_hydration_snippet.json
```