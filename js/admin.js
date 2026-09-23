/* admin.js — the editor. Reads/writes the same content/site-data.json + localStorage
 * overrides that cms.js applies to the live site. No backend: "Save" keeps edits in
 * this browser (localStorage) so the preview updates instantly; "Export" downloads a
 * content/site-data.json you replace in the repo for a permanent, cross-device change. */
(function () {
  'use strict';

  const PASSKEY_STORAGE = 'cms-admin-unlocked';
  const DEFAULT_PASSPHRASE = 'letmein'; // client-side deterrent only — see the notice in the UI

  let baseData = null;   // content/site-data.json as shipped
  let workingData = null; // baseData + any local overrides, edited live in the form
  let currentSectionId = null;
  let dirty = false;

  const els = {};

  function $(sel, root) { return (root || document).querySelector(sel); }
  function $all(sel, root) { return Array.from((root || document).querySelectorAll(sel)); }

  function getPath(obj, path) {
    return path.split('.').reduce((acc, k) => (acc === undefined || acc === null ? undefined : acc[k]), obj);
  }
  function setPath(obj, path, value) {
    const keys = path.split('.');
    let node = obj;
    for (let i = 0; i < keys.length - 1; i++) {
      const k = keys[i];
      if (node[k] === undefined || node[k] === null || typeof node[k] !== 'object') {
        node[k] = /^\d+$/.test(keys[i + 1]) ? [] : {};
      }
      node = node[k];
    }
    node[keys[keys.length - 1]] = value;
  }

  // ---------------- Auth gate (client-side only; see banner in the UI) ----------------
  function checkUnlocked() {
    return sessionStorage.getItem(PASSKEY_STORAGE) === '1';
  }
  function tryUnlock(pass) {
    // A real deployment should replace this with server-side auth; this only
    // deters casual browsing since anyone can read this script.
    const stored = (window.CMS && window.CMS.data && window.CMS.data.meta && window.CMS.data.meta.adminPassphrase) || DEFAULT_PASSPHRASE;
    if (pass === stored) {
      sessionStorage.setItem(PASSKEY_STORAGE, '1');
      return true;
    }
    return false;
  }

  // ---------------- Boot ----------------
  async function boot() {
    els.gate = $('#admin-gate');
    els.app = $('#admin-app');
    els.gateForm = $('#gate-form');
    els.gateError = $('#gate-error');
    els.sidebar = $('#admin-sidebar');
    els.formPanel = $('#admin-form-panel');
    els.formTitle = $('#form-title');
    els.formBody = $('#form-body');
    els.preview = $('#preview-frame');
    els.previewPageLabel = $('#preview-page-label');
    els.saveBtn = $('#btn-save');
    els.exportBtn = $('#btn-export');
    els.importInput = $('#import-input');
    els.resetBtn = $('#btn-reset');
    els.dirtyBadge = $('#dirty-badge');
    els.logoutBtn = $('#btn-logout');
    els.searchInput = $('#field-search');

    els.gateForm.addEventListener('submit', onGateSubmit);
    els.saveBtn.addEventListener('click', onSave);
    els.exportBtn.addEventListener('click', onExport);
    els.importInput.addEventListener('change', onImport);
    els.resetBtn.addEventListener('click', onReset);
    els.logoutBtn.addEventListener('click', onLogout);
    els.searchInput.addEventListener('input', onSearch);

    if (checkUnlocked()) {
      await enterApp();
    } else {
      els.gate.style.display = '';
      els.app.style.display = 'none';
    }
  }

  function onGateSubmit(e) {
    e.preventDefault();
    const pass = $('#gate-pass').value;
    if (tryUnlock(pass)) {
      enterApp();
    } else {
      els.gateError.textContent = 'Incorrect passphrase.';
      els.gateError.style.display = '';
    }
  }

  function onLogout() {
    sessionStorage.removeItem(PASSKEY_STORAGE);
    location.reload();
  }

  async function enterApp() {
    els.gate.style.display = 'none';
    els.app.style.display = '';
    await loadData();
    buildSidebar();
    const first = window.ADMIN_SCHEMA.groups[0].sections[0];
    openSection(window.ADMIN_SCHEMA.groups[0].id, first.id);
  }

  async function loadData() {
    const res = await fetch('content/site-data.json', { cache: 'no-store' });
    baseData = await res.json();
    let overrides = null;
    try {
      const raw = localStorage.getItem('cms-overrides');
      overrides = raw ? JSON.parse(raw) : null;
    } catch (e) { overrides = null; }
    workingData = overrides ? deepMerge(clone(baseData), overrides) : clone(baseData);
  }

  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  function isPlainObject(v) { return v && typeof v === 'object' && !Array.isArray(v); }
  function deepMerge(base, patch) {
    if (Array.isArray(base) && Array.isArray(patch)) {
      const out = base.slice();
      patch.forEach((item, i) => { out[i] = isPlainObject(item) && isPlainObject(out[i]) ? deepMerge(out[i], item) : (item !== undefined ? item : out[i]); });
      return out;
    }
    if (isPlainObject(base) && isPlainObject(patch)) {
      const out = Object.assign({}, base);
      Object.keys(patch).forEach((k) => { out[k] = isPlainObject(patch[k]) || Array.isArray(patch[k]) ? deepMerge(base[k], patch[k]) : patch[k]; });
      return out;
    }
    return patch !== undefined ? patch : base;
  }

  // ---------------- Sidebar ----------------
  function buildSidebar() {
    els.sidebar.innerHTML = '';
    window.ADMIN_SCHEMA.groups.forEach((group) => {
      const groupEl = document.createElement('div');
      groupEl.className = 'admin-nav-group';
      const heading = document.createElement('div');
      heading.className = 'admin-nav-group__label';
      heading.textContent = group.label;
      groupEl.appendChild(heading);

      const list = document.createElement('div');
      list.className = 'admin-nav-group__items';
      group.sections.forEach((section) => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'admin-nav-item';
        btn.dataset.group = group.id;
        btn.dataset.section = section.id;
        btn.textContent = section.label;
        btn.addEventListener('click', () => openSection(group.id, section.id));
        list.appendChild(btn);
      });
      groupEl.appendChild(list);
      els.sidebar.appendChild(groupEl);
    });
  }

  function findSection(groupId, sectionId) {
    const group = window.ADMIN_SCHEMA.groups.find((g) => g.id === groupId);
    if (!group) return null;
    const section = group.sections.find((s) => s.id === sectionId);
    return section ? { group, section } : null;
  }

  function openSection(groupId, sectionId) {
    const found = findSection(groupId, sectionId);
    if (!found) return;
    currentSectionId = groupId + '/' + sectionId;

    $all('.admin-nav-item', els.sidebar).forEach((b) => {
      b.classList.toggle('is-active', b.dataset.group === groupId && b.dataset.section === sectionId);
    });

    renderForm(found.section);
    syncPreview(found.section);
  }

  // ---------------- Form rendering ----------------
  function renderForm(section) {
    els.formTitle.textContent = section.label;
    els.formBody.innerHTML = '';

    section.fields.forEach((field) => {
      els.formBody.appendChild(renderField(field));
    });

    if (section.richlist) {
      els.formBody.appendChild(renderRichlist(section.richlist));
    }
  }

  function fieldWrap(label, controlEl, path) {
    const wrap = document.createElement('div');
    wrap.className = 'admin-field';
    wrap.dataset.searchKey = (label + ' ' + path).toLowerCase();
    const lbl = document.createElement('label');
    lbl.textContent = label;
    lbl.setAttribute('for', 'f-' + path.replace(/\./g, '-'));
    wrap.appendChild(lbl);
    wrap.appendChild(controlEl);
    return wrap;
  }

  function renderField(field) {
    const val = getPath(workingData, field.path);
    const id = 'f-' + field.path.replace(/\./g, '-');

    if (field.type === 'textarea') {
      const ta = document.createElement('textarea');
      ta.id = id; ta.rows = 3;
      ta.value = val !== undefined && val !== null ? val : '';
      ta.addEventListener('input', () => onFieldChange(field.path, ta.value));
      return fieldWrap(field.label, ta, field.path);
    }

    if (field.type === 'image') {
      const container = document.createElement('div');
      container.className = 'admin-image-field';

      const row = document.createElement('div');
      row.className = 'admin-image-row';
      const input = document.createElement('input');
      input.type = 'text'; input.id = id; input.placeholder = 'https://\u2026 or leave blank';
      input.value = val || '';
      input.addEventListener('input', () => { onFieldChange(field.path, input.value); updateThumb(); });
      row.appendChild(input);

      const uploadBtn = document.createElement('label');
      uploadBtn.className = 'admin-upload-btn';
      uploadBtn.textContent = 'Upload\u2026';
      const fileInput = document.createElement('input');
      fileInput.type = 'file'; fileInput.accept = 'image/*'; fileInput.style.display = 'none';
      fileInput.addEventListener('change', () => {
        const file = fileInput.files[0];
        if (!file) return;
        if (file.size > 1.5 * 1024 * 1024) {
          alert('For a static, backend-free site, uploaded images are stored as data directly inside content/site-data.json. Please keep images under ~1.5MB, or better, host the image elsewhere and paste its URL instead.');
          return;
        }
        const reader = new FileReader();
        reader.onload = () => { input.value = reader.result; onFieldChange(field.path, reader.result); updateThumb(); };
        reader.readAsDataURL(file);
      });
      uploadBtn.appendChild(fileInput);
      row.appendChild(uploadBtn);
      container.appendChild(row);

      const thumb = document.createElement('img');
      thumb.className = 'admin-image-thumb';
      function updateThumb() {
        thumb.style.display = input.value ? '' : 'none';
        thumb.src = input.value || '';
      }
      updateThumb();
      container.appendChild(thumb);

      const hint = document.createElement('p');
      hint.className = 'admin-hint';
      hint.textContent = 'Blank = keep the generated placeholder graphic already on the site.';
      container.appendChild(hint);

      return fieldWrap(field.label, container, field.path);
    }

    // default: text
    const input = document.createElement('input');
    input.type = 'text'; input.id = id;
    input.value = val !== undefined && val !== null ? val : '';
    input.addEventListener('input', () => onFieldChange(field.path, input.value));
    return fieldWrap(field.label, input, field.path);
  }

  function renderRichlist(richlist) {
    const wrap = document.createElement('div');
    wrap.className = 'admin-richlist';

    const heading = document.createElement('h3');
    heading.textContent = richlist.label;
    wrap.appendChild(heading);

    const sampleNote = document.createElement('p');
    sampleNote.className = 'admin-hint';
    sampleNote.textContent = 'This article was drafted as sample content during the redesign. Edit freely, or replace it entirely.';
    wrap.appendChild(sampleNote);

    const list = document.createElement('div');
    list.className = 'admin-richlist__items';
    wrap.appendChild(list);

    function renderBlocks() {
      list.innerHTML = '';
      const blocks = getPath(workingData, richlist.path) || [];
      blocks.forEach((block, i) => {
        const row = document.createElement('div');
        row.className = 'admin-richlist__row';

        const controls = document.createElement('div');
        controls.className = 'admin-richlist__controls';

        const typeSelect = document.createElement('select');
        ['p', 'h3'].forEach((t) => {
          const opt = document.createElement('option');
          opt.value = t; opt.textContent = t === 'h3' ? 'Subheading' : 'Paragraph';
          if (block.type === t) opt.selected = true;
          typeSelect.appendChild(opt);
        });
        typeSelect.addEventListener('change', () => {
          blocks[i].type = typeSelect.value;
          onFieldChange(`${richlist.path}.${i}.type`, typeSelect.value, true);
        });
        controls.appendChild(typeSelect);

        const upBtn = document.createElement('button');
        upBtn.type = 'button'; upBtn.className = 'admin-icon-btn'; upBtn.title = 'Move up'; upBtn.textContent = '\u2191';
        upBtn.disabled = i === 0;
        upBtn.addEventListener('click', () => { [blocks[i - 1], blocks[i]] = [blocks[i], blocks[i - 1]]; commitBlocks(blocks); });
        controls.appendChild(upBtn);

        const downBtn = document.createElement('button');
        downBtn.type = 'button'; downBtn.className = 'admin-icon-btn'; downBtn.title = 'Move down'; downBtn.textContent = '\u2193';
        downBtn.disabled = i === blocks.length - 1;
        downBtn.addEventListener('click', () => { [blocks[i + 1], blocks[i]] = [blocks[i], blocks[i + 1]]; commitBlocks(blocks); });
        controls.appendChild(downBtn);

        const delBtn = document.createElement('button');
        delBtn.type = 'button'; delBtn.className = 'admin-icon-btn admin-icon-btn--danger'; delBtn.title = 'Remove'; delBtn.textContent = '\u00d7';
        delBtn.addEventListener('click', () => { blocks.splice(i, 1); commitBlocks(blocks); });
        controls.appendChild(delBtn);

        row.appendChild(controls);

        const ta = document.createElement('textarea');
        ta.rows = block.type === 'h3' ? 1 : 3;
        ta.value = block.text || '';
        ta.addEventListener('input', () => { blocks[i].text = ta.value; onFieldChange(`${richlist.path}.${i}.text`, ta.value, true); });
        row.appendChild(ta);

        list.appendChild(row);
      });
    }

    function commitBlocks(blocks) {
      setPath(workingData, richlist.path, blocks);
      markDirty();
      renderBlocks();
      livePreviewUpdate();
    }

    const addRow = document.createElement('div');
    addRow.className = 'admin-richlist__add';
    const addP = document.createElement('button');
    addP.type = 'button'; addP.className = 'btn-secondary'; addP.textContent = '+ Add paragraph';
    addP.addEventListener('click', () => {
      const blocks = getPath(workingData, richlist.path) || [];
      blocks.push({ type: 'p', text: '' });
      commitBlocks(blocks);
    });
    const addH = document.createElement('button');
    addH.type = 'button'; addH.className = 'btn-secondary'; addH.textContent = '+ Add subheading';
    addH.addEventListener('click', () => {
      const blocks = getPath(workingData, richlist.path) || [];
      blocks.push({ type: 'h3', text: '' });
      commitBlocks(blocks);
    });
    addRow.appendChild(addP);
    addRow.appendChild(addH);
    wrap.appendChild(addRow);

    renderBlocks();
    return wrap;
  }

  function onFieldChange(path, value, skipSet) {
    if (!skipSet) setPath(workingData, path, value);
    markDirty();
    livePreviewUpdate();
  }

  function markDirty() {
    dirty = true;
    els.dirtyBadge.style.display = '';
  }
  function clearDirty() {
    dirty = false;
    els.dirtyBadge.style.display = 'none';
  }

  // ---------------- Search / filter fields across the current form ----------------
  function onSearch() {
    const q = els.searchInput.value.trim().toLowerCase();
    $all('.admin-field', els.formBody).forEach((f) => {
      f.style.display = !q || f.dataset.searchKey.includes(q) ? '' : 'none';
    });
  }

  // ---------------- Live preview ----------------
  function resolvePreviewPage(section) {
    if (section.preview) return section.preview;
    if (typeof section.insightIndex === 'number') {
      const slug = getPath(workingData, `insights.${section.insightIndex}.slug`);
      return slug ? slug + '.html' : 'insights.html';
    }
    return 'index.html';
  }

  function syncPreview(section) {
    const page = resolvePreviewPage(section);
    els.previewPageLabel.textContent = page;
    const url = page + '?admin-preview=1';
    if (!els.preview.src.endsWith(url)) {
      els.preview.src = url;
    } else {
      livePreviewUpdate();
    }
  }

  function livePreviewUpdate() {
    try {
      const win = els.preview.contentWindow;
      if (win && win.CMS) {
        win.CMS.baseData = win.CMS.baseData || baseData;
        const merged = win.CMS.deepMerge(win.CMS.baseData, workingData);
        win.CMS.data = merged;
        applyToDoc(win.document, merged, win.CMS);
      }
    } catch (e) { /* preview not ready yet */ }
  }

  function applyToDoc(doc, data, CMS) {
    doc.querySelectorAll('[data-cms]').forEach((el) => {
      const v = CMS.getPath(data, el.getAttribute('data-cms'));
      if (v !== undefined && v !== null) el.textContent = v;
    });
    doc.querySelectorAll('[data-cms-attr]').forEach((el) => {
      let map; try { map = JSON.parse(el.getAttribute('data-cms-attr')); } catch (e) { return; }
      Object.keys(map).forEach((attr) => {
        const v = CMS.getPath(data, map[attr]);
        if (v !== undefined && v !== null && v !== '') el.setAttribute(attr, v);
      });
    });
  }

  els_onPreviewLoad_bind();
  function els_onPreviewLoad_bind() {
    document.addEventListener('DOMContentLoaded', () => {
      const frame = document.getElementById('preview-frame');
      if (!frame) return;
      frame.addEventListener('load', () => pollUntilCmsReady());
    });
  }

  function pollUntilCmsReady(attempt) {
    attempt = attempt || 0;
    try {
      const win = els.preview.contentWindow;
      if (win && win.CMS && win.CMS.data) {
        livePreviewUpdate();
        return;
      }
    } catch (e) { /* cross-origin or not ready */ }
    if (attempt < 40) setTimeout(() => pollUntilCmsReady(attempt + 1), 50);
  }

  // ---------------- Save / Export / Import / Reset ----------------
  function diffFromBase(base, working) {
    // Store the full working tree as the override; simplest and robust for this scale of data.
    return working;
  }

  function onSave() {
    const overrides = diffFromBase(baseData, workingData);
    localStorage.setItem('cms-overrides', JSON.stringify(overrides));
    clearDirty();
    flash(els.saveBtn, 'Saved');
  }

  function onExport() {
    const blob = new Blob([JSON.stringify(workingData, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = 'site-data.json';
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  function onImport(e) {
    const file = e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(reader.result);
        workingData = parsed;
        markDirty();
        const [g, s] = (currentSectionId || 'site/site-identity').split('/');
        const found = findSection(g, s);
        if (found) { renderForm(found.section); livePreviewUpdate(); }
        flash(els.importInput.closest('label') || els.exportBtn, 'Imported');
      } catch (err) {
        alert('That file is not valid JSON.');
      }
    };
    reader.readAsText(file);
    e.target.value = '';
  }

  function onReset() {
    if (!confirm('Discard all local edits and reload the original content/site-data.json? This cannot be undone.')) return;
    localStorage.removeItem('cms-overrides');
    workingData = clone(baseData);
    clearDirty();
    const [g, s] = (currentSectionId || 'site/site-identity').split('/');
    const found = findSection(g, s);
    if (found) { renderForm(found.section); livePreviewUpdate(); }
  }

  function flash(el, text) {
    if (!el) return;
    const original = el.textContent;
    el.textContent = text;
    setTimeout(() => { el.textContent = original; }, 1400);
  }

  window.addEventListener('beforeunload', (e) => {
    if (dirty) { e.preventDefault(); e.returnValue = ''; }
  });

  document.addEventListener('DOMContentLoaded', boot);
})();
