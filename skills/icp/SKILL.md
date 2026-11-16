---
name: icp
description: GTM Pillar 2a — Ideal Customer Profile for any product, built inside the beachhead chosen in Pillar 1. Generates 2–4 candidate ICPs, locks weights before scoring, scores all six fit dimensions, picks one, writes the ICP statement, a unit-economics anti-ICP, trigger signals and a validation plan. Switches to an Early Customer Profile (ECP) for pre-PMF products. Deep by default (researcher → strategist → evidence auditor). Produces 02_ICP.md plus usable assets (scorecard, Apollo/Sales Navigator filters, real target-account list, qualification checklist). Trigger with "build the ICP for X", "ideal customer profile for X", "who should X sell to", "early customer profile for X", "anti-ICP for X", "GTM pillar 2 for X".
version: 1.0.0
---

# GTM ICP — Pillar 2a

**Answers:** *which companies, inside the beachhead, are the best fit — and which are not?*
ICP = **company**. The humans inside it are `gtm-machine-os:personas` (Pillar 2b). Keep them apart.

## Before anything

Follow the shared protocol — it is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/02_ICP-and-Buying-Center.md` — ICP sections only (through "Picking the first ICP accounts") + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **Chapter 3** (ECP vs ICP, assumption mapping, confidence ladder, Campbell anti-persona) |
| **Upstream** | `00_Intake.md` · `01_Segmentation.md` (beachhead + not-now list) |
| **Writes** | `products/<slug>/02_ICP.md` · `products/<slug>/assets/02_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `02b` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 2 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `01_Segmentation.md` is missing, **stop** and offer `gtm-machine-os:segmentation` (protocol §3). A legacy
`02_ICP-and-Buying-Center.md` is read as input; once `02_ICP.md` is written, add a line at the top
of the legacy file: `Superseded for ICP by 02_ICP.md (YYYY-MM-DD)`.

## Procedure

### 1. ICP or ECP?
Read intake §2 stage. **Idea / prototype / pre-revenue / early revenue pre-PMF → ECP mode**
(Framework 02 "earn your ICP" ladder; Voje ch.3). In ECP mode the target is *who you can address,
serve and monetise in the next one or two quarters* — early-adopter mindset, self-onboarding,
generous feedback, willing to endorse — and the artifact title says **Early Customer Profile**.
Scaling products → ICP mode. State the mode and why in the first paragraph.

### 2. Mine what exists
If there are real customers: pull the top 10–20 by revenue, margin, retention, expansion (framework
step 1) and look for shared attributes. Those patterns are `VALIDATED`. If there are none, say so
and move on — do not simulate a customer base.

### 3. Research — deep step ①
Launch `gtm-machine-os:researcher` in the background with:
- **Trigger brief:** observable events that precede buying in this category, and how each is
  detected (job posts, funding, tool migration, regulation, leadership change) with a tool or
  source per trigger.
- **Technographic / operational brief:** what stack ICP companies run, how to detect it
  (BuiltWith, app marketplaces), integration prerequisites.
- **Buyer-language brief:** public verbatim descriptions of the problem from the beachhead
  (reviews, forums, communities), with links. Report absence honestly.
- **Account brief:** 10–20 **real** companies matching the beachhead definition, with URL, size,
  geography, and the evidence they fit. **Run as its own small brief** (≤40 checks, save as you
  go). For every list *method* proposed (e.g. "reviewers of app X"), measure its yield on a
  sample of ≥20 — `PASS n / checked N` — before the artifact relies on it (protocol §7). These seed the "dream 10" (framework "easiest to get into"
  rule: urgent need · early-adopter mindset · money to spend · existing relationship).

### 4. Candidates and weights
Generate **2–4 candidate ICPs** inside the beachhead. Then **write the weights before any score**
— start from the source weights (Firmographics 20 · Size 10 · Trigger 20 · Problem 25 · Economic
15 · Cultural 10) and adjust only against the stated purpose of the run (intake §6). Every change
from source gets a one-line reason. State the scale (1–5).

### 5. Score all six dimensions — every candidate
Firmographic · problem · trigger · operational · economic · cultural. Dimensions 4–6 are not
optional; they predict churn. Each cell: score, reason, tag. Choose the winner. Close totals
(within ~0.3) go to the strategist as a genuine tie.

### 6. Judgement — deep step ③
Send `gtm-machine-os:strategist` the weights, the scored table and the research. Ask for: the ICP (one),
the losers and why, **the anti-ICP**, and what would flip the choice.

### 7. Go deep on the winner only
- **ICP statement** — framework template, every bracket filled.
- **Six dimensions in full**, each tagged.
- **Anti-ICP** — disqualifying traits **and** a unit-economics test (Campbell): eagerness to buy is
  not fit. Name who looks keen but would cost more to acquire and serve than they return
  (heavy discounting, custom work, low NPS, wrong value metric).
- **Triggers** — each with its detection method and tool.
- **Assumption map** — known/unknown × important/unimportant; the important-unknown quadrant is
  the validation backlog. *"Do they know they have the problem?"* is tested first.
- **Validation status** — which of the framework's four validation steps have actually run.

### 8. Attack — deep step ④
Send `gtm-machine-os:evidence-auditor` the winning scores, the anti-ICP, the trigger claims, **every company
in the target-account list (spot-check it exists and fits)**, and the strategist's ICP choice. Fix
or carry every non-surviving claim into Open questions. If the audit undermines the chosen ICP,
present Option A / Option B per protocol §5 ④b.

### 9. Assets
Research reports and raw pulls go to `products/<slug>/research/` (protocol §5). Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `02_icp-scorecard.csv` | weights row + one row per candidate, six scores, weighted total, tags | re-scoring as evidence lands |
| `02_account-qualifier.md` | a yes/no checklist a person can run on any account in 2 minutes: must-haves, disqualifiers (anti-ICP), trigger present?, score threshold | qualifying inbound leads and outbound lists |
| `02_search-filters.md` | the ICP translated into **Apollo** filters and **LinkedIn Sales Navigator** filters (industry, headcount band, geography, technologies, keywords, job-posting signals) plus exclusion filters from the anti-ICP | building the first list today |
| `02_target-accounts.csv` | real companies only: name, URL, why they fit (dimension by dimension), trigger observed + date, source, tag, qualifier result | the first outreach list / dream 10 |

**Apollo, optional:** if the Apollo tools are connected, offer to run the filters to (a) count
the addressable accounts — this answers framework validation step 3, "does the segment exist at
usable size?" — and (b) enrich `02_target-accounts.csv`. State the credit cost first and wait for
a yes. Never create contacts or sequences.

### 10. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-machine-os:personas` (buying center + personas).

## Checks before presenting (framework output contract, ICP items)
- [ ] Mode stated (ICP / ECP) with reason
- [ ] Weights written before scores; changes from source justified; scale stated
- [ ] 2–4 candidates, all six dimensions scored for each
- [ ] ICP statement has no brackets left
- [ ] Anti-ICP present, including the unit-economics test
- [ ] Every trigger has a detection method
- [ ] Validation status line: which of the four steps have run
- [ ] Target accounts are real and sourced — zero invented companies
- [ ] Every list method shows a measured yield (`PASS n / checked N`); no pool from multiplied borrowed rates
- [ ] All four assets written

Playbook "Pillar 2 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it; the buying-center box belongs to `gtm-machine-os:personas`):
- [ ] The 10–20 best customers are pulled and 5–10 champions interviewed
- [ ] Candidate ICPs pass the operational-fit filter and are scored on the six dimensions
- [ ] The ICP statement is written from the template
- [ ] The anti-ICP is written
- [ ] The ICP is validated: account count in Sales Navigator or Apollo, and one micro-campaign
