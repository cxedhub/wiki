/* last-updated-static.js
   Adds a "Last updated" footer to standalone HTML pages that live in
   static/ and therefore bypass Hugo's templating (and its last-updated partial).
   Include via <script src="...last-updated-static.js"></script> before </body>. */
(function () {
  // Derive the static/ path from the current URL.
  // Deployed at /wiki/…  or at root during local dev.
  var raw = decodeURIComponent(location.pathname);
  var staticPath = raw.replace(/^\/wiki\//, '').replace(/^\//, '');
  var ghBase = 'https://github.com/cxedhub/wiki/commits/main/static/';

  // Build the element
  var wrap = document.createElement('div');
  wrap.className = 'last-updated-static';
  wrap.style.cssText =
    'text-align:center;padding:10px 16px 2px;margin-top:16px;' +
    'border-top:1px solid #e0ddd4;font-size:0.82rem;color:#5a7fa0;';

  var link = '<a href="' + ghBase + staticPath + '" target="_blank" rel="noopener" ' +
    'title="View version history" style="color:#5a7fa0;text-decoration:none;display:inline-flex;' +
    'align-items:center;gap:4px;vertical-align:middle">' +
    '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" ' +
    'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' +
    '<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/>' +
    '<path d="M3 3v5h5"/><path d="M12 7v5l4 2"/></svg> Changes</a>';

  wrap.innerHTML = '<span style="font-style:italic">Last updated</span> ' + link;

  // Try the GitHub API (public, 60 req/h; cache in localStorage for 24 h)
  var cacheKey = 'lu_' + staticPath;
  var cached = null;
  try { cached = JSON.parse(localStorage.getItem(cacheKey)); } catch (e) { /* ignore */ }

  if (cached && Date.now() - cached.ts < 86400000) {
    setDate(cached.date);
  } else {
    fetch('https://api.github.com/repos/cxedhub/wiki/commits?path=static/' +
      encodeURIComponent(staticPath) + '&per_page=1')
      .then(function (r) { return r.json(); })
      .then(function (j) {
        if (j && j[0] && j[0].commit) {
          var d = j[0].commit.committer.date;
          try { localStorage.setItem(cacheKey, JSON.stringify({ ts: Date.now(), date: d })); } catch (e) { /* ignore */ }
          setDate(d);
        }
      })
      .catch(function () { /* graceful — link is still shown */ });
  }

  function setDate(iso) {
    var d = new Date(iso);
    var opts = { year: 'numeric', month: 'long', day: 'numeric' };
    var span = wrap.querySelector('span');
    if (span) span.textContent = 'Last updated ' + d.toLocaleDateString('en-US', opts);
  }

  // Insert before existing footer, or append to body
  var footer = document.querySelector('.page-footer, p.footer, .poll-footer');
  if (footer) {
    footer.parentNode.insertBefore(wrap, footer);
  } else {
    document.body.appendChild(wrap);
  }
})();
