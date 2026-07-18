# Loop Hardening Contract

`SET` can export the optional `loop-hardening` profile for repeated delivery work. It adapts three useful Loopkit patterns without installing a runner or granting execution authority.

## Harness stripping

Measure a representative baseline, disable one non-safety component in isolation, then classify it as `REMOVE`, `RESTORE`, `HARMFUL`, or `INCONCLUSIVE`. Never strip sandboxing, budgets, stop conditions, human gates, or root verification, and never modify a live run in place.

## Runtime-path sprint

Freeze a versioned packet containing the deliverable, 3–7 observable acceptance predicates, the real runtime path, exclusions, owned files, stop conditions, and verification. A revision creates a new version with a reason and human confirmation. The executor cannot accept its own result.

## Broken-window revalidation

Before a new sprint, exercise the latest accepted result through its actual runtime path and record `STILL_GREEN`, `REOPENED`, or `INCONCLUSIVE`. A failure stops new work, retains evidence, reopens the result, and proposes a bounded repair. It never triggers automatic revert, commit, merge, deploy, or release.

Build or source inspection is not runtime proof when device, browser, production, or external-system behavior is claimed. Root-owned verification remains required.
