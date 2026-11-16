---
name: motion
description: GTM Pillar 8 — GTM Motion & Routes to Market for any product; the first Phase 2 skill, run after the Phase 1 coherence gate. Scores all six motion-selection criteria (deal economics, product complexity, buyer journey, time-to-value, internal capability, buyer expectations) against the Business Profile and the locked Phase 1 artifacts, names a primary motion (sales-led, marketing-led, product-led, partner-led) plus layered motions with the trigger that activates each, runs the product-led fit test and the partner-led trade check, lists the roles the motion requires as cost with a named owner or "unfilled", builds the route-to-market model (route, role, first step, capture vs generate) on the channels Phase 1 already chose, picks KPIs from the motion's own row, checks ACV against the motion, and writes an explicit scope for pillars 7, 9, 10 and 11 that later skills read. Deep by default (researcher → strategist → evidence auditor). Produces 09_GTM-Motion-and-Routes-to-Market.md plus usable assets (motion map, roles and owners sheet, routes-to-market sheet, downstream scope, channel-economics check, partner terms when a partner route is chosen). Trigger with "GTM motion for X", "how should X sell", "sales-led or product-led for X", "routes to market for X", "who sells X", "motion map for X", "GTM pillar 8 for X", or as the first Phase 2 step.
version: 1.0.0
---

# GTM Motion & Routes to Market — Pillar 8

**Answers:** *how do we actually reach and sell to customers, and who does each part?*
Strategy says who and why. The motion is the sequence of channels, roles, tools and messages that converts them. **A motion commits you to a cost structure: a motion you cannot staff is not a motion.**

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/08_GTM-Motion-and-Routes-to-Market.md`: read in full. The four motions and comparison table, the six selection criteria, key roles by segment, "Partner-Led — read this before choosing it", "When Product-Led fails", the 2026 growth formula (capture vs generation), "Motions combine", and the output contract. Plus `Frameworks/09_Sales-Led-Growth-and-Sales-Process.md` **§1** (SLG characteristics and roles) and **§4** (running it solo or at low ACV) · `Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.7** (channel economics, Bullseye, capture vs generate, seven growth channels, ABM account maths, Wes Bush PLG test, partnership metrics) and **ch.8** (the five-role GTM squad, budget lines incl. labour in CAC). Source: `Learning_resources/_extracted/B2B Growth Masterclass I Session #12 & 13.txt` p3–p11 (p12 case study and p13 diagram are image-only; use the framework's visual reading). Playbook: "Pillar 8 — GTM Motion & Routes to Market" |
| **Upstream** | `00_Discovery.md` (Business Profile: P3 deal size, P4 how they buy, P5 stage, P7 where they sell, P8 capacity, P9 engagement; product truth for time-to-value) · `02_ICP.md` (band, triggers, account count) · `02b_Buying-Center-and-Personas.md` (buying-group size, veto roles, info sources) · `05_Messaging-and-Channels.md` (the chosen channels and exclusions) · `07_Pricing-and-Packaging.md` (tiers, entry offer → ACV) · `08_Coherence-Audit.md` (verdict) |
| **Writes** | `products/<slug>/09_GTM-Motion-and-Routes-to-Market.md` · `products/<slug>/assets/09_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `10` to `15` `STALE` (revenue process, demand gen, outbound, enablement, metrics, execution audit) |

**Phase 2 gate.** Phase 2 executes the locked strategy; it does not remake it.
- `08_Coherence-Audit.md` missing → **stop**, offer `gtm-machine-os:coherence-audit`. Verdict `FAIL` → **stop**, name the breaks. `PASS-WITH-GAPS` → proceed, and list the gaps that touch the motion in Open questions.
- Any upstream above missing or `STALE` → stop (protocol §3).
- State the coherence verdict in the header. Never change ICP, positioning, messaging or pricing here. A conflict (e.g. the motion needs a channel `05` excluded, or `07` ACV can't carry the roles) becomes a **finding for the owning skill**, not an edit.

## Rules specific to this pillar

1. **Score all six criteria; don't average them.** Score each against named evidence (Framework 08 "Choosing the motion"; source p8, p10). Where criteria disagree, explain the disagreement: it usually shows where a layer is needed.
2. **ACV comes from `07`, not from hope.** Compute ACV per tier from the `07` prices (monthly × 12, or per-deal × deals a year). If it disagrees with P3, that is a finding for `pricing` or `discovery`. Framework contract item 7: a low price on a sales-led motion fails on unit economics.
3. **Apply the profile defaults** (spine, "How the profile changes each pillar"), then adjust:
   - **P3 deal size:** > 50K → sales-led or partner-led · 10–50K → marketing-led + sales-led · < 5K → product-led / self-serve. **5–10K is a `SOURCE-GAP`**: the source gives no rule between 5K and 10K. Decide on criteria 2–6 and the `09` §4 "thin founder-led layer", and mark the choice `ASSUMED`.
   - **P4 how they buy:** 7+ in the buying group → sales-led · 1–3 people, self-serve → product-led or a thin founder-led layer · heavy setup → no product-led core (rule 5).
   - **P1 business type:** Software / SaaS and Data / API can be product-led ("developers, product teams, small teams"). Services and productised services sell people's time, so the product-led row does not apply as written; use sales-led or marketing-led + sales-led by ACV. Marketplace / platform: plan each side as its own motion and sequence them (Voje ch.7 cold-start case: build the side the other depends on first). Physical product: **`SOURCE-GAP`** — mark the motion `ASSUMED`.
   - **P2 revenue model:** subscription / usage fits product-led below the self-serve ceiling · retainer / project / licence fit sales-led or hybrid · transaction / commission: a marketplace listing is partner-shaped distribution with product-led economics (Framework 08, partner section).
   - **P5 stage:** before PMF, the founder sells first and does things that don't scale (Voje ch.7). The motion is a hypothesis with a review date, and KPIs start with activation and PMF signals.
   - **P7 where they sell:** regional or vertical nuance with trusted local players → test a partner-led layer.
   - **P8 capacity:** weight criterion 5 hardest. With one or two people: one primary motion, and a layer only if it has a named owner with stated hours.
   - **P9 engagement (client mode):** roles are named from the client's team. Under advisory, the client owns every execution role; we own none.
4. **Layers, not options.** Name the primary motion, then each layered motion with the **trigger that activates it** (e.g. "sales steps in when an account passes N seats or asks for an invoice"). Framework 08 "Motions combine".
5. **Product-led must pass the test.** Run the Wes Bush three factors (Voje ch.7) and the framework's question: *can a new user reach the real value, alone, in minutes, without context from you?* Measure time-to-value from the product (discovery product truth), and check it fits the trial window. If the answer is no, product-led may be the acquisition layer only. Add a human-guided activation layer, as in the course case study (Framework 08, "When Product-Led fails").
6. **Partner-led must pass the trade check.** State what you give (margin share, feedback, customer control), what you must build (enablement, deal registration, conflict boundary, PRM) and what you must survive (channel conflict, partner churn, registration leak). Name real partner candidates with URLs, never invented ones. Record margin share, enablement plan and conflict boundary (contract item 5).
7. **Roles are cost, owned by name.** List every role the chosen motions require (Framework 08 "Key roles by segment"; `09` §1 roles; Voje ch.8 squad), its jobs, the hours a week it needs, and who fills it today: a **named person** or **"unfilled"**. An unfilled role is a gap, never an aspiration. One person may hold several roles; add up their hours against P8.
8. **Routes execute Phase 1 channels.** Each route-to-market row maps to a channel `05` chose. Give it a role, an owner, a first step doable this week, one metric, and capture or generate. Capture harvests the ~5% in market; generation moves the other 95% (Framework 08, 2026 formula). A route list with only capture routes says so as a risk.
9. **KPIs come from the motion's own row.** Don't track sales-led metrics on a product-led motion. Every KPI starts as `UNKNOWN — needs measurement` until there is a baseline.
10. **Channel economics before any paid route.** Funnel maths (spend → clicks → trial → activation → paid) against `07` revenue in the runway. LTV ≥ 3× CAC, and CAC includes labour and tools (Voje ch.7, ch.8 endnote 102). ABM only if the account maths says 50–100 accounts (Voje ch.7).
11. **Write the downstream scope.** For pillars 7, 9, 10 and 11 (and the KPI set for 12), state the depth — **full · light · through partners · not now** — what to build, what to skip, and why. Use the spine defaults (product-led → light 9 and 10; partner-led → 9 runs through partners) and the `09` §4 stage compression. Later skills read this section first.
12. **Never act externally.** No partner outreach, no listings, no hires, no ad spend, no CRM changes. Drafts and specs only.

## Procedure

### 1. Gate and profile
Run the Phase 2 gate. Read the Business Profile and write the `**Profile:**` line with the motion default it sets. Compute ACV per tier (rule 2).

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save as they go. Reuse `04`/`05`/`07` research first.
- **How alternatives sell:** for the ≥3 alternatives in `04`, record self-serve sign-up, demo request, trial length, partners or resellers, and published pricing visibility. Verbatim, with URL and date. This feeds criterion 6.
- **Partner and marketplace routes** (only if criterion 5 or P7 points there): real candidate partners or marketplaces, their terms, revenue share, listing rules. Cap at 15 candidates.
- **Time-to-value:** from product truth (`00`) and docs, not research. Steps from sign-up to first real value, and how long they take.

### 3. Draft (deep step ②)
- The six criteria scored, with evidence tags.
- The product-led test (rule 5) and partner trade check (rule 6), whenever either motion is in play.
- Primary motion + layers with triggers; rejected motions, each with its "when NOT to use" reason.
- Roles table (rule 7), routes table (rule 8), KPIs (rule 9), channel economics (rule 10), downstream scope (rule 11).

### 4. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the criteria scores, the profile, ACV, roles and capacity. Ask for:
- the **primary motion and layers**, with triggers;
- **which role to fill first** if capacity is short;
- the **depth for 7, 9, 10, 11**;
- what would flip each call.

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`:
- each criterion score and its evidence;
- the ACV arithmetic and its fit with the motion;
- the time-to-value claim;
- partner claims and terms;
- role hours against P8;
- the channel economics;
- consistency with `02`/`02b`/`05`/`07`;
- the strategist's call.

Fix each finding or carry it into Open questions. If the audit undermines the strategist's call, present Option A / B (protocol §5 ④b).

### 6. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `09_motion-map.md` | One page: primary motion, layers with triggers, ACV fit, rejected motions in one line each, review date | Briefing anyone who joins in five minutes |
| `09_roles-and-owners.csv` | Role, motion, jobs, hours/week, owner (named or `unfilled`), cost per month or `UNKNOWN`, first hire or reassignment | Seeing the staffing gap and deciding the next hire |
| `09_routes-to-market.csv` | Route, motion layer, `05` channel, role, owner, first step, capture/generate, metric, start date | Starting each route this week |
| `09_downstream-scope.md` | Depth for 7, 9, 10, 11 (full / light / through partners / not now), what to build and skip, the KPI set for 12 | Input every later Phase 2 skill reads first |
| `09_channel-economics.csv` | Live `=` formulas: spend → clicks → trial → activation → paid → CAC (incl. labour and tools) vs LTV; payback; the ABM account maths | Checking a paid route before spending |
| `09_partner-terms.md` | Only if a partner route is chosen: candidate partners with URLs, value to each side, margin share, enablement plan, conflict boundary, success metrics by type (Voje ch.7) | Opening a partner conversation with the terms already decided |

### 7. Tracker and present
Update the tracker (protocol §10). Then present per protocol §8. Next skill: `gtm-machine-os:revenue-process` (Pillar 10).

## Checks before presenting (playbook done-when, then framework output contract)
- [ ] The motion is chosen with the decision rules, and the reason is written down (deal size, how buyers decide)
- [ ] Routes to market are listed, each with a role and a first step
- [ ] Each role is assigned to a named person
- [ ] Any role without a person is marked `unfilled` as a gap; the box above stays unticked until every role is named
- [ ] Phase 1 coherence verdict stated in the header; not FAIL; no Phase 1 decision changed, conflicts filed as findings
- [ ] Primary motion named, all six criteria scored, disagreements explained rather than averaged
- [ ] Layered motions named, each with its activation trigger
- [ ] Roles listed as cost, with hours against P8 capacity; unfilled roles shown as gaps
- [ ] KPIs from the motion's own row; baselines `UNKNOWN — needs measurement` where unmeasured
- [ ] Route-to-market model: each route maps to a `05` channel and is tagged capture or generate; partner routes carry margin share, enablement and conflict boundary
- [ ] Rejected motions, each with its "when NOT to use" reason
- [ ] ACV from `07` matches the motion; channel economics checked before any paid route
- [ ] Product-led test and partner trade check run wherever those motions are in play
- [ ] Every `SOURCE-GAP` profile choice is marked `ASSUMED`
- [ ] Downstream scope for 7, 9, 10, 11 (+ KPI set for 12) written
- [ ] All assets written; tracker updated
