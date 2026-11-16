---
name: metrics
description: GTM Pillar 12 — Metrics & Feedback Loops for any product, run last in Phase 2. Consolidates every success metric and test threshold the earlier pillars already set (03 targets, 04 validation signals, 05 message tests and channel metrics, 06 proof measurement, 07 price tests, 10 SLAs, 11 sprint experiments, 12 outbound dashboard) into one instrumented system — a goal layer (North Star Metric, this quarter's One Metric That Matters, optional OKRs), PMF signals first for pre-PMF products (Sean Ellis 40% test, retention curve), KPIs by stage with leading and lagging indicators, unit economics (CAC two ways, LTV on margin, LTV:CAC and payback per niche), and the retention metric the revenue model calls for. Every metric gets a definition, formula, source event, owner, cadence and the action it triggers at a threshold set in advance. Adds the weekly scorecard and growth meeting, an ICE-ranked test backlog, the review cadence, a symptom → cause → owning-skill diagnosis table, and the triggers that send the strategy back to Pillars 1–3. Deep by default (researcher → strategist → evidence auditor). Produces 14_Metrics-and-Feedback.md plus usable assets (KPI dictionary, dashboard spec, weekly scorecard with live formulas, instrumentation gaps, ICE backlog, review calendar, diagnosis table). Trigger with "metrics for X", "KPI dashboard for X", "what should X measure", "weekly scorecard for X", "growth meeting for X", "test backlog for X", "is X working", "GTM pillar 12 for X".
version: 1.0.0
---

# GTM Metrics & Feedback Loops — Pillar 12

**Answers:** *what is working, what isn't, and what do we change next — decided by numbers set in advance, not by mood?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/12_Market-Readiness-Launch-and-Metrics.md` **§4** (four metric families, track by phase, metrics must trigger actions, the reconciliation note) and §3 course-correction triggers; output contract items 4–5. `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.1** (NSM + OKRs), **ch.4** "Metrics and analytics" + "Product-Market Fit" (OMTM, LTV on margin, single source of truth, slice by segment and cohort, "infotainment", Sean Ellis 40%, retention curve, three proofs per ECP), **ch.7** channel economics, **ch.8** (CAC includes wages and tools, weekly meeting, experimentation loop, Thomke filter, backlog hygiene), glossary formulas. The measurement sections already in `04_Positioning.md` ("Metrics — is positioning working?"), `05_Messaging-and-Channels.md` §B primary metric per channel + §4 messaging diagnostics, `06_Proof-System.md` [6] Measurement. Practitioner layer: `GTM_ROOT/Playbook/GTM-Playbook.md` "Pillar 12 — Metrics & Feedback Loops". Source text: `HubSpots Go-To-Market Playbook.txt` p25 (course correction), p27–30 (ch.6); `Go-To-Market Strategist - Maja Voje 2023.txt` p21–30, p149–170, p270, p335, p345–348, p371; `B2B Growth Masterclass _ Session #8.txt` p13; `B2B Growth Masterclass _ Session #11.txt` p21 (6–12-month pricing review) |
| **Upstream** | **Required:** `00_Discovery.md` (Business Profile, A9 capacity, **A10 instrumentation**) · Phase 1 artifacts `01`–`07` · `08_Coherence-Audit.md` (verdict). **Read where they exist:** `09` motion · `10` revenue process & SLAs · `11` demand gen (sprint experiments) · `12` outbound (dashboard) · `13` enablement (stack, owners). Upstream measurement assets: `03_measurement-backlog.csv`, `04_validation-plan.md`, `05_channel-plan.md`, `05_message-tests.csv`, `07_unit-economics.csv`, `07_price-test-plan.md`, `06_harvest-and-instrumentation.md`, `06_proof-tracker.csv`, `08_validation-backlog.csv` |
| **Writes** | `products/<slug>/14_Metrics-and-Feedback.md` · `products/<slug>/assets/14_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `15_Execution-Audit.md` `STALE` if it exists; nothing earlier. Its findings may **recommend** re-running earlier pillars (§ Review loop); it never sets an upstream artifact `STALE` itself |

**Phase 2 gate.** Phase 2 executes the locked strategy; it does not remake it. If `08` is missing or its verdict is **FAIL**, stop and offer `gtm-machine-os:coherence-audit`. State the verdict in the header. Any upstream Phase 1 artifact `STALE` → stop (protocol §3). A missing Phase 2 artifact (`09`–`13`) does not stop the run: list it as a gap, take that stage's metrics from the playbook defaults and mark them `ASSUMED`. If `09` is missing, read the motion from the Business Profile defaults in `SPINE.md`, marked `ASSUMED`, and recommend `gtm-machine-os:motion`. Owning skills for Phase 2 findings: `motion` (09), `revenue-process` (10), `demand-gen` (11), `outbound` (12), `enablement` (13). This skill never changes ICP, positioning, messaging, pricing or any upstream threshold; a conflict becomes a finding for the owning skill.

## Rules specific to this pillar

1. **No action, no metric.** Every row in the dictionary has: name · definition · formula · family and funnel stage · leading or lagging · source system and event (linked to the `00` A10 row) · single source of truth · owner · cadence · baseline · target and where the target came from · threshold · **the action it triggers** · owning skill. A metric without a pre-set threshold and action is "infotainment" (`Frameworks/13` ch.4): cut it.
2. **Consolidate, don't reinvent.** First harvest every metric and threshold the upstream artifacts already set, verbatim, with `file §`. Pillar 12 instruments them; it does not re-decide them. Two upstream thresholds that disagree are a finding for both owning skills.
3. **Baselines are measured, never estimated.** No data → `UNKNOWN — needs measurement`, plus the date the first reading is due. A framework benchmark (e.g. first-touch reply ≥4–6%, `05` §4) is a `RESEARCHED` target with its source, never the product's baseline. Each target names one of the five target sources (`Frameworks/12` §4: industry standard · historical · growth requirement · resource constraint · market conditions).
4. **Goal layer first.** One **NSM** (value delivered, not revenue; pick the game: attention · transaction · productivity). One **OMTM** for this quarter: a ratio at the current bottleneck, valid 2–6 months, with an owner. OKRs only if capacity allows (3–5 objectives, ≤5 KRs, reviewed monthly, graded 0–1; below 0.5 → try a different assumption). `Frameworks/13` ch.1, ch.4.
5. **Stage drives the set (P5).**
   - *Idea / Prototype / Pre-revenue:* insights per week from research, free-user retention, satisfaction; the PMF instrument is built now and fires later. Funnel KPIs are defined but not targeted.
   - *Early revenue (pre-PMF):* **PMF signals first** — Sean Ellis survey per ECP (>40% "very disappointed"), cohort retention curve (does it flatten?), the three proofs per ECP. Funnel KPIs second. Bad PMF signals → check the segment before the product (`Frameworks/13` ch.4).
   - *Scaling:* full funnel by stage, the four families phased launch → growth → optimisation, unit economics per niche.
   - The minimum review window is 3 months (`Frameworks/13` ch.8); don't call a result in 4 weeks.
6. **Motion picks the headline (`09`).** Product-led headlines time to first value, activation and expansion, not win rate. Sales-led headlines win rate, cycle length, pipeline velocity. Partner-led adds partner-sourced pipeline. `Frameworks/12` §4 reconciliation.
7. **Retention follows the revenue model (P2).**
   - Retainer: monthly client (logo) churn, client health, onboarding milestones, QBR outcomes, referral revenue (playbook "KPIs by stage").
   - Subscription: churn, net revenue retention, expansion revenue; average lifetime ≈ 1 ÷ monthly churn (glossary).
   - Transaction / commission: repeat-transaction rate; LTV = AOV × repeat transactions × lifespan, on margin.
   - Usage, Project / milestone, Licence, Performance-linked: `SOURCE-GAP` — no source defines their retention metric. Propose one (e.g. usage growth per account; repeat-project rate; renewal rate) marked `ASSUMED`.
8. **Unit economics, honestly.** CAC tracked **two ways**: ads only, and fully loaded with wages and tools (`Frameworks/13` ch.8, endnote 102; Voje p371). LTV on **margin**, not revenue. LTV:CAC (rule of thumb ≥3) and CAC payback **per niche and per channel**, never blended. Reuse the `07_unit-economics.csv` cost inputs; do not re-derive them.
9. **One source of truth per metric.** Vendors over-attribute (`Frameworks/13` ch.4). Name the system that wins for each metric (CRM, product database, analytics, billing). Slice every metric by segment/niche and by cohort.
10. **Instrumentation is a spec, not a deployment.** Every metric whose event is not captured today (`00` A10) becomes a gap row: event name, trigger, properties, system, owner. This skill writes the spec. It never deploys tracking code, builds a dashboard in a tool, creates calendar events, edits a CRM or sends anything.
11. **Experiments are ranked by ICE and filtered first.**
    - A card enters the backlog only if it is fully written (hypothesis · metric · threshold · owner) and passes Thomke's seven questions (`Frameworks/13` ch.8).
    - **ICE** (Impact × Confidence × Ease) is the playbook's ranking. The sources give Impact × Ease and Epperson's scorecard but no ICE scale: `SOURCE-GAP`. Default 1–10 per factor, ICE = I × C × E, marked `ASSUMED`. Anchor Confidence to the evidence grade (protocol §4 C=1–5 ladder, ×2).
    - At most three experiments approved per week (playbook); aim at 1–5 objectives; no quota of tests per sprint.
12. **The smallest dashboard that drives decisions (P8).** One or two people → NSM + OMTM + the weekly scorecard (≤7 rows, the playbook's count) + the PMF block if pre-PMF; growth meeting biweekly once it runs smoothly (Voje p335). Larger teams get one view per decision-maker, need-to-know only. If the scorecard can't be filled in the time the profile says is available, cut rows, not the cadence.
13. **Cadence follows cycle length (P3/P4).** Review weekly or monthly depending on the sales cycle (HubSpot p30). Long cycles (P3 > 50K, 7+ buyers): pipeline weekly, win rate and cycle time monthly to quarterly. Self-serve, low ACV: conversion and activation weekly. Launch phase: daily for the first 30 days (`Frameworks/12` §3).
14. **P1 business type sets the vocabulary.** Services: client, proposal, monthly fee, utilisation. SaaS: account, trial, activation, seat. Marketplace: both sides' liquidity (`SOURCE-GAP` beyond the NSM "transaction game" — mark `ASSUMED`). Physical product: gross margin band 20–50% (glossary); the rest `ASSUMED`.
15. **P7 and P9.** Tracking that touches personal data follows the legal gate for the markets in P7 (cookie consent, data residency); the frameworks give no rule → `SOURCE-GAP`, flag it for the owner. In client mode (P9 = advisory), we write the dictionary and spec; the client owns the dashboard, meeting and calendar rows in the tracker.

## Procedure

### 1. Gate and harvest (rules 1–2)
Run the Phase 2 gate. Read the Business Profile and state the defaults applied. Then build the **harvest table**: every metric, target and threshold from `03`–`13` and their assets, with `file §`, its current status (set / measured / UNKNOWN) and duplicates or conflicts.

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save to `products/<slug>/research/`:
- what the existing stack (`00` A9/A10, `13`) can capture natively, and at what cost;
- external benchmarks only where the frameworks give none for this business type — tagged `RESEARCHED`, used as targets, never as baselines.

### 3. Draft (deep step ②)
- **Goal layer:** NSM (game → key action → metric), OMTM with its bottleneck evidence, OKRs if any.
- **PMF block** (rule 5): survey per ECP, cohort definition, retention curve, what "flattening" means here.
- **KPIs by stage** — awareness · interest · consideration · outbound · conversion · retention · expansion — leading and lagging, adapted to the motion, retention per P2.
- **Unit economics:** CVR, CAC ads-only and fully loaded, ROAS if paid, LTV on margin, LTV:CAC, payback per niche.
- **Instrumentation map:** each metric → A10 row → source of truth; gaps → spec.
- **Thresholds and actions** for every row, plus course-correction triggers with pre-approved responses (including sales below 70% of target, `Frameworks/12` §3).
- **Operating cadence:** weekly scorecard, 45–60 min growth meeting (scorecard → where the funnel broke → stop / fix / scale → ≤3 experiments with owners), review cadence table with owners.
- **Diagnosis table:** the playbook's four symptoms, the `Frameworks/12` signal → action table, the `05` hook / offer / proof diagnostics and the `04` keep / change / kill rule, each mapped to its owning skill.
- **Review loop:** the metric movements that recommend re-running Pillars 1–3 (and 4–6), each with its threshold and review window, plus the scheduled 6–12-month review (segments, prices, offer ladder; Session #11 p21: margins, CAC:LTV, price realisation, win/loss by tier).

### 4. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the harvest table and draft. Ask for: the NSM and the OMTM; the cut to the smallest dashboard for this capacity; which thresholds trigger which action; which re-run triggers are real; what would flip each call.

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`: every formula, every threshold and its source, every baseline claim, vanity or actionless metrics, double counting across stages, attribution claims, metrics that can't be captured, and consistency with each upstream threshold. Fix each finding or carry it into Open questions; Option A / B if the strategist's call falls (protocol §5 ④b).

### 6. Assets
Write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `14_kpi-dictionary.csv` | One row per metric with every rule-1 field, incl. the A10 link and the triggered action | Building any dashboard in any tool; settling "what does this number mean" |
| `14_dashboard-spec.md` | Views per decision-maker: NSM + OMTM tiles, PMF block, stage KPIs, unit economics; source of truth and refresh per tile; "could a spreadsheet do it?" first | Building the live dashboard in the chosen tool |
| `14_weekly-scorecard.csv` | Spreadsheet, one row per week: raw counts in, live `=` formulas out (rates, CAC two ways, LTV:CAC), and an `IF` status column that prints the pre-set action when a threshold is crossed | Filling in 15 minutes before the growth meeting |
| `14_instrumentation-gaps.csv` | Event spec per missing metric: event, trigger, properties, system, owner, blocks which metric | Handing to whoever builds the tracking |
| `14_ice-backlog.csv` | Fully written experiment cards: hypothesis, metric, stage, owning skill, Thomke pass, I, C, E, `=I*C*E`, threshold, owner, status, result, decision; seeded from upstream tests | Approving ≤3 experiments a week |
| `14_review-cadence.csv` + `14_review-calendar.ics` | Each review (weekly → 6–12 months): owner, inputs, decisions, re-run triggers checked; the `.ics` has recurring events and no attendees, so importing it sends nothing | Putting every review on the calendar in one import |
| `14_diagnosis-table.csv` | Symptom → check metric → likely cause → owning skill → pre-approved first response → re-run recommended? | Running "where did the funnel break" in the meeting |

### 7. Tracker and present
Update `00_Playbook-Tracker.md` per protocol §10. "Live" and "on the calendar" boxes are ticked only when the owner confirms the dashboard is built and the events are imported; this skill's specs alone leave them unticked. When a pre-set re-run trigger fires, add `REVIEW-DUE` to that pillar's tracker row (protocol §10.7), never `STALE`. Present per protocol §8. On a first run, next is the Phase 2 gate: `gtm-machine-os:execution` (its step 7 cross-check). **Then:** the review loop — when a trigger fires or the scheduled review comes due, re-run the pillar it names (`gtm-machine-os:segmentation`, `icp`, `personas`, `value-prop`, `positioning`, `messaging`, `pricing`, `proof`; Phase 2: `motion`, `revenue-process`, `demand-gen`, `outbound`, `enablement`); re-running that pillar is what stales downstream (protocol §9).

## Checks before presenting (playbook done-when, then framework output contract)
- [ ] The KPI dashboard is live, with leading and lagging indicators per stage
- [ ] CAC is tracked two ways: ads only and fully loaded
- [ ] The weekly scorecard is filled and the weekly growth meeting is on the calendar
- [ ] The test backlog is ranked by ICE
- [ ] Each review in the cadence table is on the calendar with an owner
- [ ] Metrics dashboard by phase (launch / growth / optimisation), motion-appropriate, each metric with a target, its source and the action it triggers (`Frameworks/12` contract 5)
- [ ] Course-correction triggers written with pre-approved responses, incl. a sales-vs-target threshold (`Frameworks/12` contract 4)
- [ ] Harvest table complete: every upstream metric and threshold imported with `file §`; conflicts raised as findings, none silently changed
- [ ] NSM and OMTM chosen, with the alternatives that lost; PMF block present if P5 is before PMF
- [ ] Retention metric matches P2; LTV on margin; LTV:CAC and payback per niche
- [ ] Every metric has source event (A10), source of truth, owner, cadence; every uncaptured one is in the gaps spec
- [ ] No baseline estimated; unknowns are `UNKNOWN — needs measurement` with a first-reading date
- [ ] Dashboard sized to P8 capacity
- [ ] Re-run triggers for Pillars 1–3 written with thresholds and review windows; 6–12-month review scheduled
- [ ] All assets written; scorecard and backlog formulas evaluate on a test row
