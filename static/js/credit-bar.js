/* credit-bar.js
   Injects a "How to Credit" bar that mirrors the site-wide recommended
   citation from layouts/_default/baseof.html. Standalone HTML resources
   under static/ bypass the Hugo layout, so they need this explicit bar.
   Include via <script src="...credit-bar.js"></script> before </body>. */
(function () {
  if (document.querySelector('.cxed-how-to-credit')) return;

  var wrap = document.createElement('aside');
  wrap.className = 'cxed-how-to-credit';
  wrap.setAttribute('aria-label', 'How to credit');
  wrap.style.cssText =
    'max-width:860px;margin:24px auto 8px;padding:14px 18px;' +
    'background:#1B2A4A;color:#e2e8f0;border-radius:8px;' +
    'font-family:inherit;font-size:0.78rem;line-height:1.55;text-align:center;';

  wrap.innerHTML =
    '<strong style="color:#f8fafc;display:block;margin-bottom:4px;' +
    'font-size:0.72rem;text-transform:uppercase;letter-spacing:.8px;">' +
    'How to Credit</strong>' +
    'Borowczak, A.C. &amp; Borowczak, M. (2026). ' +
    '<em>CxEd Hub: Cross-Disciplinary Computing-Integrated K-12 Lesson Plans.</em> ' +
    'Retrieved from <a href="https://cxedhub.github.io/wiki/" ' +
    'style="color:#93c5fd;text-decoration:none;">https://cxedhub.github.io/wiki/</a>. ' +
    'Licensed under <a href="https://creativecommons.org/licenses/by-sa/4.0/" ' +
    'style="color:#93c5fd;text-decoration:none;">CC BY-SA 4.0</a>.';

  // Insert before existing footer if present, otherwise append to body.
  var footer = document.querySelector(
    '.page-footer, p.footer, .poll-footer, .last-updated-static'
  );
  if (footer && footer.parentNode) {
    footer.parentNode.insertBefore(wrap, footer);
  } else {
    document.body.appendChild(wrap);
  }
})();
