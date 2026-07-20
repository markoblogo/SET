# SET Agents Contract

<!-- AGENTSGEN:START section=agentsgen_contract -->
## agentsgen_contract

- schema: compact-contract-v1
- expected_files:
  - AGENTS.md
  - RUNBOOK.md
  - docs/ai/task-contract.json
- check_mode: required
- repomap_mode: compact
<!-- AGENTSGEN:END section=agentsgen_contract -->

<!-- AGENTSGEN:START section=task_contract -->
## task_contract

- schema: task-contract-v1
- route_states: [accepted, used, confirmed]
- risk_class: low
- evidence_required: true
- owner: repo-maintainer
<!-- AGENTSGEN:END section=task_contract -->

<!-- AGENTSGEN:START section=verification -->
## verification

- lint:
  - `python3 -m json.tool .agentsgen.json`
- contracts:
  - `agentsgen check --all --ci`
- pack:
  - `agentsgen pack --autodetect --check --format=json`
<!-- AGENTSGEN:END section=verification -->
