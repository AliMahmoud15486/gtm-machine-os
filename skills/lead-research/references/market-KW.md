# Market reference — Kuwait (B2B leads, incl. retail chains)

Researched 2026-10-20. Generic to any product selling to Kuwaiti companies. Re-check before relying on any rule
older than 6 months. Tags: `RESEARCHED-P` = primary text read; `RESEARCHED-S` = law-firm / reputable secondary
summary (primary not machine-readable or not found); `ASSUMED` = inference. **Primary texts of the 2024 CITRA
regulation and Law 20/2014 are scanned images on official sites and were not read article-by-article here.**

## Sources

| Source | Business fields | Owner fields | Cost | Connection | Verdict |
|---|---|---|---|---|---|
| MOCI commercial-register e-services (`ereg.moci.gov.kw`) | CR / licence data (fields UNKNOWN — login wall) | UNKNOWN | UNKNOWN | account login | **Verification only**, manual; no free public search found (2026-10-20) |
| Kuwait Chamber of Commerce & Industry (`kuwaitchamber.org.kw`) | member directory UNKNOWN (site not fetchable, HTTP 307) | UNKNOWN | UNKNOWN | browser | Check manually; >79,000 registered members (Wikipedia, secondary) |
| Boursa Kuwait (`boursakuwait.com.kw`) | listed-company profiles, sector, annual reports, board | board names (public filings) | free | browser (site returned 403 to fetch) | **Use for the listed tier**; retail sits in Consumer Discretionary / Staples sectors (Kamco reports) |
| Mall directories — The Avenues (`the-avenues.com/kuwait/en/shop`, 21 shop categories), 360 Mall (`360-kuwait.com`, "under maintenance" 2026-10-20), Assima (`theassima.com`, not checked; 3D Wayfinder hosts a directory) | brand / tenant names, category | none | free | browser (JS-rendered) | **Discovery**: brand names only; mall sites publish only mall-level contacts |
| Apollo | 70 orgs: HQ Kuwait, NAICS 44/45 excl. auto/fuel/grocery/restaurants, 51–2,000 staff (search run 2026-10-20). Same filter for KSA: 338 | names, titles, business emails (enrichment) | search free; enrichment 1 credit/person | connected (MCP) | Usable for the mid/large tier; test match rate on a sample; enrichment only if the gate allows a data provider |
| Third-party "Kuwait B2B databases" (companydata.com, InfobelPRO) | claim MOCI-sourced CR, address, status | some | paid | account | **Avoid** until provenance and terms are checked (vendor claims only) |
| LinkedIn / Sales Navigator; Instagram | profiles | sometimes | Sales Nav paid | account | **Manual only** (platform terms ban automated collection) |

**Structure note** (`RESEARCHED-S`, Mordor Intelligence + Alshaya Wikipedia, 2024–26): mall retail is concentrated in
franchise operators running dozens of international brands each (one Kuwait-HQ operator: 70+ brands). `ASSUMED`:
many mall "brands" resolve to one operator — dedupe brand → operating company before counting accounts.

## Legal rules that bind outreach

- **No comprehensive personal-data law** for all businesses (`RESEARCHED-S`: DLA Piper, last modified 2025-02-04;
  Chambers 2026, GLA & Co., updated 2026-03-10). No draft comprehensive PDPL found in 2025–26 searches.
- **CITRA Data Privacy Protection Regulation.** Resolution 42/2021 applied "to the public and private sectors in the
  State of Kuwait" (Art. I) (`RESEARCHED-P`, citra.gov.kw PDF, read 2026-10-20). **Replaced by Decision 26/2024**
  (gazette 2024-02-18, per Tamimi/Access Partnership 2024-03-19), which applies **only to CITRA-licensed service
  providers** — though "service provider" is defined broadly to include anyone operating a **website, app or cloud
  service** collecting personal data (`RESEARCHED-S`, DLA Piper). Whether a non-licensed seller is caught is
  **UNKNOWN — needs Kuwaiti counsel**.
  - Consent: explicit user consent before collection (`RESEARCHED-S`, Access Partnership 2024-03-19).
  - Cross-border: licensees must notify data subjects / record destination countries (Art. 4(11) per Chambers).
  - Penalties: none in the regulation; CITRA Law 37/2014 provides 1–5 yrs prison and/or KWD 500–20,000
    (`RESEARCHED-S`, DLA Piper); Art. 49 lets CITRA order a remedy within 90 days (Chambers).
- **Law 20/2014 (Electronic Transactions), Ch. 7 privacy** — binds companies generally. Personal data in electronic
  systems may not be accessed/disclosed without the person's consent; must state purpose, keep accurate, secure
  (`RESEARCHED-S`, ASAR / GlobalComplianceNews 2015-12-11; Chambers 2026). Art. 37: up to 3 yrs and KWD 5,000–20,000.
  Whether "personal data" covers juristic persons is **unclear** (ASAR). It contains **no marketing-specific rule**
  found by any source.
- **Spam / e-marketing.** No general anti-spam law for non-licensees found. CITRA rules bind **licensees**:
  opt-out database for unwanted messages (CITRA Regulations Art. 12), commercial messages only **07:00–22:00
  Kuwait time**, marketing contacts must identify sender and reason and let the recipient stop (User Guidelines
  Art. 14) (`RESEARCHED-S`, Chambers 2026; Lexis Middle East 2022-04-27). A CITRA DND registry is claimed only by SMS
  vendors — **unverified**. Kuwait SMS senders need registered sender IDs via operators (vendor claims, `RESEARCHED-S`).
- **No email-specific rule and no B2B exemption** found in any source (Chambers: B2B "not addressed").
- **WhatsApp Business policy** (last updated 2026-09-23, `RESEARCHED-P`): message only people who gave you their
  number **and** opted in; you own the opt-in method and must comply with local law; honour all opt-outs. Applies
  in Kuwait as everywhere.
- **Cybercrime Law 63/2015**: unlawful access to data, up to 6 months / KWD 500–2,000, more if data disclosed.

## What this means for the skill's defaults in Kuwait

1. L1 (companies) is workable from free public sources: Boursa filings (listed tier), mall directories for brand
   discovery, Apollo for the 51–2,000-staff tier; MOCI is verification only (login).
2. L2 (people): Apollo / LinkedIn for named decision-makers; use **business-domain** addresses; resolve brand →
   operator first. Third-party CR databases stay out until provenance is checked.
3. L3 (nurture): a cold first contact to a **company's general published address** has **no explicit prohibition
   found** for non-licensees — but its lawfulness is **UNKNOWN — needs Kuwaiti counsel** (DPPR scope via "website
   operator", Law 20/2014 consent, juristic-person coverage all unresolved). Default until cleared: manual, capped,
   identify sender and reason, one-click stop, 07:00–22:00 send window, honour opt-out immediately.
   **Never cold WhatsApp. Never cold SMS.** Promotional sequences only after reply or opt-in.

## Sources (accessed 2026-10-20)

- CITRA Res. 42/2021: https://www.citra.gov.kw/sites/en/LegalReferences/Resolution-No-42-On-Data-Privacy-Protection-Regulation.pdf
- CITRA DPPR scan (13 pp, not OCR'd): https://www.citra.gov.kw/sites/en/LegalReferences/Data_Privacy_Protection_Regulation.pdf
- Chambers DP&P 2026 Kuwait (GLA & Co., 2026-03-10): https://practiceguides.chambers.com/practice-guides/data-protection-privacy-2026/kuwait
- DLA Piper Kuwait (2025-02-04): https://www.dlapiperdataprotection.com/countries/kuwait/law.html
- Access Partnership (2024-03-19): https://accesspartnership.com/access-alert-kuwaiti-regulator-introduces-new-data-protection-regulation
- Tamimi (gazette 2024-02-18): https://www.tamimi.com/news/kuwait-data-privacy-protection-regulations/
- Law 20/2014 summary (ASAR, 2015-12-11): https://www.globalcompliancenews.com/2015/12/11/kuwait-law-regarding-electronic-transactions-in-force-introduction-of-a-concept-akin-to-data-privacy/
- Law 20/2014 EN translation (scan): kdipa.gov.kw/wp-content/uploads/2022/08/ (Electronic Transactions Law 20/2014 PDF)
- CITRA user-rights regulations (Lexis ME, 2022-04-27): https://www.lexis.ae/2022/04/27/kuwait-regulations-to-protect-the-rights-of-technology-users-approved/
- WhatsApp Business Policy (2026-09-23): https://whatsappbusiness.com/policy/
- MOCI: https://www.moci.gov.kw/ · The Avenues: https://www.the-avenues.com/kuwait/en/shop · Retail concentration: https://www.mordorintelligence.com/industry-reports/retail-industry-in-kuwait/companies
