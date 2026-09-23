/* main.js — back-to-top control, footer year, newsletter micro-form */
(function () {
  'use strict';

  const toTop = document.querySelector('.to-top');
  if (toTop) {
    const onScroll = () => toTop.classList.toggle('is-visible', window.scrollY > 600);
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
    toTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  document.querySelectorAll('[data-year]').forEach((el) => {
    el.textContent = new Date().getFullYear();
  });

  /* Attorneys page: practice-area filter chips (was previously non-functional) */
  const personGrid = document.querySelector('.person-card')?.closest('.grid');
  const personFilterBar = document.querySelector('.filter-bar');
  if (personGrid && personFilterBar) {
    const cards = Array.from(personGrid.querySelectorAll('.person-card'));
    personFilterBar.addEventListener('click', (e) => {
      const chip = e.target.closest('[data-filter]');
      if (!chip) return;
      personFilterBar.querySelectorAll('[data-filter]').forEach((c) => c.classList.toggle('is-active', c === chip));
      const filter = chip.getAttribute('data-filter');
      cards.forEach((card) => {
        const tags = (card.getAttribute('data-filter-tags') || '').split(/\s+/);
        card.style.display = filter === 'all' || tags.includes(filter) ? '' : 'none';
      });
    });
  }

  const newsletterForm = document.querySelector('[data-newsletter]');
  if (newsletterForm) {
    newsletterForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const btn = newsletterForm.querySelector('button');
      const input = newsletterForm.querySelector('input');
      if (!input.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim())) {
        input.focus();
        return;
      }
      const original = btn.innerHTML;
      btn.textContent = 'Subscribed';
      input.value = '';
      setTimeout(() => (btn.innerHTML = original), 2400);
    });
  }
})();
