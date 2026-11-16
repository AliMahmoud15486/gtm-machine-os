# Pillar Skill Protocol

Every per-pillar skill (`gtm-engine:segmentation`, `gtm-engine:icp`, `gtm-engine:personas`, …) follows this protocol.
Skill files hold only what is specific to their pillar; everything shared lives here, once.

The skills are packaged as the private **`gtm-engine` plugin** in `~/.claude/skills/gtm-engine/`
(auto-loads, callable from any working folder as `gtm-engine:<skill>`;
agents as `gtm-engine:researcher` / `strategist` / `evidence-auditor`). The **system** stays in one place:

```
GTM_ROOT = ~/.claude/skills/gtm-engine
```

Always use absolute paths under `GTM_ROOT` — the session's working directory may be another
project entirely. The path contains spaces; quote it in every shell command.

---

## 1. Load the contract

Before anything else, read `GTM_ROOT/CLAUDE.md`. Its working rules (evidence tags, no fabricated
customer language, propose-never-lock, numbers-not-adjectives, cite by filename+page, staleness)
apply in full even when the session started in another folder, where that file is not
auto-loaded.

## 2. Resolve the product

- Product workspace: `GTM_ROOT/products/<slug>/`. Ask for the slug only if it can't be inferred.
- If the workspace doesn't exist: copy `GTM_ROOT/products/_TEMPLATE/` to it and fill
  `00_Intake.md` before running any pillar.
- **Read the product's own documentation first** (paths listed in intake §3, or the current
  working folder if the skill was invoked from inside the product's repo). Ask the owner only what the
  docs cannot answer.
- **Never write GTM artifacts into the product's repo.** Everything goes to
  `GTM_ROOT/products/<slug>/`.

## 3. Prerequisite gate

Each skill declares its upstream artifacts. Before running:

| Upstream state | Action |
|---|---|
| `00_Discovery.md` missing (any pillar) | **Stop.** Offer `gtm-engine:discovery`. Pillars cite its fact base instead of rediscovering the company. |
| Business Profile missing, or any of P1–P5 `UNKNOWN` (any pillar) | **Stop.** Ask only the missing fields, in one round, or offer to re-run discovery. A pillar run without knowing the business type, revenue model, deal size, how they buy and the stage produces generic output. |
| Missing | **Stop.** Say which skill must run first. Offer to run it. Do not quietly fill the gap inline. |
| `STALE` | Stop. Say it must be re-run or re-confirmed first. |
| `DRAFT` / `PROPOSED` | Proceed, but the header states *"built on unlocked upstream"* and the open-questions section repeats the upstream's unresolved decisions. |
| `LOCKED` | Proceed. |
| Phase 2 skill (`09`–`14`) and `08_Coherence-Audit.md` is missing or its verdict is **FAIL** | **Stop.** Phase 2 executes the strategy; it does not remake it. Offer `gtm-engine:coherence-audit`. PASS-WITH-GAPS proceeds, and the header repeats the open gaps. |

A legacy combined file (e.g. older `02_ICP-and-Buying-Center.md`) counts as upstream input for
whatever sections it contains.

**Apply the profile.** Read the Business Profile (`00_Discovery.md` §0, or `00_Intake.md` §2 for
older workspaces) before any other work. Look up the defaults it sets for your pillar in
`GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"). State them in the
artifact's header block, e.g. `**Profile:** services · retainer · ACV 18K · early revenue →
ECP, value-ladder pricing, hybrid motion`. Departing from a default is a `PROPOSED` decision,
with its reason. Use the profile's language in examples: a retainer business's "client" and
"monthly fee", a SaaS business's "account", "seat" and "trial". Don't borrow examples from a
different business type.

## 4. Evidence model

Every factual claim carries exactly one tag:

| Tag | Meaning | Grade |
|---|---|---|
| `VALIDATED` | Customer data, a real interview, or a real buying signal. Name the source. | Add the confidence grade `C=1–5` from `Frameworks/13` ch.3: interview 1 · survey 2 · solution test 2.5 · waitlist 3.5 · sign-ups 4 · co-creation 4.5 · presale 4.8 · MVP up to 5 |
| `RESEARCHED` | External source. Cite URL or file + page, and date. | Researcher's High / Medium / Low |
| `ASSUMED` | The owner's judgement or Claude's inference. Say which. | — |

Unknown numbers: `UNKNOWN — needs measurement`. Never an adjective in their place.
Count the tags for the header. If `ASSUMED` > 60%, the header says **hypothesis** in words.

## 5. Deep mode — the default

Every pillar skill runs deep unless the owner says "fast" for this run. Deep mode is a fixed pipeline:

```
 ① Research          gtm-engine:researcher (background, parallel where the skill names >1 brief)
        ↓
 ② Draft             inline — candidates, scoring, tables, against the framework's output contract
        ↓
 ③ Judgement         gtm-engine:strategist — makes the skill's named call, returns recommendation +
                     alternatives that lost + what would flip it
        ↓
 ④ Attack            gtm-engine:evidence-auditor — attacks the drafted claims AND the strategist's
                     recommendation; every REFUTED/WEAKENED verdict is either fixed or carried
                     into Open questions, never dropped
        ↓
 ④b Reconcile        if the audit undermines the strategist's call, do not quietly pick one —
                     present Option A (strategist) and Option B (post-audit) side by side,
                     what each rests on, the cheap test that separates them, and a
                     recommendation. The owner chooses.
        ↓
 ⑤ Assets            build the usable assets (§7)
        ↓
 ⑥ Present           summary for locking (§8)
```

Rules for the subagents:
- Pass them `GTM_ROOT`, the slug, the framework file path, and the upstream artifact paths in the
  prompt — they start with no context.
- The researcher returns findings; it never concludes. The strategist recommends; it never locks.
- **Persist the research.** Save each researcher report verbatim to
  `products/<slug>/research/YYYY-MM-DD_<NN>_<brief>.md`, tell the researcher to write raw pulls
  (API dumps, scraped tables) into `products/<slug>/research/raw/YYYY-MM-DD_<source>/` rather
  than a temp folder, and add a row to `products/<slug>/research/README.md`. A claim whose
  research only lived in a session transcript cannot be re-checked later.
- **Keep briefs small and save-as-you-go.** One brief = one question, capped (e.g. ≤40 stores,
  ≤3 tries per lookup). Tell the agent to create its report file first and append as it works,
  so a stalled agent leaves usable output. If an agent stalls, retry with a narrower brief that
  reuses whatever it already saved — never re-run the same large brief.
- **Late research goes to the auditor.** Any research file that lands after the draft is written
  is either folded into the draft before the audit, or named in the auditor's prompt as unused
  evidence to check the draft against.
- Strategist and auditor may run **in parallel** only when the auditor's scope excludes the
  judgement (e.g. sizing). The judgement itself is always attacked — send it to the same auditor
  as a follow-up if they ran in parallel.
- Record in the artifact which steps ran: `Deep run: research ✓ · strategist ✓ · audit ✓ (N
  claims: S survive / W weakened / R refuted)`.
- Fast mode skips ①③④ and says so in the header. A fast-mode artifact cannot be marked
  `LOCKED` until its auditor pass has run.

## 6. The decision artifact

Path: `GTM_ROOT/products/<slug>/<NN>_<Name>.md`. Required header:

```markdown
# <Pillar> — <Product>

**Status:** DRAFT | PROPOSED | LOCKED | STALE
**Last updated:** YYYY-MM-DD
**Evidence base:** N VALIDATED / N RESEARCHED / N ASSUMED — ~X% assumed
**Profile:** <type · revenue model · ACV band · stage> → <the spine defaults applied, and any departure>
**Framework:** Frameworks/0X_....md (+ Frameworks/13 ch.N)
**Upstream:** <artifact> (<status>) · …
**Run:** deep — research ✓ · strategist ✓ · audit ✓ | fast
```

Body follows the skill's template. Cite the framework, never restate it. Always ends with:
- `## Decisions for the owner` — each `PROPOSED`, with the alternatives that lost.
- `## Open questions` — anything only the owner can resolve, plus surviving auditor findings.
- `## Validation backlog` — what to test, how, success threshold, cheapest method first.

## 7. Usable assets — the "tomorrow morning" layer

The artifact is the decision. The assets are what you **do** with it. Each skill names its
assets; they live in `GTM_ROOT/products/<slug>/assets/` and are named `<NN>_<asset>.<ext>`.

Asset rules:
- An asset must be usable without reading the artifact: a CSV that imports, a filter set that
  pastes into Apollo / LinkedIn Sales Navigator, a script that can be read on a call.
- Assets carry the same evidence discipline. A company in a target-account list is a **real,
  researched company with a URL** — never a plausible invented name.
- **Measure a list before you size it.** Any pool or list a skill proposes ("~115 named stores",
  "the first outreach list") must first be run on a real sample (≥20 candidates): resolve each,
  apply the qualifier, and report the **measured pass rate**. A pool computed by multiplying
  borrowed rates is `ASSUMED` and may not be presented as a list. Report yields as
  `PASS n / checked N` next to every list.
- **Apollo** (if its tools are connected): searches can count and list real accounts. Before any
  call that spends credits, state the estimated cost and wait for the owner's yes. Never create
  contacts, sequences, or send anything from a strategy skill.

## 8. Present for locking

End the run with a short chat summary, not the document:
1. What was decided (each `PROPOSED`).
2. What it rests on — the evidence ratio, stated as a number.
3. The single weakest assumption, and the cheapest test for it.
4. The assets produced, with paths.
5. What runs next, and whether it's unblocked.

Then wait. Only the owner marks `LOCKED`. When he does, set the status, the date, and add a row to the
run log in `00_Intake.md`.

## 9. Staleness

Re-running a pillar marks every **downstream** artifact `STALE` (set the status line, add a
one-line reason with the date). Downstream order:

```
00 Discovery (incl. Business Profile — a change to P1–P5 is material) → 01 Segmentation → 02 ICP → 02b Buying Center & Personas → 03 Value Prop → 04 Positioning
  → 05 Messaging → 06 Proof → 07 Pricing → 08 Coherence Audit
  → 09 GTM Motion → 10 Revenue Process → 11 Demand Gen → 12 Outbound → 13 Enablement → 14 Metrics
  → 15 Execution Audit
```

Re-running any Phase 1 pillar also marks every Phase 2 artifact (`09`–`15`) `STALE`, because Phase 2
executes the Phase 1 decisions.

Staleness is mirrored in the playbook tracker (§10): every artifact set `STALE` also gets `STALE`
in `00_Playbook-Tracker.md`, and its done-when ticks are cleared.

## 10. Update the playbook tracker

Every project has `products/<slug>/00_Playbook-Tracker.md`, which records where it stands on the
12 playbook pillars. The map from pillar to skill to artifact is `GTM_ROOT/Playbook/SPINE.md`.
At the end of every run, before §8's summary:

1. **Create it if missing** by copying `GTM_ROOT/products/_TEMPLATE/00_Playbook-Tracker.md`.
   Replace `<Product>`, then set each row's status from the status line of any artifact that
   already exists.
2. **Your row:** set the status to match the artifact's status line (`DRAFT` / `PROPOSED`, never
   `LOCKED`), the last-run date, and the done-when count.
3. **Your done-when list:** tick a box only when the artifact you just wrote shows it, and add
   where (`→ 0X_File.md §N`). A box the artifact doesn't satisfy stays unticked. Mark a box that
   doesn't fit this project `N/A — <reason>`. Never tick on intention or assumption. A box whose
   evidence is `ASSUMED` can be ticked only if the box asks for a decision, not for validation.
   **Execution boxes** say something exists in the real world: "built", "live", "passed",
   "signed", "agreed", "on the calendar", "warmed". Those tick only when the owner (or the client, in
   client mode) confirms it happened, and the pointer names who confirmed and when, e.g.
   `→ confirmed by the owner 2026-11-20`. A spec in an artifact never ticks an execution box. Phase 2
   skills write specs, so most of their execution boxes stay open after a run, and that's expected.
4. **Downstream rows:** set `STALE` wherever §9 staled the artifact, and clear those ticks.
5. **Decisions log:** add one row per `PROPOSED` decision this run made.
6. When the owner locks an artifact (§8), set the row to `LOCKED` in the same edit as the run log.
7. `gtm-engine:metrics` adds `REVIEW-DUE` to a row when one of its pre-set re-run triggers fires.
   It never sets `STALE` itself. The owner decides whether to re-run, and the re-run then stales
   downstream as usual (§9).

The coherence audit reads the tracker. A Phase 1 PASS needs pillars 1–6 with every done-when box
ticked or marked N/A.
