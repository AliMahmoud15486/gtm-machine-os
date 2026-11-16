---
name: outbound
description: GTM Pillar 9 — Outbound Architecture for any product, built on the locked Phase 1 strategy, the GTM motion and the lead lists. Designs the outbound system around the lists (it does not rebuild them) — a legal gate per country × channel, list architecture at segment → persona level with tiers 1/2/3 and triggers, a qualification rule applied before any send, the reply-equation trace (person · trigger · message · channel · CTA), message variants per persona in Context → Problem → Impact → Proof → Offer → CTA drawn only from approved messaging and proof, a short or extended sequence with an exit ramp, channel rules (WhatsApp never for a first cold pitch), a sending-infrastructure spec (domains, warm-up, daily limits), a human-edit step, an A/B plan and a weekly outbound dashboard with an ICP feedback path. Calls lead-research when lists are missing. Never sends and never creates sequences or contacts in any tool. Deep by default (researcher → strategist → evidence auditor). Produces 12_Outbound.md plus usable assets (legal gate, list architecture, qualification rule, sequences, channel rules, sending spec, edit checklist, A/B plan, weekly dashboard). Trigger with "outbound for X", "cold outreach for X", "outbound sequence for X", "outreach plan for X", "how do we prospect for X", "GTM pillar 9 for X".
version: 1.0.0
---

# GTM Outbound Architecture — Pillar 9

**Answers:** *how do we create qualified conversations with named accounts that are not looking for us — lawfully, at a volume we can staff, without burning the market?*

## Before anything

Follow the shared protocol. It is part of this skill:
`~/.claude/skills/gtm-machine-os/Phase1_Strategy/SKILL-PROTOCOL.md`

| | |
|---|---|
| **Method** | `GTM_ROOT/Frameworks/14_Outbound-Prospecting-and-Outreach.md`: read in full — the reply equation (§2), list building and qualification (§3), offer (§4), message structure and ice-breaker (§5), magnets and case studies (§6), sequencing (§7), channels (§8), the 13 principles (§9), AI-assisted ABM and the dashboard (§10), inconsistencies, **Source gaps**, output contract. Plus `Frameworks/09_Sales-Led-Growth-and-Sales-Process.md` §3 [1] (targeting & prospecting: tiers, triggers, exit criteria) · `Frameworks/13_Maja-Voje-GTM-Strategist.md` **ch.7** (outbound channel rules, D1–D17 cadence, ABM account maths) · `Frameworks/10_Lead-Nurture.md` §3 (compliance caveats) |
| **Upstream (required)** | `08_Coherence-Audit.md` (verdict) · `02_ICP.md` (triggers, anti-ICP) · `02b_Buying-Center-and-Personas.md` + `assets/02b_role-finder.md` · `05_Messaging-and-Channels.md` + `assets/05_channel-plan.md`, `05_copy-kit.md`, `05_messaging-matrix.csv`, `05_banned-phrases.txt`, `05_copy-lint.py` · `06_Proof-System.md` + `assets/06_proof-tracker.csv` (**approved proof only**) · `assets/03_claims-register.csv` · `09_GTM-Motion-and-Routes-to-Market.md` (how much outbound) · `10_Revenue-Process-and-SLAs.md` (hand-off, SLA, stage [1] exit) |
| **Upstream (if present)** | `11_Demand-Generation.md` (lead magnet as soft CTA) · `07_Pricing-and-Packaging.md` (entry offer) · `leads/` from `gtm-machine-os:lead-research` (L1 accounts, L2 contact routes, L3 nurture, leads-log) |
| **Writes** | `products/<slug>/12_Outbound.md` · `products/<slug>/assets/12_*` |
| **Template** | `template.md` in this skill's folder |
| **Downstream on re-run** | marks `13`, `14` and `15` `STALE` (protocol §9) |

**Gates** (protocol §3): Phase 2 — stop if `08` is missing or FAIL; PASS-WITH-GAPS proceeds and the header repeats the gaps. If `09` is missing, stop and offer `gtm-machine-os:motion`; if `10` is missing, stop and offer `gtm-machine-os:revenue-process`. If `09` gives outbound **no role**, write a one-page `12_Outbound.md` saying so, with the trigger that would bring it in, and stop. If `leads/` is missing, design the architecture anyway and **offer `gtm-machine-os:lead-research`**; the list done-when boxes stay unticked.

## The Business Profile — how it changes this pillar

Read the profile (protocol §3) and state in the header which of these applied.

| Profile | Default this skill applies | Source |
|---|---|---|
| **P3/P4 → volume vs relevance** | Large TAM, low ACV, self-serve or light setup → wider lists, **short sequence (1–2)**, per-segment relevance. Small TAM, high ACV, 7+ buyers → **relevance-based, ABM-style**, **extended sequence (4–7)**, one hypothesis per account, multi-persona | `14` §7 (#19 p29), §5 (#20 p7); `13` ch.7 ABM maths (LTV × win rate → accounts; 50–100 → ABM) |
| **P3 < 5K and product-led motion** | Outbound stays light: a narrow trigger-led layer or none, per `09` | SPINE defaults; `08` |
| **P7 markets** | One legal-gate row per country × channel; message variants in each market language; who-replies-more measured per market, not assumed | `14` §3 (#19 p6), Source gaps 1 |
| **P8 capacity** | **Volume cap = hours available ÷ hours per account** (research + human edit + reply handling). Minutes per touch are `SOURCE-GAP` → `ASSUMED` until timed on the first 20. One or two people → one channel pair, one segment at a time | SPINE (P8 → 9); Source gaps 5 |
| **P5 stage** | Before paying customers: **no case-study touch** — the proof slot uses what `06` approves (credentials, a measured pilot result) or the CTA becomes a lead magnet / research request. Never a borrowed or invented result | `14` §5–6; `06` |
| **P1 type / P2 revenue model** | The CTA ladder uses the entry offer from `07` (e.g. a diagnostic for services, a trial or pilot for software). The frameworks give no outbound rule that differs by P1 or P2 beyond this — `SOURCE-GAP`: mark the choice `ASSUMED` | `14` §4 (#19 p18) |
| **P9 engagement (client mode)** | Advisory: we write the architecture and assets; the client sends, owns the gate sign-off and the dashboard. Done-with-you: name who edits and who sends per channel | SPINE |

## Rules specific to this pillar

1. **The legal gate comes first, per country × channel.** No source covers outreach law (`14` Source gaps 1). Research primary sources (statute, regulator guidance) per market and channel: consent for cold B2B email, calls, LinkedIn, WhatsApp; lawful basis for scraped or enriched data; identification and opt-out duties. Tag each rule `RESEARCHED` with URL and date or `ASSUMED`. A channel that is not cleared is **not used**, or its first touch is non-promotional (a research or interview request), matching lead-research's consent-market rule. Every message carries an opt-out; opt-outs are permanent suppressions. A legal adviser signs off the first sequence per country — until then the gate row is `open`.
2. **Do not rebuild the lists.** Lists come from `leads/` (L1 accounts, L2 contact routes). This skill defines the **list architecture** — segment → persona → sending account, tiers and the trigger per tier — and reads the lists into it. Map lead-research tiers to the source's tiers: **A → 1** (fit + trigger), **B → 2** (fit, no trigger), **C → 3** (borderline). Report the measured yield from `leads-log.md`; never resize a list by multiplying borrowed rates (protocol §7).
3. **Qualify before sending, and keep the reason.** One qualification rule per segment (the `14` §3 YES/NO fit check, built from `02`'s ICP and anti-ICP), and a recorded reason per lead (`14` inconsistencies: reasoning is persisted).
4. **Trace the reply equation.** Every sequence names its person (`02b`), trigger (`02`), message (`03`/`04`/`06`), channel (`05`/`09`) and CTA (`05`/`11`). A blank term is a defect, not a style choice.
5. **Claims and proof only from upstream.** Message lines come from `05_copy-kit.md`, `05_messaging-matrix.csv` and the claims register; proof only from `06` with its consent level. **Never invent a case result, a client name, a statistic or a quote.** Personalisation tokens only from recorded L1/L2 fields with a source.
6. **Message shape.** Context → Problem → Impact → Proof → Offer → CTA; **one problem per message**; no links or images on touch one; a one-word-reply CTA; no meeting ask on touch one (`14` §5). Lint every line with `assets/05_copy-lint.py`.
7. **Channel rules.** WhatsApp never for a first cold pitch — only after a reply or a meeting, and only if the gate allows it. LinkedIn as a credibility channel: profile first, account-risk ceiling on automation. Calls as warm follow-up (`14` §8).
8. **Sending infrastructure is a spec, with sourced numbers.** Separate sending domains, DNS authentication, warm-up period, daily cap per mailbox and per LinkedIn account, bounce and complaint stop-thresholds. The course gives none of these numbers (`14` Source gaps 2): take them from the provider's own documentation (`RESEARCHED`) or mark `ASSUMED`. The cap used is the lower of the infrastructure cap and the P8 hours cap.
9. **AI drafts, a person edits.** Every message gets a human specificity and tone pass and the smart-stranger test before it goes out (`14` §9, principles 11 and 13). Write who does it and how long it takes.
10. **Reference L3, don't duplicate it.** This skill owns the **cold sequence** (touches, spacing, channels, exit ramp, variants for A/B). If `leads/L3_sequence-copy.md` exists, audit its cold-stage copy against rule 6 and reuse what passes; write only missing variants. Everything after a reply stays in L3 and in `10` (hand-off, SLA).
11. **Execution, not strategy.** Conflicts with ICP, positioning, messaging or pricing become findings for the owning skill. Do not change them here.
12. **Never act externally.** No sending, no sequence, campaign or contact created in any tool, no domain bought. Credit-spending lookups only after stating the cost and getting the owner's yes.

## Procedure

### 1. Gate and inputs
Gates above. Read the profile, `08`'s verdict and open gaps, `09`'s outbound role and capacity, `10`'s stage [1] exit and SLA, and `leads-log.md` (yields, tiers, contact-route coverage).

### 2. Research (deep step ①)
Small `gtm-machine-os:researcher` briefs, saved as they go (protocol §5):
- **Legal, one brief per market:** cold-outreach rules per channel, lawful basis for B2B contact data, opt-out duties. Primary sources only.
- **Sending infrastructure:** the chosen tools' documented limits (daily sends, warm-up guidance, LinkedIn weekly invitation and InMail limits) — current, with dates.

### 3. Draft (deep step ②)
- **Legal gate** table (rule 1).
- **List architecture** and tiers; volume maths: accounts per week = min(infrastructure cap, P8 hours cap); weeks to cover Tier 1.
- **Qualification rule** per segment (rule 3).
- **Offer and CTA ladder:** entry offer (`07`), lead magnet per persona (`11` if present), approved proof per persona (`06`).
- **Messages** per persona × touch, two variants for the touch under test; the reply-equation trace per sequence.
- **Sequence architecture:** short or extended, with the reason; spacing; touch roles (ice breaker → case study or magnet → break-up); exit ramp; hand-off to L3 and `10` on reply.
- **Channel rules**, **sending spec**, **human-edit step**, **A/B plan** (one variable, metric, threshold and review date set now; sample size `ASSUMED` — Source gaps 5).
- **Weekly dashboard:** metrics, formulas, owner, review day, and the ICP feedback path to `02`.

### 4. Judgement (deep step ③)
Send `gtm-machine-os:strategist` the draft. Ask for: volume vs relevance; short vs extended; the channel mix and order; the first CTA (reply, magnet or meeting); which segment and tier go first; what would flip each call.

### 5. Attack (deep step ④)
Send `gtm-machine-os:evidence-auditor`: every legal rule and its source; every line of copy against the claims register and `06` (any proof not approved is critical); token traceability; the volume arithmetic; infrastructure numbers and their sources; consistency with `02b`/`05`/`09`/`10`. Fix or carry into Open questions; Option A / B if the audit undermines the strategist (protocol §5 ④b).

### 6. Assets
Write to `products/<slug>/assets/`:

| File | What it is | Usable for |
|---|---|---|
| `12_legal-gate.csv` | Country × channel: rule, source + date, tag, status (cleared / open / excluded), opt-out method, adviser sign-off | Knowing what may be sent where, today |
| `12_list-architecture.csv` | Segment × persona × tier: trigger, sending account, list file in `leads/`, measured yield, weekly volume | Loading lists into the right sequence |
| `12_qualification-rule.md` | Per segment: the fit criteria, the YES/NO prompt, the reason field, disqualifiers from the anti-ICP | Qualifying every lead before it is sent |
| `12_sequences.md` | Per persona: each touch (day, channel, purpose, copy, variant, claim row, proof ID), break-up, exit ramp; market language first; linted | Pasting into a sequencer after the owner's yes |
| `12_channel-rules.md` | Per channel: when it may be used, limits, account-risk ceiling, who sends | Briefing anyone who sends |
| `12_sending-spec.md` | Domains, DNS authentication, warm-up plan, daily caps, stop-thresholds, each number sourced or `ASSUMED` | Setting up sending without burning the main domain |
| `12_human-edit-checklist.md` | The pre-send pass: specificity, one problem, approved proof, token check, smart-stranger test, lint | The edit step on every AI draft |
| `12_ab-test-plan.csv` | Test, variable, variants, metric, threshold, minimum sends, review date, decision | Running tests without moving the goalposts |
| `12_weekly-dashboard.csv` | Weekly rows with formulas: sends, accepts, replies, positive replies, meetings, by segment × persona × channel × variant; qualification and disqualification rates; ICP notes | The weekly outbound review and the feedback to `02` |

### 7. Tracker and present
Update `00_Playbook-Tracker.md` per protocol §10. Present per protocol §8. Next skill: `gtm-machine-os:enablement` (Pillar 11).

## Checks before presenting

Pillar 9 done-when (Playbook), item for item:
- [ ] The legal gate is cleared
- [ ] The list is built at segment and persona level, and accounts are tiered 1/2/3
- [ ] Every lead is qualified before sending
- [ ] The sequence is written: one problem per message, a real approved proof point, a one-word-reply CTA
- [ ] Domains are warmed and daily sending limits are set
- [ ] A person edits every message before it goes out
- [ ] The weekly outbound dashboard is live

Tick only what the artifact shows. Warm domains, adviser sign-off and a live dashboard are **the owner's execution**: the spec and template do not tick them.

Also:
- [ ] Gates applied; `08` verdict and gaps in the header; profile defaults stated
- [ ] Reply-equation trace complete for every sequence
- [ ] Every claim traces to the claims register or copy kit; every proof to an approved `06` row; zero invented results, names or quotes
- [ ] Copy linted; tokens trace to recorded L1/L2 fields
- [ ] WhatsApp absent from every first touch; LinkedIn limits and account risk stated
- [ ] Volume cap = min(infrastructure cap, hours cap), arithmetic shown
- [ ] L3 referenced, not duplicated; post-reply hand-off points to `10`
- [ ] Every `SOURCE-GAP` choice marked `ASSUMED`
- [ ] Nothing sent; no sequence, contact or domain created in any tool
