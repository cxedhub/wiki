// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  // ── Homepage explore filtering ──
  var homeSearch = document.getElementById('home-search');
  var lessonList = document.getElementById('lesson-list');
  if (homeSearch && lessonList) {
    initExploreFilters();
    return;
  }

  // ── Lessons page filtering (legacy) ──
  var searchInput = document.getElementById('search-input');
  var gradeFilter = document.getElementById('filter-grade');
  var subjectFilter = document.getElementById('filter-subject');
  var domainFilter = document.getElementById('filter-domain');
  var clearBtn = document.getElementById('clear-filters');
  var countEl = document.getElementById('filter-count');
  var cards = document.querySelectorAll('#lesson-list .card');

  if (!searchInput || cards.length === 0) return;

  function normalize(s) {
    return (s || '').toLowerCase().trim();
  }

  function filterCards() {
    var query = normalize(searchInput.value);
    var grade = normalize(gradeFilter.value);
    var subject = normalize(subjectFilter.value);
    var domain = normalize(domainFilter.value);
    var visible = 0;

    cards.forEach(function (card) {
      var text = normalize(card.textContent);
      var cardGrades = normalize(card.dataset.grades);
      var cardSubjects = normalize(card.dataset.subjects);
      var cardDomains = normalize(card.dataset.domains);

      var matchSearch = !query || text.indexOf(query) !== -1;
      var matchGrade = !grade || cardGrades.indexOf(grade) !== -1;
      var matchSubject = !subject || cardSubjects.indexOf(subject) !== -1;
      var matchDomain = !domain || cardDomains.indexOf(domain) !== -1;

      if (matchSearch && matchGrade && matchSubject && matchDomain) {
        card.style.display = '';
        visible++;
      } else {
        card.style.display = 'none';
      }
    });

    countEl.textContent = visible + ' of ' + cards.length + ' lessons shown';
  }

  searchInput.addEventListener('input', filterCards);
  gradeFilter.addEventListener('change', filterCards);
  subjectFilter.addEventListener('change', filterCards);
  domainFilter.addEventListener('change', filterCards);

  clearBtn.addEventListener('click', function () {
    searchInput.value = '';
    gradeFilter.value = '';
    subjectFilter.value = '';
    domainFilter.value = '';
    filterCards();
  });

  filterCards();
});

// ── Explore filters (homepage) ──
function initExploreFilters() {
  var searchInput = document.getElementById('home-search');
  var cards = Array.from(document.querySelectorAll('#lesson-list .card'));
  var resultsCount = document.getElementById('results-count');
  var activeFiltersEl = document.getElementById('active-filters');
  var noResults = document.getElementById('no-results');
  var clearAllBtn = document.getElementById('clear-all-filters');
  var noResultsClear = document.getElementById('no-results-clear');
  var sortSelect = document.getElementById('sort-select');
  var filterSidebar = document.getElementById('filter-sidebar');
  var mobileToggle = document.getElementById('mobile-filter-toggle');
  var mobileApply = document.getElementById('mobile-apply-filters');
  var totalCount = cards.length;

  // Collect all checkboxes
  var checkboxes = Array.from(document.querySelectorAll('.filter-check input[type="checkbox"]'));

  function getActiveFilters() {
    var filters = { grade: [], subject: [], domain: [], tag: [] };
    checkboxes.forEach(function (cb) {
      if (cb.checked) {
        filters[cb.dataset.filterType].push(cb.value);
      }
    });
    return filters;
  }

  function matchesFilter(cardAttr, filterValues) {
    if (filterValues.length === 0) return true;
    var cardValues = (cardAttr || '').split('|').map(function (s) { return s.trim().toLowerCase(); });
    // OR logic within a category: card must match at least one selected value
    return filterValues.some(function (fv) {
      return cardValues.indexOf(fv.toLowerCase()) !== -1;
    });
  }

  function applyFilters() {
    var filters = getActiveFilters();
    var query = (searchInput.value || '').toLowerCase().trim();
    var visible = 0;

    cards.forEach(function (card) {
      var matchSearch = !query || card.textContent.toLowerCase().indexOf(query) !== -1;
      var matchGrade = matchesFilter(card.dataset.grades, filters.grade);
      var matchSubject = matchesFilter(card.dataset.subjects, filters.subject);
      var matchDomain = matchesFilter(card.dataset.domains, filters.domain);
      var matchTag = matchesFilter(card.dataset.tags, filters.tag);

      if (matchSearch && matchGrade && matchSubject && matchDomain && matchTag) {
        card.style.display = '';
        visible++;
      } else {
        card.style.display = 'none';
      }
    });

    // Update count
    resultsCount.innerHTML = 'Showing <strong>' + visible + '</strong> of ' + totalCount + ' lessons';

    // Show/hide no-results
    noResults.style.display = visible === 0 ? '' : 'none';

    // Render active filter chips
    renderActiveChips(filters, query);

    // Update badge counts (show how many visible cards match each option)
    updateBadgeCounts(filters, query);
  }

  function renderActiveChips(filters, query) {
    var html = '';
    if (query) {
      html += '<span class="active-chip">Search: "' + escapeHtml(query) + '" <button data-action="clear-search">&times;</button></span>';
    }
    var types = ['grade', 'subject', 'domain', 'tag'];
    types.forEach(function (type) {
      filters[type].forEach(function (val) {
        html += '<span class="active-chip active-chip-' + type + '">' + escapeHtml(val) + ' <button data-action="uncheck" data-type="' + type + '" data-value="' + escapeHtml(val) + '">&times;</button></span>';
      });
    });
    activeFiltersEl.innerHTML = html;

    // Bind chip remove buttons
    activeFiltersEl.querySelectorAll('button').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (btn.dataset.action === 'clear-search') {
          searchInput.value = '';
        } else {
          // Uncheck the matching checkbox
          checkboxes.forEach(function (cb) {
            if (cb.dataset.filterType === btn.dataset.type && cb.value === btn.dataset.value) {
              cb.checked = false;
            }
          });
        }
        applyFilters();
      });
    });
  }

  function updateBadgeCounts(currentFilters, query) {
    // For each checkbox, show how many visible results it would produce
    // if toggled on (or if already on, how many it currently contributes to)
    checkboxes.forEach(function (cb) {
      var badge = cb.parentElement.querySelector('.filter-badge');
      if (!badge) return;

      // Count how many cards match all OTHER filters plus this checkbox value
      var type = cb.dataset.filterType;
      var val = cb.value;
      var count = 0;

      cards.forEach(function (card) {
        var matchSearch = !query || card.textContent.toLowerCase().indexOf(query) !== -1;
        if (!matchSearch) return;

        // Check all filter types
        var match = true;
        ['grade', 'subject', 'domain', 'tag'].forEach(function (ft) {
          if (ft === type) {
            // For this filter type, check only this specific value
            var cardValues = (card.dataset[ftToDataset(ft)] || '').split('|').map(function (s) { return s.trim().toLowerCase(); });
            if (cardValues.indexOf(val.toLowerCase()) === -1) match = false;
          } else {
            // For other types, use current filters
            if (!matchesFilter(card.dataset[ftToDataset(ft)], currentFilters[ft])) match = false;
          }
        });

        if (match) count++;
      });

      badge.textContent = count;
      // Dim options with 0 results
      cb.parentElement.classList.toggle('filter-check-empty', count === 0);
    });
  }

  function ftToDataset(ft) {
    var map = { grade: 'grades', subject: 'subjects', domain: 'domains', tag: 'tags' };
    return map[ft];
  }

  function escapeHtml(str) {
    var div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // Sorting
  sortSelect.addEventListener('change', function () {
    var val = sortSelect.value;
    var parent = document.getElementById('lesson-list');
    var sorted = cards.slice();

    if (val === 'title') {
      sorted.sort(function (a, b) { return (a.dataset.title || '').localeCompare(b.dataset.title || ''); });
    } else if (val === 'title-desc') {
      sorted.sort(function (a, b) { return (b.dataset.title || '').localeCompare(a.dataset.title || ''); });
    } else if (val === 'date') {
      sorted.sort(function (a, b) { return (b.dataset.date || '').localeCompare(a.dataset.date || ''); });
    }

    sorted.forEach(function (card) { parent.appendChild(card); });
  });

  // Event listeners
  searchInput.addEventListener('input', applyFilters);
  checkboxes.forEach(function (cb) {
    cb.addEventListener('change', applyFilters);
  });

  clearAllBtn.addEventListener('click', clearAll);
  if (noResultsClear) noResultsClear.addEventListener('click', clearAll);

  function clearAll() {
    searchInput.value = '';
    checkboxes.forEach(function (cb) { cb.checked = false; });
    applyFilters();
  }

  // Mobile sidebar toggle
  if (mobileToggle) {
    mobileToggle.addEventListener('click', function () {
      filterSidebar.classList.toggle('open');
      document.body.classList.toggle('filters-open');
    });
  }
  if (mobileApply) {
    mobileApply.addEventListener('click', function () {
      filterSidebar.classList.remove('open');
      document.body.classList.remove('filters-open');
    });
  }

  // Initial render
  applyFilters();
}
