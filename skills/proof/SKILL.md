---
name: proof
description: GTM Pillar 5 — Proof System for any product. Maps every message pillar to the evidence it needs (claims → evidence grid), designs the harvest plan with automatic capture hooks specified in the product and CRM, records consent levels, keeps every number date-stamped with its derivation, packages proof per persona × stage, assigns distribution, chooses risk reversal with boundaries, and scores each proof asset on Hormozi's 13 rules. For pre-proof products the honest output is a harvesting and measurement plan (incl. the experiment that will generate the first publishable number), not a library of assets that don't exist. Deep by default (researcher → strategist → evidence auditor). Produces 06_Proof-System.md plus usable assets (claims→evidence grid, harvest & instrumentation spec, consent form, proof-interview script, case-study template, compliant review-request script, pilot/measurement protocol, proof tracker). Trigger with "proof for X", "proof system for X", "case studies for X", "testimonials for X", "how do we prove X works", "social proof for X", "GTM pillar 5 for X".
version: 1.0.0
---

# GTM Proof System — Pillar 5

**Answers:** *why is it safe to believe us, and how do we capture the evidence that makes it so?*
Hormozi: **claim your proof, don't prove your claim.** Collect first; claim only what the data supports.

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/06_Proof-System.md`: read in full. The Proof Stack [1]–[6], case studies, risk-free guarantees, the output contract, and **the Hormozi 13 rules plus the compliance caveat on incentives** |
| **Upstream** | `05_Messaging-and-Channels.md` (pillars, channels, message tests) · `03_Value-Proposition.md` + `assets/03_claims-register.csv` (claims and their statuses, measurement backlog, PMF plan) · `04_Positioning.md` (only-ness, risk reversal, validation plan, the offer idea) · `02b_…` (personas). **Not** pricing: Proof runs before Pricing (Pillar 6) and does not need `07_Pricing-and-Packaging.md` |
| **Writes** | `products/<slug>/06_Proof-System.md` · `products/<slug>/assets/06_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `07` (pricing) onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 5 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `05` is missing or STALE, **stop** and offer `gtm-engine:messaging` (protocol §3).

## Rules specific to this pillar

1. **One grid row per message pillar, no exceptions** (framework contract item 1). Add rows for the only-ness claim and the risk reversal. Each row carries:
   - claim (verbatim from the claims register);
   - proof type;
   - asset format;
   - source;
   - owner;
   - **status**: exists / harvesting / instrument needed / blocked;
   - the register status it would upgrade to.
2. **Proof that doesn't exist is a plan, not an asset.** For pre-customer products, each row says how and when the evidence will be generated:
   - the experiment;
   - its sample;
   - its threshold;
   - its date.

   Never draft "example" testimonials, sample numbers or placeholder logos. **That is fabrication** (`CLAUDE.md` rule 3).
3. **Instrument before you ship** (framework [2], contract item 7). Every automatic harvest hook is specified concretely:
   - the event, field or table in the product;
   - the CRM field ("proof used?");
   - the asset ID;
   - the consent template.

   If the hook needs a code change, file it for the product owner. **This skill doesn't edit product files.**
4. **Consent is recorded, at three levels, per customer:**
   - anonymous metrics only;
   - named quote / logo;
   - full case study / reference call.

   No consent, no use. Record it in `assets/06_proof-tracker.csv`.
5. **Every number:**
   - is date-stamped;
   - keeps its derivation (query, period, n);
   - states its attribution caveat (what else changed);
   - respects any threshold the owner set: e.g. "publish only after n stores", and as *those stores'* result, not a general rate.
6. **Platform review rules beat Hormozi's incentive tips.** Never offer incentives for platform/marketplace reviews. Never sentiment-gate (ask only happy customers). Ask everyone the same way. Incentives are allowed only for owned proof (case-study time, interviews) and must be disclosed. Check each platform's terms (research them).
7. **Score proof assets on the 13 rules.** Each planned asset gets a quick score (how many rules it ticks), and the plan pushes toward live / raw / show / others-saying / identical-to-them / numbers. The strongest proof is **the prospect's own result before they buy** (e.g. the trial's own data), so design for that first.
8. **Risk reversal with boundaries** (framework §Risk-free guarantees, contract item 8). The guarantee must be executable on the platform's billing. Write its conditions and its abuse limits down. It must be consistent with `04`. **Proof owns the risk-reversal choice** (type, conditions, boundaries); `gtm-engine:pricing` (`07`) then sets the commercial terms of any pilot or guarantee consistent with it. Where the risk reversal needs an entry offer, take the offer idea from `03`/`04` and leave its price to pricing — say so in the artifact.
9. **Read the product's own published privacy policy and terms before designing any harvest.** Retention promises, legal bases claimed, and processor/controller roles. Never propose keeping data longer than the policy says. Copy only minimal fields into purpose-built tables.
10. **Pilots that produce a number must be pre-registered and honest about power.**
    - Specify the assignment exactly (hash, encoding, merchant-visible key), the outcome classes and cut-off, a single look, and the interval method.
    - **Simulate P(positive) at plausible effects** and state it before signing.
    - Never share unblinded interim arm results.
    - Decouple any customer commitment from statistical significance.
    - Recruit only stores whose own data can show the outcome (a gate).
11. **Ask for reviews independent of outcomes**, including pilot customers (ask at the end regardless of result). Disclose material connections.
12. **Verification and compliance** (framework [3]): who checks a number before it ships; legal limits on comparative or performance claims in the market; data-protection rules for customer data in proof.

## Procedure

### 1. Map the claims (framework [1])
From `05` pillars, the `04` only-ness and risk reversal, and the claims register: one row each.

### 2. Research (deep step ①)
Small `gtm-engine:researcher` briefs that save as they go:
- **Platform review and testimonial rules:** incentives, prompting, display of reviews, responding to reviews.
- **Local rules on performance and comparative claims, and on using customer data or names in marketing** (e.g. consumer-protection, advertising and data-protection law).
- **How proof is displayed in the category:** what competitors show (reviews, counts, logos, case studies); what third-party verification exists (badges, platform certifications, awards).

### 3. Harvest plan (framework [2]), across all five source categories
1. product data;
2. customer conversations;
3. reviews;
4. third parties;
5. internal ops.

Each with its hook, cadence and owner. For pre-proof products, include **the measurement experiment** that produces the first publishable number (e.g. a holdout or pilot protocol), consistent with the `03` PMF plan and the `04` validation plan.

### 4. Consent and verification (framework [3], rules 4–5, 9)

### 5. Packaging matrix: persona × stage, nine cells (framework [4])
Cells may be "none yet → risk reversal / trial result" where proof doesn't exist.

### 6. Distribution (framework [5])
Website / listing · sales or outreach · onboarding / in-product · partners · procurement (or "n/a" with the reason).

### 7. Measurement (framework [6])
Does proof move conversion? Which metric, and from which source.

### 8. Risk reversal (rule 8)

### 9. Judgement (deep step ③)
Send `gtm-engine:strategist` the grid, harvest plan, matrix and risk reversal. Ask for:
- the **first proof to generate** and the fastest honest path to it;
- the pilot / measurement design;
- the risk-reversal choice;
- what to say **while there is no proof**;
- what would flip each call.

### 10. Attack (deep step ④)
Send `gtm-engine:evidence-auditor` the grid, the hooks (are they real in the product?), the consent design, the pilot protocol (will it produce an attributable number?), the review-request script (platform-compliant?) and the risk-reversal terms. Fix each finding, or carry it into Open questions.

### 11. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `06_claims-evidence-grid.csv` | One row per pillar, only-ness and risk reversal: claim, proof type, format, source, hook, owner, status, 13-rule score, register-status upgrade | Running the proof backlog; the coherence audit's trace 4 |
| `06_harvest-and-instrumentation.md` | Every hook specified (event, field or table; CRM field; asset ID scheme; cadence; owner), plus the code changes it needs | Getting capture live before the first customer |
| `06_pilot-protocol.md` | The experiment that produces the first publishable number: design (e.g. holdout), sample, duration, metric, attribution guard, threshold, data handling, what may be published and how | Turning the first stores into honest proof |
| `06_consent-form.md` | Three-level consent in the market language, with what each level allows and how to withdraw | Before any quote, logo or case study |
| `06_proof-interview-script.md` | Post-result interview (Hormozi rule 7 probes; capture rules: verbatim, consent, numbers with source) + the case-study template (situation → action → result, with derivation) | Producing case studies |
| `06_review-request.md` | Platform-compliant review-request copy and timing (same ask for everyone, no incentive), in the market language, linted | Growing reviews without breaking platform rules |
| `06_proof-tracker.csv` | Asset ID, type, customer (anon label), consent level, date, number + derivation, where used, "proof used?" | The library, and its measurement |

### 12. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-engine:pricing` (Pillar 6).

## Checks before presenting (framework output contract)
- [ ] Grid: one row per pillar + only-ness + risk reversal; each with type, format, owner, status
- [ ] Harvest plan across all five source categories with hooks specified concretely; code changes filed
- [ ] Consent: three levels, recorded per customer in the tracker
- [ ] Every number rule: date, derivation, attribution caveat, the owner's thresholds respected
- [ ] Packaging matrix: persona × stage, nine cells
- [ ] Distribution assignments across all five destinations (or n/a with reason)
- [ ] Instrumentation specified before assets ship (asset IDs, "proof used?" field)
- [ ] Risk reversal chosen, executable on the platform, with boundaries
- [ ] No pricing dependency: any entry offer comes from `03`/`04`, its price is left to `gtm-engine:pricing`
- [ ] No fabricated proof: no example testimonials, sample numbers or placeholder logos
- [ ] Review requests platform-compliant (no incentives, no sentiment-gating); copy linted
- [ ] All assets written

Playbook "Pillar 5 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it):
- [ ] The claims → evidence grid is filled: 2–3 provable claims per message pillar, each with an owner
- [ ] Every number is date-stamped and could be checked by a skeptical CFO
- [ ] Consent is recorded for each client at one of the three levels
- [ ] Proof fields are in the onboarding and offboarding forms, and the CRM dashboard is saved
- [ ] One proof format is ready per persona and stage
- [ ] Risk reversal is chosen, with success defined and conditions set
- [ ] A "proof used?" checkbox is on every CRM stage change
