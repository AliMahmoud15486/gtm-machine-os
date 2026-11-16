# Phase 2 — Execution

**Status: SKILLS BUILT 2026-11-15** — six skills, none yet run on a product
**Pillars:** 7–12
**Prerequisite:** the Phase 1 coherence audit for that product, with any verdict but FAIL (protocol §3).

Answers: *How does pipeline actually get generated and converted, and how do we know it's working?*

## Skills (run in this order)

**Orchestrator:** `gtm-machine-os:execution` runs these six in order, at the depth `09` sets for each, then the Phase 2 cross-check → `15_Execution-Audit.md` (the Phase 2 gate) and a 30/60/90 execution plan.

| Run | Pillar | Skill | Artifact | Method |
|---|---|---|---|---|
| 1 | 8 Motion | `gtm-machine-os:motion` | `09_GTM-Motion-and-Routes-to-Market.md` | `Frameworks/08`, `09` §1/§4, `13` ch.7–8 |
| 2 | 10 Revenue process | `gtm-machine-os:revenue-process` | `10_Revenue-Process-and-SLAs.md` | `Frameworks/09`, `10` |
| 3 | 7 Demand gen | `gtm-machine-os:demand-gen` | `11_Demand-Generation.md` | `Frameworks/10`, `13` ch.7, `05` |
| 4 | 9 Outbound | `gtm-machine-os:outbound` (+ `lead-research`) | `12_Outbound.md`, `leads/` | `Frameworks/14`, `09` [1], `13` ch.7 |
| 5 | 11 Enablement | `gtm-machine-os:enablement` | `13_Enablement.md` | `Frameworks/12` §3/§5, `13` ch.8, `09` [6]/[8] |
| 6 | 12 Metrics | `gtm-machine-os:metrics` | `14_Metrics-and-Feedback.md` | `Frameworks/12` §4, `13` ch.1/4/8 |

Every skill reads the Business Profile first, writes specs and drafts only (it never sends, spends,
publishes or configures tools), and updates the project's `00_Playbook-Tracker.md`. Map:
`Playbook/SPINE.md`. Where method comes only from the playbook (course decks not in the library),
skills cite `Playbook/GTM-Playbook.md` and say so.

## Why Phase 2 waits for the Phase 1 gate

Execution without locked strategy produces activity, not pipeline. Specifically:

- Outbound sequences need the message pillars from Pillar 4 and proof lines from Pillar 5
- Channel selection is already decided in Pillar 4 — Phase 2 executes that choice, it doesn't remake it
- Demand-gen campaigns need the ICP and trigger fit from Pillar 2 to target anything
- Pillar 12's KPIs are the leading/lagging indicators already specified in the positioning and
  messaging frameworks — they get instrumented here, not invented here

## What already exists elsewhere

`Frameworks/04_Positioning.md` and `05_Messaging-and-Channels.md` already carry the measurement
sections (leading/lagging metrics, messaging diagnostics, channel primary metrics). Pillar 12
will consolidate and instrument these rather than starting fresh.

`Frameworks/06_Proof-System.md` §5 already specifies the distribution playbook across website,
sales, outbound, partners, and procurement. Pillars 7–9 execute against it.

## Still open

1. Run the six skills on one real product and fix what that run exposes (none has run yet).
2. Add the missing course decks to `Learning_resources/` (see the roadmap's source-file notes).
3. Remaining source gaps, each declared in its skill: outreach legal limits per country, sending
   infrastructure numbers, SLA targets, campaign calendar / content ops, training and comp design,
   and marketplace / transaction businesses in pillars 6–12.
