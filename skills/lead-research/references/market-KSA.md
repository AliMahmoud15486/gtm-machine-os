# Market reference — Saudi Arabia (e-commerce SMB leads)

Researched 2026-10-11 (the source run's `research/` lead-sources file has URLs and dates). Re-check before
relying on any price or rule older than 6 months. Generic to any product selling to Saudi online stores.

## Sources

| Source | Business fields | Owner fields | Cost | Connection | Verdict |
|---|---|---|---|---|---|
| Salla storefront (`twilight::init` store object) | store id, name, payments (COD), CR number, SBC certificate, freelance doc, published contacts, social, apps, order texts | **none** (no owner field) | free | none | **Use** (scanner); contacts copied by hand only if the gate allows |
| Zid storefront | CR, VAT, published contacts | none | free | none | Use (scanner detects platform; Zid parsing is shallow) |
| Salla marketplace reviews API | reviewer store **name**, rating, comment, date | none | free | none | Use for sourcing (resolve name → storefront) |
| App Store search / lookup (`itunes.apple.com`, `country=sa`) | merchant apps, rating counts | none | free | none | Use (size/brand proxy) |
| Store Leads | 13,262 live Salla, 12,269 live Zid stores (2026-10-02); filters; % with phone/email | none | $75/mo UI; **$250/mo** CSV/API | account | **Discovery only**: its terms ban using its data for bulk commercial messages |
| BuiltWith | ~52.4k Salla sites (different counting) | none | paid | account | Discovery cross-check |
| Apollo | KSA brands at the upper SMB band (free lookup returned 0/4 named micro-stores, 2026-10-11); people search: 206 owner/founder/CEO records at 1–50-staff KSA perfume/abaya/cosmetics orgs, ~half with an email on file | names, titles, business emails (enrichment) | lookup + people search free; enrichment 1 credit/person | connected (MCP) | Test match rate on a sample; enrichment only if the gate allows a data provider |
| Wathq CR API | CR status, activities | **manager/partner names + national IDs**, optional contacts | ~SAR 3/record via a reseller; Wathq's own price UNKNOWN | API key / account | **Verification only.** Never store national IDs; don't use for list-building |
| SBC e-store authentication; MoC CR lookup | authentication / CR status | limited | free | captcha, one at a time | Manual verification |
| LinkedIn / Sales Navigator; Instagram / TikTok / Snapchat | profiles | sometimes | Sales Nav paid | account | **Manual only**: platform terms ban automated collection |
| Apify social/profile scrapers | profiles, bios, links | sometimes | per result | connected (MCP) | **Avoid** for contact harvesting (platform terms; CST harvesting rule) |
| Google Places | weak for online-only stores | none | paid API | key | Avoid |

## Legal rules that bind outreach (primary texts)

- **PDPL Art. 25:** advertising/awareness material to a person's personal postal or electronic address needs their **prior consent**, with a way to stop.
- **PDPL Art. 26:** personal data may be used for marketing only if collected **directly from the person** with consent.
- **Implementing Regulation Arts. 28–29:** consent requirements; easy opt-out.
- **CST anti-spam regulation (v3, 2022) 4.6.6.1:** promotional messages and calls need **express consent, with proof**. **4.6.10:** addresses collected by harvesting software may not be used.
- **No B2B exemption** found in any of these. Whether a cold first contact to an owner-run store is lawful is **UNKNOWN — needs Saudi counsel**.
- **WhatsApp Business policy (updated 2026-09-23):** message only people who gave you their number and opted in (app and API).
- **Penalties:** PDPL up to SAR 5M per violation; Telecom Law up to SAR 25M (secondary source).
- **Draft PDPL amendments** tightening marketing rules: consultation 2026-10-06 → 2026-11-05. Re-check after.

## What this means for the skill's defaults in KSA

1. L1 (companies) is fully workable from public storefronts and free sources.
2. L2 (owners): the company-published contact is the main route; owner names are rarely public; Wathq is verification only; B2B providers (Apollo etc.) only if the product's gate and counsel allow.
3. L3 (nurture): until counsel clears a cold first touch, the first step is **non-promotional** (e.g. a founder's research/interview request to a published business-domain address, manual, capped) or an **inbound / consent-capturing** route (listing, community, referrals). Promotional sequences start only after a reply or opt-in. Never cold WhatsApp.
