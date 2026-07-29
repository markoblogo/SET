# GEPA-Style Optimization Contract

`SET` can export a compact GEPA-style optimization contract for projects that
want bounded prompt or skill improvement without installing GEPA or enabling an
autonomous optimizer runtime.

## Use when

- a prompt, skill, router text, or agent-facing artifact already has a stable
  evaluator;
- execution traces contain useful side-information such as errors, judge notes,
  failure classes, or tool-output diagnostics;
- the team wants search over small candidate edits instead of one-shot prompt
  rewrites;
- acceptance should remain human-reviewed and held-out validated.

## Core contract

- Treat the target as a versioned text artifact, not a magic self-improver.
- Optimize against an explicit evaluator, rubric, or bounded task set.
- Preserve actionable side-information from traces; do not reduce everything to
  one score if the failure reason is available.
- Search with a fixed budget: candidate count, metric calls, and validation
  cost must be declared before the run.
- Prefer multiple bounded candidate proposals over the first plausible rewrite.
- Use held-out or independently selected validation before acceptance.
- Output is a proposal artifact with evidence, not an auto-adopted change.

## Good targets

- skills with repeated activation paths;
- system prompts or routing prompts with stable mock tasks;
- review rubrics or judge prompts with measurable disagreement/failure patterns;
- fallback-provider or response-style text where behavior can be scored without
  production side effects.

## Bad targets

- live calls, deals, payments, or outbound production actions;
- text with no stable evaluator or no review owner;
- changes that require protected transcripts or secret-bearing traces;
- full-system rewrites disguised as “optimization”.

## Boundary

This contract is disabled, proposal-first, and planning-only. It does not
install GEPA, run continuous search, mutate prompts automatically, or widen
write authority.
