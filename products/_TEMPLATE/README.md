# Product workspace template

Copy this folder to `products/<slug>/` for each product. One product, one workspace, no
cross-contamination.

## Files the Phase 1 run creates

| File | Pillar | Framework it answers to |
|---|---|---|
| `00_Playbook-Tracker.md` | all | Where the project stands on all 12 playbook pillars, with their "done when" checklists. Every skill updates it at the end of a run. Map: `Playbook/SPINE.md` |
| `00_Discovery.md` | 0 | Step 0 fact base + §0 Business Profile — `gtm-engine:discovery` skill (run first) |
| `00_Intake.md` | — | filled by `gtm-engine:discovery`; the owner (or the client) confirms |
| `00b_Discovery-Call.md` | 0 | client mode only: the discovery-call script |
| `01_Segmentation.md` | 1 | `Frameworks/01_Segmentation-and-Targeting.md` — `gtm-engine:segmentation` skill |
| `02_ICP.md` | 2a | `Frameworks/02_ICP-and-Buying-Center.md` — `gtm-engine:icp` skill |
| `02b_Buying-Center-and-Personas.md` | 2b | `Frameworks/02_ICP-and-Buying-Center.md` — `gtm-engine:personas` skill |
| `assets/` | all | usable assets per pillar (`01_*.csv`, `02_*.md`, …) — see `Phase1_Strategy/SKILL-PROTOCOL.md` §7 |
| `03_Value-Proposition.md` | 3a | `Frameworks/03_Value-Proposition.md` — `gtm-engine:value-prop` skill |
| `04_Positioning.md` | 3b | `Frameworks/04_Positioning.md` — `gtm-engine:positioning` skill |
| `05_Messaging-and-Channels.md` | 4 | `Frameworks/05_Messaging-and-Channels.md` — `gtm-engine:messaging` skill |
| `06_Proof-System.md` | 5 | `Frameworks/06_Proof-System.md` — `gtm-engine:proof` skill |
| `07_Pricing-and-Packaging.md` | 6 | `Frameworks/07_Pricing-and-Packaging.md` — `gtm-engine:pricing` skill |
| `08_Coherence-Audit.md` | gate | run the `gtm-engine:coherence-audit` skill |

## Files the Phase 2 run creates (numbered in run order)

| File | Pillar | Framework it answers to |
|---|---|---|
| `09_GTM-Motion-and-Routes-to-Market.md` | 8 | `Frameworks/08_GTM-Motion-and-Routes-to-Market.md` — `gtm-engine:motion` |
| `10_Revenue-Process-and-SLAs.md` | 10 | `Frameworks/09_Sales-Led-Growth-and-Sales-Process.md` — `gtm-engine:revenue-process` |
| `11_Demand-Generation.md` | 7 | `Frameworks/10_Lead-Nurture.md`, `13` ch.7 — `gtm-engine:demand-gen` |
| `12_Outbound.md` + `leads/` | 9 | `Frameworks/14_Outbound-Prospecting-and-Outreach.md` — `gtm-engine:outbound`, `gtm-engine:lead-research` |
| `13_Enablement.md` | 11 | `Frameworks/12_…`, `13` ch.8 — `gtm-engine:enablement` |
| `14_Metrics-and-Feedback.md` | 12 | `Frameworks/12_…`, `13` — `gtm-engine:metrics` |
| `15_Execution-Audit.md` | gate | the Phase 2 cross-check — `gtm-engine:execution` (the Phase 2 orchestrator) |

Phase 2 needs the Phase 1 coherence audit (not FAIL). Full map: `Playbook/SPINE.md`.

## Required header on every artifact

```markdown
# <Pillar name> — <Product>

**Status:** DRAFT | PROPOSED | LOCKED | STALE
**Last updated:** YYYY-MM-DD
**Evidence base:** N VALIDATED / N RESEARCHED / N ASSUMED — ~X% assumed
**Profile:** <type · revenue model · ACV band · stage> → <the spine defaults applied, and any departure>
**Framework:** Frameworks/0X_....md
**Upstream:** <artifact> (<status>) · …
**Run:** deep — research ✓ · strategist ✓ · audit ✓ | fast
```

The authoritative header is `Phase1_Strategy/SKILL-PROTOCOL.md` §6; Phase 2 artifacts add a `**Phase 1 gate:**` line.

`STALE` is set automatically when an upstream pillar is re-run. A stale artifact blocks a
coherence-audit PASS.

## Evidence tags

Every factual claim carries exactly one:

- **`VALIDATED`** — from customer data or a real interview. Name the source.
- **`RESEARCHED`** — from an external source. Cite it with a date.
- **`ASSUMED`** — the owner's judgement or an inference. Say so plainly.

Untagged claims are defects. This is what makes the strategy auditable a year later, when nobody
remembers which parts were known and which were guessed.
