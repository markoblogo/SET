# Bounded Orchestration Contract

`SET` can export a disabled, provider-neutral planner-review-executor contract for downstream runners without becoming an agent scheduler or model router.

Select it with:

```json
"capability_profile": "bounded-orchestration"
```

The contract appears at `orchestrator_bundle.context_package.bounded_orchestration_contract`. It grants no execution or mutation authority.

## Plan protocol

- A planner emits `PLAN_DRAFT` with a versioned, complete plan.
- A reviewer returns `PLAN_APPROVED` for that exact version or `PLAN_REVISE` with findings.
- Findings use stable IDs such as `F-001`; IDs survive every round.
- A revised plan records every finding as `INCORPORATED` or `REJECTED` with a concrete reason. Unresolved `OPEN` findings block approval.
- Stop immediately on approval. Never exceed five review rounds. If round five still requires revision, halt before releasing executor work.

## Bounded executor packet

Every executor receives one self-contained packet with an ID, objective, boundaries, minimal context, owned files, dependencies, stop conditions, acceptance criteria, verification, and handoff format.

Parallel packets require non-overlapping file and write ownership. Overlap or unclear ownership blocks parallel release. Executors must preserve unrelated work and report blockers instead of widening scope.

## Route evidence

Use only these states:

- `route accepted`: the host accepted the requested route controls; runtime identity remains unproven.
- `used and confirmed`: host metadata proves the effective runtime model or route.
- `unavailable`: the route cannot run or cannot satisfy required controls.

Child prose, saved configuration, and model-name claims are not runtime confirmation.

## Root verification

Executor completion is evidence, not acceptance. The root integrates outputs, inspects the resulting diff or artifact, runs the smallest sufficient checks, and records integrated outputs, checks, result, and remaining risks before reporting completion.

## Boundary

SET exports this contract only. It does not spawn agents, schedule work, choose models/providers, mutate files, merge, release, perform external actions, or replace root and human authority.

## Attribution

Adapted from the role and handoff discipline in [Cjbuilds/Codex-Orchestration](https://github.com/Cjbuilds/Codex-Orchestration), rewritten as a provider-neutral, disabled-by-default SET contract without adopting the plugin runtime.
