/* Chat provider "Open in..." buttons.
   Copies a prompt to the clipboard, opens the chosen provider in a new tab,
   and shows the OS-appropriate paste hint. */
(function () {
  if (window.ChatProviders) return;

  var PROVIDERS = [
    { id: 'chatgpt',    label: 'ChatGPT',    url: 'https://chatgpt.com/' },
    { id: 'claude',     label: 'Claude',     url: 'https://claude.ai/new' },
    { id: 'gemini',     label: 'Gemini',     url: 'https://gemini.google.com/app' },
    { id: 'copilot',    label: 'Copilot',    url: 'https://copilot.microsoft.com/' },
    { id: 'grok',       label: 'Grok',       url: 'https://grok.com/' },
    { id: 'perplexity', label: 'Perplexity', url: 'https://www.perplexity.ai/' }
  ];

  var isMac = /Mac|iPhone|iPad|iPod/i.test(
    (navigator.userAgentData && navigator.userAgentData.platform) ||
    navigator.platform || navigator.userAgent || ''
  );
  var PASTE_KEY = isMac ? 'Cmd+V' : 'Ctrl+V';

  var STYLE = [
    '.cpb-row{display:flex;flex-wrap:wrap;gap:0.4rem;align-items:center;margin:0.6rem 0 0.2rem;font-family:inherit}',
    '.cpb-label{font-size:0.78rem;color:#64748b;margin-right:0.15rem;letter-spacing:0.02em}',
    '.cpb-btn{cursor:pointer;font-size:0.78rem;font-weight:600;padding:0.3rem 0.65rem;border-radius:999px;border:1px solid #cbd5e1;background:#fff;color:#1e293b;line-height:1.2;transition:all 0.15s;font-family:inherit}',
    '.cpb-btn:hover{background:#1e293b;color:#fff;border-color:#1e293b;transform:translateY(-1px)}',
    '.cpb-btn[data-provider="chatgpt"]:hover{background:#10a37f;border-color:#10a37f}',
    '.cpb-btn[data-provider="claude"]:hover{background:#d97706;border-color:#d97706}',
    '.cpb-btn[data-provider="gemini"]:hover{background:#1a73e8;border-color:#1a73e8}',
    '.cpb-btn[data-provider="copilot"]:hover{background:#0078d4;border-color:#0078d4}',
    '.cpb-btn[data-provider="grok"]:hover{background:#111;border-color:#111}',
    '.cpb-btn[data-provider="perplexity"]:hover{background:#20808d;border-color:#20808d}',
    '.cpb-row--dark .cpb-label{color:#94a3b8}',
    '.cpb-row--dark .cpb-btn{background:rgba(255,255,255,0.08);color:#e2e8f0;border-color:rgba(255,255,255,0.22)}',
    '.cpb-row--dark .cpb-btn:hover{color:#fff}',
    '#cpb-fallback-toast{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#1e293b;color:#fff;padding:0.7rem 1.1rem;border-radius:8px;font-size:0.9rem;z-index:9999;box-shadow:0 4px 14px rgba(0,0,0,0.3);max-width:90vw;opacity:0;transition:opacity 0.25s}',
    '#cpb-fallback-toast.cpb-show{opacity:1}',
    '@media print{.cpb-row{display:none!important}}'
  ].join('\n');

  function injectStyle() {
    if (document.getElementById('cpb-style')) return;
    var s = document.createElement('style');
    s.id = 'cpb-style';
    s.textContent = STYLE;
    document.head.appendChild(s);
  }

  function toast(msg) {
    if (typeof window.showToast === 'function') { try { window.showToast(msg); return; } catch (e) {} }
    if (typeof window.flash === 'function')     { try { window.flash(msg); return; } catch (e) {} }
    var t = document.getElementById('cpb-fallback-toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'cpb-fallback-toast';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add('cpb-show');
    clearTimeout(t._hideTimer);
    t._hideTimer = setTimeout(function () { t.classList.remove('cpb-show'); }, 3200);
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text).then(function () { return true; }).catch(function () { return fallbackCopy(text); });
    }
    return Promise.resolve(fallbackCopy(text));
  }

  function fallbackCopy(text) {
    try {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.top = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      var ok = document.execCommand('copy');
      document.body.removeChild(ta);
      return ok;
    } catch (e) { return false; }
  }

  function openProvider(provider, getText) {
    var text = '';
    try { text = typeof getText === 'function' ? getText() : String(getText || ''); } catch (e) {}
    if (!text || !text.trim()) {
      toast('No prompt to copy yet — fill in the form first.');
      return;
    }
    // Open the tab synchronously so popup blockers don't intervene.
    var w = window.open(provider.url, '_blank', 'noopener');
    copyText(text).then(function (ok) {
      if (ok) {
        toast('Prompt copied! Paste into ' + provider.label + ' with ' + PASTE_KEY);
      } else {
        toast('Could not copy automatically — use the Copy button, then paste with ' + PASTE_KEY);
      }
      if (w) { try { w.focus(); } catch (e) {} }
    });
  }

  function render(container, getText, opts) {
    injectStyle();
    opts = opts || {};
    var row = document.createElement('div');
    row.className = 'cpb-row' + (opts.dark ? ' cpb-row--dark' : '');
    if (opts.label !== false) {
      var lbl = document.createElement('span');
      lbl.className = 'cpb-label';
      lbl.textContent = opts.label || 'Open in:';
      row.appendChild(lbl);
    }
    PROVIDERS.forEach(function (p) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'cpb-btn';
      b.dataset.provider = p.id;
      b.textContent = p.label;
      b.title = 'Copy prompt and open ' + p.label;
      b.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        openProvider(p, getText);
      });
      row.appendChild(b);
    });
    container.appendChild(row);
    return row;
  }

  window.ChatProviders = {
    providers: PROVIDERS,
    pasteKey: PASTE_KEY,
    render: render,
    copyText: copyText
  };
})();
