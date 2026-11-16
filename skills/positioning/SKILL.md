---
name: positioning
description: GTM Pillar 3b — Positioning for any product, built on the value proposition. Makes the five positioning choices (category, target + context, primary promise, only-ness, reasons-to-believe), tests every only-ness claim with the "could a competitor claim this tomorrow?" litmus against real competitor copy plus the USP filter (valued AND unique), scripts all four alternatives including do-nothing and build-in-house, maps the 3-Circles and a positioning map on axes buyers actually decide on, and writes the statement, category narrative and message pillars. Deep by default (researcher → strategist → evidence auditor). Produces 04_Positioning.md plus usable assets (positioning one-pager, battlecards, 3-Circles + positioning map, validation plan). Trigger with "position X", "positioning for X", "how is X different", "only-ness for X", "battlecards for X", "positioning statement for X", "GTM pillar 3b for X".
version: 1.0.0
---

# GTM Positioning — Pillar 3b

**Answers:** *why should this customer buy from **us**, and not from someone else or nobody?*
Positioning ≠ messaging. This pillar decides; Pillar 4 words it.

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/04_Positioning.md` (read in full; the output contract is at the bottom) + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.6** (Peršolja's 8 steps, USP filter, special ops: new-company / horizontal / repositioning) and **ch.2** (four competitor types, 2×2 map rules) |
| **Upstream** | `03_Value-Proposition.md` (drivers, category, product truth, claims register) · `02_ICP.md` · `02b_…` · `01_Segmentation.md` + `assets/01_competitors.csv` |
| **Writes** | `products/<slug>/04_Positioning.md` · `products/<slug>/assets/04_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `05` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 3 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `03_Value-Proposition.md` is missing or STALE, **stop** and offer `gtm-machine-os:value-prop` (protocol §3).

## Rules specific to this pillar

1. **The six inputs, stated up front** (framework §Inputs). They are: ICP + triggers · jobs, pains and outcomes · competitive landscape · offer + delivery capability · proof assets · **unit economics**. A missing input is named, not skipped. Proof assets usually don't exist yet (Pillar 5), so the position is built on mechanism + risk reversal and says so.
2. **The story must be true.** Every asset or capability used comes from the `03` product truth inventory with status `Available today`. Roadmap items may appear only in a labelled "edge to build" section.
3. **Only-ness: 1–2 claims, and each passes two tests, with the reasoning recorded:**
   - **(a) Litmus.** *Could a competitor claim this tomorrow?* Check against each competitor's **actual published copy** (URL + date + verbatim). "Nobody claims it" is not enough: also ask whether they *could*, i.e. whether the mechanism is one API call or one template away.
   - **(b) USP filter (Peršolja).** Is it **valued by the customer** (evidence: reviews, interviews, observed behaviour, not our opinion) **and** unique to us or very few?
   - **Record the failed attempts too.** That reasoning is worth more than the survivor.
   - **If nothing survives:** say plainly that this is a price fight. Then name the asset to **engineer backwards** (Voje ch.6): the missing, valued thing worth building.
4. **Four alternatives, always:** do-nothing · build-in-house / DIY / manual · generic vendor (suites, platform native) · point tool (direct competitors). Plus every named direct competitor. For each:
   - where they're strong, stated honestly;
   - where we're stronger, using `Available today` capabilities only;
   - the risk they carry;
   - **3 discovery questions that expose the gap**, in the market's language.
5. **3-Circles includes the unflattering regions.** Competitors' unique points, white space and irrelevant points are named, not just ours.
6. **The map's axes come from evidence of what buyers decide on** (review themes, interview criteria), never from what flatters us (Voje ch.2 rule). Scores live in a data table with sources. Bubble size = market share or install proxy where known.
7. **Message pillars map 1:1 to the `03` value drivers.** Each pillar carries proof bullets **taken only from the `03` claims register with a publishable status**. Where none exists: "proof: none yet → risk reversal: …".
8. **Respect locked decisions.** Category, driver order and the proof threshold from `03` are inputs, not things to re-argue. If the research says one is wrong, raise it as an open question for the owner.
9. **Validation thresholds are set before testing.** Keep / change / kill numbers are written in advance (framework).

## Procedure

### 1. Inputs and the asset inventory
- Restate the six inputs with their status.
- Pull the asset list from the `03` product truth inventory, plus any team capability (e.g. language, founder background) that is true and evidenced.
- Run each asset through **"so what?" ×5** to get from capability to benefit.

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs that save as they go (protocol §5):
- **Competitor positioning teardown.** For each direct competitor and suite: their category word, hero line, target, main claims, proof shown, price anchor (verbatim, URL, date). **For each candidate only-ness claim, does anyone already claim it, and how close are they to being able to?** Reuse `03` research and fetch only what's new.
- **Decision criteria.** What buyers praise and complain about when choosing tools in this category (reviews, forums, interviews). Count the themes. These become the map's axes and the battlecards' landmines.
- **Hands-on checks, where cheap and legitimate:** published trials, public docs, demo videos. **Never** place fake orders or impersonate a customer.

### 3. Only-ness candidates → tests (rule 3)
List 3–6 candidates. Run the litmus test and the USP filter on each, with evidence. Keep 1–2, or declare a price fight plus an edge to build.

### 4. Alternatives scripts (rule 4)
One block per alternative.

### 5. 3-Circles and positioning map (rules 5–6)

### 6. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the inputs, the only-ness tests, the alternatives, the circles and the map. Ask for:
- **the 1–2 only-ness claims**, or the price-fight call plus the edge to build;
- **the competitive positioning pillar**: value-based / problem–solution / quality / innovator;
- **the positioning statement** (six lines);
- **the category narrative** (old way → new way);
- **the three message pillars** with objection and counter;
- any **special ops** that apply (new-company / horizontal / repositioning);
- what would flip each call.

### 7. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`:
- every only-ness claim, with its litmus reasoning (it must re-check competitor copy itself);
- every competitor claim we attribute to someone;
- the map scores;
- the alternatives' "where they're strong";
- the statement;
- the pillars' proof bullets;
- any research that landed after the draft.

Fix each finding, or carry it into Open questions. If the audit undermines the only-ness call, present Option A / B (protocol §5 ④b).

### 8. Assets
Research goes to `products/<slug>/research/`. Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `04_positioning-one-pager.md` | Internal page: six-line statement, only-ness with its RTBs, category narrative (old → new), the three pillars (label · meaning · proof · objection → counter), what we never claim | Briefing anyone who writes or sells; the input to Pillar 4 |
| `04_battlecards.md` | One card per alternative (incl. do-nothing and DIY) and per named competitor: what they say (verbatim + source), where they're strong, where we win (Available-today only), landmines to avoid, **3 discovery questions** (AR + EN where relevant), the one line to use | Sales calls, outreach replies, objection handling |
| `04_positioning-map.csv` + `04_positioning-map.svg` | The map's data (axes, scores, sources, bubble size) and a rendered chart | Showing the position at a glance; re-scoring as evidence lands |
| `04_three-circles.md` | Our unique points · points of parity · competitors' unique points · white space · irrelevant points, each with evidence | Roadmap and messaging focus; the edge to build |
| `04_validation-plan.md` | Which of the five loops runs, when, sample size, and keep / change / kill thresholds **set now** | Knowing in 30–60 days whether the position works |

### 9. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-machine-os:messaging` (Pillar 4).

## Checks before presenting (framework output contract)
- [ ] Six inputs stated; missing ones named
- [ ] Statement in the six-line template, all slots filled
- [ ] 1–2 only-ness claims, each with litmus reasoning against **cited** competitor copy and USP-filter evidence; failed attempts recorded. Or an explicit price-fight call plus the edge to build
- [ ] All four alternatives plus named competitors scripted, each with 3 discovery questions
- [ ] 3-Circles with white space and irrelevant points named
- [ ] Map axes justified by buyer-decision evidence; data table with sources
- [ ] Three message pillars, 1:1 with `03` drivers; proof bullets only from publishable claims
- [ ] Category narrative: old way → new way
- [ ] Validation plan with keep / change / kill thresholds set in advance
- [ ] Locked upstream decisions respected; conflicts raised as open questions
- [ ] All assets written

Playbook "Pillar 3 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it; the canvas, driver, claim and category boxes belong to `gtm-machine-os:value-prop`):
- [ ] The positioning statement is written, and its only-ness claim passes the "competitor tomorrow" test
- [ ] Each alternative is scripted: do nothing, build in-house, a generic provider, a tool alone
- [ ] The 30–60 day validation targets are set
