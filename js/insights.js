/* insights.js — category filtering, search, and load-more for the insights grid */
(function () {
  'use strict';

  const grid = document.querySelector('[data-insights-grid]');
  if (!grid) return;

  const cards = Array.from(grid.children);
  const chips = document.querySelectorAll('[data-filter]');
  const searchInput = document.querySelector('[data-insights-search]');
  const loadMoreBtn = document.querySelector('[data-load-more]');
  const emptyState = document.querySelector('[data-insights-empty]');
  const PAGE_SIZE = 6;

  let activeCategory = 'all';
  let query = '';
  let visibleCount = PAGE_SIZE;

  function applyFilters() {
    const filtered = cards.filter((card) => {
      const matchesCategory = activeCategory === 'all' || card.dataset.category === activeCategory;
      const haystack = (card.dataset.title + ' ' + card.dataset.excerpt).toLowerCase();
      const matchesQuery = !query || haystack.includes(query);
      return matchesCategory && matchesQuery;
    });

    cards.forEach((card) => card.classList.add('filter-hidden'));
    filtered.slice(0, visibleCount).forEach((card) => card.classList.remove('filter-hidden'));

    if (loadMoreBtn) {
      loadMoreBtn.style.display = filtered.length > visibleCount ? 'inline-flex' : 'none';
    }
    if (emptyState) {
      emptyState.style.display = filtered.length === 0 ? 'block' : 'none';
    }
  }

  chips.forEach((chip) => {
    chip.addEventListener('click', () => {
      chips.forEach((c) => c.classList.remove('is-active'));
      chip.classList.add('is-active');
      activeCategory = chip.dataset.filter;
      visibleCount = PAGE_SIZE;
      applyFilters();
    });
  });

  if (searchInput) {
    searchInput.addEventListener('input', () => {
      query = searchInput.value.trim().toLowerCase();
      visibleCount = PAGE_SIZE;
      applyFilters();
    });
  }

  if (loadMoreBtn) {
    loadMoreBtn.addEventListener('click', () => {
      visibleCount += PAGE_SIZE;
      applyFilters();
    });
  }

  applyFilters();
})();
