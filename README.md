# GTM Engine

A Claude Code plugin that runs go-to-market for any B2B product. It covers discovery, 12 strategy
and execution pillars and two consistency gates. Every claim carries its evidence, an adversarial
auditor attacks every draft, and only a human can lock a decision.

This is the **engine**: skills, sub-agents, the shared protocol, gates, templates and the Business
Profile. The method behind each pillar is a **slot**: each one keeps the output contract and leaves
room for your own playbook. The case study of how it was built:
[theglocalpm.com/case-study-gtm-machine.html](https://theglocalpm.com/case-study-gtm-machine.html).

## Why

AI writes a convincing GTM strategy in minutes. Nobody can tell afterwards which parts were known
and which were guessed, and documents written in isolation contradict each other. The engine is
built around that:

- **Evidence tags** on every claim: `VALIDATED`, `RESEARCHED` or `ASSUMED`.
- **No invented customer language.** No interviews means the document says so.
- **The AI proposes, a human locks.** Decisions ship as `PROPOSED` with the options that lost.
- **An adversarial auditor** returns *survives*, *weakened* or *refuted* for each claim.
- **Two gates.** A coherence audit after strategy; a cross-check after execution.
- **Drafts only.** Nothing is sent, spent, published or configured by the engine.

## How it runs

```
0 Discovery + Business Profile
  → 1 Segmentation → 2 ICP & buying center → 3 Value prop & positioning → 4 Messaging
  → 5 Proof → 6 Pricing → Gate 1: coherence audit
  → 8 Motion → 10 Revenue process → 7 Demand gen → 9 Outbound → 11 Enablement → 12 Metrics
  → Gate 2: execution cross-check → metrics loop back to 1–3
```

**Business Profile first.** Discovery records nine fields: business type, revenue model (retainer,
project, subscription …), deal size, how buyers buy, stage, GTM maturity, markets, capacity and,
for client work, the engagement. No pillar runs while the first five are unknown, and each pillar
applies the defaults the profile sets (`Playbook/SPINE.md`). For example, a pre-PMF business gets
an early customer profile instead of an ICP.

**Each project has a tracker** (`products/<slug>/00_Playbook-Tracker.md`): status per pillar and a
"done when" checklist. A box ticks only with a pointer to the section that proves it, and real-world
steps ("built", "live", "signed") tick only on the owner's dated confirmation.

## Skills

| Step | Skill | Writes |
|---|---|---|
| 0 | `gtm-engine:discovery` | `00_Discovery.md`, `00_Intake.md`, tracker |
| Phase 1 | `gtm-engine:strategy` runs `segmentation`, `icp`, `personas`, `value-prop`, `positioning`, `messaging`, `proof`, `pricing` | `01`–`07` |
| Gate 1 | `gtm-engine:coherence-audit` | `08` |
| Phase 2 | `gtm-engine:execution` runs `motion`, `revenue-process`, `demand-gen`, `outbound` (+ `lead-research`), `enablement`, `metrics` | `09`–`14`, `leads/` |
| Gate 2 | the execution cross-check (inside `execution`) | `15` |

Sub-agents: `researcher` (finds facts, never concludes), `strategist` (makes the call, shows what
lost) and `evidence-auditor` (attacks the draft from a skeptical-CFO stance).

## Install

Requires [Claude Code](https://claude.com/claude-code).

```bash
git clone https://github.com/AliMahmoud15486/gtm-engine.git ~/.claude/skills/gtm-engine
```

Restart Claude Code, then run `/gtm-engine` to see the skill map. Start with plain language:

```
Start GTM for Acme
What's the next GTM step for Acme?
Run Phase 2 for Acme
```

Product workspaces are created under `products/<slug>/` in the plugin folder and are git-ignored.

Optional: Python 3 for the copy linter (`skills/messaging/copy-lint.py`) and the storefront
scanner (`skills/lead-research/scripts/storefront_scan.py`), and an Apollo connection for account
searches. Paid lookups state their cost and wait for approval.

## Bring your own method

Each file in `Frameworks/` is a slot with the pillar's output contract. Write your method above
the contract, or run on the contracts alone: the skills meet the contract and mark their method
choices `ASSUMED`. Some skills mention sections or sources from the author's private method files;
where those are missing, the contract is what counts.

## Status

The strategy pillars have been run on real products. The execution pillars are new and haven't run
on a product yet. Gates are checks, not measured evals: no catch rate is claimed.

## License

MIT. See `LICENSE`.
