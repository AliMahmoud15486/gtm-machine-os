---
name: enablement
description: GTM Pillar 11 — Enablement & Readiness for any product, built on the locked Phase 1 strategy and the Phase 2 motion, revenue process, demand-gen and outbound artifacts. Assembles rather than re-creates — indexes every sales-toolkit asset the earlier pillars produced against its sales stage and owner, and lists what is missing with the skill that owns it. Maps the GTM squad (five roles) onto the people the business actually has, runs the enablement and launch-readiness checklists, specifies the smallest tech stack that supports the journey (one tool per function, owner, cost, consent and DPA per market), extends the value-prop ROI model into a buyer-facing model (3 scenarios; net value, ROI %, payback, break-even), drafts the 12-section proposal template shaped to the revenue model, and writes a 30-day roll-out with internal advocacy and the weekly operating meeting. Specs and drafts only — never sets up tools, changes a CRM or sends anything. Deep by default (researcher → strategist → evidence auditor). Produces 13_Enablement.md plus usable assets (toolkit index, enablement checklist, stack spec, ROI model, proposal template, 30-day roll-out). Trigger with "enablement for X", "sales toolkit for X", "is X ready to launch", "tech stack for X", "proposal template for X", "ROI model for a deal", "GTM pillar 11 for X".
version: 1.0.0
---

# GTM Enablement & Readiness — Pillar 11

**Answers:** *what people, assets and systems does the team need to run the playbook the same way every time?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Playbook/GTM-Playbook.md` **Pillar 11** (30-day roadmap, B2B sales toolkit, enablement checklist, tech stack, ROI model, proposal; its "done when" list) · `GTM_ROOT/Frameworks/12_Market-Readiness-Launch-and-Metrics.md` §3 (launch phases, readiness before launch, launch execution checklist, 10× rule, daily stand-ups) and §5 (internal advocacy) · `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.8** (timeline sentence, 5-role squad, organisation + weekly meeting, tools criteria, budget ratios, 90-day plan) · `GTM_ROOT/Frameworks/09_Sales-Led-Growth-and-Sales-Process.md` stages [6] value & business case and [8] proposal, §4 (solo / low-ACV compression) · `GTM_ROOT/Frameworks/11_AI-in-GTM.md` §4, §7 (agent-assist candidates and bright lines — reference only). Sources: `Learning_resources/_extracted/HubSpots Go-To-Market Playbook.txt` p19, p21–22, p24–26, p31 · `B2B Growth Masterclass _ Session #20.txt` p47 (B2B Toolkit contents) |
| **Upstream** | `08_Coherence-Audit.md` (verdict) · `09_GTM-Motion-and-Routes-to-Market.md` · `10_Revenue-Process-and-SLAs.md` (stages, business case, handoff) · `03_Value-Proposition.md` + `assets/03_roi-calculator.csv`, `03_claims-register.csv` · `07_Pricing-and-Packaging.md` + `assets/07_plan-sheet.md` · `06_Proof-System.md` + `assets/06_proof-tracker.csv` · and whichever exist of `02`/`02b`, `04` (battlecards), `05` (copy kit, matrix, linter), `11_Demand-Generation.md`, `12_Outbound.md`, `leads/` · Business Profile P1, P2, P3, P4, P5, P7, P8, P9 |
| **Writes** | `products/<slug>/13_Enablement.md` · `products/<slug>/assets/13_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `14_Metrics-and-Feedback.md` and `15_Execution-Audit.md` `STALE` |

**Gate (protocol §3, Phase 2).** Read the verdict in `08_Coherence-Audit.md` and state it in the header. **FAIL → stop**; offer `gtm-machine-os:coherence-audit` after the named fixes. `08` missing → stop. Then: `03`, `06`, `07`, `09`, `10` must exist and not be `STALE` — if one is missing, stop and offer its skill (`value-prop`, `proof`, `pricing`, `motion`, `revenue-process`). `11` and `12` are optional; their absence becomes MISSING rows in the toolkit, not a stop.

## Rules specific to this pillar

1. **Assemble, never re-create.** Enablement points at the real files earlier pillars wrote. Find them by listing `products/<slug>/` and `assets/` — never guess a path. A toolkit asset that doesn't exist is a `MISSING` row with the skill that owns it. Don't draft it here. The only assets this skill authors are the six below.
2. **Never change upstream decisions.** ICP, positioning, messaging, prices, tiers, discount rules, stages and SLAs are read, not edited. A conflict (a price in a deck that differs from `07`, a stage name that differs from `10`) is a **finding for the owning skill**, in §11 of the artifact.
3. **The motion sets the toolkit's size** (`09`; `Frameworks/09` §4). Product-led, self-serve, P3 < 5K: no proposal, SOW or business case — checkout and the plan page replace them. Mark those rows and the proposal box `N/A — <motion>`, and make the ROI model a self-serve calculator. Hybrid: the toolkit for the sales-assisted tier only. Sales-led or partner-led: the full toolkit. Partner route in `09`: add the channel-management checks (`Frameworks/12` §3).
4. **Every toolkit asset maps to a stage in `10`.** Use `10`'s stage names, not the playbook's. An asset no stage uses is cut or flagged.
5. **Profile shapes the proposal and the ROI model** (P1, P2):
   - Retainer: monthly fee, workstreams, a minimum term, 30/60/90.
   - Project: milestones, deliverables, payment per milestone.
   - Subscription or usage: tier and value metric, limits, term, order form, pilot-to-paid terms from `07`.
   - The 12-section method comes from service selling. For subscription or usage, mapping the sections is `ASSUMED`; say so.
   - Transaction or commission: `SOURCE-GAP` (no source covers take-rate proposals). Mark the shape `ASSUMED`.
6. **ROI model: extend `03`, don't fork it.** Copy the driver formulas exactly from `03_roi-calculator.csv` and cite the row. Add investment from `07` (the price exactly as published), switching cost, and the playbook's four outputs. Add the funnel formula only when a driver is pipeline or revenue. Add a cost-of-delay row (monthly cost of inaction from `03`/`10`). ≤3 inputs the buyer supplies on a call. Conservative, expected and upside scenarios. Before customers, the inputs are `ASSUMED`. The model is then labelled a hypothesis, and so is any ROI line in the proposal.
7. **Proof lines need consent.** Only assets marked publishable in `03_claims-register.csv` and consented in `06_proof-tracker.csv` go into the proposal or the toolkit. Before proof exists (P5 pre-revenue), the proof section offers the `06` pilot protocol and risk reversal, never a placeholder case study.
8. **Smallest stack** (playbook; Voje ch.8 "process first, then tools — could a spreadsheet do it?"):
   - one tool per function, and only for a journey step that exists in `10`/`11`/`12`;
   - Voje's criteria: easy to onboard, inexpensive, scalable tier price checked, integrable;
   - P8 = one or two people: one CRM that also covers email, pages and pipeline before any add-on;
   - tool costs `RESEARCHED` with URL and date, or `UNKNOWN — needs measurement`;
   - budget check against Voje's ratios: tools up to ~10% of the GTM budget, labour 30–70%, contingency ~10%.
   Tool choice is `ASSUMED` and `PROPOSED`: the sources give examples, not a selection rule.
9. **Consent and DPA per market (P7).** For each market, record the rules for tracking consent, messaging consent, a DPA with each processor that holds personal data, and lawful use of scraped contact data. Take the rules from a primary source (regulator or statute, URL, date), via the researcher. GDPR/ePrivacy is the playbook's example, not a default for other markets. Every row ends "needs legal review" until counsel confirms it. This skill gives no legal advice.
10. **Ticks need proof the thing is live.** This skill writes specs. "Stack set up", "CRM stages live" and "review on the calendar" are ticked only when the owner (or the client) confirms them, recorded as `VALIDATED` with a date. A spec alone leaves the box unticked.
11. **Squad from real people (Voje ch.8).** Map the five roles (GTM Lead, Intelligence, Architects, Voice of Customer, Get Things Done) onto named people from P8. One person may hold several roles; say so. A role nobody holds is a risk, not a hire recommendation by default. One owner per pillar.
12. **Client mode (P9).** Advisory: we write the specs and templates, and the client owns every execution row (stack set-up, CRM configuration, training, calendar). The owner column says so. Done-with-you: split rows by name. Retainer: we may own execution rows the owner agrees to.
13. **SOURCE-GAPs — declare, don't invent:**
    - training and certification programme design (curriculum, certification, ramp time);
    - commission and compensation plan design (HubSpot p24 lists "commission structures defined" only);
    - security, procurement and legal packs for large deals;
    - take-rate proposals.
    Where the business needs one, write `SOURCE-GAP`, keep the item as a checklist line with an owner, and mark any proposal `ASSUMED`.
14. **Agent-assist is a note, not a build** (`Frameworks/11`). Tag stack rows and recurring tasks with a candidate mode (co-pilot / agentic / always-on). Never across the bright lines: no auto-send, no record deletion, no pricing or contract terms committed by an agent.

## Procedure

### 1. Gate and inventory
Run the gate above. List every file in `products/<slug>/`, `assets/` and `leads/` with its status line. Read the Business Profile and the spine defaults (P8 smallest stack, P9 advisory). Write the timeline sentence (Voje ch.8): *"In [secured time], we have to achieve [GTM objective]"*, taking the objective from `09`/`14` if present, or else `ASSUMED`.

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save to `products/<slug>/research/` as they go:
- **Data protection per P7 market:** tracking and messaging consent, processor DPAs, contact-data scraping. Primary sources, dated.
- **Stack facts:** for the current tools (from `00_Discovery.md`) and ≤2 candidates per missing function, record the scaling-tier price, DPA availability, data residency and native integrations. Vendor pages, dated.

### 3. Draft (deep step ②)
In this order: toolkit index (rules 1, 3, 4) → squad and ownership (11, 12) → enablement checklist → stack spec, consent/DPA and budget check (8, 9) → ROI model (6) → proposal template (5, 7) → 30-day roll-out. The roll-out:
- maps the playbook's four weeks onto artifacts that already exist; done weeks are cited, not repeated;
- puts the remaining work into dated tasks with owners;
- includes an internal advocacy session ("lead with use cases, not features", `Frameworks/12` §5) and the weekly 45–60 min meeting with Voje's agenda (`14` owns the scorecard it reviews);
- includes daily stand-ups for the first 30 days of launch (HubSpot p25), and links to the course-correction triggers in `14`, or flags them for `14` if it isn't built.

### 4. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the inventory, profile, motion and draft. Ask for:
- the stack per function and the alternative that lost;
- what is in and out of the toolkit for this motion;
- the proposal shape;
- the squad mapping and the uncovered roles;
- what to build first in the 30 days;
- what would flip each call.

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor` everything below:
- every toolkit path (does it exist? its status?);
- the ROI formulas against `03` and the prices against `07`;
- each proposal proof line against the claims register and consent;
- each consent and DPA claim and its source;
- tool prices;
- stage names against `10`;
- every tick and the evidence behind it.
Fix each finding, or carry it into Open questions. Upstream conflicts go to §11 as findings for their skill.

### 6. Assets
Write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `13_toolkit-index.csv` | One row per toolkit asset: asset · sales stage (`10`'s names) · built from (artifact) · owning skill · person owner · status (`EXISTS` / `STALE` / `MISSING` / `N/A — reason`) · path · last updated · publishable? | Finding the right asset at each stage; the gap list for upstream skills |
| `13_enablement-checklist.md` | The playbook's 7 items + HubSpot's sales-readiness and technology-infrastructure checks (+ channel management if a partner route exists), each with owner, status, evidence and date | Running the readiness review; ticking the done-when honestly |
| `13_stack-spec.csv` | Function · journey step served · tool (current or proposed) · alternative that lost · owner · monthly cost (source, date) · personal data held · consent/DPA note per market · DPA status · integrations · agent-assist mode | Setting up or auditing the stack; procurement and DPA signing |
| `13_roi-model.csv` | Live `=` formulas: buyer inputs → `03` driver formulas → value → investment (`07`) + switching cost → **net value, ROI %, payback months, break-even**, at conservative / expected / upside; cost-of-delay row; funnel block if relevant. Recompute one scenario by hand in the artifact | Building the business case with the buyer on a call |
| `13_proposal-template.md` | The 12 sections, each with "built from" path, pre-filled from upstream where it exists, `[brackets]` for deal facts, the "ready to write?" gate, the language-that-closes rules and the pitfalls table as a pre-send check. Linted with `assets/05_copy-lint.py` if it exists | Writing a proposal in an hour that matches strategy, prices and proof |
| `13_rollout-30-day.md` | Week 1–4 tasks with owner and date; the internal advocacy session; the weekly meeting agenda; launch stand-ups; links to `14` triggers | Running the first month without re-planning |

### 7. Tracker and present
Update `00_Playbook-Tracker.md` per protocol §10 (Pillar 11 row and its done-when list; `14` and `15` to `STALE` if they exist). Present per protocol §8: toolkit coverage as `EXISTS n / needed N`, missing assets with their owning skills, open ticks waiting on confirmation, and the weakest assumption. Next skill: `gtm-machine-os:metrics` (Pillar 12).

## Checks before presenting

Playbook "Pillar 11 is done when":
- [ ] The enablement checklist above is fully ticked
- [ ] Every toolkit asset exists and is linked to its sales stage
- [ ] The tech stack is set up, with consent and data processing agreements covered
- [ ] The ROI model is built with three scenarios
- [ ] The proposal template is ready with all 12 sections

Also:
- [ ] Coherence verdict stated; not FAIL; `03`, `06`, `07`, `09`, `10` present and not STALE
- [ ] No upstream asset re-created; every MISSING row names its owning skill; conflicts logged as findings
- [ ] Toolkit sized to the motion; N/A rows give the reason
- [ ] ROI driver formulas identical to `03`, prices identical to `07`; four outputs; one scenario recomputed
- [ ] Proposal proof lines publishable and consented; shape matches P1/P2; linted
- [ ] Stack: one tool per function, owner, sourced cost or UNKNOWN, consent/DPA per P7 market with a primary source
- [ ] Squad roles mapped to named people; one owner per pillar; P9 ownership applied
- [ ] Every SOURCE-GAP declared; no tick without confirmation of a live system
- [ ] All six assets written; tracker updated
