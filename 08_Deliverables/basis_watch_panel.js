/**
 * WTM BasisWatch + Implied Rate — bottom panel module
 * CME BasisWatch-style crypto bridge between TradFi and desk hydration.
 */
(function basisWatchPanel(global) {
  'use strict';

  const CME_MONTH = { F: 0, G: 1, H: 2, J: 3, K: 4, M: 5, N: 6, Q: 7, U: 8, V: 9, X: 10, Z: 11 };
  const MONTH_LABEL = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  const ASSETS = {
    BTC: { root: 'BT', spotKey: 'btc_spot_usd', label: 'Bitcoin', barchartSpread: 'https://www.barchart.com/futures/quotes/BTM26/spreads' },
    ETH: { root: 'ETH', spotKey: 'eth_spot_usd', label: 'Ethereum', barchartSpread: 'https://www.barchart.com/futures/quotes/ETHM26/spreads' },
  };

  const CROSS_ASSET_ROOTS = [
    { root: 'DX', label: 'US Dollar (DX)', role: 'FX bridge' },
    { root: 'HG', label: 'Copper (HG)', role: 'Industrial' },
    { root: 'ZM', label: 'Soybean Meal (ZM)', role: 'Ag complex' },
    { root: 'TA', label: 'Iron Ore (TA)', role: 'China industrial' },
  ];

  const DEPLOY_CURVE_URL = 'data/barchart/barchart_curve_history.json';
  let curveCache = null;
  let curveFetchPromise = null;

  function el(id) { return document.getElementById(id); }

  function fmtNum(n, d = 2) {
    if (n == null || !Number.isFinite(n)) return '—';
    return n.toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  }

  function fmtPct(n, d = 2) {
    if (n == null || !Number.isFinite(n)) return '—';
    return `${fmtNum(n, d)}%`;
  }

  function parseCmeSymbol(sym) {
    const m = String(sym || '').match(/^([A-Z0-9!]+)([FGHJKMNQUVXZ])(\d{2})$/);
    if (!m) return null;
    const month = CME_MONTH[m[2]];
    if (month == null) return null;
    const year = 2000 + parseInt(m[3], 10);
    const expiry = lastFridayOfMonth(year, month);
    return { root: m[1], monthCode: m[2], month, year, expiry, label: `${MONTH_LABEL[month]} ${year}` };
  }

  function lastFridayOfMonth(year, month) {
    const d = new Date(Date.UTC(year, month + 1, 0));
    while (d.getUTCDay() !== 5) d.setUTCDate(d.getUTCDate() - 1);
    return d;
  }

  function daysBetween(a, b) {
    return Math.max(1, Math.round((b - a) / 86400000));
  }

  function daysToExpiry(expiry, asOf = new Date()) {
    return daysBetween(asOf, expiry);
  }

  function heatClass(ann) {
    if (!Number.isFinite(ann)) return 'bw-heat--na';
    if (ann >= 12) return 'bw-heat--hot';
    if (ann >= 6) return 'bw-heat--warm';
    if (ann >= 0) return 'bw-heat--flat';
    return 'bw-heat--cold';
  }

  function curveShapeLabel(contracts) {
    if (!contracts.length) return '—';
    const front = contracts.slice(0, Math.min(3, contracts.length));
    const avg = front.reduce((s, c) => s + (c.annBasis || 0), 0) / front.length;
    if (avg >= 4) return 'Contango';
    if (avg <= -2) return 'Backwardation';
    return 'Flat';
  }

  async function ensureCurveHistory() {
    if (curveCache) return curveCache;
    if (curveFetchPromise) return curveFetchPromise;
    if (location.protocol === 'file:') {
      curveCache = { records: [] };
      return curveCache;
    }
    curveFetchPromise = fetch(`${DEPLOY_CURVE_URL}?_=${Date.now()}`)
      .then(r => (r.ok ? r.json() : { records: [] }))
      .then(data => { curveCache = data || { records: [] }; return curveCache; })
      .catch(() => { curveCache = { records: [] }; return curveCache; });
    return curveFetchPromise;
  }

  function recordsForRoot(records, root) {
    return (records || []).filter(r => {
      const meta = r.contract_meta || {};
      return meta.contract_root === root || String(r.raw_symbol || '').startsWith(root);
    });
  }

  function buildContracts(records, spot, asOfDate) {
    const asOf = asOfDate ? new Date(asOfDate) : new Date();
    const rows = records
      .map(r => {
        const parsed = parseCmeSymbol(r.raw_symbol);
        if (!parsed) return null;
        const price = Number(r.latest?.close ?? r.points?.[r.points.length - 1]?.close);
        if (!Number.isFinite(price) || price <= 0) return null;
        const dte = daysToExpiry(parsed.expiry, asOf);
        if (dte < 0) return null;
        const absBasis = price - spot;
        const pctBasis = spot > 0 ? (absBasis / spot) * 100 : null;
        const annBasis = spot > 0 && dte > 0 ? ((price / spot) - 1) * (365 / dte) * 100 : null;
        const chg = Number(r.latest?.change);
        const pctChg = Number(r.latest?.pct_change);
        return {
          symbol: r.raw_symbol,
          label: parsed.label,
          expiry: parsed.expiry,
          dte,
          price,
          absBasis,
          pctBasis,
          annBasis,
          chg,
          pctChg,
        };
      })
      .filter(Boolean)
      .sort((a, b) => a.expiry - b.expiry);
    return rows;
  }

  function synthesizeEthCurve(btcContracts, ethSpot, btcSpot) {
    if (!btcContracts.length || !ethSpot || !btcSpot) return [];
    const ratio = ethSpot / btcSpot;
    return btcContracts.map(c => ({
      ...c,
      symbol: c.symbol.replace(/^BT/, 'ETH'),
      price: c.price * ratio,
      absBasis: c.price * ratio - ethSpot,
      pctBasis: ((c.price * ratio - ethSpot) / ethSpot) * 100,
      annBasis: c.annBasis,
      synthetic: true,
    }));
  }

  function pickFrontContract(contracts, rollLogic, manualNear) {
    if (!contracts.length) return null;
    if (rollLogic === 'manual' && manualNear) {
      const hit = contracts.find(c => c.symbol.toUpperCase().includes(String(manualNear).toUpperCase().slice(0, 3)));
      if (hit) return hit;
    }
    if (rollLogic === 'constant') {
      const target = 30;
      let best = contracts[0];
      let bestDist = Math.abs(best.dte - target);
      contracts.forEach(c => {
        const d = Math.abs(c.dte - target);
        if (d < bestDist) { best = c; bestDist = d; }
      });
      return best;
    }
    return contracts.find(c => c.dte >= 7) || contracts[0];
  }

  function forwardRates(contracts) {
    const out = [];
    for (let i = 1; i < contracts.length; i++) {
      const a = contracts[i - 1];
      const b = contracts[i];
      const days = daysBetween(a.expiry, b.expiry);
      const fwd = a.price > 0 ? ((b.price / a.price) - 1) * (365 / days) * 100 : null;
      out.push({ from: a.symbol, to: b.symbol, days, fwd, calendar: b.price - a.price });
    }
    return out;
  }

  function richestTenor(contracts) {
    if (!contracts.length) return null;
    return contracts.reduce((best, c) => (!best || (c.annBasis || -999) > (best.annBasis || -999) ? c : best), null);
  }

  function steepestCalendar(forwards) {
    if (!forwards.length) return null;
    return forwards.reduce((best, f) => (!best || Math.abs(f.fwd || 0) > Math.abs(best.fwd || 0) ? f : best), null);
  }

  function crossAssetStrip(records) {
    return CROSS_ASSET_ROOTS.map(spec => {
      const recs = recordsForRoot(records, spec.root);
      const latest = recs.map(r => r.latest).filter(Boolean).sort((a, b) => String(b.date).localeCompare(String(a.date)))[0];
      const sym = recs[0]?.raw_symbol || spec.root;
      return {
        ...spec,
        symbol: sym,
        price: latest?.close,
        change: latest?.pct_change,
      };
    });
  }

  function rollStateLabel(contracts, front) {
    if (!front || contracts.length < 2) return '—';
    const idx = contracts.findIndex(c => c.symbol === front.symbol);
    const next = contracts[idx + 1];
    if (!next) return 'Back of curve';
    if (front.dte <= 14) return `Roll window · ${front.symbol} → ${next.symbol}`;
    return `Hold ${front.symbol}`;
  }

  function buildModel(state, curveData) {
    const bw = state.basisWatch || {};
    const assetKey = bw.asset || 'BTC';
    const asset = ASSETS[assetKey] || ASSETS.BTC;
    const records = curveData?.records || [];
    const sleeve = state.hydration?.crypto_sleeve?.assets || {};
    const spotRec = sleeve[asset.spotKey];
    const spot = Number(spotRec?.last_price);
    const spotChg = Number(spotRec?.chg_1d ?? spotRec?.['1_day']) * 100;
    const asOf = state.hydration?.as_of || state.provenance?.dataAsOf || new Date().toISOString();

    let contracts = buildContracts(recordsForRoot(records, asset.root), spot, asOf);
    let dataNote = '';
    if (!contracts.length && assetKey === 'ETH' && spot > 0) {
      const btcSpot = Number(sleeve.btc_spot_usd?.last_price);
      const btcContracts = buildContracts(recordsForRoot(records, 'BT'), btcSpot, asOf);
      contracts = synthesizeEthCurve(btcContracts, spot, btcSpot);
      dataNote = 'ETH curve synthesized from BTC term structure · wire CME ETH futures for live curve';
    } else if (!contracts.length) {
      dataNote = 'Import hydration + publish desk preview for Barchart curve JSON';
    }

    const rollLogic = bw.rollLogic || 'nearest';
    const manualNear = state.btcL3?.nearMonth || '';
    const front = pickFrontContract(contracts, rollLogic, manualNear);
    const forwards = forwardRates(contracts);
    const cross = crossAssetStrip(records);
    const richest = richestTenor(contracts);
    const steepest = steepestCalendar(forwards);
    const shape = curveShapeLabel(contracts);

    const exec = state.hydration?.global || state.hydration?.execution || {};
    const refMid = Number(exec.basis_spread || exec.ref_mid);

    return {
      assetKey,
      asset,
      spot,
      spotChg: Number.isFinite(spotChg) ? spotChg : null,
      asOf,
      contracts,
      front,
      forwards,
      cross,
      richest,
      steepest,
      shape,
      rollLabel: rollStateLabel(contracts, front),
      dataNote,
      refMid: Number.isFinite(refMid) ? refMid : null,
      mode: bw.mode || 'live',
      view: bw.view || 'basis',
    };
  }

  function renderSummaryCards(model) {
    const front = model.front;
    const spot = model.spot;
    return `
      <div class="bw-card"><span class="bw-card-label">Spot (CF proxy)</span><strong class="bw-card-value">${spot > 0 ? '$' + fmtNum(spot, 0) : '—'}</strong><span class="bw-card-meta">${Number.isFinite(model.spotChg) ? fmtPct(model.spotChg) + ' 1d' : '—'}</span></div>
      <div class="bw-card"><span class="bw-card-label">Front futures</span><strong class="bw-card-value">${front ? '$' + fmtNum(front.price, 0) : '—'}</strong><span class="bw-card-meta">${front ? front.symbol : '—'}</span></div>
      <div class="bw-card"><span class="bw-card-label">Ann. basis</span><strong class="bw-card-value">${front ? fmtPct(front.annBasis) : '—'}</strong><span class="bw-card-meta">${front ? fmtPct(front.pctBasis) + ' %' : '—'}</span></div>
      <div class="bw-card"><span class="bw-card-label">Curve shape</span><strong class="bw-card-value">${model.shape}</strong><span class="bw-card-meta">${model.rollLabel}</span></div>
      <div class="bw-card"><span class="bw-card-label">Richest tenor</span><strong class="bw-card-value">${model.richest ? model.richest.symbol : '—'}</strong><span class="bw-card-meta">${model.richest ? fmtPct(model.richest.annBasis) + ' ann.' : '—'}</span></div>
      <div class="bw-card"><span class="bw-card-label">Steepest cal.</span><strong class="bw-card-value">${model.steepest ? model.steepest.to : '—'}</strong><span class="bw-card-meta">${model.steepest ? fmtPct(model.steepest.fwd) + ' fwd' : '—'}</span></div>
    `;
  }

  function renderBasisTable(model) {
    if (!model.contracts.length) {
      return '<p class="bw-empty">No futures curve in bundle — run daily chain and publish desk preview.</p>';
    }
    const rows = model.contracts.map(c => `
      <tr class="${model.front && c.symbol === model.front.symbol ? 'bw-row-front' : ''}">
        <td>${c.symbol}</td>
        <td>${c.label}</td>
        <td class="tabular-nums">${c.dte}d</td>
        <td class="tabular-nums">$${fmtNum(c.price, 0)}</td>
        <td class="tabular-nums">${fmtNum(c.absBasis, 0)}</td>
        <td class="tabular-nums">${fmtPct(c.pctBasis)}</td>
        <td class="tabular-nums ${heatClass(c.annBasis)}">${fmtPct(c.annBasis)}</td>
        <td class="tabular-nums">${Number.isFinite(c.pctChg) ? fmtPct(c.pctChg) : '—'}</td>
      </tr>
    `).join('');
    return `<table class="bw-table"><thead><tr><th>Contract</th><th>Expiry</th><th>DTE</th><th>Futures</th><th>Abs basis</th><th>% basis</th><th>Ann. basis</th><th>Chg</th></tr></thead><tbody>${rows}</tbody></table>`;
  }

  function renderImpliedTable(model) {
    if (!model.contracts.length) return '<p class="bw-empty">No curve — import hydration first.</p>';
    const spotRows = model.contracts.map(c => `
      <tr><td>${c.symbol}</td><td class="tabular-nums">${fmtPct(c.annBasis)}</td><td class="tabular-nums">${c.dte}d</td></tr>
    `).join('');
    const fwdRows = model.forwards.map(f => `
      <tr><td>${f.from} → ${f.to}</td><td class="tabular-nums">${fmtPct(f.fwd)}</td><td class="tabular-nums">${fmtNum(f.calendar, 0)}</td><td class="tabular-nums">${f.days}d</td></tr>
    `).join('');
    return `
      <div class="bw-implied-grid">
        <div><h4 class="bw-subhead">Spot-implied annualized</h4>
          <table class="bw-table bw-table--compact"><thead><tr><th>Tenor</th><th>Rate</th><th>DTE</th></tr></thead><tbody>${spotRows}</tbody></table>
        </div>
        <div><h4 class="bw-subhead">Forward calendar rates</h4>
          <table class="bw-table bw-table--compact"><thead><tr><th>Leg</th><th>Fwd %</th><th>Spread $</th><th>Days</th></tr></thead><tbody>${fwdRows || '<tr><td colspan="4">—</td></tr>'}</tbody></table>
        </div>
      </div>`;
  }

  function renderHeatmap(model) {
    if (!model.contracts.length) return '';
    const cells = model.contracts.map(c => `
      <div class="bw-heat-cell ${heatClass(c.annBasis)}" title="${c.symbol}: ${fmtPct(c.annBasis)} ann.">
        <span class="bw-heat-sym">${c.symbol.replace(/[0-9]/g, '')}</span>
        <span class="bw-heat-val">${fmtPct(c.annBasis, 1)}</span>
        <span class="bw-heat-dte">${c.dte}d</span>
      </div>
    `).join('');
    return `<div class="bw-heatmap" aria-label="Basis heatmap by tenor">${cells}</div>`;
  }

  function renderCrossAsset(model) {
    return model.cross.map(x => `
      <div class="bw-cross-pill">
        <span class="bw-cross-label">${x.label}</span>
        <span class="bw-cross-val">${Number.isFinite(x.price) ? fmtNum(x.price, x.price < 10 ? 4 : 2) : '—'}</span>
        <span class="bw-cross-chg">${Number.isFinite(x.change) ? fmtPct(x.change) : ''}</span>
      </div>
    `).join('');
  }

  function drawBasisChart(model) {
    const canvas = el('bwCurveCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();
    canvas.width = Math.max(280, rect.width) * dpr;
    canvas.height = Math.max(120, rect.height) * dpr;
    ctx.scale(dpr, dpr);
    const w = rect.width;
    const h = rect.height;
    ctx.clearRect(0, 0, w, h);
    const contracts = model.contracts;
    if (!contracts.length || !(model.spot > 0)) {
      ctx.fillStyle = '#8b9cb3';
      ctx.font = '11px system-ui,sans-serif';
      ctx.fillText('Curve populates after hydration + Barchart curve JSON', 12, h / 2);
      return;
    }
    const prices = [model.spot, ...contracts.map(c => c.price)];
    const minP = Math.min(...prices) * 0.998;
    const maxP = Math.max(...prices) * 1.002;
    const pad = { l: 44, r: 12, t: 14, b: 28 };
    const plotW = w - pad.l - pad.r;
    const plotH = h - pad.t - pad.b;
    const xAt = i => pad.l + (i / Math.max(1, contracts.length)) * plotW;
    const yAt = p => pad.t + plotH - ((p - minP) / (maxP - minP || 1)) * plotH;

    ctx.strokeStyle = 'rgba(255,255,255,0.08)';
    ctx.beginPath();
    ctx.moveTo(pad.l, pad.t);
    ctx.lineTo(pad.l, h - pad.b);
    ctx.lineTo(w - pad.r, h - pad.b);
    ctx.stroke();

    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(94,179,255,0.55)';
    ctx.beginPath();
    ctx.moveTo(pad.l, yAt(model.spot));
    ctx.lineTo(w - pad.r, yAt(model.spot));
    ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle = '#9ec5f0';
    ctx.font = '9px system-ui';
    ctx.fillText('Spot', pad.l + 4, yAt(model.spot) - 4);

    ctx.strokeStyle = '#e07b39';
    ctx.lineWidth = 2;
    ctx.beginPath();
    contracts.forEach((c, i) => {
      const x = xAt(i + 1);
      const y = yAt(c.price);
      if (i === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    });
    ctx.stroke();
    ctx.lineWidth = 1;

    contracts.forEach((c, i) => {
      const x = xAt(i + 1);
      const y = yAt(c.price);
      ctx.fillStyle = model.front && c.symbol === model.front.symbol ? '#3d8bfd' : '#c5d0dc';
      ctx.beginPath();
      ctx.arc(x, y, model.front && c.symbol === model.front.symbol ? 4 : 3, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#8b9cb3';
      ctx.font = '8px system-ui';
      ctx.fillText(c.symbol.replace(/\d{2}$/, ''), x - 8, h - 8);
    });
  }

  function renderPanel(state) {
    const panel = el('basisWatchPanel');
    if (!panel) return;
    const collapsed = state.basisWatch?.collapsed;
    panel.classList.toggle('basis-watch-panel--collapsed', !!collapsed);
    const model = state._basisWatchModel || buildModel(state, curveCache || { records: [] });

    const status = el('bwStatusChip');
    if (status) {
      status.textContent = model.mode === 'snapshot' ? 'Snapshot' : 'Live';
      status.className = `bw-status-chip bw-status-chip--${model.mode}`;
    }
    const note = el('bwDataNote');
    if (note) note.textContent = model.dataNote || (model.contracts.length ? `As of ${String(model.asOf).slice(0, 19)}` : '');

    const summary = el('bwSummaryCards');
    if (summary) summary.innerHTML = renderSummaryCards(model);

    const main = el('bwMainView');
    if (main) {
      main.innerHTML = model.view === 'implied'
        ? renderImpliedTable(model)
        : `${renderHeatmap(model)}${renderBasisTable(model)}`;
    }

    const cross = el('bwCrossAsset');
    if (cross) cross.innerHTML = renderCrossAsset(model);

    document.querySelectorAll('.bw-view-tab').forEach(btn => {
      btn.classList.toggle('bw-view-tab--active', btn.dataset.bwView === model.view);
    });
    document.querySelectorAll('.bw-asset-btn').forEach(btn => {
      btn.classList.toggle('bw-asset-btn--active', btn.dataset.bwAsset === model.assetKey);
    });

    drawBasisChart(model);
    state._basisWatchModel = model;
  }

  async function refresh(state, hooks) {
    await ensureCurveHistory();
    if (state.basisWatch?.mode === 'snapshot' && state.basisWatch.snapshot) {
      curveCache = state.basisWatch.snapshot.curve || curveCache;
    }
    state._basisWatchModel = buildModel(state, curveCache);
    renderPanel(state);
    if (hooks?.renderAll) hooks.renderAll();
  }

  function exportCsv(state) {
    const model = state._basisWatchModel || buildModel(state, curveCache || { records: [] });
    const lines = ['contract,expiry,dte,futures,spot,abs_basis,pct_basis,ann_basis'];
    model.contracts.forEach(c => {
      lines.push([c.symbol, c.label, c.dte, c.price, model.spot, c.absBasis, c.pctBasis, c.annBasis].join(','));
    });
    const blob = new Blob([lines.join('\n')], { type: 'text/csv' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `wtm_basiswatch_${model.assetKey}_${new Date().toISOString().slice(0, 10)}.csv`;
    a.click();
    URL.revokeObjectURL(a.href);
  }

  function exportPng(state) {
    const canvas = el('bwCurveCanvas');
    if (!canvas) return;
    const a = document.createElement('a');
    a.href = canvas.toDataURL('image/png');
    a.download = `wtm_basiswatch_curve_${new Date().toISOString().slice(0, 10)}.png`;
    a.click();
  }

  function captureSnapshot(state) {
    state.basisWatch = state.basisWatch || {};
    state.basisWatch.snapshot = {
      capturedAt: new Date().toISOString(),
      curve: curveCache ? JSON.parse(JSON.stringify(curveCache)) : null,
      model: state._basisWatchModel,
    };
    state.basisWatch.mode = 'snapshot';
  }

  function init(hooks) {
    const getState = hooks.getState;
    const markDirty = hooks.markDirty || (() => {});

    el('btnBwCollapse')?.addEventListener('click', () => {
      const s = getState();
      s.basisWatch = s.basisWatch || {};
      s.basisWatch.collapsed = !s.basisWatch.collapsed;
      renderPanel(s);
      markDirty();
    });

    document.querySelectorAll('.bw-view-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        const s = getState();
        s.basisWatch = s.basisWatch || {};
        s.basisWatch.view = btn.dataset.bwView || 'basis';
        renderPanel(s);
        markDirty();
      });
    });

    document.querySelectorAll('.bw-asset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const s = getState();
        s.basisWatch = s.basisWatch || {};
        s.basisWatch.asset = btn.dataset.bwAsset || 'BTC';
        refresh(s, hooks);
        markDirty();
      });
    });

    el('bwRollLogic')?.addEventListener('change', e => {
      const s = getState();
      s.basisWatch = s.basisWatch || {};
      s.basisWatch.rollLogic = e.target.value;
      refresh(s, hooks);
      markDirty();
    });

    el('bwModeToggle')?.addEventListener('change', e => {
      const s = getState();
      s.basisWatch = s.basisWatch || {};
      if (e.target.value === 'snapshot') captureSnapshot(s);
      else s.basisWatch.mode = 'live';
      renderPanel(s);
      markDirty();
    });

    el('btnBwRefresh')?.addEventListener('click', () => {
      curveCache = null;
      curveFetchPromise = null;
      const s = getState();
      if (s.basisWatch) s.basisWatch.mode = 'live';
      refresh(s, hooks);
    });

    el('btnBwExportCsv')?.addEventListener('click', () => exportCsv(getState()));
    el('btnBwExportPng')?.addEventListener('click', () => exportPng(getState()));
    el('btnBwBarchart')?.addEventListener('click', () => {
      const s = getState();
      const model = s._basisWatchModel || buildModel(s, curveCache || { records: [] });
      window.open(model.asset.barchartSpread, '_blank', 'noopener');
    });
    el('btnBwKoyfin')?.addEventListener('click', () => {
      window.open('https://app.koyfin.com/crypto/BTCUSD', '_blank', 'noopener');
    });

    ensureCurveHistory().then(() => refresh(getState(), hooks));
    window.addEventListener('resize', () => renderPanel(getState()));
  }

  global.WTM_BasisWatch = {
    init,
    render: renderPanel,
    refresh,
    exportCsv,
    exportPng,
    buildModel,
    ensureCurveHistory,
  };
})(typeof window !== 'undefined' ? window : globalThis);