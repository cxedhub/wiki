/*
 * Client-side draft cache for the CRAFT lesson templates.
 *
 * Stores up to MAX_DRAFTS lesson drafts in localStorage (per-browser,
 * per-template namespace) so a user can close the tab and come back
 * without losing work. Drafts are a pure client-side convenience —
 * the canonical "save" is still the .md export in Step 3.
 *
 * The active template must expose:
 *   - collect()                 → data object matching the f-* form
 *   - setField(id, value)
 *   - setSelectedStandards(dict)
 *   - getAllSelectedStandards()
 *   - refreshStdDropdowns()
 *   - flash(msg)                (optional; for toast messages)
 *
 * The host page can set window.LESSON_DRAFT_NAMESPACE (e.g. 'florida')
 * to keep drafts from different templates in separate slots.
 */
(function () {
  const VERSION = 'v1';
  const MAX_DRAFTS = 10;
  const SAVE_DEBOUNCE_MS = 800;

  const FIELD_IDS = [
    ['title', 'f-title'], ['author', 'f-author'], ['grade', 'f-grade'],
    ['subject', 'f-subject'], ['discipline', 'f-discipline'],
    ['duration', 'f-duration'], ['summary', 'f-summary'], ['tags', 'f-tags'],
    ['sep', 'f-sep'], ['ccc', 'f-ccc'], ['dci', 'f-dci'],
    ['cReal', 'f-c-real'], ['cCareer', 'f-c-career'],
    ['rMisc', 'f-r-misc'], ['rCorrect', 'f-r-correct'],
    ['aIdo', 'f-a-ido'], ['aWedo', 'f-a-wedo'], ['aYoudo', 'f-a-youdo'],
    ['aMaterials', 'f-a-materials'],
    ['fFormative', 'f-f-formative'], ['fCtm', 'f-f-ctm'],
    ['tNext', 'f-t-next'], ['tExt', 'f-t-ext'],
    ['summative', 'f-summative'], ['notes', 'f-notes']
  ];

  // Inputs that belong to the loader / uploader UI, not the lesson itself.
  const IGNORE_INPUT_IDS = new Set([
    'f-loadtext', 'f-loadfile', 'f-toploadfile'
  ]);

  function ns() { return window.LESSON_DRAFT_NAMESPACE || 'default'; }
  function storageKey() { return 'craft:lesson-drafts:' + VERSION + ':' + ns(); }
  function currentKey() { return 'craft:lesson-drafts:current:' + ns(); }

  let saveTimer = null;
  let currentId = null;
  let suspendAutoSave = false;

  function readList() {
    try {
      const raw = localStorage.getItem(storageKey());
      if (!raw) return [];
      const parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : [];
    } catch (e) { return []; }
  }
  function writeList(list) {
    try { localStorage.setItem(storageKey(), JSON.stringify(list)); }
    catch (e) { /* quota/unavailable — silently drop */ }
  }
  function uid() {
    return 'd-' + Date.now().toString(36) + '-' +
      Math.random().toString(36).slice(2, 8);
  }
  function getCurrentId() {
    if (currentId) return currentId;
    try { currentId = sessionStorage.getItem(currentKey()) || null; }
    catch (e) { currentId = null; }
    return currentId;
  }
  function setCurrentId(id) {
    currentId = id || null;
    try {
      if (id) sessionStorage.setItem(currentKey(), id);
      else sessionStorage.removeItem(currentKey());
    } catch (e) { /* ignore */ }
  }

  function isFormEmpty() {
    for (const [, id] of FIELD_IDS) {
      const el = document.getElementById(id);
      if (el && el.value && el.value.trim()) return false;
    }
    if (typeof getAllSelectedStandards === 'function') {
      const st = getAllSelectedStandards() || {};
      for (const fw in st) {
        if ((st[fw] || []).length) return false;
      }
    }
    return true;
  }

  function collectData() {
    if (typeof collect !== 'function') return null;
    try { return collect(); }
    catch (e) { return null; }
  }

  function autoSave() {
    if (suspendAutoSave) return;
    if (isFormEmpty()) { renderList(); return; }
    const data = collectData();
    if (!data) return;

    const list = readList();
    let id = getCurrentId();
    let entry = id ? list.find(d => d.id === id) : null;
    if (!entry) {
      id = id || uid();
      entry = { id: id, data: null, title: '', updatedAt: 0 };
      list.push(entry);
      setCurrentId(id);
    }
    entry.data = data;
    entry.title = (data.title || 'Untitled Lesson').slice(0, 120);
    entry.updatedAt = Date.now();

    list.sort((a, b) => (b.updatedAt || 0) - (a.updatedAt || 0));
    if (list.length > MAX_DRAFTS) list.length = MAX_DRAFTS;
    writeList(list);
    renderList();
    showStatus('Draft saved');
  }

  function scheduleSave() {
    if (saveTimer) clearTimeout(saveTimer);
    saveTimer = setTimeout(autoSave, SAVE_DEBOUNCE_MS);
  }

  function applyData(data) {
    suspendAutoSave = true;
    try {
      for (const [, id] of FIELD_IDS) {
        const el = document.getElementById(id);
        if (el) el.value = '';
      }
      if (typeof setSelectedStandards === 'function') setSelectedStandards({});

      if (data) {
        for (const [key, id] of FIELD_IDS) {
          if (data[key] !== undefined && typeof setField === 'function') {
            setField(id, data[key]);
          }
        }
        if (data.standards && typeof setSelectedStandards === 'function') {
          setSelectedStandards(data.standards);
        }
      }
      if (typeof refreshStdDropdowns === 'function') refreshStdDropdowns();
    } finally {
      suspendAutoSave = false;
    }
  }

  function loadDraft(id) {
    const list = readList();
    const d = list.find(x => x.id === id);
    if (!d) return;
    setCurrentId(id);
    applyData(d.data);
    renderList();
    if (typeof flash === 'function') flash('Draft loaded — ' + (d.title || 'Untitled'));
  }

  function deleteDraft(id) {
    if (!window.confirm('Delete this saved draft? This can\'t be undone.')) return;
    const list = readList().filter(d => d.id !== id);
    writeList(list);
    if (getCurrentId() === id) setCurrentId(null);
    renderList();
  }

  function newDraft() {
    if (!isFormEmpty()) {
      const ok = window.confirm(
        'Start a new draft? The form will be cleared. ' +
        'Your current work stays saved in the drafts list below ' +
        '(or download it as .md in Step 3 for a permanent copy).'
      );
      if (!ok) return;
    }
    setCurrentId(null);
    applyData(null);
    renderList();
    if (typeof flash === 'function') flash('Started a new draft');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function fmtTime(ts) {
    if (!ts) return '';
    const diff = (Date.now() - ts) / 1000;
    if (diff < 60) return 'just now';
    if (diff < 3600) return Math.floor(diff / 60) + ' min ago';
    if (diff < 86400) return Math.floor(diff / 3600) + ' hr ago';
    const d = new Date(ts);
    return d.toLocaleDateString(undefined, { month: 'short', day: 'numeric' }) +
      ' ' + d.toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' });
  }

  function escHtml(s) {
    return (s == null ? '' : '' + s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function renderList() {
    const panel = document.getElementById('draft-cache-panel');
    if (!panel) return;
    const list = readList().sort((a, b) => (b.updatedAt || 0) - (a.updatedAt || 0));
    const current = getCurrentId();

    if (!list.length) { panel.style.display = 'none'; panel.innerHTML = ''; return; }
    panel.style.display = '';

    let h = '';
    h += '<div class="draft-cache-head">';
    h += '<span class="draft-cache-title">💾 Saved drafts on this device</span>';
    h += '<button type="button" class="btn secondary draft-cache-new" onclick="lessonDraftCache.newDraft()">＋ New draft</button>';
    h += '</div>';
    h += '<p class="draft-cache-note">Drafts autosave to this browser only (not synced across devices). ';
    h += 'For a permanent or shareable copy, use <strong>Download .md</strong> in Step 3.</p>';
    h += '<ul class="draft-cache-list">';
    list.forEach(d => {
      const title = d.title || 'Untitled Lesson';
      const isCurrent = d.id === current;
      h += '<li class="draft-cache-item' + (isCurrent ? ' is-current' : '') + '">';
      h += '<div class="draft-cache-item-main">';
      h += '<span class="draft-cache-item-title">' + escHtml(title);
      if (isCurrent) h += ' <span class="draft-cache-badge">editing</span>';
      h += '</span>';
      h += '<span class="draft-cache-item-time">' + escHtml(fmtTime(d.updatedAt)) + '</span>';
      h += '</div>';
      h += '<div class="draft-cache-item-actions">';
      if (!isCurrent) {
        h += '<button type="button" class="btn secondary" onclick="lessonDraftCache.loadDraft(\'' + d.id + '\')">Load</button>';
      }
      h += '<button type="button" class="btn secondary draft-cache-del" onclick="lessonDraftCache.deleteDraft(\'' + d.id + '\')" aria-label="Delete draft" title="Delete draft">✕</button>';
      h += '</div>';
      h += '</li>';
    });
    h += '</ul>';
    panel.innerHTML = h;
  }

  let statusHideTimer = null;
  function showStatus(text) {
    const el = document.getElementById('draft-cache-status');
    if (!el) return;
    const time = new Date().toLocaleTimeString(undefined, { hour: 'numeric', minute: '2-digit' });
    el.textContent = '✓ ' + text + ' · ' + time;
    el.classList.add('show');
    if (statusHideTimer) clearTimeout(statusHideTimer);
    statusHideTimer = setTimeout(() => el.classList.remove('show'), 2500);
  }

  function injectStyles() {
    if (document.getElementById('draft-cache-styles')) return;
    const style = document.createElement('style');
    style.id = 'draft-cache-styles';
    style.textContent = [
      '#draft-cache-panel{border:1px solid var(--gray200,#E8E8E8);border-left:4px solid var(--teal,#1ABC9C);border-radius:10px;padding:14px 18px;margin:0 0 18px;background:#fff;display:none}',
      '.draft-cache-head{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}',
      '.draft-cache-title{font-weight:600;font-size:0.95rem;color:var(--ink,#1B2A4A)}',
      '.draft-cache-new{margin:0 !important;padding:6px 12px !important;font-size:0.8rem !important}',
      '.draft-cache-note{font-size:0.78rem;color:var(--gray600,#666);margin:6px 0 10px;line-height:1.5}',
      '.draft-cache-list{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:6px}',
      '.draft-cache-item{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:8px 10px;border:1px solid var(--gray100,#F5F5F5);border-radius:6px;background:#fafbfe}',
      '.draft-cache-item.is-current{border-color:var(--teal,#1ABC9C);background:#eef9f6}',
      '.draft-cache-item-main{display:flex;flex-direction:column;min-width:0;flex:1}',
      '.draft-cache-item-title{font-weight:600;font-size:0.88rem;color:var(--ink,#1B2A4A);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}',
      '.draft-cache-badge{display:inline-block;font-size:0.65rem;background:var(--teal,#1ABC9C);color:#fff;padding:1px 6px;border-radius:10px;margin-left:4px;vertical-align:middle;font-weight:700;text-transform:uppercase;letter-spacing:0.04em}',
      '.draft-cache-item-time{font-size:0.75rem;color:var(--gray600,#666);margin-top:2px}',
      '.draft-cache-item-actions{display:flex;gap:4px;flex-shrink:0}',
      '.draft-cache-item-actions .btn{margin:0 !important;padding:5px 10px !important;font-size:0.78rem !important}',
      '.draft-cache-del{color:var(--gray600,#666) !important}',
      '.draft-cache-del:hover{color:var(--red,#C0392B) !important;border-color:var(--red,#C0392B) !important}',
      '#draft-cache-status{position:fixed;bottom:24px;right:24px;background:#1B2A4A;color:#fff;font-size:0.78rem;font-weight:600;padding:7px 12px;border-radius:20px;opacity:0;pointer-events:none;transition:opacity 0.25s;z-index:90}',
      '#draft-cache-status.show{opacity:0.9}'
    ].join('');
    document.head.appendChild(style);
  }

  function ensureStatusEl() {
    if (document.getElementById('draft-cache-status')) return;
    const el = document.createElement('div');
    el.id = 'draft-cache-status';
    el.setAttribute('role', 'status');
    el.setAttribute('aria-live', 'polite');
    document.body.appendChild(el);
  }

  function isLessonInput(target) {
    if (!target) return false;
    if (target.id && IGNORE_INPUT_IDS.has(target.id)) return false;
    // The "load from markdown" textarea and file pickers live inside
    // <details class="load-box"> or the top-actions uploader.
    if (target.closest && (target.closest('.load-box') || target.closest('.top-actions'))) {
      return false;
    }
    return true;
  }

  function bindInputs() {
    const root = document.querySelector('.page-wrap') || document.body;
    const handler = e => { if (isLessonInput(e.target)) scheduleSave(); };
    root.addEventListener('input', handler);
    root.addEventListener('change', handler);
    // Standards chips/dropdowns mutate the form imperatively — catch those too.
    document.addEventListener('click', e => {
      const t = e.target;
      if (!t) return;
      if (t.classList && (t.classList.contains('std-dropdown-item') ||
          (t.closest && (t.closest('.std-chip') || t.closest('.std-custom-row'))))) {
        setTimeout(scheduleSave, 50);
      }
    });
  }

  function wrapLoadMarkdown() {
    if (typeof window.loadMarkdown !== 'function') return;
    const orig = window.loadMarkdown;
    window.loadMarkdown = function () {
      // Imported markdown starts a fresh draft slot so it doesn't
      // overwrite whatever draft was being edited before.
      setCurrentId(null);
      const r = orig.apply(this, arguments);
      scheduleSave();
      return r;
    };
  }

  window.lessonDraftCache = {
    loadDraft: loadDraft,
    deleteDraft: deleteDraft,
    newDraft: newDraft,
    save: autoSave
  };

  document.addEventListener('DOMContentLoaded', () => {
    injectStyles();
    ensureStatusEl();
    renderList();
    bindInputs();
    wrapLoadMarkdown();
  });
})();
