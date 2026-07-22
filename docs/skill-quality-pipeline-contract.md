# Skill Quality Pipeline Contract

`SET` can export the optional `skill-quality-pipeline` profile for runners that want SkillOpt-style skill improvement without installing SkillOpt or enabling self-editing.

Use it in a registry entry:

```json
"capability_profile": "skill-quality-pipeline"
```

The contract appears at `orchestrator_bundle.context_package.skill_quality_pipeline_contract`. It is disabled by default and grants no write, publishing, or runtime authority.

## Contract

- Treat a skill as a versioned procedural artifact with measurable quality.
- Capture rollout evidence: task, input, skill ID, skill version, trajectory reference, verifier, score, and failure class.
- Generate only bounded `add`, `delete`, or `replace` edits; do not rewrite a whole skill or expand authority.
- Accept a candidate only when a held-out or independently selected validation set improves without protected-control regressions.
- Keep rejected edits in a buffer with the reason so weak, duplicate, overfit, or guardrail-reducing changes are not repeated.
- Export `best_skill.md` only after validation and explicit human acceptance.
- Treat SkillOpt-Sleep-like output as staged review material; automatic adoption is forbidden.

## Project Fit

- `SET`, ABVX Agent Skills, and Lab: `seed skill -> benchmark tasks -> candidate skill -> validation -> public/README update` after acceptance.
- `index`, 1d3x Cortex, and CortexABV: eval packets, `find-partners`, fallback-provider checks, editorial routing, and corpus-routing adapters.
- CoqPi: call-assist and translation prompt skills, plus future partner-finder prompts, using synthetic or recorded mock transcripts only.

## Non-Goals

- no SkillOpt install, vendoring, or runtime dependency;
- no harvesting of local transcripts or protected data;
- no automatic skill mutation, publication, or adoption;
- no connection to live calls, outbound messaging, transactions, production routes, or protected-data writes.
