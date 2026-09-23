/* lead-form.js — validates a form, then hands the compiled message to WhatsApp
 * and/or email so it is actually delivered. There is no backend on this site,
 * so rather than pretend a message was "received" (as the previous placeholder
 * did), this opens the real channel the firm already uses and lets the visitor
 * send it themselves with one click.
 *
 * Markup contract, per form:
 *   <form data-lead-form data-subject="New enquiry">
 *     <div class="field"><label>Full Name</label><input name="name" required></div>
 *     ...
 *     <div class="form-status" role="alert"></div>
 *     <div class="lead-form__actions"></div>   <!-- populated after validation -->
 *     <button type="submit">Prepare Message</button>
 *   </form>
 */
(function () {
  'use strict';

  function validateField(field) {
    const input = field.querySelector('input, textarea, select');
    if (!input) return true;
    let valid = input.checkValidity();
    if (input.type === 'email' && input.value.trim()) {
      valid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
    }
    if (input.type === 'tel' && input.value.trim()) {
      valid = /^[0-9+()\-\s]{7,}$/.test(input.value.trim());
    }
    field.classList.toggle('field--error', !valid);
    return valid;
  }

  function fieldLabel(field) {
    const label = field.querySelector('label');
    return label ? label.textContent.trim() : '';
  }

  function buildMessage(form, subject) {
    const lines = [subject, ''];
    Array.from(form.querySelectorAll('.field')).forEach((field) => {
      const input = field.querySelector('input, textarea, select');
      if (!input || !input.value.trim()) return;
      let value = input.value.trim();
      if (input.tagName === 'SELECT') {
        const opt = input.options[input.selectedIndex];
        value = opt ? opt.textContent.trim() : value;
      }
      lines.push(`${fieldLabel(field)}: ${value}`);
    });
    return lines.join('\n');
  }

  function getSiteContact() {
    const data = (window.CMS && window.CMS.data && window.CMS.data.site) || {};
    return {
      whatsapp: data.whatsappHref || 'https://wa.me/2349029607089',
      email: data.emailHref || 'mailto:masalawu11@gmail.com'
    };
  }

  function renderActions(container, message, subjectForEmail) {
    container.innerHTML = '';
    const contact = getSiteContact();

    const intro = document.createElement('p');
    intro.className = 'lead-form__ready';
    intro.textContent = 'Your message is ready. Send it with one tap:';
    container.appendChild(intro);

    const row = document.createElement('div');
    row.className = 'lead-form__buttons';

    const waUrl = contact.whatsapp.split('?')[0] + '?text=' + encodeURIComponent(message);
    const waLink = document.createElement('a');
    waLink.href = waUrl;
    waLink.target = '_blank';
    waLink.rel = 'noopener noreferrer';
    waLink.className = 'btn btn--primary';
    waLink.innerHTML = 'Send via WhatsApp <svg class="btn-arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" width="14" height="14" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4"/></svg>';
    row.appendChild(waLink);

    const mailUrl = contact.email + '?subject=' + encodeURIComponent(subjectForEmail) + '&body=' + encodeURIComponent(message);
    const mailLink = document.createElement('a');
    mailLink.href = mailUrl;
    mailLink.className = 'btn btn--ghost';
    mailLink.textContent = 'Send via Email';
    row.appendChild(mailLink);

    container.appendChild(row);

    const preview = document.createElement('details');
    preview.className = 'lead-form__preview';
    const summary = document.createElement('summary');
    summary.textContent = 'View message';
    preview.appendChild(summary);
    const pre = document.createElement('pre');
    pre.textContent = message;
    preview.appendChild(pre);
    container.appendChild(preview);
  }

  document.querySelectorAll('[data-lead-form]').forEach((form) => {
    const status = form.querySelector('.form-status');
    const actions = form.querySelector('.lead-form__actions');
    const submitBtn = form.querySelector('[type="submit"]');
    const subject = form.dataset.subject || 'New enquiry from the website';

    form.querySelectorAll('.field').forEach((field) => {
      const input = field.querySelector('input, textarea, select');
      if (!input) return;
      input.addEventListener('blur', () => validateField(field));
      input.addEventListener('input', () => { if (field.classList.contains('field--error')) validateField(field); });
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const fields = Array.from(form.querySelectorAll('.field'));
      const allValid = fields.map(validateField).every(Boolean);

      if (status) status.classList.remove('is-visible', 'form-status--success', 'form-status--error');
      if (actions) actions.innerHTML = '';

      if (!allValid) {
        if (status) {
          status.textContent = 'Please check the highlighted fields and try again.';
          status.classList.add('is-visible', 'form-status--error');
        }
        const firstError = form.querySelector('.field--error input, .field--error textarea, .field--error select');
        if (firstError) firstError.focus();
        return;
      }

      const message = buildMessage(form, subject);
      if (actions) renderActions(actions, message, subject);
      if (status) {
        status.textContent = '';
        status.classList.remove('is-visible');
      }
      if (submitBtn) submitBtn.style.display = 'none';
      if (actions) actions.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

      document.dispatchEvent(new CustomEvent('lead-form:prepared', { detail: { formId: form.id, form } }));
    });
  });
})();
