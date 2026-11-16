---
name: execution
description: Run Phase 2 (Execution) of the GTM Machine OS for a product — the orchestrator over the six execution skills, in run order — GTM motion (pillar 8), revenue process & SLAs (10), demand generation (7), outbound (9, with lead-research for the lists), enablement (11) and metrics (12) — then the Phase 2 cross-check that proves the six fit together (motion scope, hand-offs, capacity, message and offer fidelity, metric coverage, legal gates, tracker truth). Reads the Business Profile and the motion's downstream scope to decide how deep each pillar goes (full, light, through partners, not now). Step-addressable, so one pillar can be re-run without redoing the chain. Produces the six Phase 2 artifacts (09–14) via their skills plus 15_Execution-Audit.md and a one-page execution plan. Specs and drafts only — never sends, spends, publishes or configures tools. Trigger with "run Phase 2 for X", "run execution for X", "run the GTM execution chain for X", "GTM Phase 2", "what's next after the strategy for X", or after a Phase 1 coherence audit passes.
version: 1.0.0
---

# GTM Execution — Phase 2 engine

**Answers:** *how does pipeline actually get generated and converted for this product, and do the
six execution plans fit together?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Map** | `GTM_ROOT/Playbook/SPINE.md` (pillar → framework → skill → artifact, run order, Business Profile defaults) · `GTM_ROOT/Phase2_Execution/README.md` |
| **Reads** | `00_Discovery.md` §0 Business Profile · `00_Playbook-Tracker.md` · `08_Coherence-Audit.md` (verdict) · every Phase 2 artifact that exists |
| **Runs** | `gtm-machine-os:motion` → `gtm-machine-os:revenue-process` → `gtm-machine-os:demand-gen` → `gtm-machine-os:outbound` (+ `gtm-machine-os:lead-research`) → `gtm-machine-os:enablement` → `gtm-machine-os:metrics` |
| **Writes** | `products/<slug>/15_Execution-Audit.md` · `assets/15_*` · the tracker's Phase 2 gate row |
| **Template** | `template.md` in this skill's folder (for `15_Execution-Audit.md`) |

## Gate (stop and say why)

1. **Profile.** `00_Discovery.md` missing, or Business Profile P1–P5 unknown → stop (protocol §3).
2. **Phase 1.** `08_Coherence-Audit.md` missing or **FAIL** → stop, offer `gtm-machine-os:coherence-audit`.
   PASS-WITH-GAPS → proceed, and carry its open gaps into every step's header.
3. **Staleness.** Any of `01`–`07` STALE → stop, name the skill to re-run first.
4. **Unlocked upstream.** Phase 1 decisions still PROPOSED → proceed only if the owner says so, and every
   Phase 2 artifact states "built on unlocked upstream" (protocol §3).

## Rules

1. **Orchestrate, don't duplicate.** Every step is a skill. Invoke it; never run a pillar inline.
   This skill sequences, scopes, checks the seams between pillars, and reports.
2. **The motion sets the depth.** After step 1, read `09_GTM-Motion-and-Routes-to-Market.md` and
   `assets/09_downstream-scope.md`. Each later pillar runs at the depth it names: *full*, *light*,
   *through partners* or *not now*. A *not now* pillar is skipped; its tracker row says
   `N/A — not now per 09 (<reason>)`, and its done-when boxes are marked N/A with that reason.
3. **One step, then the owner.** Default: run one skill, present it (protocol §8), wait. The owner may say
   "run straight through". Then run each skill to its draft, without waiting, and present them
   all together at the end. Never self-lock in either mode.
4. **Re-running a step** stales every later Phase 2 artifact (protocol §9) and this audit. Re-run
   only what changed. "Re-run outbound for X" is valid on its own.
5. **Lists before outbound.** If `leads/` is missing or older than the current `02`/`02b`, offer
   `gtm-machine-os:lead-research` before `gtm-machine-os:outbound`. Lead research spends credits only after
   the owner's yes.
6. **Nothing external.** No sends, sequences, contacts, ads, pages, automations, CRM or calendar
   changes, from any step. A step that would need one stops and names it as the owner's action.
7. **Seams are findings, not fixes.** The cross-check names each break with the file, the line and
   the skill that owns the fix. It doesn't edit `09`–`14` itself, except for a mechanical fix
   (a copied number) after the owner's go-ahead.

## The chain

| Step | Pillar | Skill | Artifact | Needs before it |
|---|---|---|---|---|
| 1 | 8 GTM Motion | `gtm-machine-os:motion` | `09_GTM-Motion-and-Routes-to-Market.md` | `08` not FAIL |
| 2 | 10 Revenue Process & SLAs | `gtm-machine-os:revenue-process` | `10_Revenue-Process-and-SLAs.md` | `09` |
| 3 | 7 Demand Generation | `gtm-machine-os:demand-gen` | `11_Demand-Generation.md` | `09`, and `10` (which runs first in this chain; demand-gen alone can draft without it, marked `ASSUMED`) |
| 4 | 9 Outbound | `gtm-machine-os:outbound` (lists: `gtm-machine-os:lead-research`) | `12_Outbound.md`, `leads/` | `09`, `10` |
| 5 | 11 Enablement | `gtm-machine-os:enablement` | `13_Enablement.md` | `09`, `10` (+ `11`, `12` if in scope) |
| 6 | 12 Metrics | `gtm-machine-os:metrics` | `14_Metrics-and-Feedback.md` | everything in scope |
| 7 | Gate | this skill — the cross-check below | `15_Execution-Audit.md` | `09`–`14` (or N/A by scope) |

## Step 7 — the Phase 2 cross-check

Run it in deep mode: one `gtm-machine-os:evidence-auditor` brief per two traces, in the background,
each saving as it goes (protocol §5). Meanwhile, do the fact sweep and the tracker check yourself.

**Fact sweep.** Every number or name that appears in more than one of `06`, `07` and `09`–`14` (and their
assets): prices, plan and offer names, pilot terms, SLA times, scoring bands, MQL/SQL definitions,
sequence lengths, volume caps, thresholds, owners. Every value that differs is a finding. The owner
is the upstream file in run order (`07` for a price, `10` for an SLA or a definition).

| # | Trace | Passes when |
|---|---|---|
| E1 | **Motion → scope** | `10`–`13` each run at the depth `09` set, and `14` measures the KPIs `09` named |
| E2 | **Hand-offs** | The `11` scoring hand-off band equals `10`'s MQL/SQL definition. `12` replies route into `10` stage 2. `11` nurture speed and `12` follow-up meet `10`'s SLAs |
| E3 | **Capacity** | Hours the SLAs, the sprint and outbound volume demand fit P8 and the roles named in `09`. Show the sum |
| E4 | **Message fidelity** | Every copy line in `11`/`12`/`13` assets traces to a `05` pillar. Proof lines come only from approved `06` evidence. `assets/05_copy-lint.py` passes |
| E5 | **Offer & price fidelity** | Offers, prices, tiers and pilot terms in `10`–`13` equal `07`. The risk reversal equals `06` |
| E6 | **Metric coverage** | Every threshold set in `03`–`13` appears in `14`'s KPI dictionary with an owner and an action. Every `14` metric has a source event or an instrumentation-gap row |
| E7 | **Legal & consent** | Each market in P7 has the same consent and legal position in `11`, `12` and `13`'s stack (DPA rows). Open legal gates are listed, not assumed cleared |
| E8 | **Tracker truth** | Statuses match the artifacts' status lines. No execution box ("built", "live", "signed", "warmed") is ticked without the owner's dated confirmation (protocol §10) |

**Verdict.**
- **PASS:** all traces pass and nothing is STALE.
- **PASS-WITH-GAPS:** the only breaks are declared SOURCE-GAPs or execution boxes waiting for the owner.
- **FAIL:** any E2, E4 or E5 break, a capacity overrun with no decision, or a STALE artifact.

Set the tracker's **Gate: Phase 2 execution** row and add the verdict to its decisions log.

## Assets (`products/<slug>/assets/`)

| File | What it is | Usable for |
|---|---|---|
| `15_trace-matrix.csv` | Trace, check, file:line, result, owner skill | Seeing every seam at once |
| `15_findings.csv` | Finding, severity, evidence, owning skill, fix | Re-running exactly the right skill |
| `15_fact-consistency.csv` | Fact, value per file, owner, status | Catching copied numbers that drifted |
| `15_execution-plan.md` | One page: first 30 / 60 / 90 days. Each pillar's first actions, owner, and the the owner-only actions (sends, spend, tool set-up) listed apart | Starting execution on Monday, or handing it to a client or team |

If the owner or the client wants a document, render `15_execution-plan.md` plus the verdict to PDF with
the `anthropic-skills:pdf` skill as `00_GTM-Execution-Plan.pdf`.

## Present

Per protocol §8, plus:
- the verdict;
- the breaks by owning skill;
- the hours the plan needs vs P8;
- the the owner-only actions in order (the first send, the first spend, the first tool set-up);
- when `14` says to review again.

Phase 2 is done when every in-scope artifact exists and satisfies its done-when list (execution boxes
excepted until confirmed), the cross-check is PASS or PASS-WITH-GAPS, and the owner has locked the
decisions. Then the loop is `gtm-machine-os:metrics`' review cadence, which can send the strategy back
to pillars 1–3.

## Checks before presenting
- [ ] Gate checked: profile, `08` verdict, no STALE upstream
- [ ] Motion scope read, and each later pillar run at its depth (or N/A with the reason in the tracker)
- [ ] Every step run by its skill, none inline
- [ ] Fact sweep across `06`, `07`, `09`–`14` done
- [ ] Traces E1–E8 each complete or explicitly blocked
- [ ] Verdict stated, with the rule that produced it
- [ ] Tracker: Phase 2 gate row set, decisions log updated, no unconfirmed execution box ticked
- [ ] `15_execution-plan.md` written, with the owner-only actions separated
