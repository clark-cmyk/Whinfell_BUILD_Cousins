# Whinfell Daily Data Update — Simple Guide (Clark)

**For:** Clark and anyone who wants the desk updated without reading code  
**One-click tool:** `Whinfell_Daily_AM.command` (or **Whinfell Daily AM** app on Desktop)  
**Updated:** 2026-06-28

---

## The whole day in one picture

```text
  PERPLEXITY (morning)          YOU (one click)              YOU (2 minutes in browser)
  ───────────────────          ───────────────              ──────────────────────────
  Download 8 CSV files    →    Run Whinfell Daily AM   →    Import → Review → Save
  into whinfell_drop           (automatic)                  in Transmission Control
```

You do **not** rename files, run terminal commands, or parse spreadsheets. Perplexity does the downloads; your Mac does the rest.

---

## Part 1 — Before you click (Perplexity’s job)

**Ask Perplexity once each morning** (paste the prompt from `Perplexity_Full_Collection_Prompt.txt` if needed):

> “Run the Whinfell fast collect: export the 8 Koyfin and Barchart screens to **whinfell_drop**, then run the batch tool and send me the collect report.”

**What you need before your one-click:**

| Check | What it means |
|-------|----------------|
| Files in **whinfell_drop** | Folder: `Downloads` → `whinfell_drop` — should have today’s CSV files |
| Perplexity report says **Success** | `hydration_bundle: data/hydration/latest.json` |
| **files_staged** is not zero | Pipeline actually picked up the exports |

**If whinfell_drop is empty:** don’t click yet — send Perplexity back to export.

**Perplexity is NOT allowed to:** trade, change risk, guess Whinfell scores, or rename your files.

---

## Part 2 — Your one-click morning (Clark)

### Step 1 — Double-click

On your Desktop (or in the project folder):

**`Whinfell_Daily_AM.command`**

A small window opens: **Whinfell Daily Launcher — AM**

### Step 2 — One button

Click the blue button:

**Run Whinfell Daily AM**

Wait until **Status** turns green: **Success**

- While it runs, the log scrolls — that’s normal.  
- Takes about **30 seconds to 2 minutes** if files are already in `whinfell_drop`.

### Step 3 — Transmission Control opens automatically

When the run finishes, your browser opens **Transmission Control**.

**If it doesn’t open:** double-click `Whinfell_Transmission_Control.command`

---

## Part 3 — Three clicks in Transmission Control

Do this every morning after a successful AM run:

| # | What to click | What you’re doing |
|---|---------------|-------------------|
| 1 | **Import Latest Hydration Bundle** | Load today’s data |
| 2 | Pick `latest.json` if asked | File lives in `data/hydration` (launcher can open that folder) |
| 3 | Review amber **Suggested Tracer** panel | **Accept** if marks look right · **Dismiss** if not |
| 4 | **Save State** | Locks the desk read for the day |

**Optional:** Open **Deep Dive** from the link in Transmission Control to see the full ladder and score math.

---

## Part 4 — End of day (optional one-click)

Double-click:

**`Whinfell_Daily_EOD.command`**

Click **Run Whinfell Daily EOD**

Then in Transmission Control:

1. Update handover / watch items  
2. **Save State** again  
3. Confirm gate and gross risk for tomorrow  

---

## Handy buttons on the launcher

| Button | Use when |
|--------|----------|
| **Open Hydration Folder** | You need to find `latest.json` |
| **Open Project Folder** | You need the repo on Desktop |

---

## When something goes wrong (plain English)

| What you see | What to do |
|--------------|------------|
| **Error** (red) on launcher | Open `Desktop/whinfell_launcher.log` or ask Perplexity to re-export and try again |
| “No bundle imported” in TC | AM run didn’t finish — re-run **Whinfell Daily AM** |
| Amber tracer looks wrong | **Dismiss** suggestions · fix marks manually · **Save State** |
| whinfell_drop empty | Perplexity didn’t export yet — not your one-click’s fault |
| Score feels stale | Re-run AM after fresh exports |

**Rule of thumb:** Fix the **folder** first (exports), then click **AM** again, then **Import**.

---

## What Perplexity does vs what you do

| Task | Perplexity | Clark |
|------|------------|-------|
| Open Koyfin / Barchart and download CSVs | ✓ | |
| Save to whinfell_drop | ✓ | |
| Run the processing pipeline | ✓ (or AM button does it) | ✓ **one click** |
| Import hydration in Transmission Control | | ✓ |
| Accept / Dismiss tracer | | ✓ |
| Save State | | ✓ |
| Trade or change risk | ✗ | ✓ (you only) |

---

## Research during the day (Perplexity, separate task)

When you want regime narrative or sizing text — **not** part of the one-click:

- **Prompt A** — morning regime read  
- **Prompt B** — sizing / gross risk  
- **Prompt C** — rank trade ideas  
- **Prompt D** — income outlook  
- **Prompt E** — “tape vs model” divergence  

Paste blocks from `Comet_Browser_Operations_Blueprint.md` (Saved Prompts section).  
These **do not** replace the morning CSV + one-click update.

---

## Clark’s 60-second morning checklist

```text
□ Perplexity: files in whinfell_drop + short report
□ Double-click Whinfell_Daily_AM.command
□ Click Run Whinfell Daily AM → Success
□ Transmission Control → Import Latest Hydration Bundle
□ Accept or Dismiss tracer → Save State
□ Glance at gate + weakest link → go
```

---

## File cheat sheet (no paths to memorize)

| What | Where to double-click |
|------|------------------------|
| **Morning one-click** | `Whinfell_Daily_AM.command` |
| **End-of-day** | `Whinfell_Daily_EOD.command` |
| **Operator console** | `Whinfell_Transmission_Control.command` |
| **Ladder deep dive** | `Whinfell_Transmission_Ladder_Deep_Dive.command` |
| **Today’s data file** | Launcher → **Open Hydration Folder** → `latest.json` |
| **Perplexity morning prompt** | `08_Deliverables/Perplexity_Full_Collection_Prompt.txt` |

---

## Technical guide (only if you want it)

Full pipeline detail, troubleshooting, and agent roles:

`08_Deliverables/Whinfell_Data_Update_Guide.md`

---

*Your workflow: Perplexity fills the folder · You click AM once · You import and save in Transmission Control.*