---
name: lead-research
description: Deep lead research for any product, built on the agreed ICP and personas. Three levels — L1 companies (source candidate accounts from free and connected sources, scan each website/storefront, qualify against the ICP and anti-ICP, score and tier them), L2 people (the decision-makers by persona role, found only through lawful business sources, with a contact route per account and no personal data collected beyond what the company itself publishes or a B2B provider supplies under the product's legal gate), and L3 nurture (a per-persona, per-stage nurture plan and sequence copy drawn from the messaging and value proposition, with cadence, exit rules and CRM fields — drafted, never sent). Measures yield per source before sizing a list, states every credit or paid-tool cost before spending, and names any connection that would be needed (Apollo enrichment, Apify, registry APIs, Sales Navigator, a CRM). Produces products/<slug>/leads/ (lead config, L1 accounts, L2 contact routes, L3 nurture plan + sequence copy, sources & yield log). Trigger with "build a lead list for X", "find leads for X", "prospect list for X", "who should we contact for X", "lead research for X", "find the owners of these stores", "nurture plan for these leads".
version: 1.0.0
---

# GTM Lead Research — L1 companies · L2 people · L3 nurture

**Answers:** *exactly which companies fit the ICP, who inside them to reach, by what lawful route, and what we send them over time.*
It turns Phase 1 (who we sell to and what we say) into a working list. It does **not** send anything.

## Before anything

Follow the shared protocol: `~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md` (GTM_ROOT, evidence tags, deep mode, small briefs that save as they go, measure a list's yield before sizing it, the owner proposes-and-disposes).

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/10_Lead-Nurture.md` (four pillars, compliance caveats, low-touch translation, output contract) · `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` ch.7 (list, personalisation and value-first rules, the 17-day behavioural cadence, ABM maths) · `GTM_ROOT/Frameworks/02_ICP-and-Buying-Center.md` (picking first accounts, buying centre) |
| **Upstream (required)** | `02_ICP.md` + `assets/02_account-qualifier.md` + `assets/02_search-filters.md` + `assets/02_target-accounts.csv` (who) · `02b_Buying-Center-and-Personas.md` + `assets/02b_role-finder.md` (which humans, which channel) · `05_Messaging-and-Channels.md` + `assets/05_channel-plan.md` + `assets/05_copy-kit.md` (**channels, caps, legal gates**, copy) · `assets/03_value-proposition-statement.md` (claims that may be said) |
| **Upstream (if present)** | `06_Proof-System.md` (what proof may be cited), `08_decision-register.md` (open channel/legal decisions) |
| **Writes** | `products/<slug>/leads/` only |
| **Market references** | `references/market-<CC>.md` in this skill (e.g. `market-KSA.md`: sources, prices, legal rules). If none exists for the target market, run a `gtm-machine-os:researcher` brief to create one before step 1 |
| **Tools** | `scripts/storefront_scan.py` (this skill) · `templates/lead-config.example.json` · WebSearch / WebFetch · Apollo MCP (free lookup and people search; **credits only with approval**) · Apify MCP (**paid per result; only with approval**) |

If `02_ICP.md` or `02b` is missing, stop and offer `gtm-machine-os:icp` / `gtm-machine-os:personas`. If `05` has no channel plan, L3 is drafted against `Frameworks/10` only and marked `ASSUMED`.

**Phase 2 gate** (protocol §3): if `08_Coherence-Audit.md` exists and its verdict is **FAIL**, stop and offer `gtm-machine-os:coherence-audit`.

## The compliance gate (read first, every run)

1. **The product's own legal gate wins.** Read `assets/12_legal-gate.csv` if `gtm-machine-os:outbound` has written it (it is the per-country × channel gate and supersedes the rest), else `05_channel-plan.md` (and the decision register), for: allowed channels, caps, which addresses are allowed (e.g. *business-domain only*), banned methods (e.g. *no scraping of addresses, no finder tools*), and any lawyer question still open. Apply them literally. If the plan forbids a method, the skill names it as *not used* and why.
2. **Company data vs personal data.** L1 reads public business facts (platform, payments, registration numbers, social accounts, app). L2 is personal data: collect the **minimum** — role, and a name/business contact only when (a) the company publishes it as its contact, or (b) a B2B data provider supplies it under its terms **and** the product's gate allows that provider. Never personal mobiles, never home addresses, never aggregating one person across sites, never sensitive data.
3. **No automated address harvesting where the market bans it** (e.g. Saudi CST rules). The scanner records *whether* a contact email is published and its kind (own-domain / free-provider / other), not the address. A human copies the address at the source URL, at send time, after the gate check.
4. **Cold messaging channels follow the product plan.** If cold WhatsApp / DMs / calls are excluded there, they are excluded here. Every email carries identification and a working opt-out; record opt-outs as permanent suppressions.
5. **Credits and money are the owner's call.** Before any credit-consuming or paid call (Apollo enrichment/org search, Apify actors, paid APIs), state the exact count and cost and wait for a yes. Free calls (Apollo organization lookup and people search, public pages, Salla reviews API, iTunes lookup) may run.
6. **Consent markets.** Where the law requires prior consent for promotional contact (e.g. Saudi PDPL Art. 25–26, CST 4.6.6.1) and counsel has not cleared a cold first touch, L3's first step must be **non-promotional** (a research/interview request) or an **inbound / consent-capturing** route; promotional sequences start only after a reply or opt-in. Mark the legal question open in the log.
7. **Identity numbers are never stored.** Registry lookups that return national IDs or similar (e.g. Wathq) are for verification only; store "verified: yes/no + date", nothing else.
8. **Respect data-vendor terms.** If a list vendor bans using its data for bulk commercial messages (e.g. Store Leads), use it for discovery only and take contact routes from Route 1.
9. **Never fabricate.** No invented companies, people, titles, emails or "personalisation" facts. Every personalisation token must come from a field recorded in L1/L2 with its source.

## Procedure

### 0. Lead config
Write `leads/lead-config.json` from `templates/lead-config.example.json`, filled from `02_ICP.md` (statement, six dimensions), the anti-ICP and the account qualifier: platforms, required payment methods, domain rule, size/app proxies, vertical keyword sets (market language + English), exclusion words, signal words. Every rule cites the ICP line it comes from. Note which ICP attributes are **not observable** from the outside (e.g. monthly order volume) — those become L2 discovery questions, not filters.

### 1. L1 — Source candidates (deep step ①)
List every source, run the free ones, and **measure yield on a sample of ≥20 before scaling** (`qualified n / scanned N`, per source). Typical sources, in cost order:
- **Existing lists:** `02_target-accounts.csv`, prior research raw files.
- **Platform signals (free):** app-marketplace reviewers of adjacent apps (e.g. Salla: `https://api.salla.dev/marketplace/v2/apps/{id}/reviews` returns reviewer store *names* → resolve name → storefront by web search); App Store merchant apps (`itunes.apple.com/search?...&country=sa`); platform showcase pages.
- **Web search (free):** vertical keywords × platform footprints.
- **Apollo organization lookup (free):** location, size, keyword tags. Expect it to cover the upper part of an SMB band, not micro stores — measure.
- **Paid / connected (ask first):** Apify store/catalog scrapers and social-profile scrapers (per-result pricing), store-list vendors (BuiltWith, Store Leads), registry APIs.
Dedupe by domain; keep the source and date on every row.

### 2. L1 — Scan and qualify
Run `python3 ${CLAUDE_PLUGIN_ROOT}/skills/lead-research/scripts/storefront_scan.py <inputs> leads/lead-config.json leads/L1_scan-<date>.csv`. It respects robots.txt, waits between requests, and records platform, payments (COD), custom domain, registration / business-centre / freelance-document presence, social accounts, branded app + rating count, manual-contact signals in the store's own text, vertical match, and a PASS / BORDERLINE / FAIL verdict with reasons. Then:
- apply the remaining account-qualifier checks by hand for PASS/BORDERLINE (e.g. reviews showing campaign/broadcast intent → anti-ICP);
- **score** each PASS on the ICP weights (from `assets/02_icp-scorecard.csv`) and assign **Tier A** (fits + trigger present), **Tier B** (fits, no trigger), **Tier C** (borderline);
- write `leads/L1_accounts.csv`.

### 3. L2 — People and contact routes (deep step ①, personas from 02b)
For each Tier A/B account, per persona that holds veto or is the primary user:
- **Route 1 — what the company publishes** (storefront contact, about page, official social profile, registration record): role-level contact + source URL. Usually the strongest lawful route for owner-run SMBs.
- **Route 2 — B2B data provider** (e.g. Apollo people search, free → enrichment, 1 credit per person): only if the gate allows the provider; state the count and credits first. Record provider, date, and the lawful-basis note.
- **Route 3 — manual professional networks** (LinkedIn / Sales Navigator): manual lookup only, never scraped; record "found / not found".
- **Route 4 — registries** (commercial-registration lookups): to confirm the business and its owner *role*; use paid APIs only with approval.
Write `leads/L2_contacts.csv`: account, persona, role/title, name (only if lawful per gate, else blank), contact route, contact kind (business-domain email / form / none), source URL, provider, date, gate check (pass/fail + rule), suppression flag. **Never store personal mobiles or WhatsApp numbers.**

### 4. L3 — Nurture (Frameworks/10 + 13 ch.7 + 05 copy)
Per persona × stage (cold → replied → interview/demo → trial → customer → lost/not-now):
- **Goal and exit rule** for each stage; the one metric (Frameworks/10 "three numbers").
- **Cadence** within the product's caps (e.g. ≤40/week, one follow-up) and Voje's value-first rules; channel per the product plan.
- **Messages** taken from `05_copy-kit.md` and `03_value-proposition-statement.md` only — no new claims; personalisation tokens limited to recorded L1/L2 fields (e.g. vertical, a signal with its source).
- **Speed and availability** rules (Frameworks/10 pillars I–II) for replies.
- **Not-now / lost loop** with a dated re-touch.
- **CRM fields and tool mapping** (Apollo sequence, Kit, HubSpot, or a spreadsheet): what to import, which fields, suppression list. **Drafts only** — creating sequences, adding contacts or sending needs the owner's explicit yes per action.
Write `leads/L3_nurture-plan.md` and `leads/L3_sequence-copy.md`, and lint the copy with the product's linter if it exists (`assets/05_copy-lint.py`).

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`: a sample of 10 L1 rows (re-check verdicts against the live storefronts), the L2 file (gate compliance, no personal data beyond the rule, sources real), the L3 copy (claims vs the register, banned phrases, personalisation tokens traceable), and the yield arithmetic. Fix or carry into Open questions.

### 6. Log and present
`leads/leads-log.md`: date, sources run, N scanned, yield per source, credits/money spent (0 unless approved), connections still missing, gate rules applied. Update the tracker's Pillar 9 row per protocol §10 (only the list boxes `leads/` shows), then present per protocol §8: list size by tier, yield per source, contact-route coverage, what needs the owner (credits, connections, legal), and the next send window under the channel cap.

## Outputs (`products/<slug>/leads/`)

| File | What it is | Usable for |
|---|---|---|
| `lead-config.json` | ICP rules as machine-checkable config, each rule cited | Re-running the scan as the ICP changes |
| `L1_scan-<date>.csv` | Raw scanner output | Audit trail |
| `L1_accounts.csv` | Qualified accounts: verdict, tier, score, vertical, signals, sources | The account list |
| `L2_contacts.csv` | Contact routes per account × persona, with gate check and source | Who to reach and how, lawfully |
| `L3_nurture-plan.md` | Persona × stage plan: goals, cadence, exits, metrics, CRM mapping | Running the nurture |
| `L3_sequence-copy.md` | The messages, from the copy kit and statement only, linted | Sending (after approval) |
| `leads-log.md` | Sources, yields, costs, missing connections, gate rules | Knowing what the list is worth |

## Connections (what works now vs what needs a connection)
Maintain this table in `leads-log.md` per run; market-specific facts live in `references/market-<CC>.md`. Defaults (tested 2026-10-11):

| Capability | Works now (free) | Needs approval (credits / money) | Needs a new connection or account |
|---|---|---|---|
| Find candidate companies | Web search; platform marketplace reviews API; App Store search; **Apollo organization lookup** | Apollo organization search (1 credit/request); Apify store scrapers (per result) | **Store Leads** ($75/mo UI, $250/mo CSV/API; discovery only) or BuiltWith |
| Qualify a store | **`storefront_scan.py`** (public storefront + iTunes lookup) | Apify catalogue scrapers (catalogue size as a volume proxy) | — |
| Find the decision-maker | Company-published contacts (Route 1); **Apollo people search** (masked names + has-email flags, no credits) | **Apollo people enrichment** (1 lead credit/person; phone/waterfall extra) | **Wathq CR API** (owner names, verification only; ~SAR 3/record via reseller); **LinkedIn Sales Navigator** (manual only); Hunter/Lusha-type finders (only if the gate allows) |
| Verify the business | SBC / MoC lookups by hand (captcha) | — | Wathq API |
| Nurture / send | Drafts in files | Apollo sequences, Kit broadcasts (each create/send = the owner's yes) | A CRM (e.g. HubSpot plugin needs auth); a sending domain with SPF/DKIM/DMARC; **Saudi counsel's answer on cold first contact** |

## Checks before presenting
- [ ] Gate read from the product's channel plan; every banned method named as not used
- [ ] Lead config cites the ICP line behind each rule; non-observable attributes listed as L2 questions
- [ ] Yield measured per source on ≥20 before scaling; numbers in the log
- [ ] L1: verdicts with reasons; tiers; sources and dates on every row; zero invented companies
- [ ] L2: minimum personal data; no personal mobiles/WhatsApp; gate check per row; sources real
- [ ] L3: every claim traces to the claims register / copy kit; tokens trace to recorded fields; caps and opt-out present; linted
- [ ] No credit or money spent without a recorded yes; missing connections named
- [ ] Consent-market rule applied (first touch non-promotional or inbound until counsel clears); no identity numbers stored; vendor terms respected
- [ ] Nothing sent, no sequence created, no contact added to any tool without the owner's explicit yes
