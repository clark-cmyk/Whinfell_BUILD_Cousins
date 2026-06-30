# Whinfell Desk Comet Shortcuts

Supervised-mode morning collection contract for the Whinfell desk assistant.  
Aligned with: **Master Data Dictionary v1.0 (Locked)** · `whinfell_pipeline/collection_manifest.yaml` · `whinfell_pipeline/data_dictionary.yaml`  
**Updated:** 2026-06-30 · wired URLs from `whinfell_pipeline/desk_urls.yaml`

**Paste-ready Comet block (all Koyfin + all Barchart):** `08_Deliverables/Comet_Morning_Collect_Prompt.txt`

## Full URL reference — Koyfin (all desk views)

| View | Wired URL / navigation | Export | Target file |
|------|------------------------|--------|-------------|
| **home** | https://app.koyfin.com/ | — | — |
| **WTM-Rates-Credit** | My Dashboards → WTM-Rates-Credit · assist [USGG2Y10Y](https://app.koyfin.com/macro/USGG2Y10Y) [DGS10](https://app.koyfin.com/macro/DGS10) | ⋮ → Export → CSV | `rates_*` |
| **WTM-Equities-Breadth** | My Dashboards → WTM-Equities-Breadth · assist [IWM](https://app.koyfin.com/etf/IWM.US) [SPY](https://app.koyfin.com/etf/SPY.US) | ⋮ → Export → CSV | `equities_*` |
| **WTM-Import-Core** | https://app.koyfin.com/myw/70789aa7-8084-4e4c-85d3-09f9b78dcd3a | ⋮ → Export → CSV | `credit_*` |
| **WTM-Flows-Global** | https://app.koyfin.com/myw/afb1f314-4de4-47b6-b02f-0de2601b62b9 | ⋮ → Export → CSV | `WTM-Flows-Global.csv` → `flows_*` |
| **WTM-GOV-USPRC** | https://app.koyfin.com/myw/e94a97b3-600d-47d4-91d3-a01f8749146d | ⋮ → Export → CSV | `WTM-Flows-GOV-USPRC.csv` |
| **WTM-Credit-Confirmation** | My Dashboards → WTM-Credit-Confirmation · assist [HYG](https://app.koyfin.com/etf/HYG.US) [LQD](https://app.koyfin.com/etf/LQD.US) | ⋮ → Export → CSV | `credit_*` |
| **WTM-China-Policy** | My Dashboards → WTM-China-Policy · assist [KWEB](https://app.koyfin.com/etf/KWEB.US) [CSI300](https://app.koyfin.com/index/000300.SS) | ⋮ → Export → CSV | `china_policy_*` |
| **WTM-China-Liquidity** | assist [GCN10YR](https://app.koyfin.com/macro/GCN10YR) [USDCNH](https://app.koyfin.com/forex/USDCNH) | ⋮ → Export → CSV | ladder nav only |
| **WTM-China-Credit** | assist [KHYB](https://app.koyfin.com/etf/KHYB.US) [2829.HK](https://app.koyfin.com/etf/2829.HK) | ⋮ → Export → CSV | ladder nav only |
| **WTM-China-Breadth** | assist [CSI300](https://app.koyfin.com/index/000300.SS) [HSTECH](https://app.koyfin.com/index/HSTECH) [KWEB](https://app.koyfin.com/etf/KWEB.US) | ⋮ → Export → CSV | ladder nav only |
| **WTM-China-Cyclical** | assist [COPX](https://app.koyfin.com/etf/COPX.US) | ⋮ → Export → CSV | ladder nav only |
| **Whinfell-Daily-TimeSeries** | macro watchlist · assist [BTCUSD](https://app.koyfin.com/crypto/BTCUSD) [IBIT](https://app.koyfin.com/etf/IBIT.US) | Show table → Download Available Data | `koyfin_YYYY-MM-DD.csv` |
| **WTM-Crypto-Price** | assist [BTCUSD](https://app.koyfin.com/crypto/BTCUSD) | Show table → Download Available Data | `btc_price_chart_*` |
| **WTM-Crypto-Correl** | assist [BTCUSD](https://app.koyfin.com/crypto/BTCUSD) | Show table → Download Available Data | `btc_correl_chart_*` |
| **WTM-Crypto-Correl-ETH** | https://app.koyfin.com/crypto/ETHUSD | Show table → Download Available Data | `eth_correl_chart_*` |
| **WTM-Crypto-Correl-XRP** | https://app.koyfin.com/crypto/XRPUSD | Show table → Download Available Data | `xrp_correl_chart_*` |
| **WTM-Crypto-Correl-SOL** | https://app.koyfin.com/crypto/SOLUSD | Show table → Download Available Data | `sol_correl_chart_*` |
| **WTM-Crypto-Snapshot** | auto from credit export | ⋮ → Export → CSV (optional) | `crypto_snapshot_*` |

## Full URL reference — Barchart (all desk screens)

| Screen | Wired URL | Export | Target file |
|--------|-----------|--------|-------------|
| **home** | https://www.barchart.com/futures/major-commodities | — | — |
| **my_lists** | https://www.barchart.com/my/watchlist?viewName=197689 | — | — |
| **WTM-Futures-Intraday** | https://www.barchart.com/my/watchlist?viewName=197689 | Download CSV | `futures_intraday_*` |
| **WTM-Futures-Daily** | https://www.barchart.com/futures/quotes/BTM26/historical-download | Historical → Download | `futures_daily_*` |
| **WTM-BTC-Basis** | https://www.barchart.com/futures/quotes/BTM26/spreads | Download CSV | `btc_basis_*` |
| **WTM-Options-Greeks** | https://www.barchart.com/futures/quotes/BTN26/options | Download CSV | `options_*` / `greeks_*` |
| **WTM-China-Cyclical** | assist [HGK26](https://www.barchart.com/futures/quotes/HGK26) [SCO26](https://www.barchart.com/futures/quotes/SCO26) | Download CSV | ladder nav |
| **WTM-China-Basis** | https://www.barchart.com/futures/quotes/HGK26/spreads | Download CSV | ladder nav |
| **WTM-China-Futures-Daily** | https://www.barchart.com/futures/quotes/HGK26/historical-download | Historical → Download | ladder nav |

### ARCH-4 — WTM-Barchart-Core (16 symbols, optional)

Per symbol: quote page → Historical Data → Download CSV → `whinfell_drop`.  
API fast-path (Clark): `python3 run_batch_collect.py fetch-tickers` when `BARCHART_API_KEY` set.

| Symbol | URL |
|--------|-----|
| ^BTCUSD | https://www.barchart.com/crypto/quotes/%5EBTCUSD/historical-download |
| ^ETHUSD | https://www.barchart.com/crypto/quotes/%5EETHUSD/historical-download |
| ^XRPUSD | https://www.barchart.com/crypto/quotes/%5EXRPUSD/historical-download |
| ^SOLUSD | https://www.barchart.com/crypto/quotes/%5ESOLUSD/historical-download |
| IBIT | https://www.barchart.com/etfs-funds/quotes/IBIT/historical-download |
| GBTC | https://www.barchart.com/etfs-funds/quotes/GBTC/historical-download |
| SOFR | https://www.barchart.com/futures/quotes/SQ1!/historical-download |
| $HSI | https://www.barchart.com/stocks/quotes/%24HSI/historical-download |
| $VHSI | https://www.barchart.com/stocks/quotes/%24VHSI/historical-download |
| $VXHY | https://www.barchart.com/stocks/quotes/%24VXHY/historical-download |
| CBON | https://www.barchart.com/etfs-funds/quotes/CBON/historical-download |
| KHYB | https://www.barchart.com/etfs-funds/quotes/KHYB/historical-download |
| ASHR | https://www.barchart.com/etfs-funds/quotes/ASHR/historical-download |
| DXY00 | https://www.barchart.com/futures/quotes/DXY00/historical-download |
| GCY00 | https://www.barchart.com/futures/quotes/GCY00/historical-download |
| HGY00 | https://www.barchart.com/futures/quotes/HGY00/historical-download |

## Comet memorized shortcuts (all views)

Add in Comet → **Shortcuts** (trigger → open URL or paste action):

| Trigger | Action |
|---------|--------|
| `wtm morning` | Paste `Comet_Morning_Collect_Prompt.txt` |
| `wtm koyfin` | Open https://app.koyfin.com/ |
| `wtm koyfin rates` | Open WTM-Rates-Credit (dashboard) |
| `wtm koyfin equities` | Open WTM-Equities-Breadth |
| `wtm koyfin import` | Open https://app.koyfin.com/myw/70789aa7-8084-4e4c-85d3-09f9b78dcd3a |
| `wtm koyfin flows` | Open https://app.koyfin.com/myw/afb1f314-4de4-47b6-b02f-0de2601b62b9 |
| `wtm koyfin gov` | Open https://app.koyfin.com/myw/e94a97b3-600d-47d4-91d3-a01f8749146d |
| `wtm koyfin credit` | Open WTM-Credit-Confirmation |
| `wtm koyfin china` | Open WTM-China-Policy |
| `wtm koyfin btc chart` | Open https://app.koyfin.com/crypto/BTCUSD |
| `wtm barchart` | Open https://www.barchart.com/futures/major-commodities |
| `wtm barchart intraday` | Open https://www.barchart.com/my/watchlist?viewName=197689 |
| `wtm barchart daily` | Open https://www.barchart.com/futures/quotes/BTM26/historical-download |
| `wtm barchart basis` | Open https://www.barchart.com/futures/quotes/BTM26/spreads |
| `wtm barchart options` | Open https://www.barchart.com/futures/quotes/BTN26/options |
| `wtm barchart china basis` | Open https://www.barchart.com/futures/quotes/HGK26/spreads |
| `wtm open all` | Terminal: `python3 run_batch_collect.py open --include-optional` (ask Clark) |
| `wtm collect` | Ask Clark → `python3 run_batch_collect.py run --window today` |

## Compound shortcut

### `/wtm-morning`

Expands to the combined roles, goal, arena, and plan blocks below.

```text
/roles
ROLE A — Comet Collector (you)
  Whinfell desk CSV collection assistant, supervised mode.
  Export only. No CSV parsing, scoring, regime calls, or trades.
  Save all files to ~/Downloads/whinfell_drop (never ~/Downloads root).
  Ask Clark before any terminal command.

ROLE B — Clark (approval gate)
  Approves run_batch_collect.py run.
  Imports hydration bundle in Transmission Control.
  Accepts/dismisses Suggested Tracer (matrix never auto-fills).

ROLE C — Grok BUILD / pipeline (out of scope for Comet)
  Handles raw→WTM transform (2.2e), crypto sleeve sidecar, parquet, hydrate.
  Comet does NOT edit repo code or diagnose quarantine beyond reporting.

/goal
Complete the daily Whinfell batch chain:

  Pipeline minimum (required_batch_ids): rates + futures_intraday + futures_daily
  Desk standard (~6 bulk exports):
    Koyfin: rates, equities, WTM-Import-Core (or Credit-Confirmation), china_policy, WTM-Flows-Global
    Barchart: futures_intraday, futures_daily
  Optional: btc_basis, crypto charts, ARCH-4 core batch, options/greeks, gov flows

  → scripts/normalize_whinfell_drop.sh (if raw Koyfin/Barchart names)
  → python3 run_batch_collect.py run --window today
  → data/hydration/latest.json

Clark then imports bundle in Transmission Control.
Full URL list: 08_Deliverables/Comet_Morning_Collect_Prompt.txt

Success criteria in hydration bundle:
  • global: whinfell_score, transmission_state, btc_bias
  • china: sq3_score + china_ladder.horizons (5 stages) — requires china_policy CSV
  • crypto_sleeve: btc/eth/xrp/sol spot snapshot (auto from Import-Core or Credit-Confirmation)
  • flows: node_cockpits funds_flows when flows_* staged
  • execution: near_month / basis_spread when Barchart basis staged

Target: 3–5 minutes daily core; zero CSV parsing in browser.

/arena
Repo:     ~/Desktop/Whinfell_BUILD_Cousins
Drop:     ~/Downloads/whinfell_drop
Hydrate:  data/hydration/latest.json
Crypto:   data/crypto/v1/latest_crypto_sleeve.json
TC:       08_Deliverables/Whinfell_Transmission_Control.html

Authority (read before acting):
  whinfell_pipeline/collection_manifest.yaml   ← machine plan (run_batch_collect.py plan)
  whinfell_pipeline/desk_urls.yaml             ← ALL wired URLs (Jun 30 refresh)
  whinfell_pipeline/data_dictionary.yaml
  whinfell_pipeline/examples/comet_collection_plan.json
  08_Deliverables/Comet_Morning_Collect_Prompt.txt

Crypto sleeve (first-class):
  Spot IDs: BTCUSD, ETHUSD, XRPUSD, SOLUSD
  Snapshot: auto-ingested when credit_* staged (Import-Core or Credit-Confirmation)
  Optional chart exports → whinfell_drop:
    btc_price_chart_* / btc_correl_chart_* / eth|xrp|sol_correl_chart_*
    crypto_corr_series_* (pairwise HYG/JAAA/BKLN/CWB/XLRE vs SPY)

China ladder (navigation — china_policy CSV is the daily export):
  Liquidity: https://app.koyfin.com/macro/GCN10YR
  Credit:    https://app.koyfin.com/etf/KHYB.US
  Breadth:   https://app.koyfin.com/index/000300.SS
  Cyclical:  https://app.koyfin.com/etf/COPX.US · Barchart HGK26/SCO26
  Basis:     https://www.barchart.com/futures/quotes/HGK26/spreads

Forbidden:
  13-ticker loops · CSV parsing in browser · manual renames (use normalize script)
  trades · risk/regime changes · editing pipeline code

/plan
STEP 0 — Load machine plan
  cd ~/Desktop/Whinfell_BUILD_Cousins
  python3 run_batch_collect.py plan
  python3 run_batch_collect.py open              # optional — wired tabs
  python3 run_batch_collect.py open --include-optional

STEP 1 — Koyfin (save all to whinfell_drop)
  1. WTM-Rates-Credit        → rates_*     (dashboard; assist USGG2Y10Y, DGS10)
  2. WTM-Equities-Breadth    → equities_*  (dashboard; assist IWM, SPY)
  3. WTM-Import-Core         → credit_*    https://app.koyfin.com/myw/70789aa7-8084-4e4c-85d3-09f9b78dcd3a
     OR WTM-Credit-Confirmation → credit_*   (legacy; feeds crypto snapshot)
  4. WTM-China-Policy        → china_policy_*  (REQUIRED for china_ladder)
  5. WTM-Flows-Global        → WTM-Flows-Global.csv → flows_*
     https://app.koyfin.com/myw/afb1f314-4de4-47b6-b02f-0de2601b62b9
  Each wired view: ⋮ Export → CSV (charts: Show table → Download Available Data)

STEP 2 — Barchart required (2 exports)
  6. WTM-Futures-Intraday → futures_intraday_*
     https://www.barchart.com/my/watchlist?viewName=197689
  7. WTM-Futures-Daily    → futures_daily_*
     https://www.barchart.com/futures/quotes/BTM26/historical-download

STEP 3 — Optional (skip unless Clark asks)
  8.  WTM-Flows-GOV-USPRC  https://app.koyfin.com/myw/e94a97b3-600d-47d4-91d3-a01f8749146d
  9.  Whinfell-Daily-TimeSeries (wide backup)
  10. WTM-BTC-Basis         https://www.barchart.com/futures/quotes/BTM26/spreads
  11. WTM-Options-Greeks    https://www.barchart.com/futures/quotes/BTN26/options
  12. WTM-Crypto-Price/Correl* (BTC/ETH/XRP/SOL chart URLs in Comet_Morning_Collect_Prompt.txt)
  13. ARCH-4 WTM-Barchart-Core — 16-symbol historical batch (see full URL table above)

STEP 4 — Normalize (if raw vendor filenames)
  scripts/normalize_whinfell_drop.sh ~/Downloads/whinfell_drop

STEP 5 — Ask Clark: "Ready to run daily chain?"
  On approval:
  python3 run_batch_collect.py run --window today

STEP 6 — Report template
  files_staged / files_quarantined / hydrate_path
  china_written / crypto_ingested / flows_staged (yes/no)
  china_in_bundle / crypto_in_bundle

STEP 7 — Remind Clark
  Transmission Control → Import Latest Hydration Bundle → Save State
```

### `/barchart-hydration`

Barchart-only first-pass validation (no Koyfin):

```text
/goal
Run Barchart-only first-pass hydration for the full approved symbol universe.
Validate symbol coverage, parsers, normalization, curve/spread handling, and output schemas.
Do not use Koyfin.

/arena
Repo: ~/Desktop/Whinfell_BUILD_Cousins
Output: data/barchart/v1/
Requires: BARCHART_API_KEY in environment
Authority: whinfell_pipeline/data_dictionary.yaml

/plan
cd ~/Desktop/Whinfell_BUILD_Cousins
python3 run_batch_collect.py barchart-only

Report:
  approved / core_ok / curve_ok / spread_ok / failed / empty
  outputs: barchart_core_history.json, barchart_curve_history.json,
           barchart_spread_history.json, barchart_run_manifest.json
```

## Separate shortcuts

### `/roles`

```text
ROLE A — Comet Collector (you)
  Whinfell desk CSV collection assistant, supervised mode.
  Export only. No CSV parsing, scoring, regime calls, or trades.
  Save all files to ~/Downloads/whinfell_drop (never ~/Downloads root).
  Ask Clark before any terminal command.

ROLE B — Clark (approval gate)
  Approves run_batch_collect.py run.
  Imports hydration bundle in Transmission Control.
  Accepts/dismisses Suggested Tracer (matrix never auto-fills).

ROLE C — Grok BUILD / pipeline (out of scope for Comet)
  Handles raw→WTM transform (2.2e), crypto sleeve sidecar, parquet, hydrate.
  Comet does NOT edit repo code or diagnose quarantine beyond reporting.
```

### `/role`

Alias for ROLE A only (legacy):

```text
You are the Whinfell desk CSV collection assistant (supervised mode).
You are NOT an analyst, regime classifier, or trader.
You open saved Koyfin/Barchart screens, export CSV only, save to whinfell_drop,
run one Python command, and report results. Ask Clark before terminal commands.
```

### `/goal-funds-flow` (Phase 2b — BUILD Cousins)

**Authority:** `01_Strategy_Docs/Phase2_Flows_Implementation_Spec.md` (implementation) · Option D locked

```text
Funds Flow Sponsorship — node cockpit confirmation layer

Gate: Spec §7 checklist signed → PR-1 + PR-3a may start

Layers:
  L0  flows_*.csv / credit raw
  L1  data/flows/v1/latest_flows.json
  L2  node_cockpit.funds_flows

Success:
  • funds_flow_baskets + thresholds in Master DD
  • flow_pct_aum_5d = sum of 5 daily % AUM
  • degrade_mode: full | partial_basket | fallback_1d_credit | unavailable
  • confidence_delta only — never score/gate
  • FundsFlowSponsorshipCard reads L2 only

/roles: Blueprint spec · Bridge PR-1/2 · Dynamo PR-3 · Clarity PR-4 · Clark WTM-Flows view
```

### `/arena-funds-flow` (Phase 2b — resolved: Option D)

```text
Repo: ~/Desktop/Whinfell_BUILD_Cousins
Read: 08_Deliverables/Funds_Flow_Ingest_Arena_Debate.md

Question: How to ingest ETF % AUM flows for node sponsorship?

Options:
  A — Dedicated WTM-Flows export → flows_{YYYYMMDD}_{HHMM}.csv (BUILD primary)
  B — Credit cross-section only (1D — insufficient alone)
  C — Rates wide timeseries (partial — supplement only)
  D — Hybrid A + B fallback (BUILD recommendation)
  E — WhinSig merger (reject — scope)

Desk fact: WTM-Flows-Global.csv already in whinfell_drop — QUARANTINED (rename needed).

**Resolved:** Option D (Hybrid). Implementation: Phase2_Flows_Implementation_Spec.md
```

### `/plan-funds-flow` (Phase 2b — BUILD Cousins)

```text
STEP 0 — Read 08_Deliverables/Funds_Flow_Sponsorship_PLAN.md
STEP 1 — PR-1: funds_flow_baskets in data_dictionary.yaml
STEP 2 — PR-2: whinfell_pipeline/funds_flows.py + node_cockpits wire-up
STEP 3 — PR-3: Koyfin Flow (D) / AUM ingest → flows sidecar
STEP 4 — PR-4: FundsFlowSponsorshipCard in TC node rail
STEP 5 — PR-5: WTM export flow lines + docs
STEP 6 — pytest + hydrate inspect node_cockpits.credit.funds_flows
```

### `/comet-collect`

Paste block for Comet supervised morning — **all Koyfin + all Barchart URLs**:

```text
Read and execute: 08_Deliverables/Comet_Morning_Collect_Prompt.txt
(Do not summarize — follow numbered steps 1–25 exactly.)
```

### `/goal`

```text
Complete the daily Whinfell batch chain:

  Pipeline minimum: rates + futures_intraday + futures_daily
  Desk standard: Koyfin rates, equities, Import-Core (or Credit-Confirmation), china_policy, Flows-Global
                 Barchart intraday + daily
  Optional: btc_basis, crypto charts, ARCH-4 core, options, gov flows

  → normalize_whinfell_drop.sh → run_batch_collect.py run → data/hydration/latest.json
  Full URLs: 08_Deliverables/Comet_Morning_Collect_Prompt.txt

Target: 3–5 minutes daily core; zero CSV parsing in browser.
```

### `/arena`

```text
Repo: ~/Desktop/Whinfell_BUILD_Cousins
Drop: ~/Downloads/whinfell_drop
Authority: desk_urls.yaml · collection_manifest.yaml · Comet_Morning_Collect_Prompt.txt

Wired Koyfin: Import-Core myw/70789aa7… · Flows-Global myw/afb1f314… · GOV myw/e94a97b3…
Wired Barchart: intraday viewName=197689 · daily BTM26/historical-download · basis BTM26/spreads

Forbidden: 13-ticker loops · CSV parsing · manual renames · trades
```

### `/plan`

```text
STEP 0: python3 run_batch_collect.py plan
STEP 1 Koyfin: rates · equities · Import-Core (70789aa7…) · china_policy · Flows-Global (afb1f314…)
STEP 2 Barchart: intraday (viewName=197689) · daily (BTM26/historical-download)
STEP 3 Optional: see Comet_Morning_Collect_Prompt.txt steps 7–25
STEP 4: normalize_whinfell_drop.sh
STEP 5: Ask Clark → run_batch_collect.py run --window today
STEP 6: Report staged/quarantined/hydrate + flows_staged
STEP 7: Clark → TC Import Latest Hydration Bundle
```