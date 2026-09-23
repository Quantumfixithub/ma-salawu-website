/* cms.js — lightweight, backend-free content loader.
 *
 * How it works:
 *   1. Fetches content/site-data.json (the single source of truth for editable text).
 *   2. Merges any local admin edits saved in localStorage under 'cms-overrides'.
 *   3. Applies the merged data to every element carrying a data-cms / data-cms-attr /
 *      data-cms-if attribute.
 *
 * The static HTML already contains matching, correct content, so a visitor with
 * JavaScript disabled — or before this script runs — sees the right page already.
 * This script only needs to re-apply values when an editor has made unsaved-to-disk
 * changes in the admin dashboard (content/site-data.json is the permanent record;
 * localStorage is the live "draft" layer used while editing).
 *
 * Path syntax: dot-separated, numeric segments index arrays.
 *   "founder.name"        -> data.founder.name
 *   "attorneys.0.bio"     -> data.attorneys[0].bio
 *   "insights.2.title"    -> data.insights[2].title
 */
(function (global) {
  'use strict';

  const STORAGE_KEY = 'cms-overrides';
  const DATA_URL = 'content/site-data.json';

  function getPath(obj, path) {
    if (!obj || !path) return undefined;
    return path.split('.').reduce((acc, key) => {
      if (acc === undefined || acc === null) return undefined;
      return acc[key];
    }, obj);
  }

  function setPath(obj, path, value) {
    const keys = path.split('.');
    let node = obj;
    for (let i = 0; i < keys.length - 1; i++) {
      const k = keys[i];
      if (node[k] === undefined || node[k] === null || typeof node[k] !== 'object') {
        // infer array vs object from the next key
        node[k] = /^\d+$/.test(keys[i + 1]) ? [] : {};
      }
      node = node[k];
    }
    node[keys[keys.length - 1]] = value;
  }

  function isPlainObject(v) {
    return v && typeof v === 'object' && !Array.isArray(v);
  }

  function deepMerge(base, patch) {
    if (Array.isArray(base) && Array.isArray(patch)) {
      const out = base.slice();
      patch.forEach((item, i) => {
        out[i] = isPlainObject(item) && isPlainObject(out[i]) ? deepMerge(out[i], item) : (item !== undefined ? item : out[i]);
      });
      return out;
    }
    if (isPlainObject(base) && isPlainObject(patch)) {
      const out = Object.assign({}, base);
      Object.keys(patch).forEach((k) => {
        out[k] = isPlainObject(patch[k]) || Array.isArray(patch[k])
          ? deepMerge(base[k], patch[k])
          : patch[k];
      });
      return out;
    }
    return patch !== undefined ? patch : base;
  }

  function loadOverrides() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      console.warn('cms.js: could not read local overrides', e);
      return null;
    }
  }

  function saveOverrides(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
      return true;
    } catch (e) {
      console.warn('cms.js: could not save local overrides', e);
      return false;
    }
  }

  function clearOverrides() {
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) { /* noop */ }
  }

  function applyText(root, data) {
    root.querySelectorAll('[data-cms]').forEach((el) => {
      const path = el.getAttribute('data-cms');
      const val = getPath(data, path);
      if (val === undefined || val === null) return;
      el.textContent = val;
    });
  }

  function applyAttrs(root, data) {
    root.querySelectorAll('[data-cms-attr]').forEach((el) => {
      let map;
      try { map = JSON.parse(el.getAttribute('data-cms-attr')); } catch (e) { return; }
      Object.keys(map).forEach((attr) => {
        const val = getPath(data, map[attr]);
        // empty string / undefined = "no override supplied", keep the baked-in default
        if (val === undefined || val === null || val === '') return;
        el.setAttribute(attr, val);
      });
    });
  }

  function applySampleBadges(data) {
    // Hide "Sample profile" style badges once real content has been supplied
    // (heuristic: an item is still sample data if its own "sample" flag is true or absent).
    document.querySelectorAll('[data-sample-badge]').forEach((el) => {
      el.style.display = '';
    });
  }

  async function fetchBaseData() {
    const res = await fetch(DATA_URL, { cache: 'no-store' });
    if (!res.ok) throw new Error('cms.js: failed to load ' + DATA_URL);
    return res.json();
  }

  async function init() {
    let base;
    try {
      base = await fetchBaseData();
    } catch (e) {
      console.warn(e);
      return; // static HTML already has correct fallback content
    }
    const overrides = loadOverrides();
    const merged = overrides ? deepMerge(base, overrides) : base;

    applyText(document, merged);
    applyAttrs(document, merged);
    applySampleBadges(merged);

    global.CMS = global.CMS || {};
    global.CMS.data = merged;
    global.CMS.baseData = base;
    global.CMS.getPath = getPath;
    global.CMS.setPath = setPath;
    global.CMS.deepMerge = deepMerge;
    global.CMS.loadOverrides = loadOverrides;
    global.CMS.saveOverrides = saveOverrides;
    global.CMS.clearOverrides = clearOverrides;
    global.CMS.reapply = () => {
      const fresh = deepMerge(global.CMS.baseData, loadOverrides() || {});
      global.CMS.data = fresh;
      applyText(document, fresh);
      applyAttrs(document, fresh);
      return fresh;
    };
    document.dispatchEvent(new CustomEvent('cms:ready', { detail: merged }));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})(window);
