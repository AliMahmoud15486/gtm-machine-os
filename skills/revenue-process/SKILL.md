---
name: revenue-process
description: GTM Pillar 10 — Revenue Process & SLAs for any product, built on the chosen GTM motion and the locked Phase 1 strategy. Sets the process depth from the motion (all ten stages, a stated compression, or a light self-serve funnel plus a success process), writes every stage with an owner and observable exit criteria, chooses one qualification framework, specifies a tool-agnostic CRM pipeline (sales + separate delivery pipeline, required fields, exit rules), sets SLAs from the project's own capacity and the speed-to-lead rules, specifies automation triggers, adapts the qualification-call and discovery scripts to the ICP and personas, drafts the marketing–sales contract (five definitions), the value-case and pilot terms, the handoff, onboarding, retention/expansion plan and the reporting cadence. Specs and drafts only — never configures a CRM or sends anything. Deep by default (researcher → strategist → evidence auditor). Produces 10_Revenue-Process-and-SLAs.md plus usable assets (stage map, CRM pipeline spec + field dictionary, SLA sheet, automation-trigger spec, qualification-call script, discovery guide, value-case and pilot template, marketing–sales contract, handoff and onboarding kit). Trigger with "revenue process for X", "sales process for X", "pipeline stages for X", "SLAs for X", "CRM pipeline for X", "qualification framework for X", "discovery script for X", "handoff to delivery for X", "GTM pillar 10 for X".
version: 1.0.0
---

# GTM Revenue Process & SLAs — Pillar 10

**Answers:** *how does a deal move from first reply to renewal, who owns each step, and what does "done" mean at each gate?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/09_Sales-Led-Growth-and-Sales-Process.md`: read in full — §2 process vs methodology vs playbook, §3 the ten stages with exit criteria, §4 solo / low-ACV adaptation, the output contract. `GTM_ROOT/Frameworks/10_Lead-Nurture.md` §1–§4 (availability, speed, volume, BAMFAM, the self-serve translation) and **its §3 compliance caveats**. `GTM_ROOT/Frameworks/12_Market-Readiness-Launch-and-Metrics.md` §4 (metrics by phase; metrics must trigger actions). Practitioner layer: `GTM_ROOT/Playbook/GTM-Playbook.md` "Pillar 10 — Revenue Process & SLAs". Sources: `_extracted/B2B Growth Masterclass _ Session #14.txt` (p6 roles, p7 stage focus, p11 shared SLAs, p12 process/methodology/playbook, p14 the ten stages) and `_ Session #15&16.txt` (p7 connect, p11 discovery artifacts, p12–13 qualification, p14 solution, p16 value case, p22–23 close & handover, p24 onboarding & expansion); `_ Session #17&18.txt` p5 (stage-1 exit), p21–22 (lead qualification) |
| **Upstream** | `09_GTM-Motion-and-Routes-to-Market.md` (motion → depth, roles, routes) · `02_ICP.md` (fit, anti-ICP, triggers) · `02b_Buying-Center-and-Personas.md` (roles, veto, champion, per-persona discovery script) · `03_Value-Proposition.md` (ROI model → value case) · `05_Messaging-and-Channels.md` (pillars, banned list, channel plan and legal gate) · `07_Pricing-and-Packaging.md` (offers, Entry/pilot, terms) · `06_Proof-System.md` (risk reversal, proof by persona × stage, "proof used?" field) · `08_Coherence-Audit.md` (verdict) · `00_Discovery.md` (Business Profile P1–P9, current tools, instrumentation) · optional: `leads/L3_nurture-plan.md` (CRM fields already drafted) |
| **Writes** | `products/<slug>/10_Revenue-Process-and-SLAs.md` · `products/<slug>/assets/10_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `11_Demand-Generation`, `12_Outbound`, `13_Enablement`, `14_Metrics-and-Feedback`, `15_Execution-Audit` `STALE` (protocol §9, §10.4) |

**Gate.** Phase 2 executes the locked strategy; it does not remake it.
- `09` missing or STALE → **stop**, offer `gtm-engine:motion`. The motion decides the depth of this pillar.
- `08_Coherence-Audit.md` missing → stop, offer `gtm-engine:coherence-audit`. Verdict **FAIL** → stop and name the breaks. **PASS-WITH-GAPS** → proceed and repeat the gaps in Open questions. State the verdict in the header.
- Any consumed Phase 1 artifact STALE → stop (protocol §3).
- This skill never changes ICP, personas, positioning, messaging, pricing or proof decisions. A conflict (e.g. the pilot this process needs is not in `07`'s offer architecture) becomes a finding for the owning skill, listed in Open questions.

## How the profile changes this pillar

Read the Business Profile first and state what was applied in the `**Profile:**` line.

| Signal | Default |
|---|---|
| **Motion from `09`** (driven by P3 + P4) | Product-led / self-serve (< ~5K ACV, no setup) → a **light funnel**: the product performs stages 1–2 and 10; humans step in only above a stated buying-center or deal-size threshold; the "SLAs" are activation speed rules (`Frameworks/10` §4). Thin founder-led → stages 2 → 3 → 4 → 6 → 8, compressed into 1–2 calls; 5 folds into 3; 7 is the Entry offer. High-touch / sales-led → **all ten** (`Frameworks/09` §4). Hybrid → name which segment gets which path, and the threshold that routes between them. |
| **P1 type** | Services / productised → the delivery pipeline is onboarding → active service → renewal → expansion. Software → onboarding → activation → adoption → renewal. Marketplace / two-sided → `SOURCE-GAP` (no source covers a two-sided process); mark the second side's process `ASSUMED`. |
| **P2 revenue model** | Retainer / subscription → retention rate, NRR, renewal sequence, expansion triggers (Playbook Pillar 10, "After the sale"). Project → next-project and referral motion instead of renewal. Usage → expansion = usage growth; watch the usage signal. Transaction / commission → `SOURCE-GAP`; mark retention and expansion design `ASSUMED`. |
| **P4 how they buy** | Buying-group size from `02b` sets how many stakeholders stage 2 must surface and whether stage 6 needs a champion-ready business case. Heavy setup → stage 7 pilot and a formal handover. |
| **P5 stage** | Before PMF → every discovery call is also a value-prop interview: verbatim capture into `interviews/` is a stage-3 exit criterion. Pipeline numbers are measured, not targeted (`UNKNOWN — needs measurement`). |
| **P7 where they sell** | Call, text and messaging cadences follow the consent law of each market (`Frameworks/10` §3) and the `05` channel plan / lead-research legal gate. The legal gate wins over any speed rule. |
| **P8 capacity** | Sets every SLA and availability target (rule 3). One or two people → owners are the same person, handoff SLAs become self-checks, and automation carries first response. |
| **P9 engagement** (client mode) | Advisory → we write the process and specs; the client owns configuration and every "live / signed" row in the tracker. Done-with-you → name who configures what. |

Where none of the frameworks gives a rule for the profile, write `SOURCE-GAP` and mark the choice `ASSUMED`.

## Rules specific to this pillar

1. **Process ≠ methodology ≠ playbook** (`Frameworks/09` §2). Stages and exit criteria go in the stage map; the qualification framework in its own section; scripts and templates in assets.
2. **Exit criteria are observable.** "Champion identified (name in CRM)", not "good call". Every stage used has an owner — a named person or "product" for automated stages. Compressions are stated, with what was dropped.
3. **SLAs are a `SOURCE-GAP` in the course** (`Frameworks/09` output contract item 9; roadmap Pillar 10). The Playbook's SLA and contract numbers are *illustrative*. Set each target from (a) `Frameworks/10`'s speed rules — first contact within 5 minutes, first appointment ≤ 3 days out (5 at most), immediate replies between booking and meeting — tagged `RESEARCHED` (Hormozi; US opt-in context; stats directional) and (b) the **capacity arithmetic** from P8: expected volume per week × minutes per touch ≤ hours available, shown. A target the hours can't meet is lowered or automated, never kept as an aspiration. Unknown volume → `UNKNOWN — needs measurement`, and the SLA is provisional.
4. **One qualification framework** (SPIN, SPICED, MEDDICC or BANT; "use any, don't worship acronyms", Session #15&16 p12). The framework gives no rule for choosing by profile: `SOURCE-GAP`. Choose by the `02b` buying-center size and cycle length, mark it `ASSUMED`, state what lost, and map every field into the CRM field dictionary.
5. **Scripts adapt; they don't invent.** Qualification-call and discovery scripts use the `02b` personas, the `02` triggers, the `05` pillars and banned list, and `06` proof by persona × stage. Placeholders like `[their words]` stand where customer language belongs. **No invented customer quotes, no "a typical buyer would say".** Lint against `assets/05_copy-lint.py` if it exists.
6. **Stage 3's first exit criterion is non-negotiable:** the customer's problem, impact and outcomes written in their words, with baseline numbers (`Frameworks/09` §3–4). It feeds `interviews/` and `03`. Stage 10's success memo feeds `06`. Both are proof capture points, wired to the `06` "proof used?" field.
7. **Pilot = the `07` Entry offer**, with convert-to-program terms agreed up front. Value case = the `03` ROI model run with *their* numbers. Risk reversal = `06`'s, unchanged.
8. **Automation supports the relationship.** Each trigger names its consent basis and where a person must step in. High-value prospects still get a person.
9. **Never acts externally.** No CRM configuration, no automations built, no sequences, no messages sent, no calendar set-up. Specs and drafts only. Any credit-spending lookup: state the cost, wait for the owner's yes.
10. **Live ≠ specified.** The tracker boxes "live", "agreed" and "signed" describe execution. They are ticked only when the owner (or the client) confirms it happened — never on the strength of a spec.

## Procedure

### 1. Gate, profile, depth
Run the gate. Read the profile and `09`. Write the depth decision: which stages apply, compressed how, and who owns each (from `09`'s roles).

### 2. Research (deep step ①)
Small `gtm-engine:researcher` briefs that save to `products/<slug>/research/` as they go; reuse earlier research first.
- **Consent and contact rules** for calls, texts, messaging apps and email in each P7 market, from primary sources — they bound the cadences and triggers.
- **The current tool stack** (from `00_Discovery`): which CRM or tracker exists, what its plan allows (stages, required fields, workflows). The spec stays tool-agnostic; this only adds a mapping note.
- **Buyer-side process facts** for the ICP: procurement, security or legal review steps, typical approval paths (`02b` first; external only to fill gaps).

### 3. Draft
- **Stage map:** purpose, owner, do, ask, exit criteria, artifacts, proof capture point — per stage used.
- **Qualification framework** and its fields.
- **CRM pipeline:** sales stages (Playbook table: new lead → contacted → discovery → qualified → proposal → negotiation → won/lost) mapped to the stages used, each with required fields and exit rule; loss reasons as a fixed list; a **separate delivery pipeline** by P1/P2.
- **SLA sheet** with the capacity arithmetic (rule 3); availability plan (days, hours, slot length, booking paths; `Frameworks/10` Pillar I).
- **Automation triggers:** the Playbook list (form submitted, high-intent lead, booked/missed, proposal sent, won, inactive, renewal approaching, positive feedback) adapted to the motion, each with condition, action, consent check, human step.
- **Scripts:** qualification call (8 steps; confirm authority and need, BAMFAM), discovery guide (question bank incl. cost of inaction, stop-asking list), discovery-and-pitch meeting agenda — per primary persona.
- **Value case and pilot terms** (rule 7). **Marketing–sales contract:** MQL, SQL, qualified meeting, response time and attempts, weekly sales feedback — each a number or an observable test.
- **Handoff** (Problem → People → Plan → Pitfalls), 30/60/90 plan, onboarding day plan, retention and expansion triggers by P2, **reporting cadence** (weekly sales feedback; rep or founder dashboard: show rate, close rate, lead-to-close; monthly outcome report; QBRs where P2 has a renewal).

### 4. Judgement (deep step ③)
Send `gtm-engine:strategist` the depth decision, stage map, framework choice, SLA arithmetic and pilot terms. Ask for: the recommended compression (or all ten), the qualification framework, the SLA targets the capacity can hold, whether stage 7 runs, the human-step thresholds — each with the alternatives that lost and what would flip it.

### 5. Attack (deep step ④)
Send `gtm-engine:evidence-auditor`: every exit criterion (observable?), the capacity arithmetic, every SLA's basis and tag, consent claims, the scripts (fabricated language, banned phrases, drift from `05`), consistency with `07` Entry/terms, `06` risk reversal and `02b` roles. Fix each finding or carry it into Open questions; Option A / B if the audit undermines the strategist (protocol §5 ④b).

### 6. Assets
Write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `10_stage-map.md` | Stages used, each with owner, exit criteria, artifacts, proof capture point; compression stated | The one page everyone sells from |
| `10_crm-pipeline-spec.csv` | Sales + delivery pipeline: stage, maps-to stage, owner, required fields, exit rule, trigger IDs | Configuring any CRM or spreadsheet tracker |
| `10_crm-fields.csv` | Field dictionary: name, type, allowed values, required-at stage, source (qualification framework, lead source, consent basis, loss reason, "proof used?") | Importing fields; keeping data clean |
| `10_sla-sheet.md` | Handoff · target · basis (capacity arithmetic / `Frameworks/10` rule) · tag · owner · how measured · breach action; availability plan | Agreeing and policing handoffs |
| `10_automation-triggers.csv` | Trigger · condition · action · channel · consent check · human step · owner · SLA ref · status (`spec`) | Building workflows in the chosen tool |
| `10_qualification-call-script.md` | The 8-step call per primary persona, with meeting brief for the closer | Running stage 2 tomorrow |
| `10_discovery-guide.md` | Question bank, stop-asking list, framework capture sheet, discovery-and-pitch agenda, "here's what I heard" recap template | Running stage 3 and capturing verbatim language |
| `10_value-case-and-pilot.md` | Business-case template (problem → impact → options → why us → ROI → risk) wired to `03`; pilot SOW with success metrics and convert-to-program terms from `07` | Stages 6–7 |
| `10_marketing-sales-contract.md` | The five definitions with numbers, review date, unsigned signature lines | Getting it signed |
| `10_handoff-and-onboarding.md` | Handoff doc, 30/60/90 plan, onboarding day plan, success memo, retention/expansion triggers, reporting cadence | Stages 9–10 and the monthly report |

### 7. Tracker and present
Update `00_Playbook-Tracker.md` per protocol §10 (rule 10 governs the "live / agreed / signed" boxes). Then present per protocol §8. Next skill: `gtm-engine:demand-gen` (Pillar 7).

## Checks before presenting
Playbook "Pillar 10 is done when" (the artifact must show each; execution boxes per rule 10):
- [ ] Sales stages are defined, each with exit criteria
- [ ] CRM pipeline stages and exit rules are live, with a separate delivery pipeline
- [ ] One qualification framework is chosen
- [ ] SLAs are agreed between marketing, sales and delivery
- [ ] Automation triggers are live
- [ ] The qualification-call and discovery scripts are ready
- [ ] The marketing–sales contract is signed, with all five definitions
- [ ] Onboarding steps and the reporting cadence are set

Framework output contract and this skill:
- [ ] Gate passed; coherence verdict and depth decision stated; profile line filled
- [ ] Every stage used has a named owner (or "product") and observable exit criteria; compression stated
- [ ] Discovery bank includes the cost-of-inaction question; stage-3 exit requires their words + baselines
- [ ] Business-case template wired to `03`; pilot terms match `07` Entry with convert-to-program terms
- [ ] Handoff template (Problem → People → Plan → Pitfalls) and 30/60/90 plan
- [ ] Proof capture points at stage 3 and stage 10, wired to `06`'s "proof used?" field
- [ ] Every SLA shows its basis and tag; capacity arithmetic shown; SLA `SOURCE-GAP` declared
- [ ] Every trigger and cadence checked against P7 consent law and the `05` legal gate
- [ ] No invented customer language; scripts linted; no Phase 1 decision changed (conflicts listed as findings)
- [ ] Downstream `11`–`15` marked STALE on re-run; tracker updated; all assets written
