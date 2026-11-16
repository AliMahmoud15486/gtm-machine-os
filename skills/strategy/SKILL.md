---
name: strategy
description: Run Phase 1 (Strategy) of the GTM Machine OS for a product — the six-pillar chain from market segmentation through ICP, buying center, value proposition, positioning, messaging, proof system, and pricing. Produces locked, evidence-tagged artifacts in products/<slug>/. Step-addressable, so a single pillar can be re-run without redoing the chain. Orchestrates the per-pillar skills (gtm-machine-os:segmentation, gtm-machine-os:icp, …) in order. Trigger with "run GTM strategy for X", "run the whole GTM chain for X", "GTM Phase 1".
version: 1.0.0
---

> **System root:** `GTM_ROOT = ~/.claude/skills/gtm-machine-os`. Every relative path in this file (`Frameworks/…`, `products/…`, `Learning_resources/…`) is under `GTM_ROOT` — use absolute paths, since the session may be running in another folder. Read `GTM_ROOT/CLAUDE.md` before working; it is not auto-loaded outside that folder.

# GTM Strategy — Phase 1 engine

Runs pillars 1–6 of the GTM Pillar Roadmap for one product. Generic by construction: the product
is a parameter, never baked into the framework.

> **Principle:** the deliverable is a *decision*, not a document. Every artifact this skill
> produces must be something a person could act on tomorrow, with the evidence behind it visible
> and the assumptions labelled as assumptions.

## Where things live

| Thing | Path |
|---|---|
| Framework canon (the "what") | `Frameworks/0X_*.md` |
| Pillar roadmap + phase mapping | `Frameworks/00_GTM-Pillar-Roadmap.md` |
| Product workspace | `products/<slug>/` |
| Workspace skeleton | `products/_TEMPLATE/` |
| Grep-able source text | `Learning_resources/_extracted/*.txt` (page-marked `--- p12 ---`) |
| Original sources | your own source library (not in this repo) |

**Never restate framework content inside a product artifact.** Cite the framework file. The canon
lives in one place so that improving it improves every past and future run.

## Non-negotiable rules

1. **Evidence tags on everything.** Every factual claim carries one of:
   `VALIDATED` (customer data or interview — name the source),
   `RESEARCHED` (external source — cite it),
   `ASSUMED` (the owner's judgement or inference — say so).
   An untagged claim is a defect. A strategy where >60% of claims are `ASSUMED` is a hypothesis,
   and the artifact header must say so.
2. **Never invent customer language.** If no interviews have been run, the Value Proposition
   Canvas is marked `ASSUMED — no customer interviews run` at the top. Do not synthesise
   plausible-sounding customer quotes. Ever.
3. **Honour source gaps.** Where a pillar's framework lists a `SOURCE-GAP`
   (`Frameworks/00_GTM-Pillar-Roadmap.md`, coverage table), mark that part `SOURCE-GAP` and its
   choices `ASSUMED`. Never fabricate a method and present it with the authority of a sourced one.
   (Pricing, Pillar 6, has been fully sourced since 2026-09-12: `Frameworks/07_Pricing-and-Packaging.md`.)
4. **Name the anti-ICP.** Every ICP artifact states who you will *not* serve. A strategy that
   excludes nobody has decided nothing.
5. **Numbers, not adjectives.** "Improves efficiency" fails review. "Cuts reporting time 50%,
   baseline 6h/week" passes. Where a number is unknown, write `UNKNOWN — needs measurement`
   rather than reaching for a qualitative hedge.
6. **the owner decides, the machine proposes.** Every locked decision (ICP choice, category choice,
   only-ness claim, price point) is proposed with reasoning and alternatives, and waits for
   the owner's confirmation before being marked `LOCKED`. Do not self-lock.

## Step 0 — Discovery, then intake

**Run `gtm-machine-os:discovery` first.** If `products/<slug>/00_Discovery.md` is missing, stop and
offer it; if it exists but its readiness is `NOT READY`, stop and show its ★ questions. Discovery
fills `00_Intake.md`; this step only confirms it with the owner. Every pillar cites `00_Discovery.md` and
`assets/00_fact-base.csv` instead of rediscovering the company.

The intake below is what discovery fills; use it as the checklist when confirming.


If `products/<slug>/` does not exist, copy `products/_TEMPLATE/` to it and fill
`00_Intake.md` first.

Ask only what you cannot infer from the repo. The owner's products already have substantial
documentation in the product's own docs folder — **read it before asking** (the paths are in
intake §3).

Intake captures: what the product is, what stage it's at, what customer evidence already exists
(real customers? interviews? usage data?), what's already been decided and is not up for
re-litigation, and what the GTM run is *for* (a launch, a pivot, a fundraise, a listing).

Then state the evidence base out loud: *"You have N customers, M interviews, K months of usage
data"* — because that number determines how much of this run is validated versus assumed, and
The owner should know that before reading a single artifact.

## The chain

Run in order. Each step consumes the last. Steps are individually invokable — "re-run step 3 for
<product>" is valid — but re-running a step invalidates every downstream artifact, which must be
re-marked `STALE` and re-audited.

| Step | Pillar | Framework | Artifact |
|---|---|---|---|
| 1 | Market Segmentation & Targeting | `01_Segmentation-and-Targeting.md` | `01_Segmentation.md` — **run the `gtm-machine-os:segmentation` skill** |
| 2a | ICP | `02_ICP-and-Buying-Center.md` | `02_ICP.md` — **run the `gtm-machine-os:icp` skill** |
| 2b | Buying Center & Personas | `02_ICP-and-Buying-Center.md` | `02b_Buying-Center-and-Personas.md` — **run the `gtm-machine-os:personas` skill** |
| 3 | Value Proposition | `03_Value-Proposition.md` | `03_Value-Proposition.md` — **run the `gtm-machine-os:value-prop` skill** |
| 4 | Positioning | `04_Positioning.md` | `04_Positioning.md` — **run the `gtm-machine-os:positioning` skill** |
| 5 | Messaging & Channels | `05_Messaging-and-Channels.md` | `05_Messaging-and-Channels.md` — **run the `gtm-machine-os:messaging` skill** |
| 6 | Proof System | `06_Proof-System.md` | `06_Proof-System.md` — **run the `gtm-machine-os:proof` skill** |
| 7 | Pricing & Packaging | `07_Pricing-and-Packaging.md` | `07_Pricing-and-Packaging.md` — **run the `gtm-machine-os:pricing` skill** |
| 8 | **Coherence audit** | — | `08_Coherence-Audit.md` — run `gtm-machine-os:coherence-audit` |

*(Artifact 06/07 numbering follows the pillar order — Proof is pillar 5, Pricing is pillar 6 (the
playbook order, decided by the owner 2026-11-15) — and now matches the framework files 06/07. Proof runs
before Pricing: it chooses the risk reversal; Pricing sets its commercial terms. The table above is
authoritative for which file feeds which.)*

## Per-pillar skills

Every step is a standalone skill that follows `GTM_ROOT/Phase1_Strategy/SKILL-PROTOCOL.md` (deep
by default, usable assets in `products/<slug>/assets/`, tracker update per §10). **Invoke the skill;
never run a step inline.** This orchestrator only sequences the skills, checks the gate, and reports.

## What every step does (inside its skill)

1. **Read the framework file.** It carries the method and the output contract.
2. **Gather inputs** — the prior artifacts, plus product docs elsewhere in the repo, plus
   external research where the framework calls for it.
3. **Draft against the output contract** at the bottom of the framework file. That contract is
   the definition of done. Check it item by item before presenting.
4. **Surface open questions.** Anything that would change the answer and that only the owner can
   resolve goes in an `## Open questions` section at the bottom of the artifact — not buried in
   chat, where it will be lost.
5. **Present the decisions for locking.** Summarise what the step decided, what it assumed, and
   what it could not determine. Wait for confirmation.

### Depth mode

**Deep is the default** (protocol §5). The owner can ask for fast mode at intake:

- **Fast**: a single pass, without the subagents. Good for a first draft or a small product. The
  header says so, and a fast-mode artifact can't be `LOCKED` until its auditor pass has run.
- **Deep**: delegate to this plugin's subagents (`gtm-machine-os:researcher`, `gtm-machine-os:strategist`, `gtm-machine-os:evidence-auditor`):
  - `gtm-machine-os:researcher` for competitor, market-size, and buyer-language research
  - `gtm-machine-os:evidence-auditor` to adversarially challenge every claim before it's locked
  - `gtm-machine-os:strategist` for the hard judgement calls (category choice, only-ness, segment tradeoffs)

  Deep mode costs more and is worth it for a product the owner is actually going to spend money on.

## Step-specific notes

**Step 1 — Segmentation.** The TAM/SAM/SOM arithmetic is not the deliverable; the *choice* is.
Force a "not now" list. For the owner's early-stage products, top-down TAM from industry reports will
usually be `RESEARCHED` at best — say so rather than dressing an estimate as a finding.

**Step 2 — ICP.** Run the six fit dimensions, all of them. Dimensions 4–6 (operational, economic,
cultural) are the ones normally skipped and the ones that predict churn. Where the owner has real
customers, mine them (step 1 of the framework's define-process). Where he doesn't, the ICP is a
hypothesis and gets labelled as one, with the validation plan attached.

**Step 3 — Value Proposition.** The feature → benefit → value driver table is where most of the
work happens. Be ruthless: 3–5 drivers maximum, each passing all five attribute tests. Build the
baseline-vs-target table even when the baselines are `UNKNOWN` — the gaps are the measurement
backlog.

**Step 4 — Positioning.** Apply the only-ness litmus test honestly: *"could a competitor claim
this tomorrow?"* Most first-draft claims fail. Record the failed attempts and why — that
reasoning is more useful than the survivor. Script all four alternatives including **do-nothing**
and **build-in-house**; for the owner's B2B SaaS products these are usually the real competition.

**Step 5 — Messaging.** Every persona × stage cell filled or explicitly marked deliberate-blank.
Each message pillar must trace to exactly one value driver from step 3. If a pillar has no
driver, either the pillar is decoration or step 3 missed a driver — resolve it, don't paper over.

**Step 6 — Proof System.** One row per message pillar in the Claims → Evidence grid, no
exceptions. Most of the owner's products are pre-proof; the honest output is a *harvesting plan* with
instrumentation hooks specified, not a library of assets that don't exist. Getting the
instrumentation in before the first customer is the entire value of running this early.

**Step 7 — Pricing.** The floor comes from real costs and the ceiling from the step 3 value drivers;
the price sits between them. Pricing reads Proof's risk-reversal choice and sets its commercial
terms (pilot fee, guarantee conditions). It does not re-choose the risk reversal.

**Step 8 — Coherence audit.** Invoke `gtm-machine-os:coherence-audit`. Phase 1 is not complete until it
passes. This is the step that catches the strategy being six good documents that contradict each
other.

## Completion

Phase 1 is done when all eight artifacts (`01`, `02`, `02b`, `03`–`07`) exist, each satisfies its output contract and its
done-when list in `00_Playbook-Tracker.md`, the coherence audit passes, and the owner has locked the
decisions. Update `00_Intake.md` and the tracker with the status and date. Then offer Phase 2:
`gtm-machine-os:execution`. Report: what was decided, what remains assumed, and what must be validated
before spending money on execution.
