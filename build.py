# -*- coding: utf-8 -*-
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

SITE_NAME = "M.A SALAWU & CO"
SITE_URL_PLACEHOLDER = "https://www.masalawuandco.com"  # TODO: replace with live domain
PHONE_1 = "+234 802 733 0095"
PHONE_1_TEL = "+2348027330095"
PHONE_2 = "+234 709 687 8606"  # TODO: confirm final digit — source listed "70968786064" (11 digits, one too many for a Nigerian number). Flagging for firm to verify.
PHONE_2_TEL = "+2347096878606"
EMAIL = "masalawu11@gmail.com"
ADDRESS_LINE1 = "Suit 1, Ground Floor, Hotel De James Complex"
ADDRESS_LINE2 = "Opp. 1st Bank Plc, Joseph Dosu Way"
ADDRESS_LINE3 = "Badagry, Lagos State, Nigeria"
WHATSAPP_NUMBER = "2349029607089"
HOURS = "Monday – Friday, 9:00 AM – 5:00 PM"

# ---------------------------------------------------------------- icons ----
ICONS = {
    "mark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M12 3l7 3.5v2H5v-2L12 3z"/><path d="M5 9v9M19 9v9M3 20h18M7 12v4M11 12v4M13 12v4M17 12v4"/></svg>',
    "arrow": '<svg class="btn-arrow" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" width="14" height="14"><path d="M2 8h11M9 4l4 4-4 4"/></svg>',
    "check": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 10.5l3.8 3.8L16 6"/></svg>',
    "caret": '<svg class="nav-caret" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M2 3.5L5 6.5L8 3.5"/></svg>',
    "whatsapp": '<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16.02 3C9.4 3 4 8.4 4 15.02c0 2.4.66 4.63 1.8 6.55L4 29l7.6-1.75c1.84.97 3.94 1.53 6.17 1.53h.01c6.62 0 12.02-5.4 12.02-12.02C29.8 8.4 24.4 3 16.02 3zm0 22.1c-1.98 0-3.83-.55-5.4-1.5l-.39-.23-4.5 1.04 1.07-4.4-.25-.4a9.9 9.9 0 01-1.58-5.6c0-5.48 4.47-9.95 9.96-9.95 5.5 0 9.96 4.47 9.96 9.95 0 5.5-4.46 10.09-8.87 10.09zm5.46-7.42c-.3-.15-1.77-.87-2.05-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.65-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.07-.15-.67-1.6-.92-2.2-.24-.57-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.47 0 1.46 1.06 2.87 1.21 3.07.15.2 2.09 3.2 5.07 4.48.7.3 1.26.48 1.69.62.71.22 1.36.2 1.87.12.57-.08 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M14 9h3V5.5h-3c-1.93 0-3.5 1.57-3.5 3.5v2H8v3.5h2.5V20H14v-6h2.7l.5-3.5H14v-1.5z"/></svg>',
    "x": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M5 5l14 14M19 5L5 19"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="4.5" y="9" width="3" height="10"/><circle cx="6" cy="5.5" r="1.6"/><path d="M11.5 19V9M11.5 13c0-2.2 1.5-4 3.7-4s3.3 1.5 3.3 4v6"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="4" y="4" width="16" height="16" rx="4"/><circle cx="12" cy="12" r="3.4"/><circle cx="16.6" cy="7.4" r="0.6" fill="currentColor" stroke="none"/></svg>',
    "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M12 21s7-6.4 7-12a7 7 0 10-14 0c0 5.6 7 12 7 12z"/><circle cx="12" cy="9" r="2.3"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M6 3h3l2 5-2.5 1.5a11 11 0 005 5L15 12l5 2v3a2 2 0 01-2 2C10.5 19 5 13.5 5 6a2 2 0 011-3z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><rect x="3.5" y="5.5" width="17" height="13" rx="1.5"/><path d="M4 6.5l8 6 8-6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>',
    "corporate": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M4 21V7l6-3 6 3v14M4 21h16M10 21v-5h4v5M8 10h1M8 13.5h1M15 10h1M15 13.5h1"/></svg>',
    "litigation": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M6 4v13M3 6.5L6 4l3 2.5M3 6.5l1.5 4a2 2 0 004 0l-1.5-4M9 6.5l1.5 4a2 2 0 004 0l-1.5-4M18 4v13M15 6.5L18 4l3 2.5M4 21h4M16 21h4M12 11v10"/></svg>',
    "realestate": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M4 11l8-6 8 6M6 10v10h12V10M10 20v-6h4v6"/></svg>',
    "ip": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="11" cy="11" r="7"/><path d="M11 8v3l2 2M16.3 16.3L21 21"/></svg>',
    "family": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="8.5" cy="8" r="2.4"/><circle cx="16" cy="8" r="2.1"/><path d="M3.5 20v-2a4 4 0 014-4h2a4 4 0 014 4M14.5 14.2A3.6 3.6 0 0118 12.4h.2a3.6 3.6 0 013.6 3.6V18"/></svg>',
    "contract": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M7 3h8l4 4v14H7z"/><path d="M15 3v4h4M9 12h6M9 15.5h6M9 8.5h2"/></svg>',
    "tax": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><circle cx="12" cy="12" r="9"/><path d="M9 15l6-6M9.5 9h.01M14.5 15h.01"/></svg>',
    "quote": '<svg viewBox="0 0 32 24" fill="currentColor"><path d="M0 24V14.4C0 6.4 4.8 1.2 12.8 0l1.6 4C9.6 5.6 7.2 8.8 7.2 12.8H14.4V24H0zM17.6 24V14.4c0-8 4.8-13.2 12.8-14.4L32 4c-4.8 1.6-7.2 4.8-7.2 8.8H32V24H17.6z"/></svg>',
}

# ---------------------------------------------------------- practice data --
PRACTICE_AREAS = [
    {
        "slug": "corporate-law",
        "title": "Corporate Law",
        "icon": "corporate",
        "short": "Incorporation, governance, compliance, and transactional support for businesses at every stage.",
        "intro": "We advise founders, growing companies, and established corporates on the legal architecture that keeps a business compliant and investable. Our work spans entity formation through to complex commercial transactions, giving clients one point of contact as they scale.",
        "what_we_do": [
            "Company incorporation and business registration with the Corporate Affairs Commission",
            "Corporate governance advisory, board resolutions, and statutory compliance",
            "Drafting and negotiating shareholder and partnership agreements",
            "Support on mergers, acquisitions, and corporate restructuring",
            "Regulatory compliance across relevant sectors",
        ],
        "key_services": [
            ("Business formation", "Structuring and registering companies, from private limited entities to joint ventures, with the right constitutional documents in place from day one."),
            ("Governance & compliance", "Ongoing support with statutory filings, board procedure, and compliance obligations so directors stay protected."),
            ("Mergers & acquisitions", "Due diligence, deal structuring, and negotiation support for businesses buying, selling, or merging."),
            ("Contracts & commercial agreements", "Drafting and reviewing the agreements that govern how a business operates day to day."),
        ],
        "why": [
            "A single legal team that understands both the transaction and the regulatory backdrop it sits in",
            "Clear, practical advice rather than lengthy memos that leave the real decision unanswered",
            "Continuity from formation through to later-stage transactions, with one firm holding the institutional history",
        ],
        "related": ["commercial-litigation", "contract-law", "tax-law"],
    },
    {
        "slug": "commercial-litigation",
        "title": "Commercial Litigation",
        "icon": "litigation",
        "short": "Representation in commercial disputes, arbitration, and alternative dispute resolution.",
        "intro": "When a commercial relationship breaks down, the priority is protecting the client's position without losing sight of cost and time. We represent clients before Nigerian courts and in arbitration, and we push for negotiated resolution wherever it genuinely serves the client's interest.",
        "what_we_do": [
            "Representation in commercial and contractual disputes before Nigerian courts",
            "Arbitration and alternative dispute resolution (ADR)",
            "Debt recovery and enforcement of judgments",
            "Pre-litigation strategy, including demand letters and negotiated settlement",
            "Risk assessment before a dispute is commenced",
        ],
        "key_services": [
            ("Dispute strategy", "An honest assessment of the merits, likely cost, and timeline before any filing is made."),
            ("Court representation", "Preparation and advocacy through every stage of litigation, from pleadings to trial."),
            ("Arbitration & ADR", "Representation in arbitral proceedings and structured negotiation aimed at faster resolution."),
            ("Enforcement", "Pursuing recovery once a judgment or award has been secured."),
        ],
        "why": [
            "Litigation strategy built around the client's commercial objective, not just the legal question",
            "Realistic guidance on likely outcomes and costs before proceedings begin",
            "Experience across both courtroom advocacy and negotiated settlement",
        ],
        "related": ["corporate-law", "contract-law", "real-estate"],
    },
    {
        "slug": "real-estate",
        "title": "Real Estate",
        "icon": "realestate",
        "short": "Property transactions, title verification, and landlord-tenant advisory.",
        "intro": "Property transactions in Lagos and across Nigeria carry real title risk. We conduct due diligence on land and property before money changes hands, and we act for clients across purchase, lease, and development matters.",
        "what_we_do": [
            "Title verification and due diligence on land and property",
            "Drafting and review of sale, lease, and tenancy agreements",
            "Perfection of title documents, including governor's consent where applicable",
            "Landlord and tenant disputes",
            "Advisory support on real estate development transactions",
        ],
        "key_services": [
            ("Title due diligence", "Investigating the history and status of a title before a client commits funds to a transaction."),
            ("Transaction documentation", "Drafting sale agreements, deeds, and leases that reflect the terms actually agreed."),
            ("Title perfection", "Managing the registration and consent process required to secure a client's interest in land."),
            ("Landlord–tenant matters", "Advisory and representation on tenancy disputes and recovery of premises."),
        ],
        "why": [
            "Direct, practical due diligence rather than a generic title search",
            "Familiarity with the documentation practice around Lagos State land transactions",
            "Support through the full transaction, not only the paperwork stage",
        ],
        "related": ["contract-law", "corporate-law", "commercial-litigation"],
    },
    {
        "slug": "intellectual-property",
        "title": "Intellectual Property",
        "icon": "ip",
        "short": "Protection and enforcement of trademarks, patents, copyrights, and trade secrets.",
        "intro": "A brand, invention, or creative work only has value if it is protected. We help clients register and defend their intellectual property, and we act when that property is infringed.",
        "what_we_do": [
            "Trademark search, filing, and registration",
            "Advisory on copyright protection for creative and written works",
            "Patent filing guidance",
            "Enforcement action against infringement",
            "IP due diligence in commercial transactions",
        ],
        "key_services": [
            ("Trademark registration", "Clearance searches and filing to secure a brand name, logo, or mark."),
            ("Copyright advisory", "Guidance on protecting written, creative, and digital works under Nigerian law."),
            ("Enforcement", "Cease-and-desist action and representation where a client's IP has been infringed."),
            ("IP in transactions", "Reviewing IP ownership and licensing terms as part of wider commercial deals."),
        ],
        "why": [
            "Protection strategy tailored to what the client actually needs to defend",
            "Enforcement handled with the same rigor as registration",
            "IP advice integrated with the client's wider commercial position",
        ],
        "related": ["corporate-law", "contract-law", "commercial-litigation"],
    },
    {
        "slug": "family-law",
        "title": "Family Law",
        "icon": "family",
        "short": "Guidance on divorce, child custody, adoption, and estate planning.",
        "intro": "Family law matters are personal, and we approach them accordingly, with direct communication and a clear sense of what is actually achievable. We represent individuals through divorce, custody, adoption, and estate planning matters.",
        "what_we_do": [
            "Divorce proceedings and settlement negotiation",
            "Child custody and welfare matters",
            "Adoption guidance and representation",
            "Prenuptial and postnuptial agreements",
            "Wills, estate planning, and succession matters",
        ],
        "key_services": [
            ("Divorce & separation", "Representation through the legal process, with a focus on fair and efficient resolution."),
            ("Custody & welfare", "Advocacy centred on the best interests of the children involved."),
            ("Adoption", "Guidance through the legal requirements of the adoption process."),
            ("Wills & estate planning", "Drafting wills and advising on succession to protect a family's interests."),
        ],
        "why": [
            "Direct communication during a period that is often difficult for clients",
            "Practical settlement-focused advice, with litigation pursued only where necessary",
            "Confidential handling of sensitive family matters",
        ],
        "related": ["contract-law", "real-estate", "tax-law"],
    },
    {
        "slug": "contract-law",
        "title": "Contract Law",
        "icon": "contract",
        "short": "Drafting, review, and negotiation of commercial and employment contracts.",
        "intro": "Most disputes trace back to a contract that was unclear, incomplete, or never properly reviewed. We draft and negotiate agreements that hold up when they are tested, and we review contracts clients are asked to sign before they commit.",
        "what_we_do": [
            "Drafting commercial, supply, and service agreements",
            "Employment contracts and workplace policy documents",
            "Review and negotiation of contracts presented by a counterparty",
            "Advisory on breach of contract and available remedies",
            "Contract lifecycle support for growing businesses",
        ],
        "key_services": [
            ("Drafting", "Agreements written in plain terms that reflect what was actually negotiated."),
            ("Review & negotiation", "Line-by-line review of contracts a client is asked to sign, with negotiation support."),
            ("Employment agreements", "Contracts and policies that meet statutory requirements while protecting the employer."),
            ("Breach & remedies", "Advisory on options when a counterparty fails to perform."),
        ],
        "why": [
            "Contracts drafted for the dispute that hasn't happened yet, not just the deal in front of us",
            "Turnaround times that respect commercial deadlines",
            "Plain-language drafting that clients can actually read and understand",
        ],
        "related": ["corporate-law", "commercial-litigation", "real-estate"],
    },
    {
        "slug": "tax-law",
        "title": "Tax Law",
        "icon": "tax",
        "short": "Tax compliance and advisory support for individuals and businesses.",
        "intro": "Tax exposure is easy to underestimate until it becomes a liability. We advise individuals and businesses on structuring their affairs to stay compliant with Nigerian tax law, and we assist where a dispute with a tax authority has already arisen.",
        "what_we_do": [
            "Tax compliance advisory for businesses and individuals",
            "Structuring guidance to manage tax exposure within the law",
            "Support during tax audits and reviews",
            "Representation in disputes with tax authorities",
            "Advisory on the tax implications of commercial transactions",
        ],
        "key_services": [
            ("Compliance advisory", "Guidance on meeting filing and reporting obligations as they apply to a client's business."),
            ("Transaction tax advisory", "Assessing the tax consequences of a deal before it is signed, not after."),
            ("Audit support", "Representation and preparation when a business faces a tax authority review."),
            ("Dispute resolution", "Advocacy where a disagreement with a tax authority needs to be resolved."),
        ],
        "why": [
            "Advice grounded in what is actually defensible under current Nigerian tax law",
            "Coordination with our corporate and contract teams on transaction-related tax questions",
            "Straightforward explanations of exposure and options, without unnecessary jargon",
        ],
        "related": ["corporate-law", "contract-law", "commercial-litigation"],
    },
]
PA_BY_SLUG = {p["slug"]: p for p in PRACTICE_AREAS}

# TODO: replace with real attorney photos, names and bios. Only the firm's
# founder is named in the source material supplied; every other entry here
# is a clearly marked placeholder, not a fabricated person.
ATTORNEYS = [
    {
        "name": "M. A. Salawu Esq",
        "role": "Founder &amp; Principal Partner",
        "areas": "Corporate Law, Commercial Litigation",
        "bio": "Founder of M.A Salawu &amp; Co Chamber. TODO: add full biography, call-to-bar year, and qualifications supplied by the firm.",
        "img": "img/attorneys/founder-placeholder.jpg",
        "placeholder": False,
    },
    {
        "name": "TODO: Attorney Name",
        "role": "Associate &mdash; Real Estate",
        "areas": "Real Estate, Contract Law",
        "bio": "Placeholder profile. Replace with the attorney's real name, call-to-bar year, qualifications and biography.",
        "img": "img/attorneys/placeholder-2.jpg",
        "placeholder": True,
    },
    {
        "name": "TODO: Attorney Name",
        "role": "Associate &mdash; Family Law",
        "areas": "Family Law, Tax Law",
        "bio": "Placeholder profile. Replace with the attorney's real name, call-to-bar year, qualifications and biography.",
        "img": "img/attorneys/placeholder-3.jpg",
        "placeholder": True,
    },
    {
        "name": "TODO: Attorney Name",
        "role": "Associate &mdash; Intellectual Property",
        "areas": "Intellectual Property, Corporate Law",
        "bio": "Placeholder profile. Replace with the attorney's real name, call-to-bar year, qualifications and biography.",
        "img": "img/attorneys/placeholder-4.jpg",
        "placeholder": True,
    },
]

# TODO: the original source page attributed quotes to "Olomu & Co Chambers"
# and "LexNigeria" — both inconsistent with M.A Salawu & Co. Those firm
# references have been removed from the quotes below rather than invented;
# confirm these testimonials are genuine before publishing, or replace them.
TESTIMONIALS = [
    {
        "quote": "The team handled our corporate restructuring with real attention to detail and kept us informed at every stage.",
        "name": "Emeka Nwosu",
        "role": "CEO, Sterling Holdings Ltd. &mdash; TODO: confirm attribution",
    },
    {
        "quote": "During a difficult divorce, the firm stayed focused on what mattered most and secured a settlement I was satisfied with.",
        "name": "Folake Adeyemi",
        "role": "Client &mdash; TODO: confirm attribution",
    },
    {
        "quote": "A land dispute that had dragged on for years was resolved within months, with an outcome that held up.",
        "name": "Tunde Balogun",
        "role": "Property Developer &mdash; TODO: confirm attribution",
    },
]

# Sample/placeholder editorial content for the Insights section. Clearly
# marked as samples in the page copy — replace with the firm's real articles.
ARTICLES = [
    {
        "slug": "corporate-compliance-checklist",
        "title": "A practical compliance checklist for Nigerian SMEs",
        "excerpt": "What growing businesses tend to overlook when it comes to statutory filings and governance.",
        "category": "Corporate Law",
        "date": "2026-01-14",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-1.jpg",
        "body": [
            "Many small and mid-sized businesses treat compliance as something to deal with once a problem arises, rather than a routine part of running the company. That approach is understandable but costly.",
            "The most common gaps we see are missed annual returns, board resolutions that were never properly documented, and share registers that fall out of date after an informal transfer of shares.",
            "A short annual review, covering statutory filings, board documentation, and any changes in ownership or directorship, catches most of these issues before they become expensive to fix.",
        ],
    },
    {
        "slug": "title-due-diligence-lagos",
        "title": "Why title due diligence matters before you pay for land in Lagos",
        "excerpt": "The practical steps we take before a client commits funds to a property transaction.",
        "category": "Real Estate",
        "date": "2025-11-02",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-2.jpg",
        "body": [
            "Land transactions in Lagos carry genuine title risk, and that risk rarely announces itself upfront. A search at the land registry is the starting point, not the whole process.",
            "We look at the chain of title, whether consent requirements have been satisfied, and whether the property is subject to any competing claim or encumbrance before advising a client to proceed.",
            "The cost of proper due diligence is small next to the cost of discovering a title problem after money has already changed hands.",
        ],
    },
    {
        "slug": "contract-review-checklist",
        "title": "Five clauses worth a second look before you sign",
        "excerpt": "Termination, indemnity, and liability clauses are where most contract disputes originate.",
        "category": "Contract Law",
        "date": "2025-09-18",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-3.jpg",
        "body": [
            "Most commercial disputes we handle trace back to a handful of clauses that were signed without close attention: termination rights, indemnity, limitation of liability, dispute resolution, and payment terms.",
            "A termination clause that only benefits one party, or an indemnity that is broader than the risk it is meant to cover, is often negotiable if it is caught before signature.",
            "Reviewing these clauses with counsel before signing is usually faster and cheaper than renegotiating them after a dispute has already started.",
        ],
    },
    {
        "slug": "trademark-registration-basics",
        "title": "When to register a trademark, and why timing matters",
        "excerpt": "Nigeria operates a first-to-file system, which changes how early a business should act.",
        "category": "Intellectual Property",
        "date": "2025-08-05",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-4.jpg",
        "body": [
            "Nigeria's trademark system is first-to-file, meaning the right to register generally goes to whoever files first, not necessarily whoever used the mark first.",
            "Businesses that wait until a brand is established before registering risk finding that someone else has already filed a similar mark.",
            "A clearance search before launch, followed by prompt filing, is the most reliable way to secure a brand name or logo.",
        ],
    },
    {
        "slug": "employment-contract-essentials",
        "title": "What a compliant employment contract actually needs to say",
        "excerpt": "The statutory minimums Nigerian employers are required to put in writing.",
        "category": "Contract Law",
        "date": "2025-06-21",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-5.jpg",
        "body": [
            "Nigerian labour law requires certain terms to be reduced to writing within the early weeks of employment, including job description, remuneration, and notice periods.",
            "Employers that rely on informal or verbal arrangements often discover the gap only once a dispute arises, by which point the terms are harder to establish.",
            "A written contract that meets statutory requirements protects both employer and employee, and is worth the modest upfront cost of proper drafting.",
        ],
    },
    {
        "slug": "arbitration-vs-litigation",
        "title": "Arbitration or litigation: how we help clients decide",
        "excerpt": "Cost, confidentiality, and enforceability all factor into the choice of forum.",
        "category": "Commercial Litigation",
        "date": "2025-04-30",
        "author": "M.A Salawu & Co",
        "img": "img/insights/article-6.jpg",
        "body": [
            "Arbitration is often assumed to be faster and cheaper than litigation, but that is not automatically true, particularly for smaller disputes.",
            "Where confidentiality matters, or where the contract already contains an arbitration clause, arbitration is usually the right path. Where a quick interim remedy is needed, court proceedings may be faster.",
            "We assess each dispute on its facts before recommending a forum, rather than defaulting to one option.",
        ],
    },
]

NAV_PAGES = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("practice-areas.html", "Practice Areas"),
    ("attorneys.html", "Attorneys"),
    ("insights.html", "Insights"),
    ("careers.html", "Careers"),
    ("contact.html", "Contact"),
]

# ------------------------------------------------------------- helpers ----

def rel(depth):
    """CSS/JS path prefix — all pages live at root, so always ''."""
    return ""


def topbar():
    return f"""
  <div class="topbar">
    <div class="wrap">
      <div class="topbar__contacts">
        <a href="tel:{PHONE_1_TEL}">{ICONS['phone']}<span class="long">{PHONE_1}</span></a>
        <a href="mailto:{EMAIL}">{ICONS['mail']}<span class="long">{EMAIL}</span></a>
      </div>
      <div class="topbar__hours">{HOURS}</div>
    </div>
  </div>"""


def mega_menu(active_slug=None):
    items = []
    for p in PRACTICE_AREAS:
        items.append(
            f'<a href="{p["slug"]}.html"><strong>{p["title"]}</strong><em>{p["short"].split(".")[0]}.</em></a>'
        )
    return f"""
            <li class="nav-item--dropdown">
              <a href="practice-areas.html"{' aria-current="page"' if active_slug=='practice-areas' else ''}>Practice Areas {ICONS['caret']}</a>
              <div class="mega-menu" role="menu">
                {''.join(items)}
              </div>
            </li>"""


def primary_nav_items(active):
    out = []
    for href, label in NAV_PAGES:
        slug = href.replace(".html", "")
        if slug == "practice-areas":
            out.append(mega_menu(active))
            continue
        current = ' aria-current="page"' if active == slug else ""
        out.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    return "".join(out)


def mobile_nav(active):
    pa_items = "".join(
        f'<li><a href="{p["slug"]}.html">{p["title"]}</a></li>' for p in PRACTICE_AREAS
    )
    links = []
    for href, label in NAV_PAGES:
        slug = href.replace(".html", "")
        if slug == "practice-areas":
            links.append(f"""
          <li>
            <button class="mobile-accordion-trigger" aria-expanded="false" aria-controls="mobile-practice-panel">
              Practice Areas
              <span class="accordion-icon"></span>
            </button>
            <div class="mobile-submenu" id="mobile-practice-panel">
              <ul>
                <li><a href="practice-areas.html">All Practice Areas</a></li>
                {pa_items}
              </ul>
            </div>
          </li>""")
        else:
            current = ' aria-current="page"' if active == slug else ""
            links.append(f'<li><a href="{href}"{current}>{label}</a></li>')
    return f"""
  <div class="mobile-nav" id="mobileNav">
    <div class="mobile-nav__top">
      <a href="index.html" class="brand"><span class="brand__mark">{ICONS['mark']}</span>M. A. SALAWU Esq<span>&nbsp;&amp; CO</span></a>
      <button class="nav-toggle mobile-nav__close" aria-label="Close menu" aria-expanded="true">
        <span></span>
      </button>
    </div>
    <div class="mobile-nav__body">
      <ul>{''.join(links)}</ul>
      <div class="mobile-nav__cta">
        <a href="contact.html" class="btn btn--gold btn--block">Speak With Our Team</a>
        <a href="tel:{PHONE_1_TEL}" class="btn btn--ghost btn--block">Call {PHONE_1}</a>
      </div>
      <div class="mobile-nav__contacts">
        <span>{ADDRESS_LINE1}, {ADDRESS_LINE3}</span>
        <span>{EMAIL}</span>
      </div>
    </div>
  </div>"""


def header(active):
    nav_active = "practice-areas" if active in PA_BY_SLUG else active
    return f"""{topbar()}
  <header class="site-header">
    <div class="wrap header-row">
      <a href="index.html" class="brand">
        <span class="brand__mark">{ICONS['mark']}</span>
        <span>M.A SALAWU ESQ<span style="color:var(--gold-600)">&nbsp;&amp;&nbsp;CO</span><small>CHAMBER &amp; SOLICITORS</small></span>
      </a>
      <nav class="primary-nav" aria-label="Primary">
        <ul>{primary_nav_items(nav_active)}</ul>
      </nav>
      <div class="header-cta">
        <a href="contact.html" class="btn btn--primary">Speak With Our Team {ICONS['arrow']}</a>
        <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-controls="mobileNav" aria-expanded="false">
          <span></span>
        </button>
      </div>
    </div>
  </header>
  {mobile_nav(active)}"""


def footer():
    pa_links = "".join(f'<li><a href="{p["slug"]}.html">{p["title"]}</a></li>' for p in PRACTICE_AREAS)
    return f"""
  <footer class="site-footer">
    <div class="wrap footer-top">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="brand"><span class="brand__mark">{ICONS['mark']}</span>M.A SALAWU ESQ<span>&nbsp;&amp; CO</span></a>
          <p>Legal counsel for individuals, corporate organisations, and businesses in Nigeria, built on integrity, professionalism, and close attention to each client's matter.</p>
          <div class="footer-social">
            <a href="#" aria-label="Facebook">{ICONS['facebook']}</a>
            <a href="#" aria-label="X (Twitter)">{ICONS['x']}</a>
            <a href="#" aria-label="LinkedIn">{ICONS['linkedin']}</a>
            <a href="#" aria-label="Instagram">{ICONS['instagram']}</a>
          </div>
          <p class="footer-note"><!-- TODO: confirm and link real social profiles --></p>
        </div>
        <div class="footer-col">
          <h4>Navigate</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="practice-areas.html">Practice Areas</a></li>
            <li><a href="attorneys.html">Attorneys</a></li>
            <li><a href="insights.html">Insights</a></li>
            <li><a href="careers.html">Careers</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Practice Areas</h4>
          <ul>{pa_links}</ul>
        </div>
        <div class="footer-col footer-newsletter">
          <h4>Stay Informed</h4>
          <p style="font-size:var(--step--1)">Occasional legal updates and firm news. No spam.</p>
          <form data-newsletter aria-label="Subscribe to newsletter">
            <label for="newsletter-email" class="visually-hidden">Email address</label>
            <input id="newsletter-email" type="email" placeholder="Your email address" required>
            <button type="submit" aria-label="Subscribe">{ICONS['arrow']}</button>
          </form>
        </div>
      </div>
    </div>
    <div class="wrap footer-bottom">
      <p>&copy; <span data-year>2026</span> {SITE_NAME}. All rights reserved.</p>
      <ul>
        <li><a href="privacy-policy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms of Use</a></li>
      </ul>
    </div>
  </footer>

  <a href="https://wa.me/{WHATSAPP_NUMBER}" class="whatsapp-float" target="_blank" rel="noopener noreferrer" aria-label="Chat with us on WhatsApp">
    <span class="whatsapp-float__tip">Chat with us</span>
    <span class="whatsapp-float__btn">{ICONS['whatsapp']}</span>
  </a>
  <button class="to-top" aria-label="Back to top">
    <svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" width="18" height="18"><path d="M10 15V5M5 9l5-5 5 5"/></svg>
  </button>"""


def breadcrumb(items):
    """items: list of (label, href|None)"""
    parts = []
    for i, (label, href) in enumerate(items):
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
        if i < len(items) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<nav class="breadcrumb" aria-label="Breadcrumb">{"".join(parts)}</nav>'


def page(*, active, title, description, canonical, og_type="website", body, extra_head="", extra_scripts="", schema=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_URL_PLACEHOLDER}/{canonical}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_URL_PLACEHOLDER}/{canonical}">
<meta property="og:image" content="{SITE_URL_PLACEHOLDER}/img/general/og-cover.jpg">
<meta property="og:locale" content="en_NG">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="theme-color" content="#0a2a20">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' fill='%230a2a20'/%3E%3Ctext x='50%25' y='58%25' font-size='14' fill='%23c29a42' text-anchor='middle' font-family='Georgia,serif'%3EMS%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/components.css">
<link rel="stylesheet" href="css/pages.css">
<link rel="stylesheet" href="css/responsive.css">
{schema}{extra_head}
</head>
<body>
<a href="#main" class="skip-link">Skip to content</a>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
<script src="js/navigation.js" defer></script>
<script src="js/animations.js" defer></script>
<script src="js/forms.js" defer></script>
<script src="js/main.js" defer></script>
{extra_scripts}
</body>
</html>"""


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


LOCAL_BUSINESS_SCHEMA = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "LegalService",
  "name": "{SITE_NAME}",
  "image": "{SITE_URL_PLACEHOLDER}/img/general/og-cover.jpg",
  "telephone": "{PHONE_1}",
  "email": "{EMAIL}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{ADDRESS_LINE1}, {ADDRESS_LINE2}",
    "addressLocality": "Badagry",
    "addressRegion": "Lagos State",
    "addressCountry": "NG"
  }},
  "openingHours": "Mo-Fr 09:00-17:00",
  "url": "{SITE_URL_PLACEHOLDER}"
}}
</script>"""

# =========================================================== INDEX =========
def build_index():
    practice_cards = ""
    for i, p in enumerate(PRACTICE_AREAS, start=1):
        practice_cards += f"""
        <a href="{p['slug']}.html" class="card practice-card reveal">
          <span class="practice-card__index">{i:02d}</span>
          <div>{ICONS[p['icon']]}</div>
          <h3>{p['title']}</h3>
          <p>{p['short']}</p>
          <span class="text-link">Explore Practice {ICONS['arrow']}</span>
        </a>"""

    body = f"""
  <section class="hero" id="home">
    <div class="hero__media">
      <img src="img/hero/office-exterior.jpg" alt="" role="presentation">
    </div>
    <div class="hero__grain"></div>
    <div class="wrap hero__content">
      <span class="eyebrow hero__eyebrow">M.A Salawu &amp; Co Chamber &mdash; Badagry, Lagos</span>
      <h1 data-stagger>Strategic legal counsel, built on experience and driven by integrity</h1>
      <p class="hero__lede">We advise individuals, corporate organisations, and businesses across Nigeria, combining careful attention to detail with a clear understanding of how commercial decisions actually get made.</p>
      <div class="hero__actions">
        <a href="contact.html" class="btn btn--gold">Speak With Our Team {ICONS['arrow']}</a>
        <a href="practice-areas.html" class="btn btn--ghost-light">Explore Our Practice Areas</a>
      </div>
    </div>
    <div class="hero__foot">
      <div class="wrap">
        <div class="hero__foot-item"><strong>7</strong>Core practice areas</div>
        <div class="hero__foot-item"><strong>Badagry</strong>Lagos State office</div>
        <div class="hero__foot-item"><strong>Mon&ndash;Fri</strong>9am &ndash; 5pm consultations</div>
      </div>
    </div>
  </section>

  <section class="trust-strip">
    <div class="wrap">
      <div class="trust-strip__item"><strong>Individuals</strong><span>Personal &amp; family legal matters</span></div>
      <div class="trust-strip__item"><strong>Corporates</strong><span>Governance, contracts &amp; disputes</span></div>
      <div class="trust-strip__item"><strong>Property owners</strong><span>Title, transactions &amp; disputes</span></div>
      <div class="trust-strip__item"><strong>Growing businesses</strong><span>Compliance &amp; commercial advisory</span></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="split__media reveal">
        <div class="split__media-frame"></div>
        <img src="img/general/law-firm-office-1.avif" alt="M.A Salawu &amp; Co Chamber office interior" loading="lazy">
      </div>
      <div class="reveal">
        <span class="eyebrow split__eyebrow">About The Firm</span>
        <h2>Legal counsel rooted in Nigerian law and everyday commercial reality</h2>
        <p>M.A Salawu &amp; Co Chamber Chamber was founded by M.A Salawu Esq with a clear aim: legal representation that is thorough, direct, and genuinely useful to the client, not just technically correct.</p>
        <p>Our attorneys work across corporate law, commercial litigation, real estate, intellectual property, family law, contract law, and tax law. We are based in Badagry, Lagos, and act for clients across Nigeria.</p>
        <ul class="check-list">
          <li>{ICONS['check']}Direct communication with the attorney handling your matter</li>
          <li>{ICONS['check']}Advice grounded in current Nigerian law and procedure</li>
          <li>{ICONS['check']}Transparent guidance on cost and likely timelines</li>
        </ul>
        <a href="about.html" class="btn btn--primary" style="margin-top:2rem">Meet The Firm {ICONS['arrow']}</a>
      </div>
    </div>
  </section>

  <section class="section section--ivory" id="practice-areas">
    <div class="wrap">
      <div class="section-head section-head--split reveal">
        <div>
          <span class="eyebrow">What We Do</span>
          <h2>Practice areas</h2>
        </div>
        <a href="practice-areas.html" class="text-link">View all practice areas {ICONS['arrow']}</a>
      </div>
      <div class="grid grid-3 practice-grid">{practice_cards}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Why Choose Us</span>
        <h2>An approach built around the client's actual problem</h2>
      </div>
      <div class="grid grid-4">
        <div class="value-card reveal">
          <div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="30" height="30"><path d="M12 3l8 4v5c0 5-3.4 8.4-8 9-4.6-.6-8-4-8-9V7l8-4z"/><path d="M9 12l2 2 4-4"/></svg></div>
          <h3>Integrity first</h3>
          <p>We tell clients what the law actually allows, not what is easiest to hear.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="30" height="30"><path d="M4 19V5M4 19h16M8 19v-6M12 19V9M16 19v-9"/></svg></div>
          <h3>Commercial awareness</h3>
          <p>Advice weighed against the client's actual business or personal objective.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="30" height="30"><circle cx="12" cy="8" r="3.2"/><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6"/></svg></div>
          <h3>Direct access</h3>
          <p>Clients deal with the attorney handling their matter, not a rotating point of contact.</p>
        </div>
        <div class="value-card reveal">
          <div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="30" height="30"><path d="M12 3v18M5 8l7-5 7 5M5 8v9a2 2 0 002 2h10a2 2 0 002-2V8"/></svg></div>
          <h3>Local grounding</h3>
          <p>Based in Badagry, Lagos, with working knowledge of local process and procedure.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--dark" id="attorneys">
    <div class="wrap">
      <div class="section-head section-head--split reveal">
        <div>
          <span class="eyebrow">Our People</span>
          <h2>Attorneys</h2>
        </div>
        <a href="attorneys.html" class="text-link" style="color:var(--gold-500)">Meet the full team {ICONS['arrow']}</a>
      </div>
      <div class="grid grid-4">
        {attorney_preview_cards()}
      </div>
    </div>
  </section>

  <section class="section" id="insights">
    <div class="wrap">
      <div class="section-head section-head--split reveal">
        <div>
          <span class="eyebrow">Insights</span>
          <h2>Recent thinking</h2>
        </div>
        <a href="insights.html" class="text-link">Browse all insights {ICONS['arrow']}</a>
      </div>
      <div class="grid grid-3">
        {insight_preview_cards()}
      </div>
    </div>
  </section>

  <section class="section section--ivory" id="testimonials">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Client Feedback</span>
        <h2>What clients say</h2>
      </div>
      <div style="overflow:hidden" class="reveal">
        <div data-testimonial-track style="display:flex; transition: transform .5s var(--ease);">
          {testimonial_slides()}
        </div>
      </div>
      <div style="display:flex; justify-content:center; gap:1rem; margin-top:2rem;">
        <button data-testimonial-prev class="btn btn--ghost" aria-label="Previous testimonial">&larr;</button>
        <button data-testimonial-next class="btn btn--ghost" aria-label="Next testimonial">&rarr;</button>
      </div>
      <!-- TODO: firm to confirm client names/organisations below; source content contained inconsistent firm names ("Olomu & Co Chambers", "LexNigeria") that did not match M.A Salawu & Co and have been generalised pending confirmation. -->
    </div>
  </section>

  <section class="section section--dark" id="contact-cta">
    <div class="wrap" style="text-align:center; max-width:760px; margin-inline:auto;">
      <span class="eyebrow" style="justify-content:center">Get In Touch</span>
      <h2>Speak with our team about your matter</h2>
      <p style="margin-top:1rem">Reach out for a consultation and we'll direct you to the right attorney for your matter.</p>
      <div class="hero__actions" style="justify-content:center; margin-top:2rem;">
        <a href="contact.html" class="btn btn--gold">Book A Consultation {ICONS['arrow']}</a>
        <a href="tel:{PHONE_1_TEL}" class="btn btn--ghost-light">Call {PHONE_1}</a>
      </div>
    </div>
  </section>
"""
    write("index.html", page(
        active="index",
        title=f"{SITE_NAME} | Chamber &amp; Solicitors, Badagry, Lagos".replace("&amp;", "&"),
        description="M.A Salawu & Co is a law firm in Badagry, Lagos providing corporate, litigation, real estate, IP, family, contract and tax law services across Nigeria.",
        canonical="index.html",
        body=body,
        schema=LOCAL_BUSINESS_SCHEMA,
    ))


def attorney_preview_cards():
    people = ATTORNEYS[:4]
    out = ""
    for p in people:
        out += f"""
        <div class="person-card reveal">
          <div class="person-card__photo"><img src="{p['img']}" alt="{p['name']}, {p['role']}" loading="lazy"></div>
          <div class="person-card__body">
            <h3 style="color:var(--ivory)">{p['name']}</h3>
            <div class="person-card__role">{p['role']}</div>
          </div>
        </div>"""
    return out


def insight_preview_cards():
    out = ""
    for a in ARTICLES[:3]:
        out += f"""
        <a href="insights.html" class="insight-card card reveal">
          <div class="insight-card__image"><img src="{a['img']}" alt="" loading="lazy"></div>
          <div class="insight-card__meta"><span class="tag">{a['category']}</span><span>{a['date']}</span></div>
          <h3>{a['title']}</h3>
          <p>{a['excerpt']}</p>
        </a>"""
    return out


def testimonial_slides():
    out = ""
    for t in TESTIMONIALS:
        out += f"""
        <figure class="testimonial-card" style="flex: 0 0 100%;">
          {ICONS['quote']}
          <blockquote>&ldquo;{t['quote']}&rdquo;</blockquote>
          <figcaption><strong>{t['name']}</strong><span>{t['role']}</span></figcaption>
        </figure>"""
    return out


# =========================================================== ABOUT =========
def build_about():
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("About", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">About The Firm</span>
      <h1>Built on integrity, professionalism, and close attention to detail</h1>
      <p class="page-hero__lede">M.A Salawu &amp; Co Chamber is a Nigerian law firm based in Badagry, Lagos, providing legal counsel to individuals, corporate organisations, and businesses.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">Our Story</span>
        <h2>Founded to make thorough legal counsel genuinely accessible</h2>
        <p>M.A Salawu &amp; Co Chamber Chamber was founded by M.A Salawu Esq with a vision to provide exceptional legal services rooted in integrity, professionalism, and a deep understanding of Nigerian law.</p>
        <p>Our attorneys work across corporate law, commercial litigation, real estate, intellectual property, family law, contract law, and tax law. We aim to deliver tailored solutions that protect our clients' interests while keeping their actual objectives in view.</p>
        <p>Based in Badagry, Lagos, we serve clients across Nigeria, combining local expertise with a working knowledge of how commercial and personal matters actually unfold in practice.</p>
      </div>
      <div class="split__media reveal">
        <div class="split__media-frame"></div>
        <img src="img/general/law-firm-office-1.avif" alt="M.A Salawu &amp; Co Chamber office" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section--ivory">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Founder's Message</span>
        <h2>A note from M.A Salawu Esq</h2>
      </div>
      <div class="wrap--narrow reveal" style="margin:0;">
        <blockquote style="font-family:var(--font-display); font-size:var(--step-1); color:var(--forest-900); line-height:1.5; border-left:2px solid var(--gold-500); padding-left:1.6rem;">
          "Every client comes to us with a specific problem, not a general one. Our job is to understand that problem fully before we offer a way through it. That has been the approach since the firm's founding, and it remains the standard we hold ourselves to."
        </blockquote>
        <p style="margin-top:1.4rem; font-weight:600; color:var(--forest-900)">M.A Salawu Esq<span style="display:block;font-weight:400;color:var(--stone-500);font-size:var(--step--1)">Founder &amp; Principal Partner</span></p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Mission &amp; Vision</span>
        <h2>What guides how we practise</h2>
      </div>
      <div class="grid grid-2">
        <div class="card reveal">
          <h3>Mission</h3>
          <p>To provide legal counsel that is thorough, honest, and genuinely useful — protecting our clients' interests while helping them reach their actual objectives, not just the legally cleanest outcome.</p>
        </div>
        <div class="card reveal">
          <h3>Vision</h3>
          <p>To be a firm that clients in Badagry, across Lagos, and across Nigeria trust with matters that matter to them, built one well-handled case at a time.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--ivory">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Core Values</span>
        <h2>How we work with clients</h2>
      </div>
      <div class="grid grid-4">
        <div class="value-card reveal"><div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="28" height="28"><path d="M12 3l8 4v5c0 5-3.4 8.4-8 9-4.6-.6-8-4-8-9V7l8-4z"/></svg></div><h3>Integrity</h3><p>Straightforward advice, including when the honest answer isn't the easy one.</p></div>
        <div class="value-card reveal"><div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="28" height="28"><circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/></svg></div><h3>Diligence</h3><p>Matters are researched and prepared properly, not rushed to meet appearances.</p></div>
        <div class="value-card reveal"><div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="28" height="28"><path d="M5 20c0-3.5 3-6 7-6s7 2.5 7 6M12 12a3.5 3.5 0 100-7 3.5 3.5 0 000 7z"/></svg></div><h3>Accessibility</h3><p>Clients can reach the attorney on their matter, and get a straight answer.</p></div>
        <div class="value-card reveal"><div class="value-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="28" height="28"><path d="M4 19V5M4 19h16M8 15l3-3 3 2 4-5"/></svg></div><h3>Results-focused</h3><p>Every strategy is judged by whether it actually advances the client's position.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap split split--reverse">
      <div class="reveal">
        <span class="eyebrow">Our Approach</span>
        <h2>Geographic reach</h2>
        <p>M.A Salawu &amp; Co Chamber Chamber is based in Badagry, Lagos State, and acts for clients across Lagos and Nigeria more broadly. Where a matter requires it, we work with clients and counterparties outside Nigeria on commercial matters affecting Nigerian interests.</p>
        <a href="contact.html" class="btn btn--primary" style="margin-top:1.5rem">Get In Touch {ICONS['arrow']}</a>
      </div>
      <div class="split__media reveal">
        <div class="split__media-frame"></div>
        <img src="img/general/law-firm-office-1.avif" alt="Badagry, Lagos State" loading="lazy">
      </div>
    </div>
  </section>
"""
    write("about.html", page(
        active="about",
        title=f"About Us | {SITE_NAME}",
        description="Learn about M.A Salawu & Co, a Badagry, Lagos law firm built on integrity, professionalism, and thorough legal counsel across Nigeria.",
        canonical="about.html",
        body=body,
    ))


# ================================================== PRACTICE AREAS INDEX ===
def build_practice_areas_index():
    cards = ""
    for i, p in enumerate(PRACTICE_AREAS, start=1):
        cards += f"""
        <a href="{p['slug']}.html" class="card practice-card reveal">
          <span class="practice-card__index">{i:02d}</span>
          <div>{ICONS[p['icon']]}</div>
          <h3>{p['title']}</h3>
          <p>{p['short']}</p>
          <span class="text-link">Explore Practice {ICONS['arrow']}</span>
        </a>"""
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Practice Areas", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">What We Do</span>
      <h1>Practice areas</h1>
      <p class="page-hero__lede">Seven core areas of practice, covering the matters most commonly faced by our individual, corporate, and business clients across Nigeria.</p>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="grid grid-3 practice-grid">{cards}
      </div>
    </div>
  </section>
  <section class="section section--dark">
    <div class="wrap" style="text-align:center; max-width:700px; margin-inline:auto;">
      <span class="eyebrow" style="justify-content:center">Not Sure Where To Start?</span>
      <h2>Tell us about your matter and we'll point you to the right practice</h2>
      <div class="hero__actions" style="justify-content:center; margin-top:2rem;">
        <a href="contact.html" class="btn btn--gold">Speak With Our Team {ICONS['arrow']}</a>
      </div>
    </div>
  </section>
"""
    write("practice-areas.html", page(
        active="practice-areas",
        title=f"Practice Areas | {SITE_NAME}",
        description="Corporate law, commercial litigation, real estate, intellectual property, family law, contract law, and tax law services in Nigeria.",
        canonical="practice-areas.html",
        body=body,
    ))


# ================================================= PRACTICE DETAIL PAGES ===
def build_practice_pages():
    for p in PRACTICE_AREAS:
        related_html = "".join(
            f'<a href="{PA_BY_SLUG[r]["slug"]}.html">{PA_BY_SLUG[r]["title"]} {ICONS["arrow"]}</a>'
            for r in p["related"]
        )
        what_we_do = "".join(f'<li>{ICONS["check"]}{item}</li>' for item in p["what_we_do"])
        key_services = "".join(
            f'<li><h4>{name}</h4><p>{desc}</p></li>' for name, desc in p["key_services"]
        )
        why = "".join(f'<li>{ICONS["check"]}{item}</li>' for item in p["why"])
        related_cards = "".join(
            f"""<a href="{PA_BY_SLUG[r]['slug']}.html" class="card practice-card reveal">
              <div>{ICONS[PA_BY_SLUG[r]['icon']]}</div>
              <h3>{PA_BY_SLUG[r]['title']}</h3>
              <p>{PA_BY_SLUG[r]['short']}</p>
              <span class="text-link">Explore Practice {ICONS['arrow']}</span>
            </a>"""
            for r in p["related"]
        )

        body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Practice Areas","practice-areas.html"),(p['title'], None)])}
      <span class="eyebrow" style="color:var(--gold-500)">Practice Area</span>
      <h1>{p['title']}</h1>
      <p class="page-hero__lede">{p['short']}</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap practice-detail__grid">
      <div>
        <div class="reveal">
          <h2>Overview</h2>
          <p>{p['intro']}</p>
        </div>

        <div class="reveal" style="margin-top:3rem;">
          <h3>What we do</h3>
          <ul class="check-list" style="margin-top:1rem;">{what_we_do}</ul>
        </div>

        <div class="reveal" style="margin-top:3rem;">
          <h3>Key services</h3>
          <ul class="numbered-list" style="margin-top:1rem;">{key_services}</ul>
        </div>

        <div class="reveal" style="margin-top:3rem;">
          <h3>Why clients engage us</h3>
          <ul class="check-list" style="margin-top:1rem;">{why}</ul>
        </div>
      </div>

      <aside class="side-panel reveal">
        <h4>Practice Areas</h4>
        <ul>
          {"".join(f'<a href="{q["slug"]}.html"{" style=color:var(--gold-600);font-weight:700" if q["slug"]==p["slug"] else ""}>{q["title"]}</a>' for q in PRACTICE_AREAS)}
        </ul>
        <a href="contact.html" class="btn btn--primary btn--block">Discuss Your Matter</a>
      </aside>
    </div>
  </section>

  <section class="section section--ivory">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Related</span>
        <h2>Related practice areas</h2>
      </div>
      <div class="grid grid-3 practice-grid">{related_cards}</div>
    </div>
  </section>

  <section class="section section--dark">
    <div class="wrap contact-grid" style="align-items:center;">
      <div>
        <span class="eyebrow" style="color:var(--gold-500)">Contact</span>
        <h2>Discuss a {p['title'].lower()} matter</h2>
        <p style="margin-top:1rem">Reach out directly, or send a message and we'll direct it to the right attorney.</p>
        <div style="margin-top:2rem; display:flex; flex-direction:column; gap:0.9rem;">
          <a class="text-link" style="color:var(--gold-500)" href="tel:{PHONE_1_TEL}">{ICONS['phone']}{PHONE_1}</a>
          <a class="text-link" style="color:var(--gold-500)" href="mailto:{EMAIL}">{ICONS['mail']}{EMAIL}</a>
        </div>
      </div>
      <div>
        <a href="contact.html" class="btn btn--gold">Send A Message {ICONS['arrow']}</a>
      </div>
    </div>
  </section>
"""
        write(f"{p['slug']}.html", page(
            active=p["slug"],
            title=f"{p['title']} | {SITE_NAME}",
            description=p["short"],
            canonical=f"{p['slug']}.html",
            body=body,
        ))


# =========================================================== ATTORNEYS =====
def build_attorneys():
    filter_chips = '<button class="filter-chip is-active" data-filter="all">All</button>' + "".join(
        f'<button class="filter-chip" data-filter="{p["slug"]}">{p["title"]}</button>' for p in PRACTICE_AREAS
    )
    cards = ""
    for a in ATTORNEYS:
        badge = '<span class="tag" style="margin-top:.6rem;display:inline-block">Profile placeholder</span>' if a["placeholder"] else ""
        cards += f"""
        <div class="person-card reveal">
          <div class="person-card__photo"><img src="{a['img']}" alt="{a['name']}" loading="lazy"></div>
          <div class="person-card__body">
            <h3>{a['name']}</h3>
            <div class="person-card__role">{a['role']}</div>
            <div class="person-card__areas">{a['areas']}</div>
            <p style="font-size:0.85rem;margin-top:0.7rem;">{a['bio']}</p>
            {badge}
          </div>
        </div>"""
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Attorneys", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">Our People</span>
      <h1>Attorneys</h1>
      <p class="page-hero__lede">The team representing your matter, directly. <!-- TODO: replace placeholder attorney profiles below with the firm's real team once photos and bios are supplied. --></p>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="filter-bar" role="group" aria-label="Filter attorneys by practice area">{filter_chips}</div>
      <div class="grid grid-4">{cards}
      </div>
    </div>
  </section>
"""
    write("attorneys.html", page(
        active="attorneys",
        title=f"Attorneys | {SITE_NAME}",
        description="Meet the attorneys of M.A Salawu & Co, a Badagry, Lagos law firm.",
        canonical="attorneys.html",
        body=body,
    ))


# =========================================================== INSIGHTS ======
def build_insights():
    featured = ARTICLES[0]
    rest = ARTICLES[1:]
    categories = sorted(set(a["category"] for a in ARTICLES))
    chips = '<button class="filter-chip is-active" data-filter="all">All</button>' + "".join(
        f'<button class="filter-chip" data-filter="{c}">{c}</button>' for c in categories
    )
    cards = ""
    for a in rest:
        cards += f"""
        <a href="insights-{a['slug']}.html" class="insight-card card reveal" data-category="{a['category']}" data-title="{a['title']}" data-excerpt="{a['excerpt']}">
          <div class="insight-card__image"><img src="{a['img']}" alt="" loading="lazy"></div>
          <div class="insight-card__meta"><span class="tag">{a['category']}</span><span>{a['date']}</span></div>
          <h3>{a['title']}</h3>
          <p>{a['excerpt']}</p>
        </a>"""
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Insights", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">Insights</span>
      <h1>Legal insights &amp; firm updates</h1>
      <p class="page-hero__lede">Notes from our attorneys on issues that come up often in practice. <!-- TODO: the articles below are sample content demonstrating the layout — replace with the firm's real insights before publishing. --></p>
    </div>
  </section>

  <section class="section--tight section">
    <div class="wrap">
      <a href="insights-{featured['slug']}.html" class="featured-article reveal">
        <div class="featured-article__media"><img src="{featured['img']}" alt="" loading="lazy"></div>
        <div class="featured-article__body">
          <span class="tag" style="width:fit-content">Featured &middot; {featured['category']}</span>
          <h2 style="margin-top:1rem;">{featured['title']}</h2>
          <p style="margin-top:0.8rem;">{featured['excerpt']}</p>
          <span class="text-link" style="margin-top:1.2rem;">Read Article {ICONS['arrow']}</span>
        </div>
      </a>
    </div>
  </section>

  <section class="section" style="padding-top:0;">
    <div class="wrap">
      <div class="section-head--split reveal" style="display:flex;flex-wrap:wrap;gap:1.5rem;justify-content:space-between;align-items:center;margin-bottom:2.5rem;">
        <div class="filter-bar" style="margin:0;" role="group" aria-label="Filter articles by category">{chips}</div>
        <div class="insights-search">
          <input type="search" placeholder="Search insights" aria-label="Search insights" data-insights-search>
          <button type="button" aria-label="Search">{ICONS['arrow']}</button>
        </div>
      </div>
      <div class="grid grid-3" data-insights-grid>{cards}
      </div>
      <p data-insights-empty style="display:none; text-align:center; color:var(--stone-500); margin-top:2rem;">No articles match your search.</p>
      <div class="load-more-wrap">
        <button class="btn btn--ghost" data-load-more>Load More</button>
      </div>
    </div>
  </section>
"""
    write("insights.html", page(
        active="insights",
        title=f"Insights | {SITE_NAME}",
        description="Legal insights and firm updates from M.A Salawu & Co.",
        canonical="insights.html",
        body=body,
        extra_scripts='<script src="js/insights.js" defer></script>',
    ))

    # individual article pages
    for a in ARTICLES:
        others = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
        related = "".join(f"""
        <a href="insights-{o['slug']}.html" class="insight-card card reveal">
          <div class="insight-card__image"><img src="{o['img']}" alt="" loading="lazy"></div>
          <div class="insight-card__meta"><span class="tag">{o['category']}</span><span>{o['date']}</span></div>
          <h3>{o['title']}</h3>
        </a>""" for o in others)
        body_html = "".join(f"<p>{para}</p>" for para in a["body"])
        art_body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Insights","insights.html"),(a['title'], None)])}
      <span class="tag">{a['category']}</span>
      <h1 style="margin-top:1rem;">{a['title']}</h1>
      <div class="article-hero-meta">
        <span>{a['author']}</span><span>&middot;</span><span>{a['date']}</span>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="featured-article__media reveal" style="margin-bottom:3rem;border:1px solid var(--line);">
        <img src="{a['img']}" alt="" loading="lazy" style="width:100%;aspect-ratio:16/8;object-fit:cover;">
      </div>
      <div class="article-body reveal">
        {body_html}
      </div>
    </div>
  </section>
  <section class="section section--ivory">
    <div class="wrap">
      <div class="section-head reveal"><span class="eyebrow">Related</span><h2>More insights</h2></div>
      <div class="grid grid-3">{related}</div>
    </div>
  </section>
  <section class="section section--dark">
    <div class="wrap" style="text-align:center; max-width:700px; margin-inline:auto;">
      <h2>Have a question about your own matter?</h2>
      <div class="hero__actions" style="justify-content:center; margin-top:2rem;">
        <a href="contact.html" class="btn btn--gold">Speak With Our Team {ICONS['arrow']}</a>
      </div>
    </div>
  </section>
"""
        write(f"insights-{a['slug']}.html", page(
            active="insights",
            title=f"{a['title']} | {SITE_NAME} Insights",
            description=a["excerpt"],
            canonical=f"insights-{a['slug']}.html",
            og_type="article",
            body=art_body,
        ))


# =========================================================== CAREERS =======
def build_careers():
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Careers", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">Careers</span>
      <h1>Build your practice with us</h1>
      <p class="page-hero__lede">We look for attorneys and support staff who take client work seriously and want direct responsibility for their matters.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split">
      <div class="reveal">
        <span class="eyebrow">Why Work With Us</span>
        <h2>Real responsibility, from early on</h2>
        <p>Associates at M.A Salawu &amp; Co Chamber work directly on client matters rather than sitting behind layers of review. We believe attorneys grow faster when they carry real responsibility, supported by experienced oversight.</p>
        <ul class="check-list">
          <li>{ICONS['check']}Direct client contact and matter ownership</li>
          <li>{ICONS['check']}Exposure across multiple practice areas</li>
          <li>{ICONS['check']}A small-firm environment based in Badagry, Lagos</li>
        </ul>
      </div>
      <div class="split__media reveal">
        <div class="split__media-frame"></div>
        <img src="img/general/law-firm-office-1.avif" alt="M.A Salawu &amp; Co Chamber office" loading="lazy">
      </div>
    </div>
  </section>

  <section class="section section--ivory">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Culture &amp; Development</span>
        <h2>How we support growth</h2>
      </div>
      <div class="grid grid-3">
        <div class="value-card reveal"><h3>Mentorship</h3><p>Junior attorneys work closely with senior counsel on live matters, not hypothetical exercises.</p></div>
        <div class="value-card reveal"><h3>Ongoing learning</h3><p>Time is made for continuing legal education and staying current on changes in Nigerian law.</p></div>
        <div class="value-card reveal"><h3>Clear expectations</h3><p>Straightforward feedback and a clear sense of what's expected on every matter.</p></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Open Positions</span>
        <h2>Current vacancies</h2>
      </div>
      <div class="empty-state reveal">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3" width="34" height="34" style="margin-inline:auto;"><rect x="4" y="7" width="16" height="12" rx="1.5"/><path d="M8 7V5a2 2 0 012-2h4a2 2 0 012 2v2M4 12h16"/></svg>
        <h3>No open positions at the moment</h3>
        <p style="margin-top:0.6rem;">We aren't actively hiring right now, but we're always glad to hear from strong candidates. Send your CV and a short note about the kind of work you want to do.</p>
        <a href="contact.html" class="btn btn--primary" style="margin-top:1.5rem;">Send A General Application {ICONS['arrow']}</a>
      </div>
    </div>
  </section>
"""
    write("careers.html", page(
        active="careers",
        title=f"Careers | {SITE_NAME}",
        description="Careers and general applications at M.A Salawu & Co, Badagry, Lagos.",
        canonical="careers.html",
        body=body,
    ))


# =========================================================== CONTACT =======
def build_contact():
    pa_options = "".join(f'<option value="{p["slug"]}">{p["title"]}</option>' for p in PRACTICE_AREAS)
    body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Contact", None)])}
      <span class="eyebrow" style="color:var(--gold-500)">Get In Touch</span>
      <h1>Contact us</h1>
      <p class="page-hero__lede">Reach out by phone, email, or the form below and we'll route your enquiry to the right attorney.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap contact-grid">
      <div class="reveal">
        <h3>Office details</h3>
        <div class="contact-detail">
          <div class="contact-detail__icon">{ICONS['pin']}</div>
          <div><h4>Our Office</h4><p>{ADDRESS_LINE1},<br>{ADDRESS_LINE2},<br>{ADDRESS_LINE3}</p></div>
        </div>
        <div class="contact-detail">
          <div class="contact-detail__icon">{ICONS['phone']}</div>
          <div><h4>Phone</h4><p><a href="tel:{PHONE_1_TEL}" class="text-link">{PHONE_1}</a><br><a href="tel:{PHONE_2_TEL}" class="text-link">{PHONE_2}</a></p></div>
        </div>
        <div class="contact-detail">
          <div class="contact-detail__icon">{ICONS['mail']}</div>
          <div><h4>Email</h4><p><a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a></p></div>
        </div>
        <div class="contact-detail">
          <div class="contact-detail__icon">{ICONS['clock']}</div>
          <div><h4>Working Hours</h4><p>{HOURS}</p></div>
        </div>
        <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank" rel="noopener noreferrer" class="btn btn--primary" style="margin-top:1rem;">Chat On WhatsApp {ICONS['arrow']}</a>
        <div class="map-frame reveal">
          <!-- TODO: replace with an embedded Google Map for the exact office location -->
          <iframe title="Office location map" loading="lazy" src="https://www.google.com/maps?q=Badagry,Lagos+State,+Nigeria&output=embed"></iframe>
        </div>
      </div>

      <div class="contact-form-panel reveal">
        <h3>Send a message</h3>
        <p style="margin-top:0.4rem;">We do not send email directly from this form yet &mdash; it's wired to show success and error states, ready to connect to a real backend endpoint.</p>
        <form data-validate style="margin-top:1.6rem;" data-success-message="Thank you. Your message has been received and our team will respond within one business day.">
          <div class="form-status" role="alert"></div>
          <div class="field-row">
            <div class="field">
              <label for="name">Full Name</label>
              <input type="text" id="name" name="name" required>
              <span class="field__error">Please enter your full name.</span>
            </div>
            <div class="field">
              <label for="phone">Phone Number</label>
              <input type="tel" id="phone" name="phone">
              <span class="field__error">Please enter a valid phone number.</span>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="email">Email Address</label>
              <input type="email" id="email" name="email" required>
              <span class="field__error">Please enter a valid email address.</span>
            </div>
            <div class="field">
              <label for="practice-area">Practice Area</label>
              <select id="practice-area" name="practice_area">
                <option value="">Select a practice area</option>
                {pa_options}
                <option value="other">Other / not sure</option>
              </select>
            </div>
          </div>
          <div class="field">
            <label for="subject">Subject</label>
            <input type="text" id="subject" name="subject" required>
            <span class="field__error">Please enter a subject.</span>
          </div>
          <div class="field">
            <label for="message">Message</label>
            <textarea id="message" name="message" required></textarea>
            <span class="field__error">Please tell us a little about your matter.</span>
          </div>
          <button type="submit" class="btn btn--primary btn--block">Send Message</button>
        </form>
      </div>
    </div>
  </section>
"""
    write("contact.html", page(
        active="contact",
        title=f"Contact Us | {SITE_NAME}",
        description="Contact M.A Salawu & Co in Badagry, Lagos by phone, email, WhatsApp, or the contact form.",
        canonical="contact.html",
        body=body,
    ))


# ====================================================== LEGAL PAGES ========
def build_legal_pages():
    privacy_body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Privacy Policy", None)])}
      <h1>Privacy Policy</h1>
      <p class="page-hero__lede">Last updated: <!-- TODO: insert date --></p>
    </div>
  </section>
  <section class="section">
    <div class="wrap legal-body">
      <p><!-- TODO: replace this placeholder policy with one reviewed by the firm and appropriate to applicable Nigerian data protection law (NDPR/NDPA). --></p>
      <h2>Information we collect</h2>
      <p>When you use our contact form, we collect the information you provide, such as your name, email address, phone number, and the details of your enquiry.</p>
      <h2>How we use your information</h2>
      <p>Information submitted through this website is used solely to respond to your enquiry and, where relevant, to provide legal services you have requested.</p>
      <h2>Confidentiality</h2>
      <p>Communications with our firm regarding a legal matter are treated in accordance with attorney-client confidentiality obligations under Nigerian law.</p>
      <h2>Contact</h2>
      <p>Questions about this policy can be directed to <a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a>.</p>
    </div>
  </section>
"""
    write("privacy-policy.html", page(
        active="privacy-policy", title=f"Privacy Policy | {SITE_NAME}",
        description="Privacy policy for M.A Salawu & Co.", canonical="privacy-policy.html", body=privacy_body,
    ))

    terms_body = f"""
  <section class="page-hero">
    <div class="wrap">
      {breadcrumb([("Home","index.html"),("Terms of Use", None)])}
      <h1>Terms of Use</h1>
      <p class="page-hero__lede">Last updated: <!-- TODO: insert date --></p>
    </div>
  </section>
  <section class="section">
    <div class="wrap legal-body">
      <p><!-- TODO: replace this placeholder with terms reviewed by the firm. --></p>
      <h2>No attorney-client relationship</h2>
      <p>Use of this website, including submission of the contact form, does not create an attorney-client relationship between you and M.A Salawu &amp; Co Chamber.</p>
      <h2>No legal advice</h2>
      <p>Content on this website, including the Insights section, is provided for general information only and should not be relied on as legal advice for any specific matter.</p>
      <h2>Intellectual property</h2>
      <p>The content of this website is the property of M.A Salawu &amp; Co Chamber unless otherwise stated and may not be reproduced without permission.</p>
      <h2>Contact</h2>
      <p>Questions about these terms can be directed to <a href="mailto:{EMAIL}" class="text-link">{EMAIL}</a>.</p>
    </div>
  </section>
"""
    write("terms.html", page(
        active="terms", title=f"Terms of Use | {SITE_NAME}",
        description="Terms of use for M.A Salawu & Co.", canonical="terms.html", body=terms_body,
    ))


# =========================================================== 404 ===========
def build_404():
    body = f"""
  <section class="section">
    <div class="wrap error-page">
      <span class="eyebrow">Error 404</span>
      <div class="code">404</div>
      <h1 style="margin-top:1rem;">This page doesn't exist</h1>
      <p class="lede" style="margin-top:0.8rem;">The page you're looking for may have been moved or the link may be out of date.</p>
      <div class="hero__actions" style="margin-top:2rem;">
        <a href="index.html" class="btn btn--primary">Back To Homepage {ICONS['arrow']}</a>
        <a href="contact.html" class="btn btn--ghost">Contact Us</a>
      </div>
    </div>
  </section>
"""
    write("404.html", page(
        active="404", title=f"Page Not Found | {SITE_NAME}",
        description="The page you requested could not be found.", canonical="404.html", body=body,
    ))


if __name__ == "__main__":
    build_index()
    build_about()
    build_practice_areas_index()
    build_practice_pages()
    build_attorneys()
    build_insights()
    build_careers()
    build_contact()
    build_legal_pages()
    build_404()
    print("DONE")

