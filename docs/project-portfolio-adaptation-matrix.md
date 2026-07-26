# Project Portfolio Adaptation Matrix

Date: 2026-07-26

This is a compact working portfolio index for the ABVX ecosystem and related
product repos.

It is not a full inventory of every local checkout. It intentionally excludes:

- temporary donor-review clones;
- one-off experiment folders;
- duplicate worktrees;
- service copies whose owning product repo is already listed.

Use it for two tasks:

1. decide how a project should evolve;
2. route each new external repo, skill, runtime, or method across the full
   portfolio instead of evaluating it only against the currently active repo.

## How to use this matrix

For every new donor idea, classify each listed repo as:

- `high fit`
- `possible fit`
- `low fit`
- `owner layer first`
- `not useful now`

Then decide whether the idea belongs first in:

- `SET`
- `AGENTS.md_generator`
- `ID`
- a downstream product repo

See [docs/donor-adaptation-target-matrix.md](donor-adaptation-target-matrix.md)
for the owning-layer rule.

## Portfolio

| Repo | Role | Stage | Useful donor classes | Usually not useful |
| --- | --- | --- | --- | --- |
| `SET` | orchestration, planning, capability-routing layer | active | contracts, receipts, approval gates, portfolio routing, cross-repo policy, eval/adaptation registry | UI-only polish, product-specific runtime hacks, human-profile internals |
| `AGENTS.md_generator` | repo-readable contract and pack/check runtime | active | `AGENTS.md` structure, repo read-order, proof commands, drift control, pack/check/fix loops, repo context compression | orchestration meta-policy, human memory lifecycle |
| `ID` | portable human-context protocol and release layer | active | profile lifecycle, `soul.md`, diff/provenance/freshness, share safety, public/private context boundaries | repo contract generation, workflow orchestration policy |
| `abvx-agent-skills` | reusable portable skillpack | active | skill review pipelines, compact review contracts, eval harnesses for skills, anti-slop/prose/frontend review patterns | product-specific business logic, heavy runtimes, project-local workflow state |
| `lab.abvx` | public ecosystem hub and catalog | active | public-facing docs surfaces, trust/proof presentation, discoverability, AI/LLM-readable entry surfaces, design blueprint for public pages | private runtime logic, internal ops receipts, device-specific firmware rules |
| `ABVXsite` | public ABVX ecosystem site and publishing surface | active | editorial/design review, content graph improvements, AI-visibility, browser-readable/public artifacts, schema/discovery improvements | private ops tooling, repo-contract internals, firmware/runtime-specific helpers |
| `index` | multi-tenant index platform, media and Cortex-adjacent surfaces | active | dashboards/artifacts, intake routing, media workflows, AI-visibility, browser-readable status pages, capability-aware provider routing | generic skill authoring infrastructure, identity-profile logic |
| `CortexABV-private` | local private runtime/bootstrap and proposal store | active | retrieval observability, private review artifacts, receipts, scoped memory, provider/tool registry, import governance | public marketing polish, chat-bot UX patterns as primary layer |
| `CoqPi` | private live language-call desktop assistant | active pilot | call-assist prompt/skill evals, selected-context routing, privacy/redaction, local fallback models, research-only finder/intake modules | broad autonomous multi-agent orchestration, public growth/UI ornamentation |
| `MN7R` | private brokerage workspace and monitors | active pilot | operation receipts, human approval gates, reporting artifacts, provider boundaries, optional continuous review, runtime-path verification | decorative README/design work as a primary focus, consumer-chat patterns |
| `cropto` | commodity trading/monitoring MVP surface | active prototype | product positioning, public proof/trust surfaces, routing of market/reference data workflows, AI-visibility, selective frontend review | deep human-profile protocol work, repo-generator internals |
| `DMVg` (`liqua`) | multi-tenant agro corporate platform matrix | active concept/build | system maps, design blueprints, multi-tenant contracts, content/schema routing, visibility/discovery, intake and review surfaces | agent-skill internals, human identity lifecycle |
| `menton` (`azurmenton`) | multilingual direct-booking/property publishing site | active | SEO/visibility audits, editorial/design review, public trust surfaces, browser-readable artifacts, content-map improvements | orchestration runtimes, private AI memory/protocol layers |
| `cardputer` | device firmware and on-device shell | active experimental | bug-evidence/cpat patterns, runtime-path verification, troubleshooting artifacts, reduced-surface browser-readable docs, local model selection as optional backend boundary | web-growth playbooks, heavy cloud-agent orchestration, generic README beautification as priority |

## Near-term evolution vectors

| Repo | Next useful directions |
| --- | --- |
| `SET` | portfolio-wide routing docs, adaptation/eval registry, slimmer public docs, clearer profile selection |
| `AGENTS.md_generator` | stronger repo-read-order generation, pack/check report surfaces, optional blast-radius and proof guidance |
| `ID` | stronger owner-review lifecycle, compact release flows, better public/private export boundaries |
| `abvx-agent-skills` | benchmarked skill quality, tighter review/eval loops, cleaner public cataloging of high-SNR skills |
| `lab.abvx` | clearer ecosystem navigation, public proof surfaces, stronger role separation across MCP/CLI/skills/contracts |
| `ABVXsite` | sharper ecosystem positioning, stronger AI-readable content surfaces, curated project/program pages |
| `index` | MediaHub/DMV-style artifacts, intake routing, reusable daily/weekly review pages, better visibility analytics |
| `CortexABV-private` | proposal-pack review standardization, retrieval/import observability, better tenant-scoped receipts |
| `CoqPi` | research-only partner-finder/finder intake, safer transcript/context routing, local fallback testing |
| `MN7R` | operational reporting surfaces, governed execution receipts, stronger review-before-action boundaries |
| `cropto` | public product clarity, proof-backed feature surfaces, partner-reviewable but bounded demos |
| `DMVg` (`liqua`) | multi-tenant product architecture clarity, better system maps, more explicit platform-vs-tenant boundaries |
| `menton` (`azurmenton`) | visibility/SEO loops, page-level trust upgrades, content graph strengthening |
| `cardputer` | device troubleshooting standards, browser-readable operator docs, safe companion/local-backend experiments |

## Portfolio routing defaults

When evaluating a new donor repo:

- start with `SET`, `AGENTS.md_generator`, and `ID` as owning-layer checks;
- then review active downstream repos:
  `index`, `CortexABV-private`, `CoqPi`, `MN7R`, `ABVXsite`, `lab.abvx`,
  `cropto`, `DMVg`, `menton`, `cardputer`;
- use `possible fit` only when there is a concrete path to a bounded local
  contract, artifact, or pilot;
- avoid “good idea somewhere in the ecosystem” as a reason to install or adapt.

## Notes

- `cardputer-abvx-minimal` and `cardputer-userdemo-abvx` are treated as
  derivative firmware lines, not separate portfolio projects.
- temporary checkouts under dated Codex folders remain source material, not
  portfolio entries.
