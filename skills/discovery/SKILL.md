---
name: discovery
description: GTM Step 0 — deep discovery of the company and product BEFORE any strategy work. Builds one verified fact base the whole GTM Machine OS rests on — product truth (what the code, config and live product actually do), public footprint (website, store listings, app stores, social, every public claim captured verbatim), legal pages (privacy policy, terms — promises and roles), commercial facts (prices, billing, platform cut, unit costs, payout and tax setup), platform and provider dependencies (approval status, policies, quality ratings), evidence inventory (customers, users, usage, reviews, interviews, deals), operations and capacity, instrumentation, compliance risks, a quick category and competitor scan, and the decisions already made. Cross-checks public claims against product truth to catch contradictions early, then asks the owner one ranked question bank covering only what research could not answer, each question tagged with the pillar it unblocks. Works for the owner's own products (with docs/code access) and for client companies (public research + a discovery call). Deep by default (researcher → evidence auditor). Produces 00_Discovery.md, a filled 00_Intake.md and assets (fact base, claims-vs-truth, question bank, evidence inventory, risk register, source map). Trigger with "discovery for X", "research the company X before the strategy", "deep research on X", "start a GTM for X", "onboard X into the GTM machine", "what do we know about X", or as step 0 of gtm-machine-os:strategy.
---

# GTM Discovery — Step 0 (before the strategy)

**Answers:** *what is actually true about this company and product today — and what must the owner tell us that no research can?*
Every pillar after this reads `00_Discovery.md` instead of rediscovering the company piecemeal. A fact found late (a live bug, a policy promise, a false public claim) forces rewrites in files already written; finding it here is the point of this skill.

## Before anything

Follow the shared protocol (it is part of this skill): `~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md` — GTM_ROOT, evidence tags, deep mode with small briefs that save as they go, the owner proposes-and-disposes.

| | |
|---|---|
| **Method** | This file · `GTM_ROOT/Frameworks/00_GTM-Pillar-Roadmap.md` (what each pillar will need from discovery) · the output contracts at the bottom of `Frameworks/01`–`07` (read their *inputs* lines) |
| **Inputs** | Product name; any of: docs folder in the product's own docs folder, code repo, live URLs (website, store listing, app-store pages), admin/portal access the owner can describe, prior GTM files |
| **Writes** | `products/<slug>/00_Discovery.md` · `products/<slug>/00_Intake.md` (filled from discovery; the owner confirms) · `products/<slug>/assets/00_*` · research to `products/<slug>/research/` |
| **Template** | `template.md` in this skill's folder; discovery-call script: `GTM_ROOT/products/_TEMPLATE/00b_Discovery-Call.md` (client companies) |
| **Downstream** | Every pillar. A **material** change on re-run (stage, evidence count, product truth, prices, legal promise, platform status) marks `01` onward `STALE`; a non-material refresh does not — say which it is |

If `products/<slug>/` doesn't exist, copy `products/_TEMPLATE/` to it first.

## Mode: own product or client company

- **Own product** (the owner's, with docs/code access): product truth comes from code, config and docs; the question bank goes to the owner.
- **Client company** (no code access): product truth comes from public material, demos and the discovery call (`00b_Discovery-Call.md`); the question bank becomes the call agenda. Never present a client's claims about their product as `VALIDATED` — they are `ASSUMED (owner-stated)` until seen.

State the mode in the first line of `00_Discovery.md`.

## Rules

1. **Read before asking.** Ask the owner only what the docs, code, live product and public sources cannot answer. Every question in the bank says what was already checked.
2. **Product truth is checked against the code or the live product**, not against the docs or the marketing. Where they differ, the code/live product wins and the gap is a finding.
3. **Every public claim is captured verbatim** with URL and date (website, listing, app stores, social bios, ads, decks). Each one is then marked against product truth: true · true with a condition · unsupported · false.
4. **Legal pages are read in full.** Record every promise that constrains GTM: data retention, legal bases, controller/processor role, refund/cancellation terms, claims about security or certification.
5. **Commercial facts are primary-sourced:** the live price page and billing portal, the platform's partner terms, providers' rate cards — not memory or old docs.
6. **Count the evidence exactly** (customers, users, months of usage, interviews, reviews, deals won/lost with reasons). Zero is a number. This count sets how much of the strategy can be `VALIDATED`.
7. **No fabrication.** No invented customers, quotes, numbers or competitors. Unknowns are `UNKNOWN — needs measurement` or a question in the bank.
8. **Discovery is not strategy.** Record facts, risks and questions; do not choose segments, ICPs or positioning here. A quick category/competitor scan seeds Pillar 1; it doesn't replace it.
9. **No secrets in files.** Never copy credentials, API keys, tokens or customer personal data into discovery files; record *that* access exists and where.
10. **Touch nothing.** Discovery reads; it never edits the product, its repo, listings or settings. Fixes become findings for the owner.

## The 13 areas (all of them, every run)

| # | Area | What to establish | Feeds |
|---|---|---|---|
| A1 | **Identity & entity** | Legal entity, country of incorporation and tax residency (as far as public or stated), registrations, founders/team size, brand and domain ownership | 07 pricing (tax/payouts), 05 legal |
| A2 | **Product truth** | Capabilities available today (with code/config/demo source), plans and limits *as the code enforces them*, integrations, onboarding steps, known bugs touching customers, roadmap items (labelled as such) | 03, 04, 06, 07 |
| A3 | **Public footprint & claims** | Every live surface and every claim on it, verbatim, with status vs A2 | 04, 05, 06 |
| A4 | **Legal pages** | Privacy policy, terms, DPA, cookie/consent: promises that bind GTM and data handling | 05, 06, lead research |
| A5 | **Commercial facts** | Current prices, billing mechanics, trial, refunds, platform commission, unit costs (rate cards), payout terms, discounts in use | 07 |
| A6 | **Platform & provider dependencies** | Marketplace/app-store rules and approval status, messaging/API provider policies, quality or rating systems, capacity limits, anything a third party can switch off | 04, 05, 07 |
| A7 | **Category & competitor quick scan** | How the category is named, 5–10 named alternatives incl. platform-native and DIY, their public prices — to seed Pillar 1, not to rank | 01, 04 |
| A8 | **Evidence inventory** | Customers, users, usage data (months, events), reviews (count, rating, themes with ids), interviews, deals won/lost with reasons, existing proof assets and their consent | 02, 03, 06 (sets the evidence ratio) |
| A9 | **Operations & capacity** | Who does what, founder hours per week, support SLA, budget, tools in place (CRM, email domain + SPF/DKIM/DMARC, analytics), languages served | 05, 07, Phase 2 |
| A10 | **Instrumentation** | What the product already records (events, tables, dashboards), what is missing for the metrics GTM will need | 03, 06 |
| A11 | **Compliance & risk** | Data-protection role and obligations, messaging/anti-spam rules, advertising and claims law, sector licences, platform policy risks — each with severity | 05, 06, lead research |
| A12 | **Goals, decisions & constraints** | Purpose of the run, decisions already made (not up for re-litigation), constraints, known unknowns | 00_Intake, all |
| A13 | **Business Profile** | The 9 fields defined in `GTM_ROOT/Playbook/SPINE.md` ("The Business Profile"): business type, revenue model (retainer, project, subscription …), deal size, how they buy, company stage, GTM maturity per pillar, where they sell, capacity and, in client mode, our engagement (retainer / project / advisory). Built from A1–A12 evidence, each field tagged | **Every pillar**: it sets each pillar's defaults |

**The Business Profile is the first thing written and the last thing confirmed.** Draft it as soon
as the internal read and the commercial brief land, so the rest of discovery knows what kind of
business it is looking at. Put every field still `UNKNOWN` or `ASSUMED` into the question bank as
★, because no pillar runs without it. In client mode, P2–P4 and P9 lead the discovery-call
agenda.

## Procedure

### 1. Map the sources
List every source (docs folders, repo paths, live URLs, portals the owner can describe) in `assets/00_source-map.md`, with what each can answer and any access still needed.

### 2. Internal read (own product)
Read the docs and the code/config: build the **product truth inventory** (A2) with file:line or doc references, plans/limits as enforced, onboarding, events/tables (A10). Note every place docs and code disagree.

### 3. Research (deep step ①, in parallel, in the background)
Small `gtm-machine-os:researcher` briefs that save as they go:
- **Footprint & claims brief:** fetch every live surface; capture claims verbatim with URL + date (A3); read the legal pages in full (A4).
- **Commercial & platform brief:** price/billing pages, platform partner terms, provider rate cards and policies, approval/quality status where public (A5, A6).
- **Entity & compliance brief:** entity and registration facts, the data-protection, messaging and advertising rules for the target market(s) (A1, A11). Reuse `gtm-machine-os:lead-research`'s `references/market-<CC>.md` if it exists.
- **Category brief:** category names, 5–10 alternatives with public prices (A7).
While they run, do steps 1–2 and the evidence count (A8).

### 4. Cross-check
Build `assets/00_claims-vs-truth.csv`: every public claim against A2/A4/A5 — status (true / true with condition / unsupported / false), the evidence, the fix. Also check docs vs code, listing vs pricing, legal promises vs what the code does with data. **This is where contradictions get caught before any strategy is written.**

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor` the fact base, the claims-vs-truth table and the risk register. Ask it to re-verify the weight-bearing facts at source and to look for contradictions the draft missed. Fix or carry into the question bank.

### 6. Question bank
`assets/00_question-bank.md`: only what research couldn't answer, each question with:
- ★ if it blocks a pillar outright;
- the pillar(s) it unblocks;
- what was already checked;
- answer options where possible.

Rank by how much downstream work rests on it. **Own product:** ask the owner the ★ questions now — in one round (AskUserQuestion for up to 4 at a time, the rest as a list he can answer in one reply). **Client company:** merge the bank into the discovery-call agenda (`00b_Discovery-Call.md`).

### 7. Write
- `00_Discovery.md` from `template.md`: mode, evidence count up front, **§0 Business Profile** (A13), the 13 areas (each fact tagged with source), contradictions found, risk register summary, open questions, readiness verdict.
- `00_Intake.md`: fill every section from discovery (Business Profile, stage, docs, evidence count, already decided, purpose, constraints, known unknowns); mark anything the owner hasn't confirmed as `PROPOSED`.
- `00_Playbook-Tracker.md`: create it (protocol §10). Copy the profile summary into its header, and set the Discovery row.
- Assets (below).

### 8. Readiness verdict and present
- **READY** — every ★ question answered, no unresolved critical risk that changes what can be said or sold.
- **READY WITH GAPS** — ★ answered or explicitly parked by the owner; gaps listed with the pillar they affect.
- **NOT READY** — any Business Profile field P1–P5 still unknown, a ★ question unanswered that blocks Pillar 1–3, or a critical contradiction (e.g. a live public claim that's false) the owner hasn't decided on.
Present per protocol §8: evidence count, the contradictions found, the ★ questions, the verdict. Next: `gtm-machine-os:strategy` (or `gtm-machine-os:segmentation` directly).

## Assets (`products/<slug>/assets/`)

| File | What it is | Usable for |
|---|---|---|
| `00_fact-base.csv` | Every fact: area (A1–A12), fact, value, source (file:line / URL), date, tag | The single reference every pillar cites |
| `00_claims-vs-truth.csv` | Every public claim verbatim, surface, URL, date, status vs truth, evidence, fix | Fixing false or unsupported claims before GTM amplifies them |
| `00_question-bank.md` | Ranked owner questions (★, pillar unblocked, already checked, options) + answers once given | One round of questions instead of drip-feeding |
| `00_evidence-inventory.csv` | Customers, users, usage, reviews, interviews, deals, proof assets — counts, sources, consent | Setting the evidence ratio; Pillar 5 harvest |
| `00_risk-register.csv` | Risk, area, severity (critical/major/minor), source, what it constrains, owner, action | Compliance and platform gates for every later skill |
| `00_source-map.md` | Where each doc, system, surface and portal is; what it answers; access needed | Re-running discovery; onboarding anyone else |

## Checks before presenting
- [ ] Mode stated (own product / client); evidence count exact and up front
- [ ] Business Profile (A13) filled: all 9 fields (P9 only in client mode), each tagged; unknowns are ★ questions; written in §0, the intake and the tracker
- [ ] All 13 areas covered — each with facts and sources, or an explicit UNKNOWN/question
- [ ] Product truth sourced from code/live product; doc-vs-code gaps listed
- [ ] Every public claim captured verbatim with URL + date and a status
- [ ] Legal pages read in full; binding promises listed
- [ ] Commercial facts primary-sourced and dated
- [ ] Claims-vs-truth contradictions listed with fixes; risk register with severities
- [ ] Question bank: only unanswerable-by-research questions, ★ and pillar tags, ranked; ★ asked
- [ ] `00_Intake.md` filled; nothing self-locked; no secrets or personal data copied
- [ ] Readiness verdict stated; next skill named

Playbook "Step 0 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it):
- [ ] The facts are recorded with their sources: product, public claims vs truth, legal promises, prices and costs, the evidence count
- [ ] The Business Profile is filled, all nine fields (engagement only for client work), each tagged with its evidence
- [ ] Every unknown field is a question for the owner, and P1–P5 are answered
- [ ] The owner (or client) has confirmed the profile
