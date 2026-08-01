# AI Engineering Reference Index Note

`SET` may use curated AI-engineering lists as reference indexes. They are not
dependency lists, roadmaps, or automatic donor approvals.

This note adds `owainlewis/awesome-artificial-intelligence` as a reviewed
reference-index source for practical AI engineering topics: RAG, agents, evals,
observability, deployment, coding agents, and production AI practices.

Source: https://github.com/owainlewis/awesome-artificial-intelligence

## Allowed use

- seed a short candidate list for a specific repo or capability;
- compare a new donor against known AI-engineering categories;
- route references into `CortexABV-private`, `CoqPi`, `index`, or
  `abvx-agent-skills` only after scope review;
- mark each entry as `reference`, `candidate`, `piloted`, or `rejected`;
- preserve why an entry was selected or rejected.

## Not allowed

- importing the whole awesome list into repo docs;
- treating list membership as approval to install or vendor a tool;
- generating backlog items without target repo and adaptation boundary;
- enabling weekly automation or background updates by default;
- using generic AI resources as substitutes for source-specific evaluation.

## Review fields

Use this compact shape when an entry is considered:

```text
source:
category:
target repo:
possible local use:
required adaptation:
data-egress risk:
status: reference | candidate | piloted | rejected
reason:
```

## Target fit

| Target | Useful categories |
|---|---|
| `CortexABV-private` | private RAG, memory governance, evals, observability, agent safety |
| `CoqPi` | selected-context retrieval, call-assist evals, privacy/redaction, local fallback |
| `index` / MediaHub | source monitoring, digest generation, RAG quality, observability |
| `abvx-agent-skills` | skill quality, evals, coding-agent workflows, review gates |
| `AGENTS.md_generator` | context-file quality, repo-reading discipline, multi-target exports |

## Acceptance rule

An awesome-list entry becomes actionable only after a local target, adaptation
boundary, and review status are recorded. Otherwise it remains a reference.
