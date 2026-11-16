---
name: segmentation
description: GTM Pillar 1 — Market Segmentation & Targeting for any product. Sizes the market (TAM/SAM/SOM + early adopters with stated method), builds a multi-lens segmentation map, ranks 3–5 candidate segments, runs the Market-Problem Map, and proposes one beachhead plus an explicit "not now" list. Deep by default (researcher → strategist → evidence auditor). Produces 01_Segmentation.md plus usable assets (segment ranking CSV, market-sizing sheet, competitor list). Trigger with "segment the market for X", "segmentation for X", "where should X play", "pick a beachhead for X", "TAM SAM SOM for X", "GTM pillar 1 for X".
version: 1.0.0
---

# GTM Segmentation — Pillar 1

**Answers:** *where do we play — and where, explicitly, do we not?*
**The deliverable is a choice.** The arithmetic only exists to force it.

## Before anything

Follow the shared protocol — it is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

It covers `GTM_ROOT`, the contract, product resolution, the prerequisite gate, evidence tags,
deep-mode pipeline, artifact header, assets, locking and staleness. Below is only what is
specific to Pillar 1.

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/01_Segmentation-and-Targeting.md` (read in full — the output contract is at the bottom) + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **Chapter 2** (Segment Ranking Table, Market-Problem Map, beachhead thresholds, competitor types) |
| **Upstream** | `00_Intake.md` — must be filled (stage, evidence count, already-decided list, constraints) |
| **Writes** | `products/<slug>/01_Segmentation.md` · `products/<slug>/assets/01_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `02` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 1 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

## Procedure

### 1. Frame the universe
From intake and product docs: the market (category), the **vertical** and **horizontal** cuts
(framework Step 1), and the already-decided constraints that pre-shrink it (e.g. a locked
platform or geography). Locked constraints are inputs, not candidates to re-score.

### 2. Research — deep step ①
Launch `gtm-engine:researcher` with two briefs, **in parallel, in the background**:
- **Sizing brief:** top-down figures (report, year, region) **and** bottom-up population counts
  (number of companies matching each candidate segment × an ASP source). Ask for both methods
  per layer and the gap between them.
- **Landscape brief:** 3–10 competitors across Voje's four types (direct / indirect incl. DIY
  spreadsheet / replacement / aspirational), what segment each serves, and public demand signals
  per candidate segment (review volume, community size, job postings, search interest).

While it runs, draft steps 3–4 from intake and docs.

### 3. Segmentation map — ≥3 lenses
Use at least three of the five framework layers (firmographic, needs, behavioural,
technographic, trigger). If firmographics "don't compute" (all sizes get value), segment by JTBD /
pain / current alternative instead (Voje ch.2) and say why.

Define each candidate **three ways**: top-of-mind label · firmographic definition · JTBD.
Then the four-test gate — measurable / accessible / profitable / actionable. A candidate failing
any test is cut here, with the reason recorded.

### 4. Size it — TAM / SAM / SOM / early adopters
- State **method and assumptions** for every number. Show top-down and bottom-up; if they differ
  by >10×, say which you trust and why.
- SAM: apply the four constraints explicitly — language/localisation, legal/regulatory, pricing
  model, technical requirements.
- SOM: derive from capacity (for a solo founder: hours × conversion), then cross-check against
  the **1–5% of SAM** norm. Above 5% needs a written justification.
- Early adopters: the fourth layer — who is reachable *this quarter*.

### 5. Rank 3–5 candidates
**Segment Ranking Table** (Voje ch.2): fair chance · pain · pay · market size · growth, each
1–5, **simple average**. Every score gets a one-line reason and a tag. More than five candidates
→ cut before scoring; fewer than three → say why the space is that narrow.

### 6. Market-Problem Map
Top 2–5 segments × up to 5 problems. Cell = the problem **in the segment's own words** — only
from `VALIDATED` interviews or `RESEARCHED` public sources with links. **If no real language
exists, write the problem as `ASSUMED` in neutral words and leave the quote field empty.** Never
write a plausible quote. Score pain / ease of sale / ease of implementation 1–10 (drop the last if
there's no product). Name the **traction** winner and the **money** winner separately.

### 7. Judgement — deep step ③
Send `gtm-engine:strategist` the ranking table, the map, sizing, intake constraints. Ask for:
the **beachhead** (one), whether this cycle optimises for traction or money, the **adjacent
wave 2**, the **"not now" list** with the reason each lost, and what evidence would flip the
call. Check the beachhead against the must-haves: winnable in ≤18 months (B2B: ~100 companies,
30–50% won), high pain, budget exists, healthy surrounding market, word-of-mouth potential.

### 8. Attack — deep step ④
Send `gtm-engine:evidence-auditor` the sizing numbers, the ranking scores carrying the most weight,
**every quote in the Market-Problem Map (verify against the source, and check it is filed under
the right problem)**, and the strategist's beachhead recommendation. Attack the SOM penetration
assumption hardest. Fix or carry every non-surviving claim into Open questions. If the audit
undermines the beachhead, present Option A / Option B per protocol §5 ④b.

### 9. Assets
Research reports and raw pulls go to `products/<slug>/research/` (protocol §5). Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `01_segment-ranking.csv` | segment, 3-way definition, 5 scores, average, tag per score, rank, decision (beachhead / wave 2 / not now) | re-scoring as evidence lands; sharing |
| `01_market-sizing.csv` | layer, method, inputs, source, value, tag | the investor market slide; re-running with new inputs |
| `01_competitors.csv` | name, URL, type (direct/indirect/replacement/aspirational), segment served, public price, where they win, source date | Pillar 3b positioning input; quarterly refresh |
| `01_beachhead-brief.md` | one page: beachhead definition, why, how many companies, how to find them (search filters / directories / communities), the 18-month win target in numbers, the first test | hand to whoever starts prospecting |

### 10. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-engine:icp`.

## Checks before presenting (the framework's output contract)
- [ ] TAM/SAM/SOM each with method + assumptions + tag; SOM vs 1–5% norm addressed
- [ ] Map uses ≥3 lenses; every candidate passed or failed the four tests explicitly
- [ ] 3–5 candidates ranked with reasons; one beachhead; **"not now" list present**
- [ ] Market-Problem Map contains zero unsourced quotes
- [ ] Every number tagged; no adjective standing in for an unknown number
- [ ] All four assets written

Playbook "Pillar 1 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it):
- [ ] TAM, SAM and SOM are calculated, with the method written down
- [ ] Segments are described with at least three lenses, not industry alone
- [ ] Each candidate segment is checked as measurable, accessible, profitable and actionable
- [ ] A few target segments are chosen and ranked, and the rest are parked
- [ ] The choice is validated with data (CRM, LinkedIn, market research)
- [ ] The next review date is set, 6–12 months out
