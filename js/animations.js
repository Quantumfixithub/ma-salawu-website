/* animations.js — one motion system for the whole site.
   Utilities: staggerChildren, revealOnScroll, initHeroAnimation, initParallax,
   initCounters, initCarousel. CSS carries the visuals; JS only toggles state. */
(function () {
  'use strict';

  const reduceQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const desktopQuery = window.matchMedia('(min-width: 1024px) and (hover: hover)');
  const root = document.documentElement;

  /* ---- staggerChildren: give each child an incremental transition delay ---- */
  function staggerChildren(parent, step) {
    const kids = parent.querySelectorAll('.reveal');
    kids.forEach((el, i) => el.style.setProperty('--reveal-delay', i * step + 'ms'));
    return kids;
  }

  /* ---- revealOnScroll: adds .is-visible once, groups animate together in sequence ---- */
  function revealOnScroll() {
    const groups = Array.from(document.querySelectorAll('[data-reveal-group]'));
    const singles = Array.from(document.querySelectorAll('.reveal')).filter((el) => !el.closest('[data-reveal-group]'));

    if (!('IntersectionObserver' in window) || reduceQuery.matches) {
      document.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'));
      return;
    }

    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          if (el.hasAttribute('data-reveal-group')) {
            el.querySelectorAll('.reveal').forEach((child) => child.classList.add('is-visible'));
          } else {
            el.classList.add('is-visible');
          }
          io.unobserve(el);
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -8% 0px' }
    );

    groups.forEach((g) => {
      staggerChildren(g, parseInt(g.getAttribute('data-reveal-group'), 10) || 110);
      io.observe(g);
    });
    singles.forEach((el) => io.observe(el));
  }

  /* ---- initHeroAnimation: single flag drives the whole intro sequence ---- */
  function initHeroAnimation() {
    if (!document.querySelector('.h-hero')) { root.classList.add('is-loaded'); return; }
    const go = () => requestAnimationFrame(() => requestAnimationFrame(() => root.classList.add('is-loaded')));
    if (document.readyState === 'complete' || reduceQuery.matches) go();
    else {
      // never make the user wait on slow images
      window.addEventListener('load', go, { once: true });
      setTimeout(go, 400);
    }
  }

  /* ---- initParallax: very subtle, desktop only, off for reduced motion ---- */
  function initParallax() {
    const items = Array.from(document.querySelectorAll('[data-parallax]'));
    if (!items.length) return;
    const RANGE = 36; // total travel in px
    let active = new Set();
    let ticking = false;

    function update() {
      ticking = false;
      const vh = window.innerHeight;
      active.forEach((img) => {
        const r = img.parentElement.getBoundingClientRect();
        const progress = (r.top + r.height / 2 - vh / 2) / (vh / 2 + r.height / 2); // -1 … 1
        const y = Math.max(-1, Math.min(1, progress)) * (RANGE / 2) * -1;
        img.style.transform = 'translate3d(0,' + y.toFixed(1) + 'px,0)';
      });
    }
    function onScroll() {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }
    const io = 'IntersectionObserver' in window
      ? new IntersectionObserver((entries) => {
          entries.forEach((e) => (e.isIntersecting ? active.add(e.target) : active.delete(e.target)));
          onScroll();
        }, { rootMargin: '10% 0px' })
      : null;

    function enable() {
      if (!io || reduceQuery.matches || !desktopQuery.matches) return disable();
      items.forEach((i) => io.observe(i));
      window.addEventListener('scroll', onScroll, { passive: true });
      window.addEventListener('resize', onScroll, { passive: true });
    }
    function disable() {
      if (io) items.forEach((i) => io.unobserve(i));
      active = new Set();
      window.removeEventListener('scroll', onScroll);
      items.forEach((i) => (i.style.transform = ''));
    }
    enable();
    const rerun = () => { disable(); enable(); };
    desktopQuery.addEventListener && desktopQuery.addEventListener('change', rerun);
    reduceQuery.addEventListener && reduceQuery.addEventListener('change', rerun);
  }

  /* ---- initCounters: only where real figures are supplied via data-count ---- */
  function initCounters() {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length || !('IntersectionObserver' in window)) return;
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          const el = entry.target;
          const target = parseFloat(el.dataset.count);
          const suffix = el.dataset.suffix || '';
          io.unobserve(el);
          if (reduceQuery.matches) { el.textContent = target + suffix; return; }
          const duration = 1400;
          const start = performance.now();
          (function tick(now) {
            const p = Math.min((now - start) / duration, 1);
            el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3))) + suffix;
            if (p < 1) requestAnimationFrame(tick);
          })(start);
        });
      },
      { threshold: 0.6 }
    );
    counters.forEach((el) => io.observe(el));
  }

  /* ---- initCarousel: accessible, keyboard + swipe, autoplay pauses on interaction ---- */
  function initCarousel(section) {
    const slides = Array.from(section.querySelectorAll('.h-quote'));
    if (slides.length < 2) { slides[0] && slides[0].classList.add('is-active'); return; }
    const prev = section.querySelector('[data-carousel-prev]');
    const next = section.querySelector('[data-carousel-next]');
    const dotsWrap = section.querySelector('[data-carousel-dots]');
    const viewport = section.querySelector('.h-testimonials__viewport');
    const interval = parseInt(section.getAttribute('data-autoplay'), 10) || 0;
    let index = 0;
    let timer = null;
    let stopped = reduceQuery.matches; // never autoplay for reduced motion

    const dots = slides.map((_, i) => {
      if (!dotsWrap) return null;
      const b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Show testimonial ' + (i + 1) + ' of ' + slides.length);
      b.addEventListener('click', () => { stop(); go(i); });
      dotsWrap.appendChild(b);
      return b;
    });

    function render() {
      slides.forEach((s, i) => {
        const on = i === index;
        s.classList.toggle('is-active', on);
        s.setAttribute('aria-hidden', String(!on));
        if (on) s.removeAttribute('inert'); else s.setAttribute('inert', '');
      });
      dots.forEach((d, i) => { if (!d) return; d.classList.toggle('is-active', i === index); d.setAttribute('aria-current', String(i === index)); });
    }
    function go(i) { index = (i + slides.length) % slides.length; render(); }
    function stop() { stopped = true; clearInterval(timer); }
    function start() { if (interval && !stopped) timer = setInterval(() => go(index + 1), interval); }

    prev && prev.addEventListener('click', () => { stop(); go(index - 1); });
    next && next.addEventListener('click', () => { stop(); go(index + 1); });
    section.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') { stop(); go(index - 1); }
      if (e.key === 'ArrowRight') { stop(); go(index + 1); }
    });
    ['mouseenter', 'focusin', 'touchstart'].forEach((ev) => section.addEventListener(ev, stop, { passive: true }));

    let x0 = null;
    viewport.addEventListener('touchstart', (e) => { x0 = e.touches[0].clientX; }, { passive: true });
    viewport.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 48) { stop(); go(index + (dx < 0 ? 1 : -1)); }
      x0 = null;
    }, { passive: true });

    render();
    start();
  }

  /* ---- boot ---- */
  initHeroAnimation();
  revealOnScroll();
  initParallax();
  initCounters();
  document.querySelectorAll('[data-carousel]').forEach(initCarousel);
})();
