# Fast CSV Collect — Perplexity & Comet

**Start here for agents:** [`Perplexity_Comet_Collection_Instructions.md`](Perplexity_Comet_Collection_Instructions.md)  
**Paste prompt:** `whinfell_pipeline/examples/AGENT_COLLECTION_PROMPT.txt`  
**Wired URLs:** `whinfell_pipeline/desk_urls.yaml`

**Problem:** Browser agents are slow when they download **one ticker at a time** (40–65 clicks).  
**Fix:** **8 bulk exports** from saved Koyfin/Barchart screens + automated rename/pipeline.

---

## The speed rule

| Slow (don't do daily) | Fast (do daily) |
|----------------------|-----------------|
| Loop BT1 → ER1 → … → VI*1 individually | Open 8 **saved views/screens** |
| Parse CSV in the agent | **Export only** — Python handles rename + stage |
| Save to `~/Downloads` | Save to **`~/Downloads/whinfell_drop`** |
| Rename files manually | `run_batch_collect.py normalize` |

---

## One-command morning (Clark or agent)

```bash
cd ~/Desktop/Whinfell_BUILD_Cousins
scripts/whinfell_morning_collect.sh
```

This will:

1. Open all batch URLs in the browser
2. Wait for exports in `whinfell_drop`
3. Auto-run normalize → stage → hydrate when ready

---

## Agent workflow (minimal human steps)

### Step 1 — Load the plan (read-only)

```bash
python3 run_batch_collect.py plan
```

Or use the frozen copy: `whinfell_pipeline/examples/comet_collection_plan.json`

### Step 2 — Export only (8 tabs)

For each step in the plan:

1. Open the URL (or use `python3 run_batch_collect.py open`)
2. Click **Export / Download CSV**
3. Save to `~/Downloads/whinfell_drop`

**Do not** read or transform CSV content in the browser.

### Step 3 — Run the tool (zero human rename)

```bash
python3 run_batch_collect.py run --window today
```

### Step 4 — Clark imports hydration

Transmission Control → **Import Latest Hydration Bundle**

---

## Commands reference

| Command | Purpose |
|---------|---------|
| `run_batch_collect.py plan` | JSON checklist for Comet/Perplexity |
| `run_batch_collect.py open` | Open all saved-view URLs (macOS) |
| `run_batch_collect.py normalize` | Rename vendor files → canonical names |
| `run_batch_collect.py status` | Are required files present? |
| `run_batch_collect.py watch --auto-run` | Poll drop dir, run pipeline when ready |
| `run_batch_collect.py fetch-api` | Barchart API (needs `BARCHART_API_KEY`) |
| `run_batch_collect.py run` | normalize + full daily chain |

---

## Optional: Barchart API (no browser)

If Clark has a Barchart OnDemand API key:

```bash
export BARCHART_API_KEY="your_key"
python3 run_batch_collect.py fetch-api
python3 run_batch_collect.py run
```

Fetches all 13 ticker historical series in parallel — seconds, not minutes.

---

## Paste into Comet / Perplexity

```
Whinfell FAST COLLECT mode — do not loop tickers.

1. Read whinfell_pipeline/examples/comet_collection_plan.json
2. Export each step URL to ~/Downloads/whinfell_drop (export only, no parsing)
3. Run: cd ~/Desktop/Whinfell_BUILD_Cousins && python3 run_batch_collect.py run
4. Report: files staged, quarantined, hydration path

NEVER download 13 tickers one-by-one unless Clark explicitly requests analytics archive.
```

---

## One-time setup (5 min)

1. Create saved Koyfin views per `Comet_Browser_Operations_Blueprint.md` §2
2. Create saved Barchart screens per §3
3. Paste view URLs into `whinfell_pipeline/collection_manifest.yaml` (or set env vars):
   - `KOYFIN_VIEW_RATES_URL`
   - `KOYFIN_VIEW_EQUITIES_URL`
   - `KOYFIN_VIEW_CREDIT_URL`
   - `BARCHART_SCREEN_INTRADAY_URL`
   - `BARCHART_SCREEN_DAILY_URL`

---

## Related docs

- `08_Deliverables/Perplexity_Barchart_Koyfin_Playbook.md` — vendor CSV formats
- `08_Deliverables/Comet_Browser_Operations_Blueprint.md` — saved view names
- `whinfell_pipeline/collection_manifest.yaml` — machine-readable manifest