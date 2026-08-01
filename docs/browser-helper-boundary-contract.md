# Browser Helper Boundary Contract

`SET` may allow a local browser helper for scoped web tasks. This does not make
the helper a default browser, a background agent, or a trusted external-action
executor.

This contract records the acceptable local use of tools such as
`citrolabs/ego-lite`: a browser designed for human and agent parallel work in
separate spaces.

Source: https://github.com/citrolabs/ego-lite

## Default stance

Browser helpers are disabled unless a task explicitly needs browser state,
logged-in surface review, visual QA, or web interaction that cannot be handled
through static source files.

Use them per task, not as an always-on route.

## Allowed use

- public website QA;
- logged-in dashboard review after explicit domain scope;
- source verification for research tasks;
- screenshot/snapshot evidence collection;
- form or workflow inspection without submission;
- local browser automation in an isolated helper space.

## Not allowed

- payments, contracts, purchases, or bookings;
- sending messages, emails, posts, comments, or outreach;
- changing account settings;
- entering credentials for the agent;
- broad browsing of private tabs or history;
- background monitoring;
- treating private page snapshots as publishable evidence.

## Required preflight

Before using a browser helper, record:

- `target_domain`;
- `task_goal`;
- `account_surface`;
- `allowed_actions`;
- `blocked_actions`;
- `private_data_expected`;
- `evidence_to_collect`;
- `owner_confirmation_required`.

## Receipt

After use, record:

- domain and URL scope actually visited;
- action attempted;
- evidence captured;
- external side effects;
- private data observed;
- whether owner follow-up is required.

## Project routing

| Target | Status | Boundary |
|---|---|---|
| `index` / MediaHub | allowed_optional | source/dashboard review only |
| `CortexABV-private` | allowed_optional | private research and proposal evidence only |
| `CoqPi` | allowed_optional | pre-call research only |
| `Menton` / `book-landings` / public sites | allowed_optional | visual QA and publication checks |
| payments, contracts, messaging | blocked | owner must act directly |

## Acceptance rule

A browser helper route is accepted only when the target domain, allowed actions,
and blocked actions are explicit before the session starts. Any write-like or
externally visible action requires separate owner confirmation at the moment of
action.
