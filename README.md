# M.A Salawu & Co — Website

Static, multi-page website. No build step, no framework, no dependencies beyond Google Fonts and Font Awesome-free inline SVG icons.

## Running locally

Any static file server works. From this folder:

```
python3 -m http.server 8000
```

Then open `http://localhost:8000`. Opening `index.html` directly by double-clicking also works, but a local server is closer to production (fixes some relative-path edge cases and lets `fetch` calls in `js/forms.js` work once a backend is wired up).

## Structure

```
/
├── index.html, about.html, practice-areas.html, [practice-area].html ×7
├── attorneys.html, insights.html, insights-[slug].html ×6, careers.html
├── contact.html, privacy-policy.html, terms.html, 404.html
├── css/
│   ├── style.css        — tokens, reset, typography, layout primitives
│   ├── components.css    — header, nav, footer, cards, forms, widgets
│   ├── pages.css         — hero variants, page-specific section layouts
│   └── responsive.css    — breakpoints
├── js/
│   ├── navigation.js      — header state, mobile menu, accordions
│   ├── animations.js      — scroll reveals, hero word stagger, counters, testimonial carousel
│   ├── forms.js           — contact form validation + success/error states
│   ├── insights.js        — insights filter, search, load-more
│   └── main.js            — back-to-top, footer year, newsletter micro-form
├── img/{hero,attorneys,practice,insights,general}/
├── build.py               — generator script (see note below)
└── gen_placeholders.py    — generates the placeholder images in /img
```

### About `build.py`

The header, footer, mobile nav, and per-practice-area page structure repeat across 23 pages. Rather than hand-maintain 23 near-identical copies of a shared header, this repo includes `build.py`, a small Python generator that assembles each page from shared templates plus per-page content. It was used once to produce the HTML files in this folder — **the output is plain, static HTML with no server-side dependency.** You don't need to run it again unless you want to change something that touches every page at once (e.g. the nav structure or footer). If you'd rather hand-edit individual HTML files going forward, that's fine — they don't depend on the script.

## Placeholders / TODO before launch

- **Images**: every file in `/img` is a generated placeholder (dark green background, gold border, label). Replace with real photography — office exterior/interior, attorney headshots, article images. `gen_placeholders.py` shows the exact filenames expected if you want to regenerate placeholders after adding new sections.
- **Attorneys**: only the founder, Barrister M.A Salawu, was named in the source content. The other three cards on `attorneys.html` are explicitly marked placeholders — replace with real names, roles, and bios, or remove the cards.
- **Testimonials**: the original page attributed quotes to "Olomu & Co Chambers" and "LexNigeria," neither of which matches this firm. Those references were removed rather than invented. Confirm the testimonials are genuine and attributable before publishing.
- **Insights articles**: all six articles are sample content demonstrating the layout, clearly noted as such in the page copy. Replace with the firm's real articles.
- **Phone number**: the second phone number in the original source (`70968786064`) is 11 digits, one more than a standard Nigerian number. Flagged in `build.py` — confirm the correct number.
- **Social links**: Facebook/X/LinkedIn/Instagram icons in the footer link to `#` pending real profile URLs.
- **Map**: `contact.html` embeds a generic Google Maps search for "Badagry, Lagos State" — replace with an embed pinned to the exact office address once you have the map link from Google Maps.
- **Contact form backend**: `js/forms.js` handles validation and success/error UI, but does not send email. `submitToBackend()` in that file is where you wire up a real endpoint (PHP script, Formspree, etc).
- **Canonical URLs**: `https://www.masalawuandco.com` is a placeholder domain used in `<link rel="canonical">` and Open Graph tags across every page. Update `SITE_URL_PLACEHOLDER` in `build.py` (or find-and-replace across the HTML files) once the real domain is live.
- **Privacy Policy / Terms**: both pages are structurally complete but contain placeholder legal text. Have the firm review and finalize before publishing.

## External dependencies

- Google Fonts: Fraunces (headings) and Inter (body/UI), loaded via `<link>` in the `<head>` of every page.
- No JS libraries. No Font Awesome — icons are inline SVG in `build.py` / hand-written in the HTML, so there's nothing to fetch from a CDN and no icon-font flash.

## Notes on what changed from the original single-page site

- Converted from one HTML file with anchor-based navigation (`#Practice Areas`, broken/space-containing `href` values) into 23 real, independently linkable pages.
- Rewrote copy for grammar and consistency ("Corperate", "Oraganizations", "Africa's" used as a plural, etc.) without changing the underlying facts.
- Removed the "Banking & Finance" service that appeared in the footer's Quick Links but nowhere else on the original site, since no content backed it up. Add it as an eighth practice area (with real content) if the firm wants it included.
- Practice area anchor links (`href="#Practice Areas"`, `href="#Attorneys"`, etc.) are now real page links.
