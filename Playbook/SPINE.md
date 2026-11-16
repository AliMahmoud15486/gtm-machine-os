# The Spine — playbook → method → skill → artifact

One map that ties the GTM Machine OS together for any B2B project.

- **Playbook** ([`GTM-Playbook.md`](GTM-Playbook.md)) — the manual. Read it to know *what* each
  pillar decides and when it is done. Never filled in.
- **Frameworks** ([`../Frameworks/`](../Frameworks/)) — the method in depth, cited to source.
- **Skills** (`gtm-machine-os:*`) — the engines that run a pillar for one project.
- **Artifacts** (`products/<slug>/`) — one project's answers.
- **Tracker** (`products/<slug>/00_Playbook-Tracker.md`) — where that project stands on all
  12 pillars, with each pillar's "done when" list. Template:
  [`../products/_TEMPLATE/00_Playbook-Tracker.md`](../products/_TEMPLATE/00_Playbook-Tracker.md).

## The map

| Playbook pillar | Decides | Framework | Skill | Artifact in `products/<slug>/` |
|---|---|---|---|---|
| 0 Discovery *(before the playbook)* | What is true about the company today | `12_Market-Readiness-Launch-and-Metrics.md` (readiness gate) | `discovery` | `00_Discovery.md`, `00_Intake.md` |
| 1 Segmentation & Targeting | Where to play | `01_Segmentation-and-Targeting.md` | `segmentation` | `01_Segmentation.md` |
| 2 ICP & Buying Center | Who to serve, who decides | `02_ICP-and-Buying-Center.md` | `icp`, `personas` | `02_ICP.md`, `02b_Buying-Center-and-Personas.md` |
| 3 Value Proposition & Positioning | Why buy, why us | `03_Value-Proposition.md`, `04_Positioning.md` | `value-prop`, `positioning` | `03_Value-Proposition.md`, `04_Positioning.md` |
| 4 Messaging & Channels | What to say, where | `05_Messaging-and-Channels.md` | `messaging` | `05_Messaging-and-Channels.md` |
| 5 Proof System | Why believe us | `06_Proof-System.md` | `proof` | `06_Proof-System.md` |
| 6 Packaging & Pricing | How to monetise | `07_Pricing-and-Packaging.md` | `pricing` | `07_Pricing-and-Packaging.md` |
| *Gate:* Phase 1 coherence | Do pillars 1–6 agree? | `00_GTM-Pillar-Roadmap.md` | `coherence-audit` | `08_Coherence-Audit.md` |
| 7 Demand Generation | How leads arrive | `10_Lead-Nurture.md`, `13_Maja-Voje-GTM-Strategist.md` ch.7 | `demand-gen` | `11_Demand-Generation.md` |
| 8 GTM Motion | How we reach and sell | `08_GTM-Motion-and-Routes-to-Market.md` | `motion` | `09_GTM-Motion-and-Routes-to-Market.md` |
| 9 Outbound | How we create meetings | `14_Outbound-Prospecting-and-Outreach.md`, `09_Sales-Led-Growth-and-Sales-Process.md`, `13_…` ch.7 | `outbound` (+ `lead-research` for the lists) | `12_Outbound.md`, `leads/` |
| 10 Revenue Process & SLAs | How deals move and hand off | `09_Sales-Led-Growth-and-Sales-Process.md` | `revenue-process` | `10_Revenue-Process-and-SLAs.md` |
| 11 Enablement | What the team needs | `12_Market-Readiness-Launch-and-Metrics.md`, `13_…` ch.8 | `enablement` | `13_Enablement.md` |
| 12 Metrics & Feedback | What works, what to change | `12_Market-Readiness-Launch-and-Metrics.md`, `13_…` | `metrics` | `14_Metrics-and-Feedback.md` |
| *Gate:* Phase 2 execution | Do pillars 7–12 fit together? | `../Phase2_Execution/README.md` | `execution` (cross-check) | `15_Execution-Audit.md` |

**Orchestrators:** `strategy` runs Phase 1 (discovery check → 1–6 → coherence gate); `execution` runs Phase 2 (motion → … → metrics → Phase 2 gate). Either can run one step on its own.

Framework files are in `../Frameworks/`. Skill names are short for `gtm-machine-os:<name>`.

## Run order

```
0 Discovery → 1 → 2 → 3 → 4 → 5 Proof → 6 Pricing → Coherence gate
  → 8 Motion → 10 Revenue process → 7 Demand gen → 9 Outbound → 11 Enablement → 12 Metrics → Execution gate
       └──────────── 12 Metrics feeds back into 1–3 (review every 6–12 months) ────────────┘
```

Phase 1 runs Proof before Pricing, in pillar order (decided by the owner 2026-11-15; see `CLAUDE.md`, "Known
source-file issues"). Proof chooses the risk reversal; Pricing sets its commercial terms. Phase 2 runs Motion first, because the motion decides how much of 7, 9
and 10 applies: a product-led business needs little outbound, and a partner-led one runs 9 through partners.

## The Business Profile — read before every pillar

The same playbook runs differently for a retainer agency, a SaaS product and a marketplace. It
also runs differently for a business with no customers and one with fifty. So **discovery records
a Business Profile first**, and every pillar reads it before doing anything (protocol §3). It lives
at the top of `00_Discovery.md` (§0), with a copy in `00_Intake.md` and the tracker.

| # | Field | Options (pick one; "hybrid" names both) | Why it matters |
|---|---|---|---|
| P1 | **Business type** | Services (agency, consultancy) · Productised service · Software / SaaS · Marketplace / platform · Data / API · Physical product · Hybrid | Sets which playbook examples apply, and how much of the offer is people vs product |
| P2 | **Revenue model** | Retainer (monthly) · Project / milestone · Subscription (seat or tier) · Usage-based · Transaction / commission · Licence · Performance-linked · Hybrid | Pillar 6's pricing model and value metric; how retention and expansion work (10, 12) |
| P3 | **Deal size** | Annual contract value per customer, as a number (or `UNKNOWN — needs measurement`) → band: < 5K · 5–20K · 20–50K · > 50K | The motion decision rules (8); how much sales effort a deal can carry |
| P4 | **How they buy** | Buying group size · sales-cycle length · self-serve or sales-assisted · setup effort (none / light / heavy) | Buying center (2), motion (8), revenue process depth (10) |
| P5 | **Company stage** | Idea · Prototype · Pre-revenue · Early revenue (pre-PMF) · Scaling (repeatable motion) | ICP vs ECP (2), evidence ratio, proof plan vs proof library (5), PMF signals vs funnel metrics (12) |
| P6 | **GTM maturity today** | For each pillar: nothing · informal (founder does it ad hoc) · documented · running with metrics | Where the run starts, and what it documents rather than invents |
| P7 | **Where they sell** | Countries / regions · languages · regulated sector or not | Legal gates (9, 11), channels (4, 7), currency and tax (6) |
| P8 | **Capacity** | People and hours available for GTM · monthly budget for tools and ads | What can be executed: channel count (7), outbound volume (9), stack (11) |
| P9 | **Engagement** *(client mode only)* | Our engagement with the client: retainer · one-off project · advisory · done-with-you | Depth of the run, what we deliver vs what they execute, who owns each pillar in the tracker |

Each field is evidence-tagged like any other fact. An unknown field becomes a ★ question in the
discovery question bank. The profile is `PROPOSED` until the owner (or the client, in client mode)
confirms it. **Changing P1–P5 is a material change**: it marks `01` onward `STALE`.

### How the profile changes each pillar (defaults: each pillar states which it applied)

| Profile signal | Pillar | Default it sets |
|---|---|---|
| P5 = Idea / Prototype / Pre-revenue / Early revenue | 2 ICP | Build an **ECP** (early customer profile), not an ICP (`Frameworks/13` ch.3) |
| P5 = before paying customers | 5 Proof | The output is a **harvest and measurement plan**, not a library of assets that don't exist |
| P5 = before PMF | 12 Metrics | PMF signals first (Sean Ellis 40%, retention curve), funnel KPIs second (`Frameworks/13` ch.4) |
| P2 = Retainer / Project | 6 Pricing | Value ladder (bait → front end → core → top + continuity); floor/ceiling corridor; 3 tiers |
| P2 = Subscription / Usage | 6 Pricing | Value metric first, tiers by usage or seats, free trial or freemium vs paid pilot |
| P2 = Transaction / commission | 6 Pricing | `SOURCE-GAP`: no source in `Learning_resources/` covers marketplace take rates. Price from the floor/ceiling method, and mark the take-rate choice `ASSUMED` |
| P3 > 50K, P4 = 7+ people, heavy setup | 8 Motion | Sales-led (or partner-led) |
| P3 = 10–50K, buyers research online | 8 Motion | Marketing-led + sales-led hybrid |
| P3 < 5K, self-serve, little or no setup | 8 Motion | Product-led; 9 Outbound and 10 Revenue Process stay light |
| P1 = Services or Productised service | 7 Demand gen | Funnel map A (lead magnet → call) or D (paid diagnostic) first |
| P1 = Software / SaaS | 7 Demand gen | Trial or demo funnel; activation is the conversion event |
| P8 = one or two people | 7, 9, 11 | One funnel, two channels, the smallest stack; outbound volume capped by the hours available |
| P9 = advisory | all | We write the strategy and the playbook artifacts; the client owns execution rows in the tracker |

These are starting points the playbook and frameworks already argue for, not rules. A pillar that
departs from a default says why, as a `PROPOSED` decision.

## Decided 2026-11-15 by the owner — pillar numbering

**Proof is Pillar 5, Pricing is Pillar 6**, everywhere: playbook, roadmap, skills and artifacts
(`06_Proof-System.md`, `07_Pricing-and-Packaging.md`). Phase 1 runs Proof before Pricing. Strategy-report
PDFs generated before this date keep the old numbering.

**Phase 2 artifact numbers — `LOCKED` by the owner 2026-11-16:** `09` GTM Motion · `10` Revenue Process & SLAs ·
`11` Demand Generation · `12` Outbound · `13` Enablement · `14` Metrics & Feedback · `15` Execution Audit.
Numbers follow the run order, not the pillar number.
