# Ship Router Contract

`SET` can export a compact ship router contract that selects the smallest
execution path likely to finish safely, without turning `SET` into a runtime,
scheduler, or agent platform.

Use it when the question is not only "what should we do?" but also "what kind
of path should carry this work to a real ship decision?"

## Goal

Route work into the right delivery lane before execution widens:

- direct implementation;
- review-only or audit-first pass;
- bounded loop or repeated sweep;
- human approval gate;
- blocked or local-only route.

The contract should reduce false starts, avoid premature automation, and keep
authority explicit.

## Minimal route packet

Every proposed route should name:

- `route_id`
- `objective`
- `target_surface`
- `recommended_lane`
- `why_this_lane`
- `authority`
- `required_evidence`
- `approval_boundary`
- `can_ship`
- `next_check`

The packet is a routing recommendation, not execution permission.

## Recommended lanes

- `direct` — a scoped task can proceed with normal repo rules and bounded
  verification.
- `review_first` — proof, audit, browser check, or design review should happen
  before implementation or release claims.
- `bounded_loop` — repeated work is justified, but only with explicit cadence,
  stop conditions, and owner review.
- `human_gate` — external action, release, migration, secret use, or broad
  mutation needs explicit approval before continuing.
- `blocked` — required authority, evidence, or prerequisites are missing.

## Route states

Use small explicit states:

- `route proposed`
- `route approved`
- `route active`
- `ship review required`
- `shipped within reviewed scope`
- `blocked`

Do not treat a draft lane choice as approval or shipment.

## Evidence discipline

A route is only strong if its evidence matches the claimed lane.

Examples:

- `direct` still needs the smallest sufficient verification.
- `review_first` must say which review contract or artifact is required.
- `bounded_loop` must include cadence, stop condition, and owner.
- `human_gate` must say exactly what approval unlocks the next step.

## Boundary

- `SET` may export the route contract, not execute it automatically.
- The route does not replace repo-local rules, proof, or release discipline.
- A route can narrow work, but it cannot silently widen authority.
- Shipping still requires root and human judgment where the repo contract says
  so.

## Attribution

Adapted from the routing and delivery framing in
[AgentSystemLabs/core](https://github.com/AgentSystemLabs/core), rewritten as a
small provider-neutral contract for `SET`.
