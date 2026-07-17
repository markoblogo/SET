# Bug Evidence Contract

`bug-evidence` is a disabled, provider-neutral contract for proving or rejecting a bug and an approved fix. It complements `diagnose`, `test-driven-execution`, and a durable `cpat`; it does not create an autonomous bug scanner or parallel debugging workflow.

## Authority and approval

Existing task authorization covers reversible local tests and fixes already inside the requested scope. Separate explicit approval remains required for production or device writes, destructive migrations or data mutation, out-of-scope dependency/configuration changes, security/privacy/financial/protected-evidence boundaries, scope expansion, and explicit audit-only or reproduce-only work.

## Evidence packet

A packet records a stable evidence ID, repository identity, Git SHA before and after, targeted command records before and after, captured broader checks, symptom-match evidence, route evidence, classification, limitations, and an optional `cpat_id`.

Each command record includes argv, a SHA-256 command identity, cwd, runtime, selected environment identifiers, capture time, duration, exit code, timeout state, bounded stdout/stderr, truncation, and redaction state. Do not persist credentials, tokens, personal data, protected evidence, or full environment dumps.

Route evidence uses exactly:

- `route accepted`: the host accepted route controls but runtime use is not proven;
- `used and confirmed`: host runtime metadata confirms effective use;
- `unavailable`: routing is absent, failed, or not relevant, with a reason.

## Honest classification

Allowed statuses are `REPRODUCED`, `NOT_REPRODUCED`, `NO_BUG_PROVEN`, `INCONCLUSIVE`, `STILL_FAILING`, `FIX_UNVERIFIED`, `FIX_REGRESSION`, and `FIX_PROVEN`.

`FIX_PROVEN` requires the same targeted command hash, a failing before record matching the reported or predicted symptom, a passing after record, and passing captured relevant broader checks. A manual `full_suite=passed` flag is not evidence. If a relevant broader check fails, use `FIX_REGRESSION`; if broader captured evidence is insufficient, use `FIX_UNVERIFIED`.

## Durable handoff

When the lesson is recurrent, link the evidence ID from a `cpat` verification section. Keep bulky or protected evidence in its authoritative store; the `cpat` retains only the minimum reference, result, and prevention guard.

## Boundary

`SET` exports this contract only. It does not execute tests, inspect code, install the upstream npm package, overwrite local skills, grant mutation authority, or treat source inspection alone as reproduction evidence.

Adapted from the consent-first reproduction and red-to-green evidence patterns in [`Kappaemme-git/codex-bug-reproducer`](https://github.com/Kappaemme-git/codex-bug-reproducer), with risk-based approval and captured-check classification for ABVX workflows.
