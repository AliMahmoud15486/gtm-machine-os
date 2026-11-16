---
name: personas
description: GTM Pillar 2b — Buying Center & Personas for any product, built on the ICP/ECP from Pillar 2a. Maps all six buying-center roles (plus champion and external influencers), decides who can veto and who to design for, writes evidence-tagged persona cards with awareness level and an anti-persona, and turns every open assumption into a discovery interview script. Deep by default (researcher → strategist → evidence auditor). Produces 02b_Buying-Center-and-Personas.md plus usable assets (persona cards, buying-center map CSV, per-persona discovery script, role-finder). Trigger with "personas for X", "buyer personas for X", "buying center for X", "who decides at X's customers", "DMU for X", "buyer mapping for X", "GTM pillar 2b for X".
version: 1.0.0
---

# GTM Personas — Pillar 2b

**Answers:** *which humans inside the ICP account decide, use, influence or block, and what does each one need to hear and see?*
ICP = company (Pillar 2a). Persona = human. Keep the two apart.

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-engine/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/02_ICP-and-Buying-Center.md` sections *The Buying Center*, *Navigating it*, *Levels of awareness*, *Buyer journey map*, *Mining customer insight — the 360° method* + `GTM_ROOT/Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.3** (DMU B2B case, "One ECP — with two exceptions", ECP Framework "what to include" table, Campbell anti-persona) and **ch.6** (five-role value matrix: use only its *Persona / Context / Problem* columns here; Capability / Benefit belong to Pillar 4) |
| **Upstream** | `00_Intake.md` · `02_ICP.md` (the profile, anti-ICP, assumption map). `01_Segmentation.md` for context |
| **Writes** | `products/<slug>/02b_Buying-Center-and-Personas.md` · `products/<slug>/assets/02b_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `03` onward `STALE` |

**Business Profile** (protocol §3): `00_Discovery.md` missing, or any of P1–P5 unknown → stop. Apply the Pillar 2 defaults in `GTM_ROOT/Playbook/SPINE.md` ("How the profile changes each pillar"; if none are listed, say so) and state them in the artifact's `**Profile:**` header line. A departure is a `PROPOSED` decision with its reason.

If `02_ICP.md` is missing, **stop** and offer `gtm-engine:icp` (protocol §3). A legacy
`02_ICP-and-Buying-Center.md` is read as input for its buying-center and persona sections. Once
`02b` is written, add `Superseded for buying center & personas by 02b_… (YYYY-MM-DD)` at its top.

## Rules specific to this pillar

1. **Map all six roles, always.** These are initiator, user, influencer, gatekeeper, buyer and decider (framework). Add **champion** (Voje ch.6) and **external influencers** (agencies, partners, platform staff, couriers, peers). A role nobody fills is written **"none identified"** with the reason. Never omit a row.
2. **Collapsed roles are a finding, not a shortcut.** In owner-run SMBs one person may hold five roles. Say so, and say what it means: no second conversation, so the listing, the trial and the onboarding *are* the sales process.
3. **Personas only for roles that matter.** Write a full persona for every role that has **veto power** or is the **primary user**. Other roles get a row in the map only.
4. **Persona fields follow Voje's B2B "critical" list.** The fields are job and function · motivations and goals · problems and frustrations · purchase dependencies (who else must agree) · how they measure success · preferred technologies · preferred channels and information sources · awareness level · top objection. Each field is tagged.
5. **No synthesised voice. This is the rule most likely to be broken in this pillar.**
   - A persona's "in their words" field holds only verbatim quotes, each traced to a real interview or a cited public source: URL, or review id + date.
   - If none exist, the field says `No customer language yet — see discovery script` and stays empty.
   - Never write a "typical day", "a typical owner might say", or a fictional name and photo. A persona is a set of tagged claims, not a character.
6. **Awareness level per persona.** Use the framework's 1–6 scale, with the evidence for the level. It sets Pillar 4's job: an unaware persona needs education before a pitch.
7. **Anti-persona.** Name the human who looks like a buyer but would cost more than they return. Base it on unit economics and satisfaction (Campbell), not interest. Example: the person who installs expecting something else and leaves the 1★ review.
8. **People are found by role, not compiled.**
   - The role-finder asset says which titles to look for and through which **business** channel.
   - Do not collect personal data about individuals: no personal phones, private emails, or aggregating one person's details across sites.
   - A named contact is recorded only when the company itself publishes them as its contact (site, official LinkedIn page, commercial register).

## Procedure

### 1. Shape of the buying center
From `02_ICP.md`: company size, ownership, team, and how the product is bought (self-serve app store / trial / procurement / sales-led). Predict which roles collapse into one person. State it as `ASSUMED` until research or interviews confirm it.

### 2. Research (deep step ①)
Launch `gtm-engine:researcher`, in the background, as **small briefs that save as they go** (protocol §5):
- **Role brief.** What job titles and team shapes exist at ICP accounts.
  - Sources: company team/about pages, LinkedIn company pages, job postings, commercial-register data where public.
  - Who installs tools, who handles customers, who handles logistics, who pays.
  - Measure on a sample of ≥20 ICP accounts: `identified n / checked N` per role.
- **Language brief.** Public verbatim language per role: reviews, forums, communities, social posts. Cite each one; report absence honestly.
- **Information-source brief** (Voje's 4 questions). Which publications, events and fairs, insider communities and social channels each role follows. Where they search for solutions: marketplaces, app stores, peers.

### 3. Buying-center map
Fill the map table in the template: role · who (title or "same as decider") · what they care about · their concern about *this* product · veto power (Y/N) · influence (H/M/L) · where the concern gets answered (listing, trial, onboarding, call, document). Tag every cell. Apply the DMU rule: *if the initiator stalls, go over them with ROI messaging.*

### 4. Personas
One card per role that has veto power or is the primary user, using the rule 4 fields. Add:
- **Context and problem**, from the value matrix, for that persona only.
- **What they need to see to say yes**, by evidence type (a number, a demo, a document, a peer).
- **Top objection.**

### 5. Judgement (deep step ③)
Send `gtm-engine:strategist` the map, the persona cards and the research. Ask for:
- **the primary persona to design for**, meaning whose problem the product and copy lead with;
- **the champion**;
- **who can kill the deal and how to pre-empt them**;
- **the anti-persona**;
- what would flip the call.

### 6. Attack (deep step ④)
Send `gtm-engine:evidence-auditor`:
- every persona field carrying weight;
- every quote, to verify against its source and check it is attributed to the right role;
- the awareness levels;
- the strategist's call;
- any research that landed after the draft.

Fix each finding, or carry it into Open questions. If the audit undermines the primary-persona call, present Option A / B (protocol §5 ④b).

### 7. Assets
Research goes to `products/<slug>/research/` (protocol §5). Then write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `02b_buying-center-map.csv` | One row per role: who, cares about, concern, veto, influence, where answered, evidence tag | Sales and onboarding planning; checking Pillar 4 covers every veto holder |
| `02b_persona-cards.md` | One printable page per persona: the rule-4 fields, awareness level, what they need to see, top objection, in-their-words (verbatim or empty), anti-persona page | Briefing anyone who writes copy, sells, or builds onboarding |
| `02b_discovery-script.md` | Per persona: a 20–30 minute interview script. No pitching (Mom Test). ★ marks the must-ask questions. **Every question is linked to the assumption it tests** (from `02_ICP.md` §9 and this artifact). Includes the capture rule and a results table that turns answers into `VALIDATED` (C=1) | Running the validation interviews the ICP needs. **This is the asset that moves the evidence ratio** |
| `02b_role-finder.md` | Per role: titles (Arabic and English where relevant), where to find the role through business channels, measured identification yield, and the **opening line by channel** (as a question, not a pitch) | Getting the first conversations booked |

### 8. Present
Update the tracker (protocol §10), then present per protocol §8. Next skill: `gtm-engine:value-prop` (Pillar 3a).

## Checks before presenting (framework output contract, items 5–6)
- [ ] All six roles plus champion and external influencers are present; empty roles say "none identified" with the reason
- [ ] Collapsed roles are named, with the consequence for the sales motion stated
- [ ] A persona card for every veto holder and the primary user, with all rule-4 fields tagged
- [ ] Every persona has an awareness level, with the evidence for it
- [ ] **Zero synthesised quotes, names, photos or "day in the life" fiction**
- [ ] Anti-persona present, based on unit economics and satisfaction
- [ ] Primary persona, champion and deal-killer named (strategist), with alternatives
- [ ] Role-finder shows a measured identification yield (`identified n / checked N`)
- [ ] Discovery script questions each link to a named assumption
- [ ] All four assets written

Playbook "Pillar 2 is done when" (tick in `00_Playbook-Tracker.md` per protocol §10, only where the artifact shows it; the other Pillar 2 boxes belong to `gtm-engine:icp`):
- [ ] The buying center is mapped: all six roles, who signs and who can block
