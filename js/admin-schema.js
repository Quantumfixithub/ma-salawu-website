/* admin-schema.js — declares every editable field on the site.
 * The admin app (admin.js) reads this to generate forms; nothing here executes on its own.
 * field.type: "text" | "textarea" | "richlist" (array of {type:h3|p, text}) | "image"
 */
(function (global) {
  'use strict';

  function practiceAreaFields(i, title) {
    return {
      id: 'practice-' + i,
      label: title,
      preview: 'practice-areas.html',
      fields: [
        { path: `practiceAreas.${i}.num`, label: 'Number', type: 'text' },
        { path: `practiceAreas.${i}.title`, label: 'Title', type: 'text' },
        { path: `practiceAreas.${i}.shortDesc`, label: 'Short description (card & homepage)', type: 'textarea' },
        { path: `practiceAreas.${i}.points.0`, label: 'Point 1 (featured card only)', type: 'text' },
        { path: `practiceAreas.${i}.points.1`, label: 'Point 2 (featured card only)', type: 'text' },
        { path: `practiceAreas.${i}.points.2`, label: 'Point 3 (featured card only)', type: 'text' },
      ]
    };
  }

  function attorneyFields(pathPrefix, label, preview) {
    return {
      id: 'attorney-' + pathPrefix.replace(/\./g, '-'),
      label,
      preview: preview || 'attorneys.html',
      fields: [
        { path: `${pathPrefix}.name`, label: 'Full name', type: 'text' },
        { path: `${pathPrefix}.role`, label: 'Role / title', type: 'text' },
        { path: `${pathPrefix}.areas`, label: 'Practice areas (comma separated)', type: 'text' },
        { path: `${pathPrefix}.bio`, label: 'Short biography', type: 'textarea' },
        { path: `${pathPrefix}.monogram`, label: 'Avatar initials (used until a real photo is supplied)', type: 'text' },
        { path: `${pathPrefix}.photo`, label: 'Photo URL (leave blank to keep the generated avatar)', type: 'image' },
      ]
    };
  }

  function insightFields(i, title) {
    // body blocks are generated dynamically per-article in admin.js (richlist),
    // this schema only covers the fixed metadata fields.
    return {
      id: 'insight-' + i,
      label: title,
      preview: null, // resolved at runtime from insights.{i}.slug
      insightIndex: i,
      fields: [
        { path: `insights.${i}.title`, label: 'Title', type: 'text' },
        { path: `insights.${i}.category`, label: 'Category', type: 'text' },
        { path: `insights.${i}.date`, label: 'Date (YYYY-MM-DD)', type: 'text' },
        { path: `insights.${i}.dateDisplay`, label: 'Date (display text)', type: 'text' },
        { path: `insights.${i}.excerpt`, label: 'Excerpt (used on preview cards)', type: 'textarea' },
      ],
      richlist: { path: `insights.${i}.body`, label: 'Article body' }
    };
  }

  const SCHEMA = {
    groups: [
      {
        id: 'site',
        label: 'Site Settings',
        icon: 'settings',
        sections: [
          {
            id: 'site-identity',
            label: 'Identity & contact',
            preview: 'index.html',
            fields: [
              { path: 'site.name', label: 'Firm name', type: 'text' },
              { path: 'site.nameSuffix', label: 'Name suffix (e.g. " & CO")', type: 'text' },
              { path: 'site.tagline', label: 'Tagline', type: 'text' },
              { path: 'site.phoneDisplay', label: 'Phone (display)', type: 'text' },
              { path: 'site.phoneHref', label: 'Phone (tel: link)', type: 'text' },
              { path: 'site.email', label: 'Email address', type: 'text' },
              { path: 'site.emailHref', label: 'Email (mailto: link)', type: 'text' },
              { path: 'site.whatsappHref', label: 'WhatsApp link', type: 'text' },
              { path: 'site.whatsappLabel', label: 'WhatsApp button label', type: 'text' },
              { path: 'site.addressLine1', label: 'Address line 1', type: 'text' },
              { path: 'site.addressLine2', label: 'Address line 2', type: 'text' },
              { path: 'site.addressLine3', label: 'Address line 3', type: 'text' },
              { path: 'site.addressOneLine', label: 'Address (single line, used in mobile menu)', type: 'text' },
              { path: 'site.hours', label: 'Office hours', type: 'text' },
              { path: 'site.footerDescription', label: 'Footer description', type: 'textarea' },
              { path: 'site.copyrightYear', label: 'Copyright year', type: 'text' },
            ]
          },
          {
            id: 'site-admin', label: 'Editor access', preview: 'index.html',
            fields: [
              { path: 'meta.adminPassphrase', label: 'Admin editor passphrase (see notice on the login screen \u2014 this is a soft deterrent, not real security)', type: 'text' },
            ]
          }
        ]
      },
      {
        id: 'home',
        label: 'Homepage',
        icon: 'home',
        sections: [
          {
            id: 'hero', label: 'Hero', preview: 'index.html',
            fields: [
              { path: 'hero.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'hero.titleLines.0', label: 'Headline \u2014 line 1', type: 'text' },
              { path: 'hero.titleLines.1', label: 'Headline \u2014 line 2', type: 'text' },
              { path: 'hero.titleLines.2', label: 'Headline \u2014 line 3', type: 'text' },
              { path: 'hero.titleLines.3', label: 'Headline \u2014 line 4', type: 'text' },
              { path: 'hero.titleLines.4', label: 'Headline \u2014 line 5', type: 'text' },
              { path: 'hero.lede', label: 'Supporting paragraph', type: 'textarea' },
              { path: 'hero.primaryCta', label: 'Primary button label', type: 'text' },
              { path: 'hero.secondaryCta', label: 'Secondary button label', type: 'text' },
            ]
          },
          {
            id: 'about', label: 'About section', preview: 'index.html',
            fields: [
              { path: 'about.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'about.title', label: 'Heading', type: 'textarea' },
              { path: 'about.lead', label: 'Lead paragraph', type: 'textarea' },
              { path: 'about.body', label: 'Body paragraph', type: 'textarea' },
              { path: 'about.caption', label: 'Image caption', type: 'text' },
              { path: 'about.linkLabel', label: 'Link label', type: 'text' },
            ]
          },
          {
            id: 'values', label: 'Values (4)', preview: 'index.html',
            fields: [0,1,2,3].flatMap((i) => ([
              { path: `values.${i}.num`, label: `Value ${i+1} \u2014 number`, type: 'text' },
              { path: `values.${i}.title`, label: `Value ${i+1} \u2014 title`, type: 'text' },
              { path: `values.${i}.body`, label: `Value ${i+1} \u2014 body`, type: 'textarea' },
            ]))
          },
          {
            id: 'founder', label: 'Founder card (homepage)', preview: 'index.html',
            fields: [
              { path: 'founder.name', label: 'Name', type: 'text' },
              { path: 'founder.role', label: 'Role', type: 'text' },
              { path: 'founder.areas', label: 'Practice areas', type: 'text' },
              { path: 'founder.bio', label: 'Bio', type: 'textarea' },
              { path: 'founder.monogram', label: 'Avatar initials', type: 'text' },
              { path: 'founder.photo', label: 'Photo URL (optional)', type: 'image' },
            ]
          },
          {
            id: 'whatToExpect', label: '"What to expect" list', preview: 'index.html',
            fields: [0,1,2].flatMap((i) => ([
              { path: `whatToExpect.${i}.num`, label: `Item ${i+1} \u2014 number`, type: 'text' },
              { path: `whatToExpect.${i}.text`, label: `Item ${i+1} \u2014 text`, type: 'text' },
            ]))
          },
          {
            id: 'cta', label: 'Final call to action', preview: 'index.html',
            fields: [
              { path: 'cta.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'cta.title', label: 'Heading', type: 'textarea' },
              { path: 'cta.lede', label: 'Supporting text', type: 'textarea' },
            ]
          }
        ]
      },
      {
        id: 'practice', label: 'Practice Areas', icon: 'briefcase',
        sections: [
          practiceAreaFields(0, 'Corporate Law'),
          practiceAreaFields(1, 'Commercial Litigation'),
          practiceAreaFields(2, 'Real Estate'),
          practiceAreaFields(3, 'Intellectual Property'),
          practiceAreaFields(4, 'Family Law'),
          practiceAreaFields(5, 'Contract Law'),
          practiceAreaFields(6, 'Tax Law'),
        ]
      },
      {
        id: 'attorneys', label: 'Attorneys', icon: 'people',
        sections: [
          attorneyFields('founder', 'Founder \u2014 M. A. Salawu, Esq.'),
          attorneyFields('attorneys.0', 'Attorney \u2014 Adaeze N. Chukwu'),
          attorneyFields('attorneys.1', 'Attorney \u2014 Tunde B. Fashina'),
          attorneyFields('attorneys.2', 'Attorney \u2014 Ngozi P. Eze'),
        ]
      },
      {
        id: 'insights', label: 'Insights Articles', icon: 'document',
        sections: [
          insightFields(0, 'A practical compliance checklist for Nigerian SMEs'),
          insightFields(1, 'Why title due diligence matters before you pay for land in Lagos'),
          insightFields(2, 'Five clauses worth a second look before you sign'),
          insightFields(3, 'When to register a trademark, and why timing matters'),
          insightFields(4, 'What a compliant employment contract actually needs to say'),
          insightFields(5, 'Arbitration or litigation: how we help clients decide'),
        ]
      },
      {
        id: 'consultation', label: 'Booking, Chat & Payment', icon: 'calendar',
        sections: [
          {
            id: 'consult-intro', label: 'Booking page intro', preview: 'consultation.html',
            fields: [
              { path: 'consultation.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'consultation.title', label: 'Heading', type: 'text' },
              { path: 'consultation.lede', label: 'Supporting text', type: 'textarea' },
              { path: 'consultation.formIntro', label: 'Form intro line', type: 'textarea' },
            ]
          },
          {
            id: 'consult-chat', label: 'Live chat card', preview: 'consultation.html',
            fields: [
              { path: 'consultation.chat.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'consultation.chat.title', label: 'Heading', type: 'text' },
              { path: 'consultation.chat.body', label: 'Body text', type: 'textarea' },
              { path: 'consultation.chat.note', label: 'Small note', type: 'text' },
            ]
          },
          {
            id: 'consult-payment', label: 'Payment settings', preview: 'consultation.html',
            fields: [
              { path: 'consultation.payment.eyebrow', label: 'Eyebrow', type: 'text' },
              { path: 'consultation.payment.title', label: 'Heading', type: 'text' },
              { path: 'consultation.payment.body', label: 'Intro text', type: 'textarea' },
              { path: 'consultation.payment.lockedNote', label: 'Message shown before the booking form is submitted', type: 'textarea' },
              { path: 'consultation.payment.enabled', label: 'Enabled ("true" or "false" — payment only goes live with a real key below)', type: 'text' },
              { path: 'consultation.payment.publicKey', label: 'Paystack public key (pk_live_... or pk_test_...)', type: 'text' },
              { path: 'consultation.payment.currency', label: 'Currency code', type: 'text' },
              { path: 'consultation.payment.unavailableNote', label: 'Message shown while payment is off', type: 'textarea' },
              { path: 'consultation.payment.confirmNote', label: 'Post-payment confirmation note', type: 'textarea' },
              { path: 'consultation.payment.tiers.0.label', label: 'Fee — label', type: 'text' },
              { path: 'consultation.payment.tiers.0.amount', label: 'Fee — amount in Naira (number, no symbol)', type: 'text' },
              { path: 'consultation.payment.tiers.0.description', label: 'Fee — description', type: 'textarea' },
              { path: 'consultation.payment.tiers.1.label', label: 'Second fee — label (optional, leave blank if you only charge one fee)', type: 'text' },
              { path: 'consultation.payment.tiers.1.amount', label: 'Second fee — amount in Naira', type: 'text' },
              { path: 'consultation.payment.tiers.1.description', label: 'Second fee — description', type: 'textarea' },
            ]
          }
        ]
      }
    ]
  };

  global.ADMIN_SCHEMA = SCHEMA;
})(window);
