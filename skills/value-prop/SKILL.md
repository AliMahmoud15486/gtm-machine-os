---
name: value-prop
description: GTM Pillar 3a — Value Proposition for any product, built on the ICP/ECP and personas. Inventories what the product actually does (verified against code or docs), fills one Value Proposition Canvas per ECP, selects 3–5 value drivers that pass the five attribute tests and the "differentiated value" test against real alternatives, builds baseline-vs-target and a ≤3-input ROI model that survives pessimistic inputs, chooses category and frame of reference, and assembles the statement plus UVP variants to test. Deep by default (researcher → strategist → evidence auditor). Produces 03_Value-Proposition.md plus usable assets (the paste-ready value proposition statement in the market language and English, value-prop sheet, claims register, ROI calculator, UVP test plan, measurement backlog). Trigger with "value proposition for X", "value drivers for X", "why would anyone buy X", "UVP for X", "ROI model for X", "category for X", "GTM pillar 3 for X".
version: 1.0.0
---

# GTM Value Proposition — Pillar 3a

**Answers:** *why should this customer buy anything from us, and why from us rather than the alternatives?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/03_Value-Proposition.md` (read in full; the output contract is at the bottom) + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.4**: GTM VP Canvas (one per ECP, select → verify), Dunford's two rules, three UVP formulas, SLEPPERY, PMF measurement |
| **Upstream** | `00_Intake.md` · `02_ICP.md` (profile, anti-ICP, assumption map) · `02b_Buying-Center-and-Personas.md` (personas, awareness, kill list). `01_Segmentation.md` + `assets/01_competitors.csv` for the alternatives |
| **Writes** | `products/<slug>/03_Value-Proposition.md` · `products/<slug>/assets/03_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `04` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 3 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `02_ICP.md` or `02b_…` is missing, **stop** and offer the missing skill (protocol §3).

## Rules specific to this pillar

1. **Product truth first.** Before any canvas, inventory what the product does **today**, verified against code, config, live docs or a demo. Tag each capability:
   - `Available today` (with file or source);
   - `Behind a flag / off`;
   - `Roadmap`;
   - `Doesn't exist`.

   A pain reliever or driver may rest **only** on `Available today` capabilities. Anything else is labelled roadmap everywhere it appears.
2. **Customer language is verbatim or absent.**
   - Fewer than 5 real interviews → the canvas header says `ASSUMED — no customer interviews run` (framework contract item 2).
   - Pains and gains are written in neutral words, tagged.
   - Quotes appear only with a traceable source.
3. **3–5 drivers, each a mechanism with a number.** A driver is the *cause* of a change in revenue, cost, speed, risk or quality. "We automate X" is a feature.
4. **Two filters per driver, both written down:**
   - **(a) the five attribute tests:** quantifiable, business-relevant, repeatable, provable, aligned;
   - **(b) the differentiated-value test** (Dunford). For each alternative in `01_competitors.csv`, including **do-nothing**, **DIY/manual**, the **platform's native features** and **suites that bundle the job**: does it also deliver this driver? **If every alternative delivers it, it doesn't decide the purchase.** Keep it as table stakes, but it isn't a pillar.
5. **Costs count too.** The value equation includes fees, switching cost, **and any value the product can destroy** (e.g. genuine orders lost to a timeout). A net value that is positive only in the best case is reported as such.
6. **Persona fit.** Each driver names the persona whose KPI it moves (`02b`). A driver no veto holder cares about is decoration.
7. **Public-claim discipline.** Every claim the VP could make in public goes into the claims register with a status:
   - `Publishable now`: true today and evidenced;
   - `Publishable with method`: an estimate, with its workings linked;
   - `Not publishable`: needs customer data first.

   Honour any rule already in the product docs. No performance claims without real customers.

8. **The statement is built from the register, not the other way round.** Assemble the value proposition statement
   only from claims marked `Publishable now` or `Publishable with method` (with the method shown). Any clause whose
   claim is held, refuted or decided-against is **removed and listed** under "held lines", with what would release it.
   Wording reserved for a test arm (e.g. a UVP modifier) stays out of the canonical statement. Run the copy linter on it
   if the product has one.

## Procedure

### 1. Product truth inventory
Read the product's code, config and docs (paths in intake §3). List each capability with its tag and source. Flag any gap between what the marketing copy or listing says and what the code does.

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save as they go (protocol §5):
- **Alternatives' value claims.** What each alternative in `01_competitors.csv` promises (verbatim from its listing or site, with URL and date), its price, and which drivers it covers. Include the platform's native features and DIY.
- **Baseline benchmarks.** Public numbers for each candidate driver metric, sourced and tagged by quality. Report absence.
- **Category evidence.** How buyers search for and name this kind of product: app-store categories, search terms, how competitors self-describe.

### 3. Canvas, one per ECP (framework step 1; Voje's GTM VP Canvas)
- **Customer side:** jobs (functional / social / emotional), pains, gains.
- **Value side:** products & services, pain relievers, gain creators. Each one cites a capability from step 1.
- Then **select**: only the mission-critical relievers and creators survive.
- End with **verify**: the specific tests that would confirm the selection.

### 4. Feature → benefit → driver, then the two filters
Map every `Available today` capability. Score each candidate driver on the five attributes and the differentiated-value test (rule 4). Keep 3–5 drivers.

### 5. Baseline vs target
Fill one row per driver: metric, baseline (with source, or `UNKNOWN — needs measurement`), target, business value, **where the metric is captured** (an existing product event or field, or "not instrumented"). Missing baselines become the measurement backlog.

### 6. ROI model
- **≤3 inputs a merchant can answer on a call.**
- Run it at pessimistic, central and optimistic values.
- Include fees, switching cost and value destroyed (rule 5).
- State the break-even.

### 7. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the inventory, canvas, scored drivers, ROI and category evidence. Ask for:
- the **final 3–5 drivers** and their order;
- the **category choice** (conformist / modifier / creator), with the budget line and price sensitivity it implies;
- **3 UVP hypotheses**, one per Voje formula, to test;
- the assembled statement;
- what would flip each call.

### 8. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`:
- the drivers, with their attribute and differentiated-value scores;
- the ROI model, to push it to pessimistic inputs;
- every capability claim, spot-checked against the code;
- every quote;
- the category call;
- any research that landed after the draft.

Fix each finding, or carry it into Open questions. If the audit undermines the strategist's call, present Option A / B (protocol §5 ④b).

### 9. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `03_value-proposition-statement.md` | **The value proposition statement, paste-ready:** (1) the one-liner (listing-grade); (2) the full statement in the market language **and** English; (3) the drivers it rests on, each with its register status; (4) **held lines** (claims kept out, why, and what releases them); (5) what will change the text later (pending decisions, e.g. trial size); (6) the UVP test arms, kept separate from the canonical text. Every clause traces to a claims-register row. Linted | The single source anyone copies the value proposition from: listing, website, outreach, decks, onboarding |
| `03_value-prop-sheet.md` | **The one-page deliverable:** statement, 3–5 drivers with their number (or "to be measured"), category line, risk reversal, and who it's for and not for. Every line carries its claims-register status | Briefing copy, sales and the listing; the input to Pillar 4 |
| `03_claims-register.csv` | Every claim the VP could make: wording, driver, capability source, evidence, tag, **public status** (publishable now / with method / not publishable), what would upgrade it | Stops anyone shipping an unbacked claim; Pillar 5 (proof) works from it |
| `03_roi-calculator.csv` | The ROI model as a spreadsheet: inputs, formulas (`=` cells that work in Sheets/Excel), pessimistic / central / optimistic columns, break-even row | Co-building the business case live on a call |
| `03_uvp-test-plan.md` | The 3 UVP hypotheses, how each is tested cheaply (message test, listing copy, outreach, landing page), sample size, success metric, decision rule | Choosing **one** UVP with evidence, then using it everywhere |
| `03_measurement-backlog.csv` | Each driver metric: baseline source, instrumentation status in the product, what to add, owner, when it will have data. Plus the **PMF measurement plan** (Sean Ellis survey trigger, retention cohort definition) | Engineering and analytics to-dos that make the drivers provable |

### 10. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-machine-os:positioning` (Pillar 3b).

## Checks before presenting (framework output contract)
- [ ] Product truth inventory present; every reliever and driver cites an `Available today` capability
- [ ] Canvas per ECP, both sides and all six boxes, with select and verify; `ASSUMED` header if fewer than 5 interviews
- [ ] 3–5 drivers, each scored on the five attributes **and** the differentiated-value test against named alternatives
- [ ] Every driver mapped to a persona's KPI
- [ ] Baseline-vs-target for every driver; no adjectives in place of numbers
- [ ] ROI model with ≤3 call-askable inputs, at three input levels, including fees, switching cost and value destroyed
- [ ] Category named (conformist / modifier / creator) with budget line and price sensitivity
- [ ] Assembled statement with each clause traceable to a step **and to a publishable claims-register row**; held lines listed; 3 UVP hypotheses to test, kept out of the canonical statement
- [ ] Zero unsourced quotes; every public claim in the register with a status
- [ ] All six assets written, including `03_value-proposition-statement.md` (linted)

Playbook "Pillar 3 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it; the positioning, alternatives and validation boxes belong to `gtm-machine-os:positioning`):
- [ ] The Value Proposition Canvas is filled for each ICP, using words from 5 customer interviews
- [ ] 3–5 value drivers are chosen, each with a KPI, a baseline and a target
- [ ] Every claim is paired with 1–2 proof points and a risk reverser
- [ ] The category and frame of reference are chosen
