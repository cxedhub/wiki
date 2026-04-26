/*
 * Per-section visibility toggles for the CRAFT lesson templates.
 *
 * Lets a teacher hide supplemental sections from the form (and optionally
 * from print/download exports) without losing the underlying data. Toggle
 * state is per-browser, per-template namespace; the form, the AI prompt,
 * and the draft cache always carry the complete lesson data underneath.
 *
 * Each toggle group has three states:
 *   - 'show'      → visible on form, included in print and downloads
 *   - 'hide-form' → hidden on form, still included in print and downloads
 *   - 'hide-all'  → hidden on form, omitted from print and downloads
 *
 * Hide-all does NOT strip data from collect(), the draft cache, or the LLM
 * prompt — only from the markdown / rich-text / .doc exports (via the host
 * template's collectForExport() wrapper) and from the print stylesheet.
 *
 * The host template must:
 *   1. Define window.LESSON_TOGGLE_GROUPS = [{id, label, description, fields}, ...]
 *      before this script runs. `fields` lists the data keys (the same keys
 *      collect() returns) that should be cleared on 'hide-all'.
 *   2. Mark each section's wrapper element with data-toggle-group="<id>".
 *   3. Place an empty <div id="lesson-toggles-panel"></div> wherever the
 *      controls should render.
 *   4. Route export functions through filterForExport(collect()) instead of
 *      collect() directly (typically via a small collectForExport() helper).
 */
(function () {
  const VERSION = 'v1';
  const STATES = ['show', 'hide-form', 'hide-all'];
  const STATE_LABEL = {
    'show': 'Show',
    'hide-form': 'Hide on form',
    'hide-all': 'Hide everywhere'
  };
  const STATE_HINT = {
    'show': 'Visible on form, included in downloads and print',
    'hide-form': 'Hidden on form, still in downloads and print',
    'hide-all': 'Hidden on form and stripped from downloads and print'
  };

  function ns() { return window.LESSON_DRAFT_NAMESPACE || 'default'; }
  function storageKey() { return 'craft:lesson-toggles:' + VERSION + ':' + ns(); }

  function groups() {
    const g = window.LESSON_TOGGLE_GROUPS;
    return Array.isArray(g) ? g : [];
  }

  function readState() {
    try {
      const raw = localStorage.getItem(storageKey());
      const parsed = raw ? JSON.parse(raw) : {};
      return (parsed && typeof parsed === 'object') ? parsed : {};
    } catch (e) { return {}; }
  }
  function writeState(state) {
    try { localStorage.setItem(storageKey(), JSON.stringify(state)); }
    catch (e) { /* quota / unavailable — silently drop */ }
  }

  function getState(id) {
    const s = readState()[id];
    return STATES.indexOf(s) >= 0 ? s : 'show';
  }
  function setState(id, value) {
    if (STATES.indexOf(value) < 0) value = 'show';
    const s = readState();
    s[id] = value;
    writeState(s);
    applyOne(id, value);
    renderPanel();
  }

  function applyOne(id, state) {
    const els = document.querySelectorAll('[data-toggle-group="' + cssEsc(id) + '"]');
    els.forEach(el => { el.dataset.toggleState = state; });
  }
  function applyAll() {
    groups().forEach(g => applyOne(g.id, getState(g.id)));
  }

  function filterForExport(data) {
    if (!data || typeof data !== 'object') return data;
    const out = Object.assign({}, data);
    groups().forEach(g => {
      if (getState(g.id) !== 'hide-all') return;
      (g.fields || []).forEach(key => {
        if (out[key] === undefined) return;
        if (Array.isArray(out[key])) out[key] = [];
        else if (typeof out[key] === 'object' && out[key] !== null) out[key] = {};
        else out[key] = '';
      });
    });
    return out;
  }

  function cssEsc(s) {
    return (window.CSS && window.CSS.escape)
      ? window.CSS.escape(s)
      : ('' + s).replace(/[^a-zA-Z0-9_-]/g, '\\$&');
  }
  function escHtml(s) {
    return (s == null ? '' : '' + s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function injectStyles() {
    if (document.getElementById('lesson-toggle-styles')) return;
    const style = document.createElement('style');
    style.id = 'lesson-toggle-styles';
    style.textContent = [
      // Hide on form (still in print)
      '@media screen{[data-toggle-state="hide-form"],[data-toggle-state="hide-all"]{display:none !important}}',
      // Hide everywhere — also hidden in print
      '@media print{[data-toggle-state="hide-all"]{display:none !important}}',
      // The toggle panel itself is a config UI, not lesson content — never print it.
      '@media print{#lesson-toggles-panel{display:none !important}}',
      // Panel
      '#lesson-toggles-panel{border:1px solid var(--gray200,#E8E8E8);border-left:4px solid var(--purple,#8E6BBF);border-radius:10px;margin:0 0 18px;background:#fff}',
      '#lesson-toggles-panel>summary{cursor:pointer;list-style:none;display:flex;align-items:center;justify-content:space-between;gap:10px;padding:12px 18px;font-weight:600;font-size:0.92rem;color:var(--ink,#1B2A4A)}',
      '#lesson-toggles-panel>summary::-webkit-details-marker{display:none}',
      '#lesson-toggles-panel>summary::before{content:"\\25B8";display:inline-block;transition:transform 0.15s;color:var(--purple,#8E6BBF);margin-right:4px}',
      '#lesson-toggles-panel[open]>summary::before{transform:rotate(90deg)}',
      '.lesson-toggles-summary-meta{font-size:0.72rem;font-weight:500;color:var(--gray600,#666)}',
      '.lesson-toggles-body{padding:0 18px 14px}',
      '.lesson-toggles-note{font-size:0.78rem;color:var(--gray600,#666);margin:0 0 12px;line-height:1.5}',
      '.lesson-toggles-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:8px}',
      '.lesson-toggle-row{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:10px 12px;border:1px solid var(--gray100,#F5F5F5);border-radius:6px;background:#fafbfe;flex-wrap:wrap}',
      '.lesson-toggle-row.is-hide-form{background:#fbf6e8}',
      '.lesson-toggle-row.is-hide-all{background:#fdecea}',
      '.lesson-toggle-info{flex:1;min-width:200px}',
      '.lesson-toggle-label{font-weight:600;font-size:0.86rem;color:var(--ink,#1B2A4A)}',
      '.lesson-toggle-desc{font-size:0.74rem;color:var(--gray600,#666);margin-top:2px;line-height:1.4}',
      '.lesson-toggle-seg{display:inline-flex;border:1px solid var(--gray200,#E8E8E8);border-radius:6px;overflow:hidden;flex-shrink:0;background:#fff}',
      '.lesson-toggle-seg button{background:#fff;border:none;border-right:1px solid var(--gray200,#E8E8E8);padding:6px 10px;font-family:inherit;font-size:0.76rem;font-weight:500;color:var(--gray600,#666);cursor:pointer;margin:0;line-height:1.2}',
      '.lesson-toggle-seg button:last-child{border-right:none}',
      '.lesson-toggle-seg button:hover{background:#f0fbf8;color:var(--ink,#1B2A4A)}',
      '.lesson-toggle-seg button.is-active{background:var(--purple,#8E6BBF);color:#fff;cursor:default}',
      '.lesson-toggle-seg button.is-active:hover{background:var(--purple,#8E6BBF)}',
      '.lesson-toggles-actions{margin-top:12px;display:flex;gap:8px;flex-wrap:wrap}',
      '.lesson-toggles-actions button{background:#fff;border:1px solid var(--gray200,#E8E8E8);color:var(--ink,#1B2A4A);padding:6px 12px;border-radius:6px;font-family:inherit;font-size:0.78rem;font-weight:500;cursor:pointer}',
      '.lesson-toggles-actions button:hover{border-color:var(--purple,#8E6BBF);color:var(--purple,#8E6BBF)}'
    ].join('');
    document.head.appendChild(style);
  }

  function summaryMeta() {
    const list = groups();
    if (!list.length) return '';
    let hidden = 0;
    list.forEach(g => { if (getState(g.id) !== 'show') hidden++; });
    if (!hidden) return list.length + ' sections, all visible';
    return hidden + ' of ' + list.length + ' hidden';
  }

  function renderPanel() {
    const panel = document.getElementById('lesson-toggles-panel');
    if (!panel) return;
    const list = groups();
    if (!list.length) { panel.style.display = 'none'; return; }
    panel.style.display = '';

    let h = '';
    h += '<summary>';
    h += '<span>⚙️ Display options &middot; show or hide supplemental sections</span>';
    h += '<span class="lesson-toggles-summary-meta">' + escHtml(summaryMeta()) + '</span>';
    h += '</summary>';
    h += '<div class="lesson-toggles-body">';
    h += '<p class="lesson-toggles-note">Trim the form down to just the sections you need. ';
    h += '<strong>Hide on form</strong> tucks a section out of sight while keeping it in your downloads and print copy. ';
    h += '<strong>Hide everywhere</strong> also strips it from downloaded and printed copies. ';
    h += 'Your underlying data is always preserved &mdash; the AI prompt and saved drafts include every field regardless of these settings.</p>';
    h += '<ul class="lesson-toggles-list">';
    list.forEach(g => {
      const cur = getState(g.id);
      const rowCls = cur === 'show' ? '' : (cur === 'hide-form' ? ' is-hide-form' : ' is-hide-all');
      h += '<li class="lesson-toggle-row' + rowCls + '">';
      h += '<div class="lesson-toggle-info">';
      h += '<div class="lesson-toggle-label">' + escHtml(g.label || g.id) + '</div>';
      if (g.description) h += '<div class="lesson-toggle-desc">' + escHtml(g.description) + '</div>';
      h += '</div>';
      h += '<div class="lesson-toggle-seg" role="group" aria-label="' + escHtml(g.label || g.id) + ' visibility">';
      STATES.forEach(s => {
        const isAct = s === cur;
        h += '<button type="button"' +
          (isAct ? ' class="is-active" aria-pressed="true"' : ' aria-pressed="false"') +
          ' title="' + escHtml(STATE_HINT[s]) + '"' +
          ' onclick="lessonToggles.setState(\'' + g.id.replace(/'/g, "\\'") + '\',\'' + s + '\')">' +
          escHtml(STATE_LABEL[s]) + '</button>';
      });
      h += '</div>';
      h += '</li>';
    });
    h += '</ul>';
    h += '<div class="lesson-toggles-actions">';
    h += '<button type="button" onclick="lessonToggles.resetAll()">Reset to defaults (show all)</button>';
    h += '</div>';
    h += '</div>';
    panel.innerHTML = h;
  }

  function ensurePanelEl() {
    const panel = document.getElementById('lesson-toggles-panel');
    if (!panel) return null;
    // Promote to <details> so the panel collapses naturally without extra JS.
    if (panel.tagName.toLowerCase() !== 'details') {
      const det = document.createElement('details');
      det.id = 'lesson-toggles-panel';
      // Migrate any preset attributes (open, etc.).
      if (panel.hasAttribute('open')) det.setAttribute('open', '');
      panel.parentNode.replaceChild(det, panel);
      return det;
    }
    return panel;
  }

  function resetAll() {
    writeState({});
    applyAll();
    renderPanel();
  }

  window.lessonToggles = {
    getState: getState,
    setState: setState,
    filterForExport: filterForExport,
    resetAll: resetAll,
    refresh: function () { applyAll(); renderPanel(); }
  };

  document.addEventListener('DOMContentLoaded', () => {
    injectStyles();
    ensurePanelEl();
    applyAll();
    renderPanel();
  });
})();
