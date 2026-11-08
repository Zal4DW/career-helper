# Market Map Page Template

This file holds the HTML page for the artifact titled `Career Helper Market Map`. The page is kept inside Markdown so the plugin ships only text files.

**How to use it:** copy everything between the `~~~~html` and `~~~~` fence lines, exactly as written, into a file named `market-map-board-template.html` in your working folder, and publish that file. Do not include the fence lines. Do not edit the page; the board's content lives in its database, as @references/market-map-board.md describes.

~~~~html
<title>Career Helper Market Map</title>
<meta name="claude:viewport-fit-sides" content="cover">
<!--
  Career Helper market map board. Page version 2.0.0.
  Publish this file unchanged as an artifact with the capabilities given in
  references/market-map-board.md ({db: {rules: [...]}, user: {}}).
  It holds no user data: every organisation lives in the artifact database.
    organisations/{id}   one document per organisation (fields in references/market-map-board.md)
    map/meta             {owner, posture, direction, signalWindow, firstBuilt, lastChecked, themes}
    private/seed         seed organisation and profile; owner-only; this page never reads it
  User and fetched web text is only ever rendered with textContent, and links
  are shown only when they start with https://.
-->
<style>
  /* Layout: four priority columns, strongest evidence on the left; one column per row on a phone. */
  :root {
    --bg: #f3f5f4;
    --surface: #ffffff;
    --ink: #232826;
    --ink-soft: #57615c;
    --line: #d6ddd9;
    --accent: #1f5f4a;
    --accent-ink: #ffffff;
    --accent-soft: #e4efe9;
    --warn-ink: #7a4a00;
    --warn-bg: #fff3df;
    --focus: #b25000;
    --font-body: 'Helvetica Neue', 'Segoe UI', Arial, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --bg: #151a18; --surface: #1f2522; --ink: #e5eae7; --ink-soft: #a5b0aa; --line: #38423d;
      --accent: #78c2a4; --accent-ink: #151a18; --accent-soft: #23332c;
      --warn-ink: #ffd9a0; --warn-bg: #453416; --focus: #ffb066;
      color-scheme: dark;
    }
  }
  :root[data-theme="dark"] {
    --bg: #151a18; --surface: #1f2522; --ink: #e5eae7; --ink-soft: #a5b0aa; --line: #38423d;
    --accent: #78c2a4; --accent-ink: #151a18; --accent-soft: #23332c;
    --warn-ink: #ffd9a0; --warn-bg: #453416; --focus: #ffb066;
    color-scheme: dark;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; font-family: var(--font-body); font-size: 16px; background: var(--bg); color: var(--ink);
    line-height: 1.45;
    padding-left: max(16px, env(safe-area-inset-left, 0px));
    padding-right: max(16px, env(safe-area-inset-right, 0px));
    padding-block: 18px 26px;
  }
  header h1 { margin: 0 0 2px 0; font-size: 1.35rem; text-wrap: balance; }
  header p { margin: 0; color: var(--ink-soft); font-size: 0.9rem; }
  .toolbar { display: flex; flex-wrap: wrap; gap: 8px; padding-block: 12px; align-items: center; }
  button {
    font: inherit; font-size: 0.85rem; padding: 7px 14px; border-radius: 6px;
    border: 1px solid var(--line); background: var(--surface); color: var(--ink); cursor: pointer;
  }
  button.primary { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }
  button:disabled { opacity: 0.55; cursor: not-allowed; }
  button:focus-visible, [tabindex]:focus-visible, select:focus-visible, input:focus-visible, textarea:focus-visible, a:focus-visible {
    outline: 3px solid var(--focus); outline-offset: 2px;
  }
  a { color: var(--accent); }
  .notice {
    font-size: 0.9rem; background: var(--surface); border: 1px solid var(--line);
    border-radius: 8px; padding: 10px 12px; margin: 0 0 12px 0; max-width: 65ch;
  }
  .status-msg { font-size: 0.85rem; color: var(--ink-soft); min-height: 1.2em; margin: 0 0 8px 0; }
  .themes { max-width: 65ch; font-size: 0.88rem; margin: 0 0 12px 0; }
  .themes h2 { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-soft); margin: 0 0 4px 0; }
  .themes ul { margin: 0; padding-left: 1.2em; }
  .board-wrap { overflow-x: auto; }
  .board {
    display: grid; grid-auto-flow: column; grid-auto-columns: minmax(240px, 1fr);
    gap: 12px; align-items: start; padding-bottom: 6px;
  }
  @media (max-width: 520px) { .board { grid-auto-flow: row; grid-auto-columns: auto; } }
  .column { background: var(--surface); border: 1px solid var(--line); border-radius: 10px; padding: 10px; min-height: 140px; min-width: 0; }
  .column h2 {
    font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.04em; margin: 2px 4px 2px 4px;
    display: flex; justify-content: space-between; color: var(--ink-soft);
  }
  .column .meaning { font-size: 0.75rem; color: var(--ink-soft); margin: 0 4px 10px 4px; }
  .column.drag-over { border-color: var(--accent); background: var(--accent-soft); }
  .cards { display: flex; flex-direction: column; gap: 8px; min-height: 40px; }
  .card { border: 1px solid var(--line); border-radius: 8px; background: var(--bg); padding: 10px 10px 8px 10px; cursor: grab; overflow-wrap: anywhere; }
  .card .org { font-weight: 700; font-size: 0.95rem; margin: 0; }
  .card .overview { color: var(--ink-soft); font-size: 0.82rem; margin: 1px 0 6px 0; }
  .card .meta { font-size: 0.8rem; margin: 2px 0; }
  .card .meta strong { font-weight: 600; }
  .tag { display: inline-block; background: var(--warn-bg); color: var(--warn-ink); border-radius: 4px; padding: 0 6px; font-weight: 700; font-size: 0.75rem; margin-left: 6px; }
  .card .controls { display: flex; gap: 6px; margin-top: 8px; flex-wrap: wrap; }
  .card .controls button { font-size: 0.75rem; padding: 3px 9px; }
  dialog { border: 1px solid var(--line); border-radius: 10px; background: var(--surface); color: var(--ink); max-width: 480px; width: 92vw; padding: 18px; }
  dialog::backdrop { background: rgba(0, 0, 0, 0.45); }
  dialog h3 { margin: 0 0 12px 0; font-size: 1.05rem; }
  dialog h4 { margin: 16px 0 4px 0; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.04em; color: var(--ink-soft); }
  dialog label { display: block; font-size: 0.82rem; font-weight: 600; margin: 10px 0 3px 0; }
  dialog input, dialog select, dialog textarea {
    font: inherit; font-size: 0.88rem; width: 100%; padding: 7px 9px; border: 1px solid var(--line);
    border-radius: 6px; background: var(--bg); color: var(--ink);
  }
  dialog textarea { resize: vertical; min-height: 56px; }
  dialog .row { display: flex; gap: 10px; justify-content: flex-end; flex-wrap: wrap; margin-top: 16px; }
  .evidence { font-size: 0.82rem; overflow-wrap: anywhere; }
  .evidence ul { margin: 0; padding-left: 1.2em; }
  .hint { font-size: 0.78rem; color: var(--ink-soft); margin-top: 4px; }
  @media (prefers-reduced-motion: reduce) { * { transition: none !important; } }
</style>

<header>
  <h1>Market Map</h1>
  <p id="board-meta">Organisations like yours, sorted by what the evidence says.</p>
</header>

<div class="toolbar">
  <button class="primary" id="add-card" type="button">Add organisation</button>
</div>
<p class="notice" id="notice">Loading your market map. Organisations appear in four priority columns: Act now, Warm, Watch, and Quiet.</p>
<p class="status-msg" id="status-msg" role="status" aria-live="polite"></p>
<section class="themes" id="themes" hidden>
  <h2>Themes across the map</h2>
  <ul id="themes-list"></ul>
</section>

<div class="board-wrap">
  <main class="board" id="board" aria-label="Market map board"></main>
</div>

<dialog id="edit-dialog">
  <h3 id="edit-title">Edit organisation</h3>
  <form id="edit-form">
    <label for="f-org">Organisation</label>
    <input id="f-org" required>
    <label for="f-overview">Overview</label>
    <input id="f-overview" placeholder="What they do, size band, location">
    <label for="f-priority">Priority</label>
    <select id="f-priority"></select>
    <div id="reason-field" hidden>
      <label for="f-reason">Why are you changing the priority? (optional)</label>
      <input id="f-reason" placeholder="Your judgement, in a line">
    </div>
    <label for="f-angle">Suggested angle</label>
    <textarea id="f-angle"></textarea>
    <label for="f-notes">Your notes</label>
    <textarea id="f-notes"></textarea>
    <div class="evidence" id="evidence"></div>
    <p class="hint">Signals and decision makers come from public sources Claude found and dated. Ask Claude to add or correct them, so every entry keeps its source.</p>
    <div class="row">
      <button type="button" id="delete-card">Remove</button>
      <button type="button" id="cancel-edit">Cancel</button>
      <button class="primary" type="submit" id="save-edit">Save</button>
    </div>
  </form>
</dialog>

<script>
(function () {
  'use strict';

  var PRIORITIES = ['Act now', 'Warm', 'Watch', 'Quiet'];
  var HINTS = {
    'Act now': 'A dated hiring signal in your function, or a leadership change that creates one. Take the angle this week.',
    'Warm': 'Growth or investment signals, no direct hiring signal yet. Engage and keep watching.',
    'Watch': 'Similar organisation, no signals in the window. Stays on the map.',
    'Quiet': 'No signals for two updates, or a negative signal. Offered for removal.'
  };
  var STALE_DAYS = 14;
  var TEXT = ['organisation', 'overview', 'priority', 'priorityReason', 'priorityBy', 'signalGroup', 'latestSignal', 'signalDate',
    'decisionMaker', 'angle', 'notes', 'lastChecked', 'website', 'careersPage', 'linkedinPage', 'sizeBand', 'whyOnMap'];

  var cards = [];
  var db = null;
  var canWrite = true;
  var confirmed = false;
  var queues = {};
  var reserved = {};

  var boardEl = document.getElementById('board');
  var noticeEl = document.getElementById('notice');
  var statusEl = document.getElementById('status-msg');
  var metaEl = document.getElementById('board-meta');
  var addBtn = document.getElementById('add-card');

  function announce(text) { statusEl.textContent = text; }
  function notice(text) { noticeEl.textContent = text; noticeEl.hidden = !text; }
  function localDate() {
    var d = new Date();
    var m = String(d.getMonth() + 1);
    var day = String(d.getDate());
    return d.getFullYear() + '-' + (m.length < 2 ? '0' + m : m) + '-' + (day.length < 2 ? '0' + day : day);
  }
  function isStale(card) {
    if (!card.lastChecked) { return true; }
    var d = new Date(card.lastChecked + 'T00:00:00');
    if (isNaN(d)) { return true; }
    return (Date.now() - d.getTime()) / 86400000 > STALE_DAYS;
  }
  function slug(text) {
    return String(text).toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80) || 'organisation';
  }
  function newId(org) {
    var base = slug(org);
    var id = base;
    var n = 2;
    while (reserved[id] || cards.some(function (c) { return c.id === id; })) { id = base + '-' + n; n += 1; }
    return id;
  }
  function findCard(id) {
    for (var i = 0; i < cards.length; i++) { if (cards[i].id === id) { return cards[i]; } }
    return null;
  }

  function wait(ms) { return new Promise(function (r) { setTimeout(r, ms); }); }
  function attempt(fn) {
    return fn().catch(function (e) {
      if (e && e.code === 'unavailable') { return wait(400 + Math.random() * 800).then(fn); }
      throw e;
    });
  }
  // creating: true for a set() that creates a document. Only a rejected create
  // means this viewer cannot write; update() also rejects invalid_argument when
  // the document was removed elsewhere (another device, or Claude).
  function write(id, fn, creating) {
    var p = (queues[id] || Promise.resolve()).then(function () { return attempt(fn); });
    queues[id] = p.catch(function () { /* keep the queue moving */ });
    return p.catch(function (e) { return writeFailed(e, creating); });
  }
  function writeFailed(e, creating) {
    var code = e && e.code;
    if (code === 'invalid_argument' && creating) {
      setReadOnly();
      announce('This map is read-only for you, so that change was not saved.');
    } else if (code === 'invalid_argument') {
      announce('That organisation was changed or removed elsewhere, so the change was not saved.');
    } else if (code === 'quota_exceeded') {
      announce('The map is full. Remove Quiet organisations you no longer need, then try again.');
    } else {
      announce('That change was not saved. Check your connection and try again.');
    }
    throw e;
  }
  function stamp(body) {
    body.updated = new Date().toISOString();
    body.updatedBy = 'board';
    return body;
  }
  function setReadOnly() { canWrite = false; addBtn.disabled = true; render(); }

  function render() {
    boardEl.textContent = '';
    PRIORITIES.forEach(function (priority) {
      var col = document.createElement('section');
      col.className = 'column';
      col.setAttribute('aria-label', priority);
      var inCol = cards.filter(function (c) { return c.priority === priority; });
      var h = document.createElement('h2');
      h.textContent = priority;
      var count = document.createElement('span');
      count.textContent = String(inCol.length);
      count.setAttribute('aria-label', inCol.length + ' organisations');
      h.appendChild(count);
      col.appendChild(h);
      var hint = document.createElement('p');
      hint.className = 'meaning';
      hint.textContent = HINTS[priority];
      col.appendChild(hint);
      var list = document.createElement('div');
      list.className = 'cards';
      inCol.forEach(function (card) { list.appendChild(renderCard(card)); });
      col.appendChild(list);
      if (canWrite) {
        col.addEventListener('dragover', function (e) { e.preventDefault(); col.classList.add('drag-over'); });
        col.addEventListener('dragleave', function () { col.classList.remove('drag-over'); });
        col.addEventListener('drop', function (e) {
          e.preventDefault();
          col.classList.remove('drag-over');
          movePriority(e.dataTransfer.getData('text/plain'), priority);
        });
      }
      boardEl.appendChild(col);
    });
  }

  function renderCard(card) {
    var el = document.createElement('article');
    el.className = 'card';
    el.draggable = canWrite;
    el.tabIndex = 0;
    el.setAttribute('aria-label', card.organisation + ', priority ' + card.priority + (isStale(card) ? ', not checked recently' : ''));
    var org = document.createElement('p');
    org.className = 'org';
    org.textContent = card.organisation;
    if (isStale(card)) {
      var tag = document.createElement('span');
      tag.className = 'tag';
      tag.textContent = 'STALE';
      org.appendChild(tag);
    }
    el.appendChild(org);
    if (card.overview) {
      var ov = document.createElement('p');
      ov.className = 'overview';
      ov.textContent = card.overview;
      el.appendChild(ov);
    }
    if (card.latestSignal) {
      el.appendChild(meta('Signal', (card.signalGroup ? card.signalGroup + ': ' : '') + card.latestSignal + (card.signalDate ? ' (' + card.signalDate + ')' : '')));
    }
    if (card.decisionMaker) { el.appendChild(meta('Decision maker', card.decisionMaker)); }
    if (card.angle) { el.appendChild(meta('Angle', card.angle)); }
    if (card.priorityBy === 'board') { el.appendChild(meta('Priority', 'Set by you on the board' + (card.priorityReason ? ': ' + card.priorityReason : ''))); }
    el.appendChild(meta('Last checked', card.lastChecked || 'Not yet'));

    var idx = PRIORITIES.indexOf(card.priority);
    var controls = document.createElement('div');
    controls.className = 'controls';
    if (canWrite && idx > 0) { controls.appendChild(moveButton(card, PRIORITIES[idx - 1], 'Raise')); }
    if (canWrite && idx < PRIORITIES.length - 1) { controls.appendChild(moveButton(card, PRIORITIES[idx + 1], 'Lower')); }
    var open = document.createElement('button');
    open.type = 'button';
    open.textContent = canWrite ? 'Edit and evidence' : 'Evidence';
    open.addEventListener('click', function () { openEditor(card.id); });
    controls.appendChild(open);
    el.appendChild(controls);

    if (canWrite) {
      el.addEventListener('dragstart', function (e) { e.dataTransfer.setData('text/plain', card.id); });
    }
    el.addEventListener('keydown', function (e) {
      if (e.target !== el) { return; }
      if (e.key === 'Enter') { openEditor(card.id); }
      if (!canWrite) { return; }
      if (e.key === 'ArrowLeft' && idx > 0) { movePriority(card.id, PRIORITIES[idx - 1]); }
      if (e.key === 'ArrowRight' && idx < PRIORITIES.length - 1) { movePriority(card.id, PRIORITIES[idx + 1]); }
    });
    return el;
  }
  function meta(label, value) {
    var p = document.createElement('p');
    p.className = 'meta';
    var s = document.createElement('strong');
    s.textContent = label + ': ';
    p.appendChild(s);
    p.appendChild(document.createTextNode(value));
    return p;
  }
  function moveButton(card, target, verb) {
    var b = document.createElement('button');
    b.type = 'button';
    b.textContent = verb + ': ' + target;
    b.addEventListener('click', function () { movePriority(card.id, target); });
    return b;
  }

  function movePriority(id, priority) {
    var card = findCard(id);
    if (!card || card.priority === priority || !db || !canWrite) { return; }
    var body = stamp({ priority: priority, priorityBy: 'board', priorityReason: '', priorityChanged: localDate() });
    write(id, function () { return db.doc('organisations/' + id).update(body); })
      .then(function () { announce(card.organisation + ' moved to ' + priority + '. Open it to add your reason if you like.'); }, function () {});
  }

  // Editor
  var dialog = document.getElementById('edit-dialog');
  var form = document.getElementById('edit-form');
  var prioritySelect = document.getElementById('f-priority');
  var deleteBtn = document.getElementById('delete-card');
  var evidenceEl = document.getElementById('evidence');
  PRIORITIES.forEach(function (s) { var o = document.createElement('option'); o.textContent = s; prioritySelect.appendChild(o); });
  var editingId = null;
  var startPriority = '';

  function field(id) { return document.getElementById(id); }
  function resetDelete() { confirmed = false; deleteBtn.textContent = 'Remove'; }
  function safeLink(url, text) {
    if (typeof url !== 'string' || url.indexOf('https://') !== 0) { return document.createTextNode(text || url || ''); }
    var a = document.createElement('a');
    a.href = url;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.textContent = text || url;
    return a;
  }
  function renderEvidence(card) {
    evidenceEl.textContent = '';
    if (!card) { return; }
    var links = [['Website', card.website], ['Careers page', card.careersPage], ['LinkedIn page', card.linkedinPage]];
    var h = document.createElement('h4');
    h.textContent = 'About';
    evidenceEl.appendChild(h);
    var ul = document.createElement('ul');
    links.forEach(function (pair) {
      if (!pair[1]) { return; }
      var li = document.createElement('li');
      li.appendChild(document.createTextNode(pair[0] + ': '));
      li.appendChild(safeLink(pair[1]));
      ul.appendChild(li);
    });
    if (card.sizeBand) { var s = document.createElement('li'); s.textContent = 'Size: ' + card.sizeBand; ul.appendChild(s); }
    if (card.whyOnMap) { var w = document.createElement('li'); w.textContent = 'Why on the map: ' + card.whyOnMap; ul.appendChild(w); }
    if (!ul.childNodes.length) { var none = document.createElement('li'); none.textContent = 'No details recorded yet.'; ul.appendChild(none); }
    evidenceEl.appendChild(ul);

    var hs = document.createElement('h4');
    hs.textContent = 'Signals in the window';
    evidenceEl.appendChild(hs);
    var sl = document.createElement('ul');
    (card.signals || []).forEach(function (sig) {
      if (!sig || typeof sig !== 'object') { return; }
      var li = document.createElement('li');
      li.appendChild(document.createTextNode(String(sig.date || '') + ' ' + String(sig.group || '') + ': ' + String(sig.signal || '') + ' '));
      if (sig.source) { li.appendChild(safeLink(String(sig.source), 'source')); }
      sl.appendChild(li);
    });
    if (!sl.childNodes.length) { var ns = document.createElement('li'); ns.textContent = 'No public signals recorded in the window.'; sl.appendChild(ns); }
    evidenceEl.appendChild(sl);

    var hd = document.createElement('h4');
    hd.textContent = 'Decision makers';
    evidenceEl.appendChild(hd);
    var dl = document.createElement('ul');
    (card.decisionMakers || []).forEach(function (p) {
      if (!p || typeof p !== 'object') { return; }
      var li = document.createElement('li');
      li.appendChild(document.createTextNode(String(p.name || '[NOT FOUND]') + ', ' + String(p.title || '') + ' '));
      if (p.source) { li.appendChild(safeLink(String(p.source), 'source')); }
      dl.appendChild(li);
    });
    if (!dl.childNodes.length) { var nd = document.createElement('li'); nd.textContent = 'None confirmed yet.'; dl.appendChild(nd); }
    evidenceEl.appendChild(dl);
  }

  function openEditor(id) {
    var card = id ? findCard(id) : null;
    if (id && !card) { return; }
    editingId = id || null;
    var c = card || { organisation: '', priority: 'Watch' };
    field('edit-title').textContent = card ? c.organisation : 'Add organisation';
    field('f-org').value = c.organisation || '';
    field('f-overview').value = c.overview || '';
    prioritySelect.value = c.priority || 'Watch';
    startPriority = prioritySelect.value;
    field('f-reason').value = card && card.priorityBy === 'board' ? (card.priorityReason || '') : '';
    field('reason-field').hidden = !(card && card.priorityBy === 'board');
    field('f-angle').value = c.angle || '';
    field('f-notes').value = c.notes || '';
    renderEvidence(card);
    var lock = !canWrite;
    ['f-org', 'f-overview', 'f-priority', 'f-reason', 'f-angle', 'f-notes'].forEach(function (f) { field(f).disabled = lock; });
    field('save-edit').hidden = lock;
    deleteBtn.hidden = lock || !card;
    resetDelete();
    dialog.showModal();
  }
  prioritySelect.addEventListener('change', function () {
    field('reason-field').hidden = prioritySelect.value === startPriority && field('f-reason').value === '';
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!db || !canWrite) { dialog.close(); return; }
    var org = field('f-org').value.trim();
    if (!org) { return; }
    var body = {
      organisation: org,
      overview: field('f-overview').value.trim(),
      priority: prioritySelect.value,
      angle: field('f-angle').value.trim(),
      notes: field('f-notes').value.trim()
    };
    var id = editingId;
    var card = id ? findCard(id) : null;
    if (!card || body.priority !== startPriority || card.priorityBy === 'board') {
      if (!card || body.priority !== startPriority) { body.priorityChanged = localDate(); }
      body.priorityBy = 'board';
      body.priorityReason = field('f-reason').value.trim();
    }
    dialog.close();
    if (card) {
      write(id, function () { return db.doc('organisations/' + id).update(stamp(body)); })
        .then(function () { announce('Saved changes to ' + org + '.'); }, function () {});
    } else {
      var created = newId(org);
      body.lastChecked = '';
      body.signals = [];
      body.decisionMakers = [];
      body.added = localDate();
      reserved[created] = true;
      write(created, function () { return db.doc('organisations/' + created).set(stamp(body)); }, true)
        .then(function () { announce('Added ' + org + '. Ask Claude to research it at the next update.'); }, function () {});
    }
  });
  field('cancel-edit').addEventListener('click', function () { dialog.close(); });
  deleteBtn.addEventListener('click', function () {
    if (!editingId || !db || !canWrite) { return; }
    if (!confirmed) { confirmed = true; deleteBtn.textContent = 'Confirm remove'; return; }
    var id = editingId;
    var card = findCard(id);
    dialog.close();
    write(id, function () { return db.doc('organisations/' + id).delete(); })
      .then(function () { announce((card ? card.organisation : 'Organisation') + ' removed from the map.'); }, function () {});
  });
  dialog.addEventListener('close', function () { editingId = null; resetDelete(); });
  addBtn.addEventListener('click', function () { if (db && canWrite) { openEditor(null); } });

  function renderMeta(data) {
    var parts = [];
    if (data && data.owner) { parts.push('Owner: ' + String(data.owner) + '.'); }
    if (data && data.posture) { parts.push('Posture: ' + String(data.posture) + '.'); }
    if (data && data.lastChecked) { parts.push('Last update: ' + String(data.lastChecked) + '.'); }
    metaEl.textContent = parts.length ? parts.join(' ') : 'Organisations like yours, sorted by what the evidence says.';
    var themes = data && Array.isArray(data.themes) ? data.themes.filter(function (t) { return typeof t === 'string' && t; }) : [];
    var list = document.getElementById('themes-list');
    list.textContent = '';
    themes.forEach(function (t) { var li = document.createElement('li'); li.textContent = t; list.appendChild(li); });
    document.getElementById('themes').hidden = themes.length === 0;
  }

  render();

  if (!window.claude || typeof window.claude.use !== 'function') {
    addBtn.disabled = true;
    notice('This map keeps your organisations in Claude. Open it in Claude to see and change them.');
    return;
  }

  Promise.all([window.claude.use('db'), window.claude.use('user')]).then(function (found) {
    db = found[0];
    var user = found[1];
    if (!db) {
      addBtn.disabled = true;
      notice('This map keeps your organisations in Claude. Open it in Claude, signed in, to see and change them.');
      return;
    }
    if (user) {
      user.can('data.write').then(function (ok) { if (ok === false) { setReadOnly(); } }, function () {});
    }
    var fresh = false;
    var timer = setTimeout(function () {
      if (!fresh) {
        notice(cards.length ? 'The map may be out of date: your latest changes cannot be reached yet.' : 'Your market map cannot be reached yet. It fills in when the connection returns.');
      }
    }, 10000);
    db.collection('organisations').onSnapshot(function (snap) {
      cards = snap.docs.map(function (d) {
        var data = d.data() || {};
        var c = { id: d.id };
        TEXT.forEach(function (f) { c[f] = typeof data[f] === 'string' ? data[f] : ''; });
        c.signals = Array.isArray(data.signals) ? data.signals : [];
        c.decisionMakers = Array.isArray(data.decisionMakers) ? data.decisionMakers : [];
        if (PRIORITIES.indexOf(c.priority) === -1) { c.priority = 'Watch'; }
        return c;
      });
      if (!snap.metadata.fromCache) { fresh = true; clearTimeout(timer); }
      render();
      if (fresh || cards.length) {
        notice(cards.length ? '' : 'No organisations yet. Ask Claude to build your market map, or use Add organisation.');
      }
    }, function () {
      clearTimeout(timer);
      notice('The map could not load your organisations. Close it and open it again from Claude.');
    });
    db.doc('map/meta').onSnapshot(function (snap) {
      renderMeta(snap.exists ? snap.data() : null);
    }, function () {});
  });
})();
</script>
~~~~
