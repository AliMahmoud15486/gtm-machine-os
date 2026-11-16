---
name: pricing
description: GTM Pillar 6 — Pricing & Packaging for any product, built on the value proposition, positioning and proof system. Sets the pricing objective, computes the floor from real per-account costs (platform cut, per-unit costs, infra, support time) and the ceiling from the 3a value drivers, benchmarks ≥2 alternatives by their pricing logic, designs the offer architecture (entry/core/expansion), the 8-block packaging stack, the pricing architecture (model, value metric, levels, terms) and ≤3 tiers with fences instead of discounts, adds willingness-to-pay measurement (Van Westendorp / Gabor–Granger / presale), and writes a test plan with thresholds set in advance. Deep by default (researcher → strategist → evidence auditor). Produces 07_Pricing-and-Packaging.md plus usable assets (unit-economics calculator, paste-ready plan sheet, WTP question add-on, price-test plan, price-change playbook). Trigger with "pricing for X", "price X", "packaging for X", "tiers for X", "is X priced right", "unit economics for X", "GTM pillar 6 for X".
version: 1.0.0
---

# GTM Pricing & Packaging — Pillar 6

**Answers:** *how do we capture the value we create, at a price the customer accepts and the business survives on?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/07_Pricing-and-Packaging.md`: read in full. Parts A (packaging), B (the 6-step framework), C (software translation), D–E (Hormozi pricing and price-raise, with their caveats). The output contract is at the bottom. Plus `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.5** (seven mistakes, value metric, WTP methods, reverse-engineering from the economic model, behavioural pricing) |
| **Upstream** | `03_Value-Proposition.md` (drivers, ROI model, unit-cost notes, category/frame → budget line) · `04_Positioning.md` (frame, only-ness, risk reversal) · `06_Proof-System.md` (the risk reversal it chose — type, conditions, boundaries — and the proof assets to pair with the price) · `05_Messaging-and-Channels.md` (channels → CAC) · `02_ICP.md` (band, anti-ICP) · `00_Intake.md` (existing prices, constraints) |
| **Writes** | `products/<slug>/07_Pricing-and-Packaging.md` · `products/<slug>/assets/07_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `08` (coherence audit) onward `STALE` (protocol §9) |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 6 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `03` is missing or STALE, **stop** and offer `gtm-engine:value-prop` (protocol §3). If `06` is missing or STALE, **stop** and offer `gtm-engine:proof`. If prices already exist (intake), treat them as the **current state to evaluate**, not as a given or a blank slate.

## Rules specific to this pillar

1. **No floor, no lock.** The floor is computed per account per tier from **real** costs:
   - the platform/marketplace cut (verify it in the partner terms; don't assume);
   - per-unit costs at the tier's cap (messages, API calls, compute);
   - fixed infra spread over a stated account count;
   - payment fees;
   - **support and founder time at a stated hourly value**.

   Unknown inputs are `UNKNOWN — needs measurement`, and the floor is shown as a range.
2. **Margin at the cap, not at the average.** Compute every tier's margin at its usage cap and at "unlimited" use. A tier that goes negative at plausible usage is a defect: add a fair-use cap or change the metric.
3. **The ceiling traces to drivers.** Ceiling = quantified value from the `03` ROI model × a stated capture rate (typically 10–30% for software; state your choice). Use the **pessimistic** inputs as well as the central ones. If value is unproven, the ceiling is a hypothesis, and so is any price set against it.
4. **Benchmark logic, not price lists.** For ≥2 alternatives, record model, value metric, fences, trial, annual discount, add-ons and what each tier unlocks. Include do-nothing and DIY costs (`03`/`04`). Quote verbatim, with URL and date.
5. **Value metric first.** Choose what the price scales with (per order, per verification, per seat, flat). It must track customer value, be easy to understand and be measurable in the product. State why the alternatives lost.
6. **≤3 tiers. Fences, not discounts.** Tiers differ by metric volume, features or service. Discounts set the reference price (Voje ch.3; Hormozi D5 caveats). Free trials and annual plans are fences; ad-hoc discounts are not.
7. **WTP is measured, not guessed.**
   - Before customers: Van Westendorp in interviews (≥20 answers to be readable), or Gabor–Granger in a survey.
   - With traffic: price tests.
   - **Presale beats both.**
   - Add the WTP questions to the existing interview capture (`interviews/_capture-template.md`). **Don't create a separate study** unless volume allows.
8. **Platform rules bind pricing.** Marketplace billing, plan-name mapping, trial mechanics, price-change rules for existing subscribers, refund rules, and whether discounts or coupons are possible. Research them and respect them. **This skill does not change prices in any portal or code**; it proposes and the owner decides.
9. **Model the per-unit rate risk, not just the rate.** If a third party sets a per-unit cost (e.g. a messaging category the provider can reclassify), add a stress row at the worse rate. Specify how you'd detect the change (a webhook or alert) and the pre-decided response.
10. **Capacity is a constraint on pricing.** Check provider throughput limits in their *real* unit (often per day, shared across all customers), correlated peak days, and quality-based throttling. "Unlimited" tiers need fair use.
11. **Ceiling on net value, both band ends.** Use the value model's *net* formula (minus value destroyed), at the bottom and top of the ICP band. Say plainly when a price rests on benchmarks rather than proven value.
12. **Facts the owner already knows come first.** Taxes, entity residency, platform payout terms. Ask before designing around worst cases.
13. **The billing unit must be described exactly as the code counts it.** Every send, not every success; lint the definition.
14. **Price changes follow Part E.** Grandfathering, notice, the RAISE letter. Honour any locked or already-published prices; changing a published price is a decision for the owner, with its cost.

## Procedure

### 1. Objective and current state
- Write the pricing objective in one sentence, with a margin target (adoption vs profit, by funding state; Voje ch.5).
- List the current prices and terms, if any (intake; portal; code).

### 2. Research (deep step ①)
Small `gtm-engine:researcher` briefs that save as they go; reuse `03`/`04` competitor research first.
- **Platform terms:** commission or revenue share, billing mechanics, trial rules, plan changes, refunds, coupons, price-change rules, payout timing. Primary sources.
- **Cost inputs:** per-unit rates (e.g. messaging rate cards), infra pricing for the stack in use, payment fees. Read the product's own config and docs for real usage per unit.
- **Benchmark logic:** model, metric, fences, trials, annual terms and add-ons for ≥2 alternatives, verbatim. Reuse earlier research.

### 3. Floor (rule 1–2)
Per tier, at the cap and at a stress level. Show the arithmetic.

### 4. Ceiling (rule 3)
From the `03` ROI model, at pessimistic / central / optimistic inputs.

### 5. Benchmark (rule 4)
A logic table.

### 6. Design
- **Value metric.**
- **Offer architecture:** Entry, time-boxed and ending in a deliverable or result · Core · Expansion.
- **Packaging stack:** all 8 blocks for Core.
- **Pricing architecture:** model · metric · packaging · levels · terms.
- **≤3 tiers:** scope, outcome, upgrade trigger, fence.
- **Risk-reversal terms:** the commercial terms (fee, refund amount, billing mechanics) of the pilot or guarantee `06` chose, consistent with `04`/`06`. Do not re-choose the risk reversal here.

### 7. Judgement (deep step ③)
Send `gtm-engine:strategist` the floor, ceiling, benchmark and design. Ask for:
- the recommended **value metric, tiers and price points** (or **keep current**, with reasons);
- the **fair-use** terms;
- the **entry offer**;
- what to **test** vs **decide**;
- what would flip each call.

### 8. Attack (deep step ④)
Send `gtm-engine:evidence-auditor`:
- every cost input and its source;
- the margin arithmetic at the caps;
- the ceiling's inputs;
- benchmark quotes;
- platform-rule claims;
- consistency with `03`/`04`/`05`/`06`;
- any research that landed after the draft.

Fix each finding, or carry it into Open questions. If the audit undermines the strategist's call, present Option A / B (protocol §5 ④b).

### 9. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `07_unit-economics.csv` | Spreadsheet with live `=` formulas: per tier, price → platform cut → net → per-unit cost at cap / at stress → infra share → support time → **margin**; plus break-even usage for unlimited tiers | Checking any price change in a minute |
| `07_plan-sheet.md` | Paste-ready plan blocks for the platform (names that map correctly to the code, features, limits, fair-use line), AR + EN, linted with `assets/05_copy-lint.py` if it exists | Updating the portal or listing |
| `07_wtp-questions.md` | The WTP add-on for interviews (Van Westendorp's 4 questions in the market language, plus the value metric and plan-preference probes), with how to read the answers and the minimum n | Measuring willingness to pay alongside the discovery interviews |
| `07_price-test-plan.md` | Which price or packaging tests run, when, sample, metric, thresholds set in advance (framework close-rate >70% / <25%, adapted for self-serve trial→paid), review date | Knowing when to raise, cut or re-package |
| `07_price-change-playbook.md` | For existing subscribers: notice, grandfathering, platform mechanics, the RAISE letter template (market language) | Changing prices without churn or a 1★ wave |

### 10. Present
Update the tracker (protocol §10), then present per protocol §8. Next: **run `gtm-engine:coherence-audit`** (Phase 1 gate).

## Checks before presenting (framework output contract)
- [ ] Objective in one sentence with a margin target
- [ ] Floor per tier from real, sourced costs (or explicit UNKNOWN ranges); margin at cap and at stress; no tier negative at plausible use without a fair-use cap
- [ ] Ceiling from `03` drivers × a stated capture rate, at pessimistic and central inputs
- [ ] Benchmark of ≥2 alternatives by logic, plus do-nothing and DIY cost
- [ ] Value metric chosen, with the alternatives that lost
- [ ] Offer architecture: Entry / Core / Expansion; Entry time-boxed with a deliverable
- [ ] Packaging stack: all 8 blocks for Core
- [ ] Pricing architecture: model, metric, packaging, levels, terms
- [ ] ≤3 tiers with fences, not discounts
- [ ] WTP method chosen and added to the interview capture
- [ ] Test plan with thresholds set in advance and a review date
- [ ] Consistency: frame/budget line (3a), risk reversal (3b/5: terms match the `06` choice), channels and CAC (4, `05`), platform rules
- [ ] All assets written; plan copy linted

Playbook "Pillar 6 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it):
- [ ] The value ladder is drawn: each rung has an offer, a price, a job and a bridge to the next rung
- [ ] Each offer is written with the 8 packaging blocks
- [ ] The floor is calculated from real delivery cost and overhead
- [ ] The ceiling is calculated from client value and a capture rate
- [ ] Competitors are benchmarked
- [ ] There are no more than three tiers, named by maturity
- [ ] Routing rules are written for moving up, down-selling and following up a "no"
- [ ] A price test is planned on 5–10 deals
