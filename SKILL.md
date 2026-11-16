---
name: gtm-machine
description: Map of the GTM Machine OS plugin — which skill to run for which go-to-market job, in what order, and what each needs first. Use when the user asks "what GTM skills do I have", "where do I start with GTM for X", "what's the next GTM step for X", "show the GTM machine", "start GTM for a new product", or names the GTM Machine OS without a specific pillar. Routes to the right gtm-machine-os:* skill.
---

# GTM Machine OS — skill map

System root: `~/.claude/skills/gtm-machine-os` (read its `CLAUDE.md` first).
Shared rules for every pillar skill: `Phase1_Strategy/SKILL-PROTOCOL.md`. Artifacts live in `products/<slug>/`.

## Phase 1 — Strategy (run in this order; each needs the one before)

| # | Skill | Answers | Writes |
|---|---|---|---|
| 0 | `gtm-machine-os:discovery` | **Deep research on the company first:** product truth, public claims vs truth, legal pages, commercial facts, platforms, evidence count, risks, one ranked question bank | `00_Discovery.md`, `00_Intake.md`, `assets/00_*` |
| 0b | `gtm-machine-os:strategy` | Orchestrates the whole of Phase 1 (needs discovery); fast or deep mode | confirms `00_Intake.md` |
| 1 | `gtm-machine-os:segmentation` | Where do we play? Beachhead, sizing, not-now list | `01_*` |
| 2a | `gtm-machine-os:icp` | Which companies fit (ICP/ECP, anti-ICP, target accounts) | `02_*` |
| 2b | `gtm-machine-os:personas` | Which people decide, use, block | `02b_*` |
| 3a | `gtm-machine-os:value-prop` | Why they buy: drivers, ROI, category, **the value proposition statement** | `03_*` |
| 3b | `gtm-machine-os:positioning` | Why us vs alternatives; only-ness; battlecards | `04_*` |
| 4 | `gtm-machine-os:messaging` | What we say, where; copy kit, channels, message tests | `05_*` |
| 5 | `gtm-machine-os:proof` | Proof plan, harvest hooks, consent, pilot | `06_*` |
| 6 | `gtm-machine-os:pricing` | Price, packaging, unit economics, WTP | `07_*` |
| ✓ | `gtm-machine-os:coherence-audit` | The Phase 1 gate: traces, findings, decisions, **strategy report PDF** | `08_*`, `00_GTM-Strategy-Report.pdf` |

## Phase 2 — Execution (run in this order; needs the Phase 1 coherence audit, not FAIL)

**Orchestrator: `gtm-machine-os:execution`** runs the six skills below in order, at the depth the motion sets, then the Phase 2 cross-check (`15_Execution-Audit.md`).

| # | Skill | Answers | Writes |
|---|---|---|---|
| 8 | `gtm-machine-os:motion` | How we reach and sell: motion, routes to market, roles, and how much of 7/9/10 applies | `09_*` |
| 10 | `gtm-machine-os:revenue-process` | How deals move: stages + exit criteria, CRM pipeline, qualification, SLAs, scripts, marketing–sales contract | `10_*` |
| 7 | `gtm-machine-os:demand-gen` | How leads arrive: funnel map, two channels, lead magnet, nurture, scoring, funnel build + QA, 30-day sprint | `11_*` |
| 9 | `gtm-machine-os:outbound` | How we create meetings: legal gate, tiers, sequences, channel rules, sending spec, weekly dashboard | `12_*` |
| 9 | `gtm-machine-os:lead-research` | The lists outbound runs on: L1 companies · L2 people (contact routes) · L3 nurture | `leads/` |
| 11 | `gtm-machine-os:enablement` | What the team needs: toolkit index, checklist, stack, ROI calculator, proposal template, 30-day roll-out | `13_*` |
| 12 | `gtm-machine-os:metrics` | What works: KPI dictionary, dashboard, weekly scorecard, ICE backlog, review cadence, when to re-run 1–3 | `14_*` |
| ✓ | `gtm-machine-os:execution` | The Phase 2 gate: seams between 09–14 (scope, hand-offs, capacity, message/offer fidelity, metric coverage, legal), verdict, 30/60/90 execution plan | `15_*` |

Then Phase 3 (AI layer), not built.

## Agents (used by the skills in deep mode)

- `gtm-machine-os:researcher` — external facts, tagged and cited
- `gtm-machine-os:strategist` — the judgement calls, with the alternatives that lost
- `gtm-machine-os:evidence-auditor` — adversarial check before anything is locked

## The spine

The 12-pillar **Growth & GTM Playbook** (`Playbook/GTM-Playbook.md`) is the manual for any B2B
project. `Playbook/SPINE.md` maps each playbook pillar to its framework, its skill and its
artifact. Each project tracks itself in `products/<slug>/00_Playbook-Tracker.md`: status per
pillar plus the playbook's "done when" checklists. Every skill updates it (protocol §10).

**Business Profile first.** Discovery records what kind of business this is: type, revenue
model (retainer, project, subscription …), deal size, how they buy, stage, GTM maturity, markets,
capacity, and (for clients) our engagement. No pillar runs while P1–P5 are unknown (protocol
§3). Each pillar applies the defaults the profile sets (`SPINE.md`).

## How to route a request

1. Find the product slug (`products/<slug>/`). If none, or no `00_Discovery.md`, start with `gtm-machine-os:discovery`.
2. Read `products/<slug>/00_Playbook-Tracker.md` (fall back to the `00_Intake.md` run log if there is none). The next skill is the first pillar in the spine's run order that is `NOT STARTED` or `STALE`. Every pillar 1–12 has a skill. Phase 3 (the AI layer) is the only part not built.
3. A specific ask ("price X", "find leads for X") goes straight to that skill; it checks its own prerequisites.
