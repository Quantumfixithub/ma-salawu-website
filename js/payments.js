/* payments.js — renders consultation fee tiers and, only when the firm has
 * configured a real Paystack public key, wires up real payment collection.
 *
 * IMPORTANT — read before enabling:
 *   This site has no backend, so there is no server-side step that verifies
 *   a payment actually landed in the firm's Paystack account. The flow below
 *   uses Paystack's own secure checkout (card details never touch this site's
 *   code), which is safe for collecting payment, but confirmation of success
 *   relies on: (1) Paystack's own callback firing in the browser, and
 *   (2) the client also sending their payment reference on WhatsApp as a
 *   backup, which the UI prompts for. For full automatic reconciliation,
 *   connect a backend that verifies transactions server-side via Paystack's
 *   API and the firm's secret key (which must never be placed in this
 *   client-side file).
 *
 * Until a real public key is set in content/site-data.json
 * (consultation.payment.publicKey) and consultation.payment.enabled is true,
 * this renders fee information only, with a "contact us to arrange payment"
 * fallback — never a payment button that silently does nothing or could be
 * mistaken for a working checkout.
 */
(function () {
  'use strict';

  function looksLikeRealKey(key) {
    return typeof key === 'string' && /^pk_(test|live)_[A-Za-z0-9]{10,}$/.test(key.trim());
  }

  function formatAmount(amount, currency) {
    const n = Number(amount) || 0;
    try {
      return new Intl.NumberFormat('en-NG', { style: 'currency', currency: currency || 'NGN', maximumFractionDigits: 0 }).format(n);
    } catch (e) {
      return (currency || 'NGN') + ' ' + n.toLocaleString();
    }
  }

  function loadPaystackScript(cb) {
    if (window.PaystackPop) return cb();
    const s = document.createElement('script');
    s.src = 'https://js.paystack.co/v1/inline.js';
    s.onload = cb;
    s.onerror = () => console.warn('payments.js: could not load Paystack checkout script');
    document.head.appendChild(s);
  }

  const UNLOCK_STORAGE_KEY = 'consultation-booking-prepared';

  function isUnlocked() {
    // Persisted per-browser so returning to the page (or reloading after
    // submitting) doesn't re-lock a booking that was already sent.
    try { return sessionStorage.getItem(UNLOCK_STORAGE_KEY) === '1'; } catch (e) { return false; }
  }

  function unlock() {
    try { sessionStorage.setItem(UNLOCK_STORAGE_KEY, '1'); } catch (e) { /* noop */ }
    const locked = document.getElementById('payment-locked');
    const unlocked = document.getElementById('payment-unlocked');
    if (locked) locked.style.display = 'none';
    if (unlocked) unlocked.style.display = '';
    render();
  }

  function render() {
    const tiersEl = document.getElementById('payment-tiers');
    const unavailableEl = document.getElementById('payment-unavailable');
    if (!tiersEl) return;
    if (!isUnlocked()) return; // stays behind the "send your request first" panel
    const data = (window.CMS && window.CMS.data) || {};
    const payment = (data.consultation && data.consultation.payment) || {};
    const site = data.site || {};
    const tiers = payment.tiers || [];
    const active = (payment.enabled === true || payment.enabled === 'true') && looksLikeRealKey(payment.publicKey);

    tiersEl.innerHTML = '';

    if (active) {
      const emailWrap = document.createElement('div');
      emailWrap.className = 'field';
      emailWrap.style.marginBottom = '1.4rem';
      emailWrap.innerHTML = '<label for="pay-email">Your email (for the payment receipt)</label><input type="email" id="pay-email">';
      tiersEl.appendChild(emailWrap);
      loadPaystackScript(() => {});
    }

    tiers.forEach((tier, i) => {
      if (!tier || !tier.label) return; // skip an incompletely-filled-in extra fee
      const row = document.createElement('div');
      row.className = 'consult-tier';

      const left = document.createElement('div');
      const label = document.createElement('div');
      label.className = 'consult-tier__label';
      label.textContent = tier.label + (tier.sample ? ' (sample fee — confirm before publishing)' : '');
      left.appendChild(label);
      if (tier.description) {
        const desc = document.createElement('div');
        desc.className = 'consult-tier__desc';
        desc.textContent = tier.description;
        left.appendChild(desc);
      }
      if (active) {
        const payBtn = document.createElement('button');
        payBtn.type = 'button';
        payBtn.className = 'btn btn--primary consult-tier__pay';
        payBtn.textContent = 'Pay Now';
        payBtn.addEventListener('click', () => startPayment(tier, payment, site));
        left.appendChild(payBtn);
      }
      row.appendChild(left);

      const amount = document.createElement('div');
      amount.className = 'consult-tier__amount';
      amount.textContent = formatAmount(tier.amount, payment.currency);
      row.appendChild(amount);

      tiersEl.appendChild(row);
    });

    if (!active && unavailableEl) {
      unavailableEl.style.display = '';
      const note = payment.unavailableNote || "Online payment isn't switched on yet. Contact us and we'll arrange payment directly.";
      const wa = site.whatsappHref || 'https://wa.me/2349029607089';
      unavailableEl.innerHTML = `${note} <a href="${wa}" target="_blank" rel="noopener noreferrer">Chat on WhatsApp</a> or <a href="tel:${(site.phoneHref || 'tel:+2348027330095').replace('tel:', '')}">call us</a>.`;
    } else if (unavailableEl) {
      unavailableEl.style.display = 'none';
    }
  }

  function startPayment(tier, payment, site) {
    const emailInput = document.getElementById('pay-email');
    const email = emailInput ? emailInput.value.trim() : '';
    if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      alert('Please enter a valid email address first — Paystack sends your receipt there.');
      if (emailInput) emailInput.focus();
      return;
    }
    if (!window.PaystackPop) {
      alert('The payment checkout is still loading — please try again in a moment.');
      return;
    }
    const ref = 'MAS-' + Date.now().toString(36).toUpperCase();
    const handler = window.PaystackPop.setup({
      key: payment.publicKey,
      email: email,
      amount: Math.round(Number(tier.amount) || 0) * 100, // kobo
      currency: payment.currency || 'NGN',
      ref: ref,
      metadata: { tier: tier.label },
      callback: function () {
        const wa = (site.whatsappHref || 'https://wa.me/2349029607089').split('?')[0];
        const msg = encodeURIComponent(`Hi, I just paid for "${tier.label}" (ref: ${ref}). Confirming my payment.`);
        const box = document.getElementById('payment-unavailable');
        if (box) {
          box.style.display = '';
          box.innerHTML = `Payment complete — reference <strong>${ref}</strong>. As a safety check, please also confirm it with us: <a href="${wa}?text=${msg}" target="_blank" rel="noopener noreferrer">send this reference on WhatsApp</a>.`;
        }
      },
      onClose: function () { /* user closed the popup without paying — no action needed */ }
    });
    handler.openIframe();
  }

  document.addEventListener('lead-form:prepared', (e) => {
    if (e.detail && e.detail.formId === 'booking-form') unlock();
  });

  function boot() {
    if (isUnlocked()) {
      const locked = document.getElementById('payment-locked');
      const unlocked = document.getElementById('payment-unlocked');
      if (locked) locked.style.display = 'none';
      if (unlocked) unlocked.style.display = '';
    }
    if (window.CMS && window.CMS.data) render(); else document.addEventListener('cms:ready', render, { once: true });
  }

  if (document.readyState !== 'loading') {
    boot();
  } else {
    document.addEventListener('DOMContentLoaded', boot);
  }
})();
