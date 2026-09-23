/* navigation.js — header state, mobile menu (focus-managed), accordions */
(function () {
  'use strict';

  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('#navToggle');
  const mobileNav = document.querySelector('.mobile-nav');
  const mobileClose = document.querySelector('.mobile-nav__close');
  const desktopNav = window.matchMedia('(min-width: 1081px)');

  /* ---- Header: solid green + slimmer once the page scrolls ---- */
  if (header) {
    const threshold = document.body.classList.contains('home') ? 40 : 12;
    let ticking = false;
    const apply = () => { ticking = false; header.classList.toggle('is-scrolled', window.scrollY > threshold); };
    apply();
    window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(apply); } }, { passive: true });
  }

  /* ---- Mobile menu ---- */
  if (toggle && mobileNav) {
    mobileNav.querySelectorAll('.mobile-nav__body > ul > li, .mobile-nav__cta, .mobile-nav__contacts')
      .forEach((el, i) => el.style.setProperty('--i', i));
    mobileNav.setAttribute('aria-hidden', 'true');
    mobileNav.inert = true;

    const focusables = () => Array.from(mobileNav.querySelectorAll('a[href], button:not([disabled])'))
      .filter((el) => el.offsetParent !== null || el === document.activeElement);

    function openNav() {
      mobileNav.inert = false;
      mobileNav.removeAttribute('aria-hidden');
      mobileNav.classList.add('is-open');
      toggle.setAttribute('aria-expanded', 'true');
      document.body.classList.add('nav-open');
      requestAnimationFrame(() => (mobileClose || focusables()[0]).focus({ preventScroll: true }));
    }
    function closeNav(restoreFocus) {
      if (!mobileNav.classList.contains('is-open')) return;
      mobileNav.classList.remove('is-open');
      mobileNav.setAttribute('aria-hidden', 'true');
      mobileNav.inert = true;
      toggle.setAttribute('aria-expanded', 'false');
      document.body.classList.remove('nav-open');
      if (restoreFocus) toggle.focus({ preventScroll: true });
    }

    toggle.addEventListener('click', () => (mobileNav.classList.contains('is-open') ? closeNav(true) : openNav()));
    mobileClose && mobileClose.addEventListener('click', () => closeNav(true));
    // event delegation for links inside the menu
    mobileNav.addEventListener('click', (e) => { if (e.target.closest('a')) closeNav(false); });

    document.addEventListener('keydown', (e) => {
      if (!mobileNav.classList.contains('is-open')) return;
      if (e.key === 'Escape') { e.preventDefault(); closeNav(true); return; }
      if (e.key === 'Tab') {            // keep focus inside the open menu
        const f = focusables();
        if (!f.length) return;
        const first = f[0], last = f[f.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    });

    const onResize = () => { if (desktopNav.matches) closeNav(false); };
    desktopNav.addEventListener ? desktopNav.addEventListener('change', onResize) : window.addEventListener('resize', onResize);
  }

  /* ---- Mobile accordion for Practice Areas ---- */
  document.querySelectorAll('.mobile-accordion-trigger').forEach((trigger) => {
    const panel = document.getElementById(trigger.getAttribute('aria-controls'));
    if (!panel) return;
    trigger.addEventListener('click', () => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';
      trigger.setAttribute('aria-expanded', String(!expanded));
      panel.style.maxHeight = expanded ? '0px' : panel.scrollHeight + 'px';
    });
  });

  /* ---- Generic accordions (practice pages, careers, etc.) ---- */
  document.querySelectorAll('.accordion-trigger').forEach((trigger) => {
    const panel = document.getElementById(trigger.getAttribute('aria-controls'));
    if (!panel) return;
    trigger.addEventListener('click', () => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.accordion-trigger').forEach((t) => {
        if (t !== trigger && t.closest('.accordion') === trigger.closest('.accordion')) {
          t.setAttribute('aria-expanded', 'false');
          const p = document.getElementById(t.getAttribute('aria-controls'));
          if (p) p.style.maxHeight = '0px';
        }
      });
      trigger.setAttribute('aria-expanded', String(!expanded));
      panel.style.maxHeight = expanded ? '0px' : panel.scrollHeight + 'px';
    });
  });
})();
