---
name: coherence-audit
description: The Phase 1 gate for any product. Audits the completed Phase 1 artifacts (01 segmentation, 02 ICP, 02b buying center & personas, 03 value proposition, 04 positioning, 05 messaging, 06 proof, 07 pricing) and their assets for internal contradiction. Runs seven traces (segment→ICP, pain→driver, driver→pillar, pillar→proof, persona coverage, category→pricing, only-ness→proof→alternatives), a cross-artifact fact-consistency sweep (prices, caps, names, category wording, thresholds repeated in several files), evidence ledger, fabricated-language scan, staleness and lock status, then issues PASS / PASS-WITH-GAPS / FAIL with named breaks and line-level fixes. Deep by default (parallel trace auditors → verification of every major/critical finding). Produces 08_Coherence-Audit.md plus usable assets (trace matrix, findings list, fact-consistency table, decision register, validation backlog) and one PDF strategy report: a section per pillar with the strategy, the owner's decisions and actions. Trigger with "coherence audit", "audit the GTM strategy", "check my GTM for gaps", "is my GTM consistent", "phase 1 gate", or as step 8 of gtm-machine-os:strategy.
version: 2.2.0
---

# GTM Coherence Audit — Phase 1 gate

Four excellent documents that contradict each other are worse than three mediocre ones that agree:
the contradiction only surfaces on a sales call, in front of a buyer.

Origin: the final prompt in the owner's `GTM Strategy Prompts.docx`, *"check each one of those elements
for any inconsistencies … and tell me if they would make a solid and consistent GTM Strategy or if
there're any gaps that need to be handled first."* Generalised to every Phase 1 artifact, with
explicit traces and a hard verdict.

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | This file. Framework output contracts at the bottom of each `GTM_ROOT/Frameworks/0*.md` (they define what each artifact owes) |
| **Reads** | `products/<slug>/00_Discovery.md` (§0 Business Profile) · `00_Intake.md` · `00_Playbook-Tracker.md` · `01_Segmentation.md` · `02_ICP.md` · `02b_Buying-Center-and-Personas.md` · `03_Value-Proposition.md` · `04_Positioning.md` · `05_Messaging-and-Channels.md` · `06_Proof-System.md` · `07_Pricing-and-Packaging.md` · **all of `assets/`** (copy, plan sheets, grids and CSVs are where contradictions hide) · `interviews/` (to trace any quote) |
| **Legacy files** | A file marked `Superseded … by …` is read only to check nothing still relies on its superseded content |
| **Writes** | `products/<slug>/08_Coherence-Audit.md` · `products/<slug>/assets/08_*` |
| **Downstream on re-run** | Stales nothing by itself; it is a check, not a decision. Phase 2 skills read the new verdict: a FAIL blocks them until fixed, and `15` is re-checked. |
| **Does not** | Edit any `01`–`07` artifact. Fixes are named here and applied by re-running the owning skill (or with the owner's go-ahead for a mechanical fix) |

If any of `01`–`07` is missing, stop and name the skill that produces it. Pricing (Pillar 6) has
been **sourced since 2026-09-12** (`Frameworks/07_Pricing-and-Packaging.md`), so trace 6 is a full
trace; treat a pillar as partial only if `00_GTM-Pillar-Roadmap.md` lists a live `SOURCE-GAP` for it.

## Procedure

### 1. Inventory
For each artifact: status (`PROPOSED` / `LOCKED` / `STALE`), date, the upstream date it was built
on, and which decisions inside it are LOCKED by the owner vs still PROPOSED. An artifact built on an
older upstream than the current one is **effectively stale** even if nobody marked it.

Then check `00_Playbook-Tracker.md` (create it per protocol §10 if missing):
- Each row's status must match the artifact's status line.
- Every ticked box in pillars 1–6 must point to where the artifact shows it. Spot-check at least
  one tick per pillar.
- Each unticked box in pillars 1–6 is a finding, owned by that pillar's skill.
- A tick with no pointer, or one the artifact doesn't support, is a finding, and you untick it in
  the tracker.

Also check the **Business Profile** (`00_Discovery.md` §0, defined in `Playbook/SPINE.md`):
- Every artifact's `**Profile:**` line must match it.
- Each pillar must apply the spine default for that profile, or record its departure as a
  decision.
- A pillar built for a different business type is a **major** finding. Examples: retainer pricing
  for a SaaS product, an ICP where the stage calls for an ECP, or a sales-led motion on a self-serve
  deal size.

PASS needs every pillar 1–6 box ticked or `N/A — <reason>`. After the verdict, set the tracker's
gate row and add the audit to its decisions log.

### 2. Fact-consistency sweep (before the traces)
Build a table of every fact that appears in more than one file: prices, plan names, caps, trial
terms, category wording, beachhead definition, proof thresholds, sender identity, product
behaviours, legal claims, dates. Grep each across `0*.md` and `assets/`. Every value that differs
between files is a finding; the owner is the newest LOCKED statement, else the newest artifact for
that pillar. Copy a customer would see (listing, templates, plan sheet, outreach) outranks
internal notes in severity.

### 3. The seven traces (deep step ④, in parallel)
Launch `gtm-machine-os:evidence-auditor` agents in the background, each with a **small brief that saves as
it goes** (protocol §5):
- **A:** traces 1–3
- **B:** traces 4 and 7
- **C:** traces 5–6 + the cross-cutting checks (awareness match, fabricated language, number discipline)

Each returns breaks with artifact + line + quoted text + proposed fix, and says when a trace
**completes**. While they run, do steps 1–2 and the evidence ledger yourself.

#### Trace 1: Segment → ICP containment
The ICP sits inside the chosen beachhead the sizing was built on.
**Break:** ICP firmographics outside every prioritised segment (invalidates SOM).

#### Trace 2: ICP pain → value driver
Every driver relieves a pain or creates a gain named in the ICP problem fit, the personas, or the
Value Proposition Canvas.
**Break:** a driver no stated pain motivates.

#### Trace 3: Value driver → message pillar (1:1)
Each driver becomes exactly one pillar; each pillar traces to exactly one driver. Check the
messaging matrix and the copy, not only the `05` headings.
**Break:** orphan pillar or orphan driver; copy claiming a driver the matrix doesn't carry.

#### Trace 4: Message pillar → proof
Every pillar has ≥1 row in `06_claims-evidence-grid.csv` with type, format, owner, status.
**Grade:** *missing* proof (credibility risk) vs *not yet harvested* (a plan). Also check no live
copy states a claim whose grid or claims-register status forbids it.

#### Trace 5: Persona coverage
Every veto holder and the primary user appear in the messaging matrix **and** the proof packaging
matrix, at the stage where they can block.
**Break:** a veto holder with no message or no proof.

#### Trace 6: Category → pricing → budget line
The frame of reference implies a budget line and price sensitivity; pricing sits inside it, and the
offer supports the category claim. Plan limits match what copy, listing and proof protocols assume. The
commercial terms of any pilot or guarantee in `07` match the risk reversal `06` chose.
**Break:** premium price against a price-sensitive frame; a category claim the offer can't back;
pricing that makes another artifact's promise impossible; pricing terms that change the `06` risk reversal.

#### Trace 7: Only-ness → proof → alternatives
The differentiation (a) survives "could a competitor claim this tomorrow?", (b) has a reason to
believe, (c) holds against do-nothing, DIY, generic vendor and point tool.
**Break:** unproven only-ness, or no scripted answer to do-nothing.

### 4. Cross-cutting checks
- **Evidence ledger.** Tag counts per artifact and overall, with the counting method. `ASSUMED` >
  60% caps the verdict at PASS-WITH-GAPS.
- **Fabricated customer language: critical.** Every quoted customer line traces to `interviews/` or
  a cited public source (URL / review id + date). Untraceable → critical, require removal.
- **Awareness match.** Copy aimed at an unaware persona educates before it sells.
- **Anti-ICP and anti-persona present.**
- **Number discipline.** Adjectives where a number is owed → `UNKNOWN — needs measurement`.
- **Staleness.** Any `STALE` or effectively stale artifact blocks PASS.
- **Open decisions.** Every `PROPOSED` decision still waiting on the owner. A Phase 1 whose load-bearing
  decisions (beachhead, ICP, category, price, proof threshold) are unlocked cannot PASS.
- **Repeated risks** (legal, platform, compliance) are counted once and owned by one artifact.

### 5. Verify the findings (deep step ④ again)
Send every **major or critical** finding to a fresh `gtm-machine-os:evidence-auditor` told to *refute* it:
re-read the cited line, check whether another artifact already resolves it. Drop findings that
don't survive. **Never invent a break to look thorough.**

### 6. Verdict

| Verdict | Meaning |
|---|---|
| **PASS** | All seven traces complete. No critical findings. Nothing STALE. Load-bearing decisions LOCKED. Evidence honest and adequate. Ready for Phase 2. |
| **PASS-WITH-GAPS** | Traces complete, or only non-critical breaks remain; evidence thin and/or decisions open. Safe to proceed **on stated assumptions**, with a named validation plan and decision list. The expected verdict pre-revenue; not a failure. |
| **FAIL** | A break that would produce contradictory statements to a buyer, a critical fabricated-language finding, or customer-visible copy that contradicts pricing or product truth. Name the break, the fix, and the step to re-run. |

### 7. Write
`products/<slug>/08_Coherence-Audit.md`, in this order:
1. **Verdict** + a one-paragraph rationale readable on its own.
2. **Trace table:** seven rows: trace, complete/break, detail.
3. **Findings**, most severe first: severity (critical/major/minor), artifact + line + quoted text,
   what breaks, the specific fix (*"re-run gtm-machine-os:messaging and drop pillar 4"*, not *"improve
   alignment"*), who acts (skill re-run / the owner / product owner).
4. **Fact-consistency summary** (full table in the asset).
5. **Evidence ledger**, overall and per artifact, with the counting method.
6. **Decisions waiting on the owner**, ranked by how much rests on each.
7. **Validation backlog**: what must be tested before spending money, ranked by dependency.
8. **What's genuinely solid.** An audit that only reports breaks trains people to ignore audits.

Assets in `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `08_trace-matrix.csv` | One row per link in each trace (e.g. driver → pillar → grid row → persona → stage): status, file:line | Re-checking after any re-run |
| `08_findings.csv` | id, severity, artifact, line, quoted text, break, fix, owner, status (open/fixed/won't fix) | Working the fix list to zero |
| `08_fact-consistency.csv` | fact, value per file, owner, consistent Y/N | Catching drift after every edit |
| `08_decision-register.md` | Every open PROPOSED decision across 01–07: question, options, recommendation, what it blocks, date raised | The owner deciding in one sitting |
| `08_validation-backlog.csv` | assumption, artifacts resting on it, test, sample, threshold, owner, date | Phase 2 planning |

**Final output: the GTM strategy report PDF** (`products/<slug>/00_GTM-Strategy-Report.pdf`), the whole Phase 1
strategy in one file for the owner to read, decide and act on. Template and builder live in
`products/<slug>/assets/report/` (copy from the last product that has them): `_SECTION-SPEC.md` (the per-section
contract), `_shell.html` (cover, contents, A strategy on a page, B actions this week, 09 audit, C tests, D reply
template) and `build.py` (assembles `NN_*.html` fragments, generates the reply template from the decision
cards, prints with headless Chrome: `python3 build.py <out.pdf>`).
- **One section per pillar:** 01 segmentation · 02 ICP · 03 personas · 04 value prop · 05 positioning ·
  06 messaging · 07 proof · 08 pricing, then 09 this audit. Each: the question → the answer → the strategy
  (tables) → key numbers with evidence tags → already decided by the owner → **decisions for the owner** (cards
  numbered as in `08_decision-register.md`, with recommendation, why, what lost, what it blocks, tick boxes) →
  **actions for the owner** → audit fixes for that pillar → risks.
- **Deep mode:** one general-purpose agent per two sections, each told to read `_SECTION-SPEC.md` and be faithful
  to the artifact (no new numbers, quotes or decisions). Then check: every register number appears as a card,
  every Arabic phrase is wrapped `<bdi dir="rtl" lang="ar">«…»</bdi>`, weekdays in dates are right, and look at
  the rendered pages before sending.
- Send it with SendUserFile. Nothing in it is LOCKED; it is a decision aid.

### 8. Present
Send the strategy report PDF to the owner (SendUserFile). Per protocol §8: verdict first, then the findings that matter, then decisions for the owner. Name the
re-runs in order. A re-run of any `01`–`07` makes this artifact `STALE`. On PASS or PASS-WITH-GAPS,
next is Phase 2: `gtm-machine-os:execution` (or `gtm-machine-os:motion` directly).

## Rules
- **Be honest, not harsh.** The purpose is a strategy that survives contact with a buyer.
- **Never invent a break.** If the traces complete, say so.
- **A thin evidence base is a finding, not a failure.** Pre-customer products get an honest ledger
  and a validation plan, not a demand for data that can't exist yet.
- **Point at the line.** A finding nobody can act on in five minutes is not finished.
- **Customer-visible beats internal.**
- **Don't self-lock and don't silently fix.** The audit names fixes; the owner decides; skills re-run.
