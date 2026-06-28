# China Policy Track — Data Dictionary v1.0.0

**Track ID:** `china_policy`  
**Schema version:** `1.0.0`  
**Export format:** `CHINA POLICY EXPORT v1.0`  
**Storage:** `data/china_policy/v1/china_policy_observations.parquet`  
**Global track storage (unchanged):** `data/global/` — China module never writes here.

---

## Overview

The China Policy track captures three dimensions per observation. Each observation is versioned, source-tagged, and stored in an isolated Parquet file alongside (not inside) Global track data.

| Dimension | Model class | Purpose |
|-----------|-------------|---------|
| Policy Hierarchy & Strength | `PolicyHierarchyStrength` | Where policy is set and how strong directives are |
| State Control Impulse | `StateControlImpulse` | Regulatory / state intervention direction |
| Growth & Market Impulse | `GrowthMarketImpulse` | Growth and market liquidity impulse read |

Top-level record: `ChinaPolicyObservation`

---

## Dimension 1: Policy Hierarchy & Strength

| Field | Type | Domain | Description |
|-------|------|--------|-------------|
| `hierarchy_level` | string | `central`, `provincial`, `sectoral`, `mixed` | Dominant policy-setting level |
| `policy_strength` | int | 0–100 | Strength of active policy directives |
| `dominant_theme` | string | free text | Primary policy theme (e.g. fiscal support) |
| `supporting_signals` | list[str] | — | Confirming policy signals |
| `notes` | string | — | Operator/research notes |

### Example (Python)

```python
from datetime import datetime, timezone
from china_policy_track.models import PolicyHierarchyStrength, build_observation_from_dimensions

policy = {
    "hierarchy_level": "central",
    "policy_strength": 74,
    "dominant_theme": "targeted fiscal support",
    "supporting_signals": ["PBoC guidance", "State Council measures"],
    "notes": "Central directives emphasize quality growth.",
}
ph = PolicyHierarchyStrength.from_mapping(policy)
assert ph.policy_strength == 74
```

---

## Dimension 2: State Control Impulse

| Field | Type | Domain | Description |
|-------|------|--------|-------------|
| `impulse_score` | int | -100..100 | Positive = more state control |
| `regulatory_direction` | string | `tightening`, `neutral`, `easing` | Direction of regulation |
| `state_intervention_level` | string | `low`, `medium`, `high` | Intervention intensity |
| `key_controls` | list[str] | — | Active control mechanisms |
| `notes` | string | — | Notes |

### Example

```python
from china_policy_track.models import StateControlImpulse

state = {
    "impulse_score": 38,
    "regulatory_direction": "tightening",
    "state_intervention_level": "high",
    "key_controls": ["SOE credit guidance", "platform oversight"],
}
sc = StateControlImpulse.from_mapping(state)
assert sc.regulatory_direction == "tightening"
```

---

## Dimension 3: Growth & Market Impulse

| Field | Type | Domain | Description |
|-------|------|--------|-------------|
| `growth_impulse_score` | int | 0–100 | Growth impulse strength |
| `market_sentiment` | string | `constructive`, `mixed`, `impaired` | Equity/credit sentiment |
| `liquidity_impulse` | string | `expanding`, `stable`, `contracting` | Liquidity direction |
| `key_indicators` | list[str] | — | Supporting indicators |
| `notes` | string | — | Notes |

### Example

```python
from china_policy_track.models import GrowthMarketImpulse

growth = {
    "growth_impulse_score": 61,
    "market_sentiment": "mixed",
    "liquidity_impulse": "stable",
    "key_indicators": ["credit impulse", "PMI new orders"],
}
gm = GrowthMarketImpulse.from_mapping(growth)
assert gm.liquidity_impulse == "stable"
```

---

## Top-Level Observation

| Field | Type | Description |
|-------|------|-------------|
| `track_id` | string | Always `china_policy` |
| `schema_version` | string | e.g. `1.0.0` |
| `observation_id` | string | Unique observation key |
| `as_of` | datetime (UTC) | Observation timestamp |
| `source` | string | `perplexity`, `koyfin`, `barchart`, `manual` |
| `policy_hierarchy_strength` | struct | Dimension 1 |
| `state_control_impulse` | struct | Dimension 2 |
| `growth_market_impulse` | struct | Dimension 3 |

---

## CHINA POLICY EXPORT v1.0 (Perplexity handoff)

Mirrors the Global track `WTM EXPORT v2.0` label-block pattern:

```
--- CHINA POLICY EXPORT v1.0 ---
Observation ID: china-2026-06-27-01
Timestamp: 2026-06-27T10:15:00
Source: perplexity
Policy Hierarchy Level: central
Policy Strength: 74
Dominant Policy Theme: targeted fiscal support
Policy Supporting Signals: signal1, signal2
Policy Notes: ...
State Control Impulse Score: 38
Regulatory Direction: tightening
State Intervention Level: high
Key State Controls: control1, control2
State Control Notes: ...
Growth Impulse Score: 61
Market Sentiment: mixed
Liquidity Impulse: stable
Key Growth Indicators: ind1, ind2
Growth Notes: ...
```

---

## Parquet Schema

Nested struct columns per dimension. File metadata includes `track=china_policy` and `schema_version=1.0.0`.

Coexistence rule: **only** `data/china_policy/**` is written by this module. Global track files under `data/global/` are never read or modified.

---

## Ingestion

```bash
# From Perplexity text export
python3 -m china_policy_track.ingest --input china_policy_track/examples/sample_perplexity_export.txt

# From Koyfin/Barchart JSON export
python3 -m china_policy_track.ingest --input china_policy_track/examples/sample_koyfin_export.json
```

Pipeline: `parse_input` → `ChinaPolicyObservation` → `write_observations` → Parquet.

---

## Module Layout

| File | Role |
|------|------|
| `version.py` | Track/schema/export version constants |
| `models.py` | Data classes + normalization |
| `schema.py` | PyArrow Parquet schema |
| `data_parser.py` | Perplexity + dict export parsers |
| `storage.py` | Parquet read/write (China paths only) |
| `ingest.py` | CLI entry point |