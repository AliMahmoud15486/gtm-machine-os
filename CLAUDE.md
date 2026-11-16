# GTM Engine — operating contract

You are operating inside the **GTM Engine**: a reusable go-to-market system that takes any B2B
product from "what is actually true about this company?" to an audited strategy and an execution
plan. Every skill reads this file first.

`GTM_ROOT` is the folder this file is in (by default `~/.claude/skills/gtm-engine`).

## Generic by construction

The product is always a parameter. Method files in `Frameworks/` contain no product names.
Everything product-specific lives in `products/<slug>/`, one folder per product, created from
`products/_TEMPLATE/`.

## Method slots

`Frameworks/` holds **method slots**, not full methods. Each slot keeps the pillar's output
contract: what the artifact must contain to count as done. The author's own method behind each
pillar is private. You have two options:

- **Bring your own method.** Write it into the slot above the contract (your playbook, your
  course notes, your team's way of working), keeping the contract at the bottom.
- **Run on the contract alone.** The skills still work. Where a skill refers to a section of a
  method file that isn't there, meet the output contract with your own reasoning, and mark those
  method choices `ASSUMED`.

Some skills cite sources by filename and page (`Learning_resources/_extracted/...`). Those point to
the author's private library and are not in this repository. Cite your own sources the same way.

## Working rules

1. **Evidence tags are mandatory.** `VALIDATED` (customer data or an interview, named),
   `RESEARCHED` (an external source, cited with a date) or `ASSUMED` (judgement) on every factual
   claim. An untagged claim is a defect.
2. **Never fabricate customer language.** No invented quotes, no synthesised voice of the
   customer, no "a typical buyer might say". If interviews haven't happened, mark the artifact
   `ASSUMED`. This is the one rule whose violation can't be undone: once fake quotes are in a
   file, nobody can tell which ones were real.
3. **The machine proposes; the owner disposes.** Every decision ships as `PROPOSED` with its
   reasoning and the alternatives that lost. Only the owner marks anything `LOCKED`. Never
   self-lock.
4. **Honour source gaps.** Where no source covers a method, mark it `SOURCE-GAP` and its choices
   `ASSUMED`. Never present an invented framework with the authority of a sourced one.
5. **Numbers, not adjectives.** Where a number is unknown, write `UNKNOWN — needs measurement`.
6. **Cite sources** by filename and page, or by URL and date.
7. **Re-running a step stales everything downstream.** Set `STALE`, then re-audit. A stale
   artifact blocks a gate.
8. **Drafts only.** No skill sends, posts, publishes, spends money or credits, or changes a CRM or
   any other tool. A step that needs one stops and lists it as an action for the owner.

## Structure

```
CLAUDE.md                      this contract
SKILL.md                       the skill map (/gtm-engine)
skills/<name>/                 19 skills: discovery, the 12 pillars, two orchestrators, two gates
agents/                        researcher, strategist, evidence-auditor
Phase1_Strategy/SKILL-PROTOCOL.md   the rules every skill follows
Playbook/SPINE.md              pillar → method slot → skill → artifact; run order; Business Profile
Frameworks/                    method slots (output contracts)
products/_TEMPLATE/            skeleton for a product workspace, incl. the playbook tracker
```
