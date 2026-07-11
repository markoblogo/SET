from __future__ import annotations

import argparse
import difflib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / 'registry' / 'repos'


SUPPORTED_AGENTSGEN_FIELDS = {
    'init': 'init',
    'pack': 'pack',
    'check': 'check',
    'repomap': 'repomap',
    'snippets': 'snippets',
    'analyze_url': 'analyze',
    'meta_url': 'meta',
}

SUPPORTED_ID_FIELDS = {
    'pre_task': 'id_pre_task',
    'weekly_review': 'id_weekly_review',
}

DEFAULT_REPOMAP_POLICY = {
    'compact_budget': 4000,
    'top_ranked_files': 5,
    'focus': None,
    'changed': False,
}

DEFAULT_MEMORY_CAPABILITY = {
    'enabled': False,
    'kind': 'optional-memory-capability',
    'scope': {
        'model': 'per-project',
        'key': 'repo',
        'cross_project_reads': False,
    },
    'retrieval': {
        'modes': ['full_text', 'semantic'],
        'policy': 'hybrid-when-available',
        'fallback': 'full_text',
    },
    'operations': {
        'search': {
            'purpose': 'find relevant project memory before planning or changing code',
            'required_before_mutation': True,
        },
        'read': {
            'purpose': 'inspect the full source document after a relevant search hit',
            'requires_search_reference': True,
        },
        'write': {
            'purpose': 'retain a reviewed decision, constraint, or durable lesson',
            'policy': 'audit-gated-proposal-first',
            'raw_sources_read_only': True,
            'backup_or_snapshot_required': True,
        },
    },
    'non_goals': [
        'SET does not store memory',
        'SET does not provide an MCP server',
        'memory writes are not implicit completion evidence',
    ],
}

DEFAULT_REVIEW_LENSES = [
    {
        'name': 'assumption-excavation',
        'phase': 'pre-implementation',
        'purpose': 'surface hidden assumptions before implementation or runner handoff',
    },
    {
        'name': 'pipeline-readiness-gate',
        'phase': 'pre/post/ship',
        'purpose': 'choose the smallest useful review gate for the current phase',
    },
    {
        'name': 'confidence-fragility-review',
        'phase': 'ship',
        'purpose': 'check whether confident claims are backed by evidence',
    },
    {
        'name': 'hypothesis-diversification',
        'phase': 'research/adversarial-review',
        'purpose': 'generate distinct alternatives before evidence review when first-answer mode collapse is risky',
    },
    {
        'name': 'context-degradation-review',
        'phase': 'handoff/context-review',
        'purpose': 'check for context poisoning, lost-in-the-middle failures, distraction, context clash, and stale carryover',
    },
    {
        'name': 'agent-tool-contract-review',
        'phase': 'contract-design',
        'purpose': 'review SET inputs, CLI/MCP tools, and generated agent instructions as explicit tool contracts',
    },
    {
        'name': 'loop-readiness-review',
        'phase': 'pre-schedule/pre-runner',
        'purpose': 'check recurring agent loops for cadence, state, isolation, verifier, budget, run log, rollback, and human gate',
    },
]

DEFAULT_RESEARCH_DIVERSITY_HINT = {
    'enabled': True,
    'kind': 'review-hint',
    'recommended_skill': 'hypothesis-diversification',
    'pattern': 'diversity-first-research',
    'use_when': [
        'a plan or explanation may collapse onto the first plausible story',
        'market, incident, product, or architecture analysis needs adversarial alternatives',
        'SkillOpt-style proposal generation needs multiple bounded candidates before validation',
    ],
    'workflow': [
        'generate distinct hypotheses or bounded proposals',
        'record evidence needed and disconfirming signals',
        'rank by evidence readiness rather than model confidence',
        'handoff to validation, proof loop, or human review',
    ],
    'non_goals': [
        'SET does not run a diversity runtime',
        'SET does not treat model-stated probabilities as calibrated probabilities',
        'SET does not make financial, trading, legal, medical, or safety decisions',
    ],
}

DEFAULT_CONTEXT_BUDGET_HINT = {
    'enabled': True,
    'kind': 'review-hint',
    'recommended_skill': 'context-degradation-review',
    'pattern': 'context-budget-review',
    'budget_surfaces': [
        'system and developer instructions',
        'user request',
        'repo-local durable docs',
        'memory or handoff summaries',
        'retrieved files and tool output',
        'orchestrator bundle fields',
    ],
    'workflow': [
        'identify authoritative sources',
        'demote stale or supporting-only context',
        'keep decisive constraints close to the active plan',
        'move bulky evidence into files or artifacts',
        'preserve only source-backed durable lessons',
    ],
    'non_goals': [
        'SET does not manage model context windows',
        'SET does not choose or rewrite runner prompts',
        'SET does not persist memory',
    ],
}

DEFAULT_CONTEXT_DEGRADATION_REVIEW = {
    'enabled': True,
    'kind': 'review-hint',
    'recommended_skill': 'context-degradation-review',
    'failure_modes': [
        'context-poisoning',
        'lost-in-the-middle',
        'distraction',
        'context-clash',
        'stale-carryover',
    ],
    'review_before': [
        'external runner handoff',
        'proposal apply',
        'memory write',
        'large generated documentation update',
    ],
    'non_goals': [
        'SET does not run context repair automatically',
        'SET does not override the current user message with memory or prior task history',
    ],
}

DEFAULT_LOOP_READINESS_HINT = {
    'enabled': True,
    'kind': 'review-hint',
    'recommended_skill': 'loop-readiness-review',
    'pattern': 'abvx-loop-readiness',
    'readiness_levels': {
        'L0': 'not loop-ready',
        'L1': 'report-only',
        'L2': 'proposal-first',
        'L3': 'governed loop',
    },
    'checks': [
        'cadence and stop rule',
        'durable state outside the model',
        'scope and denied targets',
        'worktree, branch, sandbox, or retained-output isolation',
        'verifier or maker-checker gate',
        'token, time, retry, and spend budget',
        'run log and failure record',
        'rollback or discard path',
        'human gate for writes, merges, releases, destructive actions, and external side effects',
    ],
    'safe_default': 'L1 report-only until state, verifier, budget, run log, rollback, and human gate are explicit',
    'non_goals': [
        'SET does not schedule loops',
        'SET does not spawn recurring agents',
        'SET does not manage worktrees',
        'SET does not auto-fix, auto-merge, deploy, or release',
    ],
}

DEFAULT_PROPOSAL_LIFECYCLE = {
    'states': [
        'run',
        'retained_output',
        'inspect',
        'select',
        'apply',
        'discard',
    ],
    'default_policy': 'proposal-first',
    'mutation_rule': 'runner output is retained separately and must not mutate the target workspace until apply',
    'settlement_actions': [
        {
            'name': 'select',
            'meaning': 'accept the proposal as the candidate output for the task without applying it to the target workspace',
        },
        {
            'name': 'apply',
            'meaning': 'merge or copy the selected proposal into the target workspace after review gates pass',
        },
        {
            'name': 'discard',
            'meaning': 'reject the retained output and leave the target workspace unchanged',
        },
    ],
}


def repomap_policy_mode(policy: dict[str, object] | None) -> str:
    if not isinstance(policy, dict):
        return 'full'
    focus = str(policy.get('focus', '') or '').strip()
    changed = bool(policy.get('changed', False))
    if focus and changed:
        return 'focus+changed'
    if focus:
        return 'focus'
    if changed:
        return 'changed'
    return 'full'


def repomap_policy_label(mode: str) -> str:
    return {
        'full': 'Full Repo Slice',
        'focus': 'Focused Code Slice',
        'changed': 'Changed Files Slice',
        'focus+changed': 'Hybrid Slice',
    }.get(mode, 'Full Repo Slice')





def resolve_id_config(tools: dict[str, object]) -> dict[str, object] | None:
    id_tool = tools.get('id')
    if not isinstance(id_tool, dict):
        return None
    enabled = id_tool.get('enabled') is True
    owner_id = str(id_tool.get('owner_id', '') or '').strip() or None
    target = str(id_tool.get('target', '') or 'set').strip() or 'set'
    pre_task = id_tool.get('pre_task') is True
    weekly_review = id_tool.get('weekly_review') is True
    if not enabled and not owner_id and not pre_task and not weekly_review:
        return None
    return {
        'enabled': enabled,
        'owner_id': owner_id,
        'target': target,
        'pre_task': pre_task,
        'weekly_review': weekly_review,
    }


def resolve_proof_loop_config(agentsgen: dict[str, object]) -> dict[str, object] | None:
    proof_loop = agentsgen.get('proof_loop')
    if not isinstance(proof_loop, dict):
        return None
    enabled = proof_loop.get('enabled') is True
    task_id = proof_loop.get('task_id')
    expected_artifacts = [
        str(item).strip()
        for item in proof_loop.get('expected_artifacts', [])
        if isinstance(item, str) and str(item).strip()
    ]
    if not enabled and not task_id and not expected_artifacts:
        return None
    return {
        'enabled': enabled,
        'task_id': str(task_id).strip() if isinstance(task_id, str) and str(task_id).strip() else None,
        'expected_artifacts': expected_artifacts,
    }


def build_capabilities(data: dict[str, object]) -> list[dict[str, object]]:
    tools = data.get('tools', {}) if isinstance(data.get('tools'), dict) else {}
    agentsgen = tools.get('agentsgen', {}) if isinstance(tools.get('agentsgen'), dict) else {}
    id_config = resolve_id_config(tools)
    capabilities: list[dict[str, object]] = []
    for key, value in agentsgen.items():
        if key == 'proof_loop':
            continue
        requested = False
        if isinstance(value, bool):
            requested = value
        elif isinstance(value, str):
            requested = bool(value)
        if value is None:
            requested = False
        if not requested:
            continue
        supported = key in SUPPORTED_AGENTSGEN_FIELDS
        item: dict[str, object] = {
            'tool': 'agentsgen',
            'key': key,
            'requested': True,
            'supported_by_set': supported,
        }
        if supported:
            item['set_input'] = SUPPORTED_AGENTSGEN_FIELDS[key]
        else:
            item['wiring_gap'] = {
                'kind': 'missing-set-input',
                'capability': f'agentsgen.{key}',
                'message': f'agentsgen.{key} is in registry but not yet wired into SET action inputs',
            }
        capabilities.append(item)
    proof_loop = resolve_proof_loop_config(agentsgen)
    if proof_loop and proof_loop.get('enabled'):
        capabilities.append({
            'tool': 'agentsgen',
            'key': 'proof_loop',
            'requested': True,
            'supported_by_set': True,
            'set_input': 'proof_loop',
            'task_id': proof_loop.get('task_id'),
        })
    if id_config and id_config.get('enabled'):
        for key, set_input in SUPPORTED_ID_FIELDS.items():
            if id_config.get(key) is True:
                capabilities.append({
                    'tool': 'id',
                    'key': key,
                    'requested': True,
                    'supported_by_set': True,
                    'set_input': set_input,
                    'owner_id': id_config.get('owner_id'),
                    'target': id_config.get('target'),
                })
    return capabilities


def resolve_repomap_policy(agentsgen: dict[str, object]) -> dict[str, object] | None:
    repomap_enabled = agentsgen.get('repomap') is True
    policy = agentsgen.get('repomap_policy')
    if not repomap_enabled and not isinstance(policy, dict):
        return None

    resolved = dict(DEFAULT_REPOMAP_POLICY)
    if isinstance(policy, dict):
        compact_budget = policy.get('compact_budget')
        top_ranked_files = policy.get('top_ranked_files')
        focus = policy.get('focus')
        changed = policy.get('changed')
        if isinstance(compact_budget, int) and compact_budget > 0:
            resolved['compact_budget'] = compact_budget
        if isinstance(top_ranked_files, int) and top_ranked_files > 0:
            resolved['top_ranked_files'] = top_ranked_files
        if focus is None or isinstance(focus, str):
            resolved['focus'] = focus
        if isinstance(changed, bool):
            resolved['changed'] = changed
    return resolved


def list_repo_configs() -> list[tuple[Path, dict[str, object]]]:
    entries: list[tuple[Path, dict[str, object]]] = []
    for path in sorted(REGISTRY_DIR.glob('*.json')):
        data = json.loads(path.read_text())
        if isinstance(data, dict) and isinstance(data.get('repo'), str):
            entries.append((path, data))
    return entries


def load_config(repo: str) -> tuple[Path, dict[str, object]]:
    for path, data in list_repo_configs():
        if data.get('repo') == repo:
            return path, data
    raise SystemExit(f'Repo config not found for {repo!r}')


def pick_workflow_preset(presets: list[str]) -> str | None:
    for name in ('site-ai', 'repo-docs', 'minimal'):
        if name in presets:
            return name
    return None


def render_workflow_yaml(workflow: dict[str, object]) -> str:
    with_block = workflow['with']
    lines = [
        'name: SET',
        '',
        'on:',
        '  workflow_dispatch:',
        '',
        'jobs:',
        '  set:',
        '    runs-on: ubuntu-latest',
        '    steps:',
        '      - uses: actions/checkout@v4',
        f"      - uses: {workflow['uses']}",
        '        with:',
    ]
    for key, value in with_block.items():
        lines.append(f'          {key}: "{value}"')
    return '\n'.join(lines) + '\n'


def repo_slug(repo: str) -> str:
    return repo.replace('/', '-')


def normalize_workflow_text(text: str) -> str:
    return text.rstrip() + '\n'


def compare_workflow(plan: dict[str, object], repo_root: Path) -> dict[str, object]:
    workflow = plan['proposed_changes'][0]['workflow']
    relative_path = Path(workflow['path'])
    actual_path = repo_root / relative_path
    expected_text = normalize_workflow_text(render_workflow_yaml(workflow))
    result: dict[str, object] = {
        'repo_root': str(repo_root),
        'workflow_path': str(relative_path),
        'actual_path': str(actual_path),
        'status': 'missing',
        'diff_preview': [],
    }
    if not actual_path.exists():
        return result
    actual_text = normalize_workflow_text(actual_path.read_text())
    if actual_text == expected_text:
        result['status'] = 'matches'
        return result
    diff_lines = list(
        difflib.unified_diff(
            expected_text.splitlines(),
            actual_text.splitlines(),
            fromfile='expected/.github/workflows/set.yml',
            tofile=str(relative_path),
            lineterm='',
        )
    )
    result['status'] = 'drift'
    result['diff_preview'] = diff_lines[:80]
    return result


def build_review_payload(
    repo: str,
    workflow: dict[str, object],
    capabilities: list[dict[str, object]],
    unmapped: list[str],
    repomap_policy: dict[str, object] | None,
    proof_loop: dict[str, object] | None,
    id_config: dict[str, object] | None,
    dry_run: bool = True,
) -> dict[str, object]:
    apply_readiness = 'blocked' if unmapped else 'ready'
    blocked_by = list(unmapped)
    workflow_yaml = render_workflow_yaml(workflow)
    branch_name = f'codex/set-plan-{repo_slug(repo)}'
    title = f'chore(set): plan config apply for {repo}'
    body_lines = [
        f'# Planned SET workflow for `{repo}`',
        '',
        'This is a planning-only export generated from the central SET registry.',
        '',
        '## Proposed workflow target',
        f'- Path: `{workflow["path"]}`',
        f'- Uses: `{workflow["uses"]}`',
        '',
        '## Resolved inputs',
    ]
    for key, value in workflow['with'].items():
        body_lines.append(f'- `{key}`: `{value}`')
    if unmapped:
        body_lines.extend(['', '## Unmapped fields'])
        for item in unmapped:
            body_lines.append(f'- {item}')
    if repomap_policy:
        body_lines.extend(
            [
                '',
                '## Repomap policy',
                f"- `mode`: `{repomap_policy_mode(repomap_policy)}`",
                f"- `label`: `{repomap_policy_label(repomap_policy_mode(repomap_policy))}`",
                f"- `compact_budget`: `{repomap_policy['compact_budget']}`",
                f"- `top_ranked_files`: `{repomap_policy['top_ranked_files']}`",
            ]
        )
        if repomap_policy.get('focus'):
            body_lines.append(f"- `focus`: `{repomap_policy['focus']}`")
        body_lines.append(f"- `changed`: `{str(bool(repomap_policy.get('changed', False))).lower()}`")
    if proof_loop and proof_loop.get('enabled'):
        body_lines.extend([
            '',
            '## Proof loop',
            '- `enabled`: `true`',
            f"- `task_id`: `{proof_loop.get('task_id') or 'missing'}`",
        ])
        if proof_loop.get('expected_artifacts'):
            body_lines.append(
                f"- `expected_artifacts`: `{', '.join(str(item) for item in proof_loop.get('expected_artifacts', []))}`"
            )
    if id_config and id_config.get('enabled'):
        body_lines.extend([
            '',
            '## ID integration',
            '- `enabled`: `true`',
            f"- `owner_id`: `{id_config.get('owner_id') or 'missing'}`",
            f"- `target`: `{id_config.get('target') or 'set'}`",
            f"- `pre_task`: `{str(bool(id_config.get('pre_task'))).lower()}`",
            f"- `weekly_review`: `{str(bool(id_config.get('weekly_review'))).lower()}`",
        ])
    body_lines.extend([
        '',
        '## Proposal lifecycle',
        '- `run`: execute in an isolated proposal/worktree context.',
        '- `retained_output`: keep generated files outside the target workspace.',
        '- `inspect`: review diffs, artifacts, proof-loop outputs, and review lenses.',
        '- `select`: mark the proposal as the candidate result.',
        '- `apply`: merge/copy selected output only after review.',
        '- `discard`: reject the proposal and leave the target workspace unchanged.',
    ])
    body_lines.extend([
        '',
        '## Notes',
        '- Generated by `python3 scripts/plan_config_apply.py`.',
        '- Planning only: no branch, no PR, no write to target repo.',
        '- Dry-run mode: proposed changes are explicit and would only be written with a manual apply flow.',
        f'- Would write: `{workflow["path"]}`',
    ])
    body = '\n'.join(body_lines) + '\n'
    apply_simulation = {
        'repo': repo,
        'base_branch': 'main',
        'head_branch': branch_name,
        'target_files': [
            {
                'path': workflow['path'],
                'source_export': 'workflow.set.yml',
                'action': 'write',
            }
        ],
        'suggested_commit_message': title,
        'manual_steps': [
            f'git checkout -b {branch_name}',
            f'cp workflow.set.yml {workflow["path"]}',
            f'git add {workflow["path"]}',
            f'git commit -m "{title}"',
            f'gh pr create --repo {repo} --base main --head {branch_name} --title "{title}" --body-file pr-body.md',
        ],
    }
    return {
        'version': 1,
        'kind': 'set-pr-payload',
        'repo': repo,
        'dry_run': dry_run,
        'capabilities': capabilities,
        'repomap_policy': repomap_policy,
        'repomap_policy_mode': repomap_policy_mode(repomap_policy),
        'proof_loop': proof_loop,
        'repomap_policy_label': repomap_policy_label(repomap_policy_mode(repomap_policy)),
        'apply_readiness': apply_readiness,
        'blocked_by': blocked_by,
        'operator_queue': '',
        'next_action_label': 'Resolve unmapped fields' if unmapped else 'Review and apply planned workflow',
        'recommended_operator_step': unmapped[0] if unmapped else apply_simulation['manual_steps'][0],
        'next_shell_command': apply_simulation['manual_steps'][0],
        'target_branch': 'main',
        'head_branch': branch_name,
        'target_workflow_path': workflow['path'],
        'title': title,
        'suggested_commit_message': title,
        'body': body,
        'workflow_yaml': workflow_yaml,
        'gh_pr_create': {
            'repo': repo,
            'base': 'main',
            'head': branch_name,
            'title': title,
            'body_file': 'pr-body.md',
        },
        'apply_simulation': apply_simulation,
    }


def build_orchestrator_bundle(
    repo: str,
    config_path: Path,
    workflow: dict[str, object],
    capabilities: list[dict[str, object]],
    unmapped: list[str],
    repomap_policy: dict[str, object] | None,
    proof_loop: dict[str, object] | None,
    id_config: dict[str, object] | None,
    dry_run: bool = True,
) -> dict[str, object]:
    workflow_with = workflow['with']
    expected_artifacts = []
    if proof_loop and proof_loop.get('expected_artifacts'):
        expected_artifacts = list(proof_loop.get('expected_artifacts', []))
    if id_config and id_config.get('enabled') and id_config.get('pre_task'):
        expected_artifacts.extend([
            'docs/ai/id-bootstrap.json',
            'docs/ai/id-bootstrap.prompt.md',
        ])
    return {
        'version': 1,
        'kind': 'set-orchestrator-bundle',
        'repo': repo,
        'mode': 'planning-only',
        'dry_run': dry_run,
        'source_config': str(config_path),
        'compatible_with': [
            'issue-to-agent-runners',
            'parallel-agent-runners',
            'proof-of-work-review-loops',
            'agent-coordination-protocols',
        ],
        'target_workflow': {
            'path': workflow['path'],
            'uses': workflow['uses'],
            'preset': workflow_with.get('workflow_preset'),
            'with': workflow_with,
        },
        'context_package': {
            'repomap_policy': repomap_policy,
            'repomap_policy_mode': repomap_policy_mode(repomap_policy),
            'repomap_policy_label': repomap_policy_label(repomap_policy_mode(repomap_policy)),
            'memory_capability': DEFAULT_MEMORY_CAPABILITY,
            'research_diversity_hint': DEFAULT_RESEARCH_DIVERSITY_HINT,
            'context_budget_hint': DEFAULT_CONTEXT_BUDGET_HINT,
            'context_degradation_review': DEFAULT_CONTEXT_DEGRADATION_REVIEW,
            'loop_readiness_hint': DEFAULT_LOOP_READINESS_HINT,
            'id_bootstrap': {
                'enabled': bool(id_config and id_config.get('enabled') and id_config.get('pre_task')),
                'owner_id': id_config.get('owner_id') if id_config else None,
                'target': id_config.get('target') if id_config else None,
                'artifacts': [
                    'docs/ai/id-bootstrap.json',
                    'docs/ai/id-bootstrap.prompt.md',
                ] if id_config and id_config.get('enabled') and id_config.get('pre_task') else [],
            },
            'rabbithole_seed': {
                'enabled': True,
                'artifact': 'rabbithole.seed.md',
                'purpose': 'optional local human-in-the-loop review seed for SET planner exports',
                'suggested_sources': [
                    'plan.json',
                    'orchestrator-bundle.json',
                    'workflow.set.yml',
                    'pr-body.md',
                ],
            },
        },
        'task_contract': {
            'proof_loop': proof_loop,
            'expected_artifacts': expected_artifacts,
            'recommended_review_lenses': DEFAULT_REVIEW_LENSES,
            'proposal_lifecycle': DEFAULT_PROPOSAL_LIFECYCLE,
            'review_ready_when': [
                'SET workflow plan is reviewed',
                'unmapped is empty',
                'expected artifacts are present or explicitly waived',
                'retained output has been inspected before select/apply',
            ],
            'blocked_by': list(unmapped),
        },
        'capabilities': capabilities,
        'handoff': {
            'recommended_runner_role': 'consume this bundle before spawning coding agents',
            'stable_inputs': [
                'repo',
                'target_workflow',
                'context_package',
                'task_contract',
            ],
            'non_goals': [
                'SET does not spawn coding agents',
                'SET does not own external runner state',
                'SET does not create branches or PRs in planning mode',
                'SET does not apply retained outputs without an external review/settlement step',
            ],
        },
    }


def render_rabbithole_seed(plan: dict[str, object]) -> str:
    workflow = plan['proposed_changes'][0]['workflow']
    bundle = plan['orchestrator_bundle']
    lines = [
        '# SET Rabbithole Seed',
        '',
        'Use this optional local seed to inspect a SET plan in Rabbithole before applying it or handing it to an external agent runner.',
        '',
        'Rabbithole is not required for SET. This file is a review aid, not source of truth.',
        '',
        '## Plan Summary',
        '',
        f"- Repo: `{plan['repo']}`",
        f"- Mode: `{plan['mode']}`",
        f"- Dry run: `{str(bool(plan.get('dry_run'))).lower()}`",
        f"- Target workflow: `{workflow['path']}`",
        f"- Action: `{workflow['uses']}`",
        f"- Preset: `{workflow['with'].get('workflow_preset', 'none')}`",
        f"- Apply readiness: `{derive_apply_readiness(plan)}`",
        '',
        '## Review Questions',
        '',
        '- Are the proposed workflow inputs correct for this repo?',
        '- Is `unmapped` empty or intentionally blocked?',
        '- Do expected proof-loop artifacts match the task?',
        '- Has any runner output been retained for inspection before apply?',
        '- Should this plan be handed to an external runner or reviewed manually first?',
        '',
        '## Proposal Lifecycle',
        '',
        '- `run` -> external runner works in an isolated proposal/worktree context.',
        '- `retained_output` -> generated files stay reviewable outside the target workspace.',
        '- `inspect` -> human or meta-agent reviews artifacts, diffs, and proof gates.',
        '- `select` -> mark one proposal as the candidate result.',
        '- `apply` -> merge/copy selected output after gates pass.',
        '- `discard` -> reject output with no target workspace mutation.',
        '',
        '## Recommended Review Lenses',
        '',
    ]
    for lens in bundle['task_contract']['recommended_review_lenses']:
        lines.append(f"- `{lens['name']}` ({lens['phase']}): {lens['purpose']}")
    lines.extend([
        '',
        '## Bundle Excerpt',
        '',
        '```json',
        json.dumps(bundle, indent=2),
        '```',
    ])
    return '\n'.join(lines) + '\n'


def build_plan(
    config_path: Path,
    data: dict[str, object],
    repo_root: Path | None = None,
    dry_run: bool = True,
) -> dict[str, object]:
    tools = data.get('tools', {}) if isinstance(data.get('tools'), dict) else {}
    agentsgen = tools.get('agentsgen', {}) if isinstance(tools.get('agentsgen'), dict) else {}
    presets = data.get('presets', []) if isinstance(data.get('presets'), list) else []
    workflow_preset = pick_workflow_preset([p for p in presets if isinstance(p, str)])
    repomap_policy = resolve_repomap_policy(agentsgen)
    proof_loop = resolve_proof_loop_config(agentsgen)
    id_config = resolve_id_config(tools)

    with_block: dict[str, str] = {'agentsgen': 'true', 'autodetect': 'true', 'path': '.'}
    if workflow_preset:
        with_block['workflow_preset'] = workflow_preset

    for key in ('init', 'pack', 'check', 'repomap', 'snippets'):
        if key in agentsgen and isinstance(agentsgen[key], bool):
            with_block[key] = 'true' if agentsgen[key] else 'false'
    if agentsgen.get('repomap') is True and repomap_policy:
        with_block['repomap_compact_budget'] = str(repomap_policy['compact_budget'])
        if isinstance(repomap_policy.get('focus'), str) and str(repomap_policy.get('focus')).strip():
            with_block['repomap_focus'] = str(repomap_policy['focus']).strip()
        if repomap_policy.get('changed') is True:
            with_block['repomap_changed'] = 'true'

    site = data.get('site') if isinstance(data.get('site'), dict) else {}
    site_url = site.get('url') if isinstance(site, dict) else None
    analyze_url = agentsgen.get('analyze_url')
    meta_url = agentsgen.get('meta_url')
    if isinstance(site_url, str) and site_url:
        with_block['site_url'] = site_url
        if workflow_preset == 'site-ai' or with_block.get('pack') == 'true':
            with_block['site_pack'] = 'true'
    if isinstance(analyze_url, str) and analyze_url:
        with_block['analyze'] = 'true'
        with_block['analyze_url'] = analyze_url
    if isinstance(meta_url, str) and meta_url:
        with_block['meta'] = 'true'
        with_block['meta_url'] = meta_url
    if proof_loop and proof_loop.get('enabled'):
        with_block['proof_loop'] = 'true'
        if proof_loop.get('task_id'):
            with_block['proof_task_id'] = str(proof_loop['task_id'])
        if proof_loop.get('expected_artifacts'):
            with_block['proof_expected_artifacts'] = ','.join(
                str(item) for item in proof_loop.get('expected_artifacts', [])
            )
    if id_config and id_config.get('enabled'):
        with_block['id_enabled'] = 'true'
        if id_config.get('owner_id'):
            with_block['id_owner_id'] = str(id_config['owner_id'])
        if id_config.get('target'):
            with_block['id_target'] = str(id_config['target'])
        if id_config.get('pre_task') is True:
            with_block['id_pre_task'] = 'true'
        if id_config.get('weekly_review') is True:
            with_block['id_weekly_review'] = 'true'

    capabilities = build_capabilities(data)
    unmapped = [
        capability['wiring_gap']['message']
        for capability in capabilities
        if capability.get('wiring_gap')
    ]

    if proof_loop and proof_loop.get('enabled') and not proof_loop.get('task_id'):
        unmapped.append('agentsgen.proof_loop is enabled but proof_task_id is missing')
    if id_config and id_config.get('enabled'):
        if not id_config.get('owner_id'):
            unmapped.append('id integration is enabled but owner_id is missing')
        if id_config.get('pre_task') is True and not id_config.get('target'):
            unmapped.append('id integration pre_task is enabled but target is missing')

    workflow = {
        'path': '.github/workflows/set.yml',
        'uses': 'markoblogo/SET@main',
        'with': with_block,
    }
    review_payload = build_review_payload(
        data['repo'],
        workflow,
        capabilities,
        unmapped,
        repomap_policy,
        proof_loop,
        id_config,
        dry_run=dry_run,
    )
    orchestrator_bundle = build_orchestrator_bundle(
        data['repo'],
        config_path,
        workflow,
        capabilities,
        unmapped,
        repomap_policy,
        proof_loop,
        id_config,
        dry_run=dry_run,
    )
    plan = {
        'version': 1,
        'dry_run': dry_run,
        'mode': 'planning-only',
        'repo': data['repo'],
        'source_config': str(config_path),
        'repomap_policy': repomap_policy,
        'repomap_policy_mode': repomap_policy_mode(repomap_policy),
        'proof_loop': proof_loop,
        'id_integration': id_config,
        'proposed_changes': [
            {
                'type': 'workflow',
                'workflow': workflow,
            }
        ],
        'capabilities': capabilities,
        'review_payload': review_payload,
        'orchestrator_bundle': orchestrator_bundle,
        'unmapped': unmapped,
        'notes': [
            'This planner does not open a PR or write files to the target repo.',
            'Use the output to review the intended SET workflow before any future apply step.',
        ],
    }
    plan['review_payload']['operator_queue'] = derive_operator_queue(plan)
    if repo_root is not None:
        plan['workflow_check'] = compare_workflow(plan, repo_root)
    return plan




def derive_status_hint(plan: dict[str, object]) -> str:
    if plan.get('unmapped'):
        return 'needs-wiring'
    return 'ready-for-review'


def derive_priority_hint(plan: dict[str, object]) -> str:
    workflow = plan['proposed_changes'][0]['workflow']
    preset = workflow['with'].get('workflow_preset')
    if plan['repo'] == 'markoblogo/lab.abvx':
        return 'high'
    if plan.get('unmapped'):
        return 'medium'
    if preset == 'site-ai':
        return 'high'
    return 'normal'


def derive_apply_readiness(plan: dict[str, object]) -> str:
    if plan.get('unmapped'):
        return 'blocked'
    return 'ready'


def derive_blocked_by(plan: dict[str, object]) -> list[str]:
    return list(plan.get('unmapped', []))


def derive_wiring_gaps(plan: dict[str, object]) -> list[dict[str, object]]:
    return [
        capability['wiring_gap']
        for capability in plan.get('capabilities', [])
        if isinstance(capability, dict) and capability.get('wiring_gap')
    ]


def derive_operator_queue(plan: dict[str, object]) -> str:
    if derive_apply_readiness(plan) == 'blocked' and derive_wiring_gaps(plan):
        return 'blocked-by-orchestrator'
    if derive_apply_readiness(plan) == 'ready' and derive_priority_hint(plan) == 'high':
        return 'ready-now'
    return 'review-later'


def derive_next_action_label(plan: dict[str, object]) -> str:
    if plan.get('unmapped'):
        return 'Resolve unmapped fields'
    return 'Review and apply planned workflow'


def derive_recommended_operator_step(plan: dict[str, object]) -> str:
    if plan.get('unmapped'):
        return plan['unmapped'][0]
    return plan['review_payload']['apply_simulation']['manual_steps'][0]


def derive_next_shell_command(plan: dict[str, object]) -> str:
    return plan['review_payload']['apply_simulation']['manual_steps'][0]


def derive_workflow_sync_status(plan: dict[str, object]) -> str:
    workflow_check = plan.get('workflow_check')
    if isinstance(workflow_check, dict):
        return str(workflow_check.get('status', 'unknown'))
    return 'not-checked'


def render_text(plan: dict[str, object]) -> str:
    workflow = plan['proposed_changes'][0]['workflow']
    with_block = workflow['with']
    gh_pr = plan['review_payload']['gh_pr_create']
    apply_sim = plan['review_payload']['apply_simulation']
    lines = [
        'SET config apply plan',
        f"repo: {plan['repo']}",
        f"source_config: {plan['source_config']}",
        f"target_workflow: {workflow['path']}",
        'with:',
    ]
    for key, value in with_block.items():
        lines.append(f'  {key}: {value}')
    unmapped = plan.get('unmapped', [])
    if unmapped:
        lines.append('unmapped:')
        for item in unmapped:
            lines.append(f'  - {item}')
        lines.append('blocked_by:')
        for item in derive_blocked_by(plan):
            lines.append(f'  - {item}')
        lines.append('wiring_gaps:')
        for gap in derive_wiring_gaps(plan):
            lines.append(f"  - {gap['message']}")
    lines.extend([
        f"apply_readiness: {derive_apply_readiness(plan)}",
        f"operator_queue: {derive_operator_queue(plan)}",
        f"wiring_gap_count: {len(derive_wiring_gaps(plan))}",
        f"dry_run: {str(plan.get('dry_run', False)).lower()}",
        'would_write:',
        f"  - {workflow['path']}",
        f"next_action_label: {derive_next_action_label(plan)}",
        f"recommended_operator_step: {derive_recommended_operator_step(plan)}",
        f"next_shell_command: {derive_next_shell_command(plan)}",
        f"workflow_sync_status: {derive_workflow_sync_status(plan)}",
        f"repomap_policy: {json.dumps(plan.get('repomap_policy')) if plan.get('repomap_policy') else 'none'}",
        f"proof_loop: {json.dumps(plan.get('proof_loop')) if plan.get('proof_loop') else 'none'}",
        f"id_integration: {json.dumps(plan.get('id_integration')) if plan.get('id_integration') else 'none'}",
        'review_bundle:',
        '  - plan.json',
        '  - workflow.set.yml',
        '  - pr-body.md',
        '  - gh-pr-create.json',
        '  - apply-simulation.json',
        '  - orchestrator-bundle.json',
        '  - proposal-lifecycle.json',
        '  - rabbithole.seed.md',
        'gh_pr_create:',
        f"  repo: {gh_pr['repo']}",
        f"  base: {gh_pr['base']}",
        f"  head: {gh_pr['head']}",
        f"  title: {gh_pr['title']}",
        f"  body_file: {gh_pr['body_file']}",
        'apply_simulation:',
        f"  base_branch: {apply_sim['base_branch']}",
        f"  head_branch: {apply_sim['head_branch']}",
        f"  target_file: {apply_sim['target_files'][0]['path']}",
        f"  commit_message: {apply_sim['suggested_commit_message']}",
        '  manual_steps:',
    ])
    for step in apply_sim['manual_steps']:
        lines.append(f'    - {step}')
    workflow_check = plan.get('workflow_check')
    if isinstance(workflow_check, dict):
        lines.extend([
            'workflow_check:',
            f"  status: {workflow_check.get('status', 'unknown')}",
            f"  actual_path: {workflow_check.get('actual_path', 'unknown')}",
        ])
        diff_preview = workflow_check.get('diff_preview', [])
        if diff_preview:
            lines.append('  diff_preview:')
            for item in diff_preview:
                lines.append(f'    {item}')
    return '\n'.join(lines)


def render_batch_text(plans: list[dict[str, object]]) -> str:
    lines = ['SET config apply batch summary', f'repo_count: {len(plans)}']
    for plan in plans:
        status_hint = derive_status_hint(plan)
        priority_hint = derive_priority_hint(plan)
        workflow = plan['proposed_changes'][0]['workflow']
        gh_pr = plan['review_payload']['gh_pr_create']
        lines.extend([
            f'- {plan["repo"]}',
            f'  workflow_preset: {workflow["with"].get("workflow_preset", "none")}',
            f'  target_workflow: {workflow["path"]}',
            f'  head_branch: {gh_pr["head"]}',
            f'  title: {gh_pr["title"]}',
            f'  status_hint: {status_hint}',
            f'  priority_hint: {priority_hint}',
            f'  apply_readiness: {derive_apply_readiness(plan)}',
            f'  operator_queue: {derive_operator_queue(plan)}',
            f'  wiring_gap_count: {len(derive_wiring_gaps(plan))}',
            f'  next_action_label: {derive_next_action_label(plan)}',
            f'  recommended_operator_step: {derive_recommended_operator_step(plan)}',
            f'  next_shell_command: {derive_next_shell_command(plan)}',
            f'  workflow_sync_status: {derive_workflow_sync_status(plan)}',
            f'  unmapped_count: {len(plan.get("unmapped", []))}',
        ])
    return '\n'.join(lines)


def export_plan(plan: dict[str, object], export_dir: Path) -> list[Path]:
    export_dir.mkdir(parents=True, exist_ok=True)
    review_payload = plan['review_payload']
    outputs = {
        'plan.json': json.dumps(plan, indent=2) + '\n',
        'workflow.set.yml': review_payload['workflow_yaml'],
        'pr-body.md': review_payload['body'],
        'gh-pr-create.json': json.dumps(review_payload['gh_pr_create'], indent=2) + '\n',
        'apply-simulation.json': json.dumps(review_payload['apply_simulation'], indent=2) + '\n',
        'orchestrator-bundle.json': json.dumps(plan['orchestrator_bundle'], indent=2) + '\n',
        'proposal-lifecycle.json': json.dumps(
            plan['orchestrator_bundle']['task_contract']['proposal_lifecycle'],
            indent=2,
        ) + '\n',
        'rabbithole.seed.md': render_rabbithole_seed(plan),
    }
    written = []
    for name, content in outputs.items():
        path = export_dir / name
        path.write_text(content)
        written.append(path)
    return written


def export_batch(plans: list[dict[str, object]], export_dir: Path) -> list[Path]:
    export_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    summary = {
        'version': 1,
        'mode': 'planning-only-batch',
        'repo_count': len(plans),
        'repos': [
            {
                'repo': plan['repo'],
                'head_branch': plan['review_payload']['gh_pr_create']['head'],
                'target_workflow': plan['proposed_changes'][0]['workflow']['path'],
                'title': plan['review_payload']['gh_pr_create']['title'],
                'status_hint': derive_status_hint(plan),
                'priority_hint': derive_priority_hint(plan),
                'apply_readiness': derive_apply_readiness(plan),
                'operator_queue': derive_operator_queue(plan),
                'blocked_by': derive_blocked_by(plan),
                'wiring_gaps': derive_wiring_gaps(plan),
                'next_action_label': derive_next_action_label(plan),
                'recommended_operator_step': derive_recommended_operator_step(plan),
                'next_shell_command': derive_next_shell_command(plan),
                'workflow_sync_status': derive_workflow_sync_status(plan),
                'repomap_policy': plan.get('repomap_policy'),
                'id_integration': plan.get('id_integration'),
                'workflow_check': plan.get('workflow_check'),
                'orchestrator_bundle': plan.get('orchestrator_bundle'),
                'unmapped_count': len(plan.get('unmapped', [])),
            }
            for plan in plans
        ],
    }
    batch_path = export_dir / 'batch-summary.json'
    batch_path.write_text(json.dumps(summary, indent=2) + '\n')
    written.append(batch_path)
    for plan in plans:
        repo_dir = export_dir / repo_slug(plan['repo'])
        written.extend(export_plan(plan, repo_dir))
    return written


def resolve_targets(repos: list[str], use_all: bool) -> list[tuple[Path, dict[str, object]]]:
    if use_all:
        return list_repo_configs()
    if not repos:
        raise SystemExit('Provide at least one repo or use --all')
    return [load_config(repo) for repo in repos]


def resolve_repo_roots(targets: list[tuple[Path, dict[str, object]]], values: list[str]) -> dict[str, Path]:
    if not values:
        return {}
    repo_names = [str(data['repo']) for _, data in targets]
    multi = len(repo_names) > 1
    mapping: dict[str, Path] = {}
    for value in values:
        if '=' in value:
            repo, path = value.split('=', 1)
            if repo not in repo_names:
                raise SystemExit(f'Unknown repo in --repo-root mapping: {repo}')
            mapping[repo] = Path(path)
            continue
        if multi:
            raise SystemExit('For multiple repos, pass --repo-root owner/name=/absolute/path')
        mapping[repo_names[0]] = Path(value)
    return mapping


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Planning-only SET config apply helper.')
    parser.add_argument('repos', nargs='*', help='Repo name(s) in owner/name format')
    parser.add_argument('--all', action='store_true', help='Plan against every repo in registry/repos')
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    parser.add_argument('--export-dir', help='Optional local directory for reviewable planner outputs.')
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Explicit planning-only mode. This is the current default behavior.',
    )
    parser.add_argument('--repo-root', action='append', default=[], help='Optional local repo root path for workflow drift checking. Use /path for one repo or owner/name=/path for multiple repos.')
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    targets = resolve_targets(args.repos, args.all)
    repo_roots = resolve_repo_roots(targets, args.repo_root)
    dry_run = True
    if args.dry_run:
        dry_run = True
    plans = [
        build_plan(
            config_path,
            data,
            repo_roots.get(str(data['repo'])),
            dry_run=dry_run,
        )
        for config_path, data in targets
    ]
    multi = len(plans) > 1
    if args.export_dir:
        if multi:
            written = export_batch(plans, Path(args.export_dir))
            for plan in plans:
                repo_dir = Path(args.export_dir) / repo_slug(plan['repo'])
                plan['exported_files'] = [str(path) for path in sorted(repo_dir.iterdir())]
            batch_summary_path = Path(args.export_dir) / 'batch-summary.json'
        else:
            written = export_plan(plans[0], Path(args.export_dir))
            plans[0]['exported_files'] = [str(path) for path in written]
            batch_summary_path = None
    else:
        written = []
        batch_summary_path = None

    if args.format == 'json':
        if multi:
            payload = {'version': 1, 'mode': 'planning-only-batch', 'repo_count': len(plans), 'plans': plans}
            if batch_summary_path:
                payload['batch_summary_file'] = str(batch_summary_path)
            print(json.dumps(payload, indent=2))
        else:
            print(json.dumps(plans[0], indent=2))
    else:
        if multi:
            print(render_batch_text(plans))
            if args.export_dir:
                print('exported_files:')
                if batch_summary_path:
                    print(f'  - {batch_summary_path}')
                for plan in plans:
                    for path in plan.get('exported_files', []):
                        print(f'  - {path}')
        else:
            print(render_text(plans[0]))
            if args.export_dir:
                print('exported_files:')
                for path in plans[0]['exported_files']:
                    print(f'  - {path}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
