# Market reference — Egypt (B2B leads, incl. retail chains)

Researched 2026-10-21. Generic to any product selling to Egyptian companies. Re-check before relying on any rule
older than 6 months — **the PDPL grace period ends ~2026-11-01, days after this snapshot.** Tags: `RESEARCHED-P` =
primary text read (English translation of the law); `RESEARCHED-S` = law-firm / reputable secondary summary;
`ASSUMED` = inference. Laws were read in **English translations** hosted by law firms, not the Arabic Official Gazette.

## Sources

| Source | Business fields | Owner fields | Cost | Connection | Verdict |
|---|---|---|---|---|---|
| Commercial Register (under the Ministry of Supply / Internal Trade Development Authority per InfobelPRO; GAFI is the investment authority, not the register) | CR status, legal form, activity | UNKNOWN | extract ~EGP 130–230 (Legalmondo, secondary) | online route claimed via Digital Egypt (needs CR or tax no.); others say in-person via lawyer — **conflicting, unverified** | **Verification only**, manual |
| GAFI (`gafi.gov.eg`, reachable 2026-10-21) | company-formation / investor services | UNKNOWN | UNKNOWN | browser | Verification / context only; no public bulk company search found |
| EGX (`egx.com.eg`, unreachable 2026-10-21) | listed-company profiles, sector, disclosures, board | board names (public filings) | free | browser | **Use for the listed tier.** Third-party sites put a few EGX names in "General Retailers" / "Distribution Services"; official sector list **not verified** |
| Mall directories — Cairo Festival City ("over 300 shops and restaurants", tenant site `festivalcitymallcairo.com`), City Stars (site is Flash-only), Mall of Egypt (`/en/shop` 404) — all checked 2026-10-21 | brand / tenant names, category | none | free | browser (JS / broken) | **Discovery**: brand names only; mall sites publish only mall-level contacts |
| Apollo | Run 2026-10-21: org search (NAICS 44–45, 51–2,000 staff, exclusions) = 293 Egypt-HQ records; ~1 in 3 of those with an in-band branch count qualified | names, titles, business emails (enrichment) | search free; enrichment 1 credit/person | MCP (not available to this pass) | Run the same NAICS 44/45 filter used for KW/KSA before relying on it; enrichment only if the gate allows a data provider |
| Third-party "Egypt company databases" (InfobelPRO, Kompass, etc.) | vendor claims | some | paid | account | **Avoid** until provenance and terms are checked |
| LinkedIn / Sales Navigator; Instagram / Facebook | profiles | sometimes | Sales Nav paid | account | **Manual only** (platform terms ban automated collection) |

`ASSUMED`: as in KW/KSA, many mall brands are run by one franchise operator — dedupe brand → operating company.

## Legal rules that bind outreach

**PDPL — Law 151/2020** (`RESEARCHED-P`, English translation, ACC/Andersen-hosted PDFs, read 2026-10-21)
- Issued 2020-07-13; in force 3 months after gazette publication (Issuing Art. 7). Applies to personal data
  processed electronically "in relation to **natural persons**" (Issuing Art. 1). Data about a company as such is
  not personal data; **a named employee's business email still is** (`ASSUMED` from the definition).
- **Art. 2:** no collection/processing without the data subject's **explicit consent** or where permitted by law.
  Art. 6 lists other legal bases (contract, legal obligation, controller's obligations / legitimate rights — text
  partly garbled in the translation read).
- **Electronic Marketing (Art. 1 definition):** any message, statement or ad "via any technological means" promoting
  goods or services "addressed to specific persons".
- **Art. 17:** direct-marketing electronic communication is **prohibited unless** (1) the data subject consented,
  (2) sender identity shown, (3) valid, complete sender address, (4) clearly marked as direct marketing,
  (5) simple opt-out / withdrawal.
- **Art. 18:** defined marketing purpose; never disclose the recipient's contact details; keep electronic consent
  records for **3 years after the last message**.
- **Art. 14–16:** cross-border transfer only to a country with equal-or-better protection **and** with a PDPC licence or
  permit; Art. 15 exceptions require explicit consent (e.g. contract performance for the data subject's benefit).
- **Art. 26:** PDPC issues licences/permits for controllers/processors **and separately for direct electronic marketing**.
- **Penalties:** Art. 43 marketing breaches EGP 200,000–2,000,000; Art. 36 processing without consent EGP
  100,000–1,000,000 (prison if for gain); Art. 42 cross-border 3+ months and/or EGP 500,000–5,000,000; Art. 45
  licence breaches EGP 500,000–5,000,000; Art. 47 de facto manager personally liable if he knew.

**Executive Regulations — Ministerial Decree 816/2025** (`RESEARCHED-S`: Consortio English translation; Baker
McKenzie 2026-01-12; Shand Partners 2026-01-11)
- Gazette No. 244 (Suppl. A) dated **2025-11-01**, in force 2025-11-02; Baker McKenzie says publicly released only
  2025-12-25. Grace period (Issuing Art. 6: one year from the ERs) ends **2026-11-01** (Shand, Baker); some sources say
  2026-10-31. **No extension found** (searches 2026-10-21).
- **ER Art. 18:** direct-marketing sender must hold a **PDPC marketing licence**, have **explicit consent**, identify caller
  and purpose at the start, offer refusal/withdrawal, keep records for the PDPC; erase data when consent is withdrawn.
- **ER Art. 29:** marketing licence categories — own products (fee = 10% of the controller/processor fee) or for
  others (25%). **ER Art. 19:** 1–100,000 records are exempt from **fees** (Shand) — whether also exempt from the
  **licence itself** is unclear (Baker says "exempt") → **UNKNOWN — needs Egyptian counsel**.
- PDPC decides within 90 business days; silence = rejection (ER Art. 26). Foreign controllers processing data of people
  in Egypt need an Egypt-based representative (Baker). PDPC licensing portal reported launched ~2026-10-07 —
  **unconfirmed** against a PDPC notice (`pdpc.gov.eg` is JS-rendered; nothing readable 2026-10-21).
- **No B2B / business-contact exemption** found in the Law, the ER translation, or any firm summary.

**Cybercrime Law 175/2018, Art. 25** (`RESEARCHED-S`, Andersen 2021-10-12, quoting the article): anyone who
"consistently sent numerous emails to a particular person without his or her consent" → 6+ months and/or EGP
50,000–100,000. Threshold for "numerous" UNKNOWN.

**SMS / calls — NTRA** (`RESEARCHED-S`; **no primary NTRA text found**)
- Promotional calls: companies must register numbers and promotional activity with operators; NTRA began
  disconnecting unregistered promotional callers from 2025-08-24 (Amwal Al Ghad, 2025-08-19). Telecom Law 10/2003 and
  Cybercrime Law cited in enforcement.
- SMS: registered alphanumeric sender IDs on all four networks; prior opt-in; opt-out (vendor guides BroadNet, sent.dm,
  2026 — not legal authority). PDPL Art. 17 already covers SMS as "any technological means" (`RESEARCHED-P`).

**Consumer Protection Law 181/2018** (`RESEARCHED-P`, Andersen translation) — "Consumer" = person buying for
**non-professional / non-commercial** needs, so B2B buyers are largely outside it (`ASSUMED`). Binding where it applies:
no deceptive advertising (Art. 9); contests notified 3 days ahead (Art. 14); no sales visits to homes unless requested
(Art. 16). No cold-email or telemarketing rule in it.

**WhatsApp Business Policy** (updated 2026-09-23, `RESEARCHED-P`): only people who gave you their number **and**
opted in; opt-in must comply with local law; honour all opt-outs.

## What this means for the skill's defaults in Egypt

1. L1 (companies) workable from EGX filings (listed tier) and mall directories (brand discovery); CR / GAFI are
   verification only; Apollo coverage must be tested before use.
2. L2 (people): business-domain addresses of named staff are **personal data** under the PDPL; storing them needs a
   legal basis (consent or another Art. 6 ground — **UNKNOWN — needs Egyptian counsel** which applies). Third-party
   databases stay out until provenance is checked; keep records ≤100k and hosted per the cross-border rules.
3. L3 (nurture): a cold **promotional** email, SMS or WhatsApp to a named person has **no B2B exemption** — PDPL Arts. 17
   and ER Art. 18 require prior consent **and** a PDPC marketing licence. A first contact to a company's **general
   published address** (info@, not a person) may fall outside "personal data" — **UNKNOWN — needs Egyptian counsel**;
   not law. Default until cleared: manual, capped, **non-promotional** (research / interview request), identify sender,
   full address, purpose and one-click stop, no repeat sends. **Never cold WhatsApp, SMS or promotional calls.**
   Promotional sequences only after reply / documented opt-in, with consent records kept 3 years.

## Sources (accessed 2026-10-21)

- PDPL 151/2020 EN: https://www.acc.com/sites/default/files/program-materials/upload/Data%20Protection%20Law%20-%20Egypt%20-%20EN%20-%20MBH.PDF · https://eg.andersen.com/wp-content/uploads/2025/06/Law-No.-151-OF-2020.pdf
- ER Decree 816/2025 EN (Consortio): https://consortiolawfirm.com/egypt-data-protection-law-executive-regulations-2025-english/
- Baker McKenzie (2026-01-12): https://connectontech.bakermckenzie.com/egypt-important-data-protection-update/
- Shand Partners (2026-01-11): https://www.shandpartners.com/insights/briefings/telecoms-media-technology/the-issuance-of-the-executive-regulations-of-the-data-protection-law-and-the-establishment-of-the-data-protection-centre/
- Portal-launch claim (low confidence, 2026-10-18): https://dataprotection.gi/jurisdictions/egypt/ · PDPC: https://pdpc.gov.eg/
- Cybercrime Art. 25 (Andersen, 2021-10-12): https://eg.andersen.com/violating-the-sanctity-of-private-life/
- NTRA calls (2025-08-19): https://en.amwalalghad.com/egypts-telecom-watchdog-to-block-unregistered-spam-call-devices-aug-24/ · SMS vendor guide: https://www.broadnet.me/blog/egypt-a2p-sms-sender-id-pdpl-guide-2026
- CPL 181/2018 EN: https://eg.andersen.com/wp-content/uploads/2025/07/Law-No.-181-of-2018.pdf
- WhatsApp Business Policy (2026-09-23): https://whatsappbusiness.com/policy/
- Commercial register (secondary): https://www.infobelpro.com/en/blog/egypt-company-lookup-guide · https://legalmondo.com/?p=28001
- Malls: https://www.cairofestivalcity.com/ · https://www.citystars.com.eg/ · EGX: https://www.egx.com.eg/ · GAFI: https://gafi.gov.eg/en
