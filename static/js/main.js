// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  // Lesson filtering
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
