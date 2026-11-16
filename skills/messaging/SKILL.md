---
name: messaging
description: GTM Pillar 4 — Messaging + Channels for any product, built on positioning. Builds the message architecture (category, one-liner, 1:1 pillars, persona overlays), a persona × stage journey matrix with every cell filled or deliberately blank, the 7-field messaging canvas, a Bullseye channel choice with exclusions and one metric per channel, and copy kits for the chosen channels — including in-product core copy and any copy end-users receive. Ingests real interview notes as verbatim language. Ships a runnable copy linter that checks every line against the banned list and claims register. Deep by default (researcher → strategist → evidence auditor). Produces 05_Messaging-and-Channels.md plus usable assets (messaging matrix, copy kit, channel plan, banned phrases + linter, message-test log, interview capture). Trigger with "messaging for X", "copy for X", "write the listing for X", "landing page copy for X", "which channels for X", "messaging matrix for X", "GTM pillar 4 for X".
version: 1.0.0
---

# GTM Messaging & Channels — Pillar 4

**Answers:** *what do we say, to whom, at which stage, and where?*
Positioning decides; messaging words it. **Messaging never invents a claim that positioning, the value proposition or the claims register doesn't carry.**

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/05_Messaging-and-Channels.md` (read in full; the output contract is at the bottom) + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.6** (messaging house, five principles, homepage storyline, value matrix, PLG stage messaging, website page roles, Laja page formula, channel kill rule) and **ch.7** (Bullseye channel selection, capture vs generate) |
| **Upstream** | `04_Positioning.md` (statement, only-ness, pillars, banned list, validation plan) · `03_Value-Proposition.md` + `assets/03_claims-register.csv` (what may be said) · `02b_…` (personas, awareness, info sources, shopper/end-user) · `02_ICP.md` (triggers) |
| **Writes** | `products/<slug>/05_Messaging-and-Channels.md` · `products/<slug>/assets/05_*` · `products/<slug>/interviews/` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `06` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 4 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `04_Positioning.md` is missing or STALE, **stop** and offer `gtm-machine-os:positioning` (protocol §3). If positioning has **open decisions**, build on the recommended option as a stated working assumption. **Isolate every line that depends on it** in a labelled variant, so the owner's choice changes only those lines.

## Rules specific to this pillar

1. **Every copy line traces to a claim.** Each line in a copy kit cites its claims-register row (or the `03`/`04` section) and carries that row's public status.
   - `Not publishable` lines never appear outside an internal note.
   - `Publishable with method` lines carry their method next to them.
2. **The banned list is code, not prose.** Collect every banned phrase from `03`, `04` and the claims register into `assets/05_banned-phrases.txt`, one per line, Arabic and English. Run `assets/05_copy-lint.py` over every copy asset **before presenting**. A lint hit is a defect.
3. **Pillars stay 1:1 with drivers** (framework contract item 7). Persona overlays translate the *same* claim. They never add a new one.
4. **Every persona × stage cell is filled or marked deliberately blank, with the reason.** This includes:
   - **post-sign-up stages** for self-serve products (activation · habit · expansion · monetisation, from Voje's PLG table);
   - **any end-user who receives the product's messages.** Their copy is messaging too, and often the most consequential.
5. **Core copy counts.** In-product text, status names, onboarding, emails, support replies and templates sent to end-users are in scope (Voje ch.6). Copy that already ships is audited against the claims register. Gaps are listed for the product owner. **This skill does not edit product files.**
6. **Channels by Bullseye, not by habit.**
   - Brainstorm all 19 traction channels.
   - Rank them into outer / middle / inner rings using evidence that **the audience is actually there** (`02b` info sources) and cost.
   - Run cheap tests on the inner 3.
   - Choose 1–3.
   - **Name every exclusion with its reason.**
   - Give each chosen channel **one** primary metric and a **kill date (3–6 months)**.
7. **Customer language only from real sources.**
   - If `products/<slug>/interviews/` has notes, ingest them first. Quote verbatim, tag `VALIDATED (interview, C=1)`, and update the claims they test in `02`/`02b`/`03`/`04`. Never tidy a quote.
   - If there are none, copy uses neutral words. It never pretends to be the customer's voice.
8. **Images and video are copy too.** Every screenshot, gallery image, benefit card and voice-over line is transcribed into a lintable sidecar (`assets/05_listing-image-text.md`) and checked like text. A clean text kit with stale images fails. Check visuals for **false depictions** too (e.g. a sender name the user won't actually see).
9. **True in production, not just in code.** A capability line is publishable only if the path it describes works *in production today*. Example: a messaging template is actually approved, not pending. Record the check and its date as a gate before any listing is submitted.
10. **Copy vs code changes.** If a "copy fix" needs a code change (a label over a computed value, a hidden field), file it as a code change for the product owner, and keep the affected screen out of screenshots until it ships.
11. **Every language the platform shows.** If the marketplace shows a second language (e.g. an English side), write that side paste-ready too, not just a gloss.
12. **Arabic is first-class.**
   - Write the market language first, in the register the market uses (the dialect and formality the buyers themselves use, e.g. a regional dialect rather than formal standard language).
   - English is a gloss.
   - Check terms against the locked category anchor exactly.

## Procedure

### 1. Inputs and interview ingestion
- List the upstream decisions with their status (LOCKED / PROPOSED / open).
- **If `interviews/` has notes:** extract verbatim language per persona, test results against the `02b` discovery-script thresholds and the `03` UVP-test and `04` validation-plan rules, and record what changed upstream.
- **If there are none:** create `interviews/README.md` + `interviews/_capture-template.md` (from `assets/02b_discovery-script.md`'s results table) so the owner can drop notes in.

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save as they go; **reuse `02b` / `04` research first.**
- **Channel evidence:** for each candidate channel, is the ICP demonstrably there (counts, sizes), what does it cost, what are the rules? Examples: marketplace listing rules and limits, community posting rules, ad platform minimums.
- **Copy conventions:** how the top listings and pages in the category are written (length, structure, language register), with examples and sources. Plus any platform copy rules (character limits, banned words, reviewer feedback).

### 3. Message architecture
Category/frame (from `04`) → one-liner (benefit + mechanism) → pillars 1:1 with drivers, each with proof from the register → persona overlays (the same claim in each persona's KPI language).

### 4. Journey matrix and canvas
- **Persona × stage**, including post-sign-up stages for self-serve products and the end-user. Each cell holds the message goal.
- **The 7-field canvas** per persona × key stage: pain/trigger · outcome · core message · proof/asset · CTA · channel. Plus the awareness level from `02b`.
- **CTA ladder:** commitment rises with stage and with how close the persona is to the work (framework §1D).

### 5. Channels (Bullseye)
Outer → middle → inner, with evidence. Then the chosen 1–3, each with:
- one metric;
- a test design;
- a budget/time cap;
- a kill date.

Then the exclusions, each with its reason.

### 6. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the architecture, matrix and Bullseye. Ask for:
- the **one-liner** (choose among variants);
- the **channel picks and order**;
- the **CTA ladder**;
- the **narrative shape**;
- what each persona must hear first;
- which copy lines are **tests** (variants) rather than decisions;
- what would flip each call.

### 7. Copy kits (for the chosen channels only, plus core copy)
For each chosen channel, a ready-to-paste kit in the market language with an English gloss, each line citing its claim. Always include:
- **core copy:** onboarding, status names, the trial summary, notification emails;
- **end-user copy:** any message the product sends to *their* customers;
- **variants for every open test** (`03` UVP test, `04` validation plan).

Use the framework's copy formulas and Laja's page formula where relevant.

### 8. Lint
Copy this skill's `copy-lint.py` to `assets/05_copy-lint.py` and build `05_banned-phrases.txt`. Include Arabic variants: the linter allows common suffixes (ة/ات/ية), but list distinct stems.
- **Test the linter** on a handful of known-bad variants before trusting it.
- **Run it over every copy asset** (the copy kit, the image sidecar, the matrix, and the `03`/`04` sheets and cards), not just the kit.
- Wrap reference lists that *quote* banned phrases in `<!-- lint:off -->` / `<!-- lint:on -->`. Mark internal lines that describe competitors with `lint:ignore`.
- Record per-file results (date, errors / warnings) in the artifact. Errors must be 0. Warnings are human-review items.

### 9. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`:
- the copy kit;
- the matrix;
- the channel plan;
- the lint output;
- any interview ingestion.

The audit checks:
- every line's claim and status;
- the Arabic: meaning drift, register, the exact locked anchor;
- the persona-cell coverage;
- the channel evidence;
- whether **any line promises what the product doesn't do today** (check against the `03` product truth inventory and the code where available).

Fix each finding, or carry it into Open questions. If the audit undermines a strategist call, present Option A / B (protocol §5 ④b).

### 10. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `05_copy-kit.md` | Ready-to-paste copy per chosen channel + core copy + end-user copy + test variants. **AR first, EN gloss**, each line tagged with its claim row and status | Shipping the listing, site, onboarding and outreach today |
| `05_messaging-matrix.csv` | Persona × stage, 7 fields + awareness + "deliberate blank" reasons | Briefing anyone writing anything; the coherence audit |
| `05_channel-plan.md` | Bullseye rings with evidence, the chosen channels (metric, test, cap, kill date), exclusions with reasons | Spending time and money on the few channels that matter |
| `05_listing-image-text.md` | Transcribed text of every image and video line, linted | Stops images undoing a clean text kit |
| `05_banned-phrases.txt` + `05_copy-lint.py` | The banned list as data, plus a linter: `python3 05_copy-lint.py <file…>` prints every hit with line number; exit code 1 on any hit | Checking any copy before it ships, by anyone |
| `05_message-tests.csv` | Messaging-experiment repository (Voje: "be a good librarian"): test, hypothesis, variants, channel, sample, threshold (from `03`/`04`), status, result, decision | Not losing what was learned |
| `interviews/README.md` + `interviews/_capture-template.md` | Where interview notes go and in what shape, so this skill (and `02b`/`03`/`04` re-runs) can ingest them | Turning conversations into `VALIDATED` evidence |

### 11. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-machine-os:proof` (Pillar 5).

## Checks before presenting (framework output contract + this skill)
- [ ] Architecture: category, one-liner, pillars 1:1 with drivers, persona overlays (same claim, different words)
- [ ] Every persona × stage cell filled or deliberately blank, **including post-sign-up stages and the end-user**
- [ ] 7-field canvas for each persona's key stages
- [ ] Channels: Bullseye with evidence, 1–3 chosen, **every exclusion named**, one metric and a kill date each
- [ ] Copy kits only for chosen channels, plus core copy and end-user copy; AR first
- [ ] Every copy line cites a claim row and status; no `Not publishable` line outside internal notes
- [ ] Lint run over **all** copy assets incl. image sidecars: 0 errors per file, recorded
- [ ] Production-truth gates recorded (e.g. template approved) before any listing submission
- [ ] Visuals checked for false depictions; copy fixes that need code filed as code changes
- [ ] Second-language side written paste-ready where the platform shows it
- [ ] Open upstream decisions isolated in labelled variants
- [ ] Interview notes ingested verbatim, or the capture folder created
- [ ] All assets written

Playbook "Pillar 4 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it):
- [ ] The one-liner and three message pillars are written, each with proof and its main objection
- [ ] The messaging matrix is filled: persona × stage
- [ ] A CTA is chosen for each stage
- [ ] A few channels are chosen, each with one primary metric
- [ ] Copy kits are drafted for the chosen channels
