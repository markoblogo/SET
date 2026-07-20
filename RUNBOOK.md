# SET Runbook (Pilot)

## Contracts
- Keep `AGENTS.md`, `RUNBOOK.md`, and `docs/ai/task-contract.json` aligned with `AGENTSGEN` section markers.

## Daily checks
- `python3 -m json.tool .agentsgen.json`
- `agentsgen check --all --ci`
- `agentsgen pack --autodetect --check --format=json`
