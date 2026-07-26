# Donor Adaptation Target Matrix

Date: 2026-07-26

Use this matrix when evaluating an external repo, skill, runtime, or workflow
pattern for selective ABVX-style adaptation.

The point is to choose the right owning layer first, before creating a new
contract or changing a repo.

## Default targets

| Target | Put here when the donor idea changes... | Do not put here when the donor idea mainly changes... |
| --- | --- | --- |
| `SET` | orchestration, planning, approval flow, capability routing, receipts, policy gates, cross-repo adaptation policy | repo authoring discipline or human identity/profile lifecycle |
| `AGENTS.md_generator` (`agentsgen`) | repo-readable contract, `AGENTS.md`/`RUNBOOK.md` generation, pack/check/fix flows, read order, repo-context surfaces, proof commands, drift control | orchestration meta-policy or portable human context |
| `ID` | human-context lifecycle, profile structure, `soul.md`, freshness, provenance, semantic diffs, share/release safety, public/private context boundaries | repo workflow orchestration or repo-contract generation |

## Fast routing rule

If the donor idea changes:

- how agents read and verify a repo -> target `AGENTS.md_generator`;
- how a reviewed human context is modeled, validated, diffed, or shared ->
  target `ID`;
- how contracts, tools, approvals, and flows are routed across repos -> target
  `SET`.

## Secondary targets

After choosing the primary owning layer, ask whether the idea also needs a
secondary projection:

- into `SET` as an orchestration contract;
- into `AGENTS.md_generator` as a repo-readable rule or generated surface;
- into `ID` as a human-context or release artifact rule;
- into downstream repos only after the owning layer is clear.

Do not start by patching downstream repos when the owning layer is still
unclear.

## Typical examples

- route states, execution receipts, approval boundaries -> `SET`
- `AGENTS.md` structure, pack/read-order, repo proof commands -> `AGENTS.md_generator`
- `soul.md` precedence, profile lifecycle, identity diff, freshness -> `ID`
- README polish, product review heuristics, runtime-specific boundaries ->
  usually downstream repos after the owning layer is decided

## Boundary

- not every donor idea belongs in `SET`;
- not every repo-context idea belongs in `AGENTS.md_generator`;
- not every memory or profile idea belongs in `ID`;
- if the same idea appears relevant to all three, define the owning layer first
  and keep the others as projections, not duplicate sources of truth.
