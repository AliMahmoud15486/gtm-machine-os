---
name: demand-gen
description: GTM Pillar 7 — Demand Generation (the growth funnel) for any product, built on the locked Phase 1 strategy and the GTM motion. Executes the channels Phase 1 chose rather than remaking them. Maps the 6-stage lifecycle (objective, audience, activity, conversion action, KPI and follow-up per stage), picks one funnel map by business type (A lead magnet → call, B VSL → application, C webinar, D paid diagnostic, WhatsApp-first, direct booking, or trial/demo with activation as the conversion), confirms one capture and one trust channel by awareness × intent fit, specs the lead magnet, landing page, thank-you page and nurture flows (availability, speed, personalisation, volume; consent-checked per market), sets lead-scoring bands tied to the revenue-process hand-off, plans traffic in four phases with a validation test plan, the 12-step build, the launch QA checklist and a 30-day sprint (1 funnel, 2 channels, ≤3 experiments with stop rules). Never spends ad budget, publishes pages or builds automations: specs, copy drafts and test plans only. Deep by default (researcher → strategist → evidence auditor). Produces 11_Demand-Generation.md plus usable assets (funnel brief, stage plan, page copy, nurture flows, lead-scoring sheet, asset and tracking map, launch QA log, traffic test plan, 30-day sprint). Trigger with "demand gen for X", "build the funnel for X", "lead magnet for X", "landing page and nurture for X", "how do leads arrive for X", "lead scoring for X", "GTM pillar 7 for X".
version: 1.0.0
---

# GTM Demand Generation — Pillar 7

**Answers:** *how do qualified leads arrive predictably, and what happens to them next?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Playbook/GTM-Playbook.md` **Pillar 7** (6-stage lifecycle, lead magnets, nurture days 0–7, lead scoring, funnel maps, capture + trust channels, awareness × channel fit, traffic roadmap, 12-step build, launch QA, 30-day sprint, done-when list) · `GTM_ROOT/Frameworks/10_Lead-Nurture.md` read in full (three numbers, four pillars, compliance caveats §3, self-serve translation §4, output contract; source `Learning_resources/_extracted/100M Lead Nurture Playbook.txt` p11 pillars, p13–18 availability, p19–24 speed, p25–32 personalisation, p33–36 volume, p44–45 checklist; book p30 missing) · `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.7** (channel economics p269–270, six inputs, Bullseye, capture-vs-generate rule p277, seven channels, ABM maths p296, Growth Loops) · `GTM_ROOT/Frameworks/05_Messaging-and-Channels.md` §1C CTA ladder, §2B channel–content fit, §4 diagnostics · `GTM_ROOT/Frameworks/06_Proof-System.md` [5] distribution, [6] measurement |
| **Upstream** | `08_Coherence-Audit.md` (verdict) · `09_GTM-Motion-and-Routes-to-Market.md` (how much inbound matters) · `10_Revenue-Process-and-SLAs.md` (MQL/SQL definition, hand-off threshold, response SLAs) · `05_Messaging-and-Channels.md` + `assets/05_channel-plan.md`, `05_copy-kit.md`, `05_copy-lint.py` · `02_ICP.md` (trigger signals) · `02b_Buying-Center-and-Personas.md` (awareness levels) · `07_Pricing-and-Packaging.md` (entry / front-end offer) · `06_Proof-System.md` (proof per persona × stage) · `00_Discovery.md` §0 Business Profile |
| **Writes** | `products/<slug>/11_Demand-Generation.md` · `products/<slug>/assets/11_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `12` onward `STALE` (12 Outbound, 13 Enablement, 14 Metrics, 15 Execution Audit) |

**Phase 2 gate.** Phase 2 executes the locked strategy; it does not remake it. Read the `08` verdict and state it in the header. **FAIL → stop**, name the breaks, offer `gtm-engine:coherence-audit`. Missing or STALE `05`, `06`, `07`, `02`, `02b` → stop (protocol §3). Missing `09` → stop and offer `gtm-engine:motion`: the motion decides whether inbound is the main engine or a support. Missing `10` → proceed, but the hand-off threshold and response SLAs are drafted `ASSUMED` and listed as a finding for `gtm-engine:revenue-process`.

## Profile defaults (SPINE "How the profile changes each pillar")

| Signal | Default this skill applies |
|---|---|
| P1 Services / Productised service | Map **A** (lead magnet → call), or **D** (paid diagnostic) in low-trust markets. Conversion = a kept call (show rate) |
| P1 Software / SaaS | Trial or demo funnel; **activation is the conversion event** (Frameworks/10 §4). Check time-to-aha fits the trial window (Voje ch.7, Vidyard) |
| P1 Marketplace / Data-API / Physical / Hybrid | `SOURCE-GAP`: no source gives a funnel map for two-sided, developer or physical-product demand. Pick the nearest map, mark it `ASSUMED`, say why |
| P2 Retainer / Project | Lead magnet bridges to the front-end offer in `07` (bait → front end). Subscription / Usage: trial, freemium or paid pilot as `07` set it. Transaction: `SOURCE-GAP`, `ASSUMED` |
| P3 > $3k with strong proof | Map **B** (VSL → application) is allowed. P3 high and TAM small: run the ABM maths (Voje p296: LTV × win rate → accounts); 50–100 accounts → ABM beats inbound, route to `gtm-engine:outbound` |
| P3 < 5K, self-serve (P4) | Direct sign-up or direct booking; scoring and SDR hand-off stay light (per `09`) |
| P4 buying group 3+ | Nurture per persona from `02b`, each persona's own CTA rung (Frameworks/05 §1D) |
| P5 before paying customers | Traffic phases 1–2 only (foundation, validation). Scoring from ICP fit + intent, `ASSUMED`; no scaling budget |
| P5 Scaling | Phases 3–4; 80% budget on verified channels, ≤20% experiments; one Growth Loop hypothesis (Voje ch.7) |
| P7 markets | **WhatsApp-first** where the market converts through chat (GCC, local services). Consent law per market decides cadence, retargeting and WhatsApp opt-in |
| P8 one or two people | **One funnel, two channels.** Availability and speed SLAs sized to real hours; no community channel under 6 h/week (Voje) |
| P9 advisory | We write specs and copy; the client owns the build, QA and sprint rows in the tracker |

Departing from a default is a `PROPOSED` decision with its reason.

## Rules specific to this pillar

1. **Execute Phase 1, don't remake it.** Channels come from `05_channel-plan.md`, words from `05_copy-kit.md`, the entry offer and prices from `07`, proof from `06`, triggers from `02`, awareness from `02b`. No new claims. A conflict becomes a finding for the owning skill, never a silent edit. If `05` lacks one capture and one trust channel, propose the pair from `05`'s own Bullseye middle ring as a finding for `gtm-engine:messaging`.
2. **Every stage, six fields.** All 6 lifecycle stages get objective, audience, activity, conversion action, KPI and follow-up. Stages 1–3 are built here; stage 4 hands to `10`; stages 5–6 (retention, expansion, referrals feeding awareness) point to `10` and say so.
3. **One funnel map for 30 days, no hybrids.** Choose by the playbook's situation table and the profile default. Write the reason and the maps that lost.
4. **Channel fit = offer × funnel × awareness × intent.** Apply Voje's rule: existing demand → capture first; adjacent demand → piggyback; neither → generate (and say that means months to ROI). Never send an unaware audience to a high-commitment step.
5. **The lead magnet earns the next step.** One per niche. It bridges to the diagnostic or entry offer from `07`; best is a result on the prospect's own data (Frameworks/06, connections). Landing page: one headline, one problem, one value proposition, benefits, proof, a short form, **one** CTA. Ask only the fields scoring and routing use, plus a consent box where the market requires it.
6. **Nurture runs on the four pillars** (Frameworks/10): availability plan, speed SLAs (first contact, days to first appointment, reply time), personalised flows per lead category with matched proof, a written week-1 cadence and reminders. Separate flows for booked, unbooked, no-response and no-show. Self-serve products map all of it onto activation (§4). **Every cadence is checked against the consent law of each target market (§3)**; a cold-contact law question stays open, never assumed cleared.
7. **Inbound leads only.** Outbound-sourced lists and their nurture belong to `gtm-engine:lead-research` (L3) and `gtm-engine:outbound`. Reference them; don't duplicate.
8. **Scoring from best customers, threshold from `10`.** Derive traits from real won customers; before customers, from ICP fit + intent signals, tagged `ASSUMED`. The playbook's points are *illustrative*. The hand-off band must equal `10`'s MQL/SQL definition. Routing keeps yellows ("yellows are the new gold").
9. **Measure throughput, not cost per lead.** Schedule rate, show rate, throughput (or activation rate), qualified conversations, closed deals. Before any paid channel run the channel-economics check (Voje p269–270: CAC vs LTV, LTV ≥ 3× CAC). Unknown → `UNKNOWN — needs measurement`.
10. **Planning figures are not benchmarks.** The funnel workshop, traffic roadmap and their budgets ($500–$1,000 test, $50/day campaigns, retargeting windows, 30–150 min per step) come from course material not in `Learning_resources/`. Cite them as "Playbook/GTM-Playbook.md, Pillar 7" and label them *planning figures*.
11. **Never acts externally.** No ad spend, no pixels installed, no pages published, no forms, automations, sequences or contacts created in any tool, no CRM changes. Paid lookups only after stating the cost and getting the owner's yes. The launch QA checklist ships **unrun**; a box is ticked only from the owner's reported result.
12. **Declared source gaps.** `SOURCE-GAP`: campaign calendar and content operations (editorial cadence, production workflow) — the roadmap marks them thin. `SOURCE-GAP`: long-term nurture beyond the 30-day show window (Frameworks/10 scope). Write no framework for them; any calendar is a dated list of sprint assets, `ASSUMED`.

## Procedure

### 1. Gate and profile
Read `08` verdict, `09`, `10`, the Business Profile. Write the profile line and the defaults applied. Read `05`'s channel plan and copy kit, `07`'s entry offer, `06`'s proof map.

### 2. Research (deep step ①)
Small `gtm-engine:researcher` briefs that save to `products/<slug>/research/`; reuse `05` channel evidence first.
- **Channel mechanics and rules** for the two chosen channels: ad platform minimums and policies, WhatsApp Business opt-in and template rules, directory or marketplace listing rules.
- **Consent law per P7 market:** calls, texts, WhatsApp, email, cookies and retargeting pixels. Primary sources.
- **Competitor funnels:** lead magnets, CTAs, forms and offers they run, quoted verbatim with URL and date.

### 3. Draft
Funnel brief (playbook step 1) → 6-stage plan → funnel map → channel pair and awareness × channel fit → lead magnet, landing and thank-you specs with copy from the kit → nurture flows, availability and speed SLAs → scoring bands and routing → traffic phase and validation test plan → 12-step build with outputs and owners → launch QA (unrun) → 30-day sprint with 3 experiments, thresholds and stop rules set now.

### 4. Judgement (deep step ③)
Send `gtm-engine:strategist` the brief, stage plan, map options, channel pair and scoring. Ask for: the **funnel map**; the **lead magnet** per niche; the **scoring threshold and routing**; the **3 experiments**; what would flip each call.

### 5. Attack (deep step ④)
Send `gtm-engine:evidence-auditor`: every copy line against the claims register (and run `assets/05_copy-lint.py`); cadences against each market's consent rules; scoring arithmetic and threshold vs `10`; budget lines labelled as planning figures; consistency with `05`/`06`/`07`/`09`/`10`. Fix each finding, or carry it into Open questions; Option A/B if the strategist's call falls (protocol §5 ④b).

### 6. Assets
Write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `11_funnel-brief.md` | One page: offer, audience, conversion goal, traffic temperature, chosen map + reason, CTA path (primary, fallback, owner, response time) | Briefing anyone who builds or runs the funnel |
| `11_funnel-stage-plan.csv` | 6 stages × objective, audience, activity, conversion action, KPI, follow-up, owner, hand-off pillar | Checking no stage is dark |
| `11_page-copy.md` | Lead magnet spec + outline, landing page and thank-you page copy (market language first, EN gloss), each line citing its claim row; linted | Building the pages |
| `11_nurture-flows.md` | Days 0–7 email/WhatsApp flows for booked, unbooked, no-response, no-show; reminder schedule; availability and speed SLAs; consent note per market | Loading into the CRM or email tool (after the owner's yes) |
| `11_lead-scoring.csv` | Signal, points, source of the trait, band thresholds, hand-off band = `10` definition, routing rule | Configuring scoring in any CRM |
| `11_asset-and-tracking-map.csv` | Every page, form, message, alert and automation: trigger, tag, stage move, owner, tool; UTMs, hidden source fields, conversion events | Building in the funnel tool without missing a piece |
| `11_launch-qa.md` | The playbook QA checklist as a pass/fail log, with date and tester columns, unrun | Launch-day audit |
| `11_traffic-test-plan.md` | Current traffic phase; angles × creatives; budget lines labelled planning figures; retargeting audiences with windows and consent basis; stop rules | Running the validation test once the owner approves spend |
| `11_30-day-sprint.csv` | 1 funnel, 2 channels, ≤3 experiments: hypothesis, asset, KPI, threshold, stop rule, review date | Running and judging the sprint |

### 7. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-engine:outbound` (Pillar 9).

## Checks before presenting (playbook "Pillar 7 is done when" + this skill)
- [ ] Each funnel stage has an objective, audience, activity, conversion action, KPI and follow-up
- [ ] One funnel map is chosen, with the reason written down
- [ ] Two channels are chosen: one to capture, one to build trust
- [ ] The lead magnet, landing page, thank-you page and nurture sequence are built *(here: specified and drafted; "built" ticks only when the owner reports them live)*
- [ ] Lead scoring bands are set
- [ ] The launch QA checklist is passed *(ticks only from the owner's run log)*
- [ ] The 30-day sprint is set: 1 funnel, 2 channels, up to 3 experiments with stop rules
- [ ] Header states the `08` verdict, the profile line and the defaults applied
- [ ] No channel, claim, price or proof that Phase 1 didn't set; conflicts listed as findings
- [ ] Speed SLAs and availability within P8 hours; hand-off band equals `10`
- [ ] Every cadence and retargeting audience checked against each market's consent law
- [ ] Throughput metrics named (or `UNKNOWN`); channel-economics check before any paid line
- [ ] Budget figures labelled planning figures; SOURCE-GAPs declared
- [ ] All copy linted; all assets written; nothing sent, spent, published or built
