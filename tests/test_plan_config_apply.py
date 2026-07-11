from __future__ import annotations

from pathlib import Path

import scripts.plan_config_apply as planner


def test_build_plan_for_set_is_planning_only() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    plan = planner.build_plan(config_path, data)
    assert plan['dry_run'] is True
    assert plan['mode'] == 'planning-only'
    assert plan['review_payload']['dry_run'] is True
    assert plan['orchestrator_bundle']['kind'] == 'set-orchestrator-bundle'
    assert plan['orchestrator_bundle']['target_workflow']['preset'] == 'repo-docs'
    assert 'workflow_preset' in plan['proposed_changes'][0]['workflow']['with']
    assert isinstance(plan['review_payload']['capabilities'], list)


def test_orchestrator_bundle_carries_proof_loop_contract() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    plan = planner.build_plan(config_path, data)
    bundle = plan['orchestrator_bundle']
    assert bundle['context_package']['repomap_policy_mode'] == 'changed'
    assert bundle['context_package']['rabbithole_seed']['artifact'] == 'rabbithole.seed.md'
    memory = bundle['context_package']['memory_capability']
    assert memory['enabled'] is False
    assert memory['scope']['model'] == 'per-project'
    assert memory['retrieval']['modes'] == ['full_text', 'semantic']
    assert memory['operations']['write']['policy'] == 'audit-gated-proposal-first'
    diversity = bundle['context_package']['research_diversity_hint']
    assert diversity['kind'] == 'review-hint'
    assert diversity['recommended_skill'] == 'hypothesis-diversification'
    assert 'SET does not run a diversity runtime' in diversity['non_goals']
    context_budget = bundle['context_package']['context_budget_hint']
    assert context_budget['kind'] == 'review-hint'
    assert context_budget['recommended_skill'] == 'context-degradation-review'
    degradation = bundle['context_package']['context_degradation_review']
    assert 'context-poisoning' in degradation['failure_modes']
    assert 'SET does not run context repair automatically' in degradation['non_goals']
    loop = bundle['context_package']['loop_readiness_hint']
    assert loop['kind'] == 'review-hint'
    assert loop['recommended_skill'] == 'loop-readiness-review'
    assert loop['readiness_levels']['L1'] == 'report-only'
    assert 'SET does not schedule loops' in loop['non_goals']
    assert bundle['task_contract']['proof_loop']['task_id'] == 'proof-loop-blocked'
    assert bundle['task_contract']['expected_artifacts'] == ['docs/ai/proof/manual-review.md']
    assert bundle['task_contract']['recommended_review_lenses'][0]['name'] == 'assumption-excavation'
    lens_names = [lens['name'] for lens in bundle['task_contract']['recommended_review_lenses']]
    assert 'context-degradation-review' in lens_names
    assert 'agent-tool-contract-review' in lens_names
    assert lens_names[-1] == 'loop-readiness-review'
    assert bundle['task_contract']['proposal_lifecycle']['default_policy'] == 'proposal-first'
    assert bundle['task_contract']['proposal_lifecycle']['states'] == [
        'run',
        'retained_output',
        'inspect',
        'select',
        'apply',
        'discard',
    ]


def test_export_plan_writes_orchestrator_bundle(tmp_path: Path) -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    plan = planner.build_plan(config_path, data)
    written = planner.export_plan(plan, tmp_path)
    names = {path.name for path in written}
    assert 'orchestrator-bundle.json' in names
    assert 'proposal-lifecycle.json' in names
    assert 'rabbithole.seed.md' in names


def test_plan_dry_run_flag_is_parsed_explicitly() -> None:
    args = planner.parse_args(['markoblogo/SET', '--dry-run', '--format', 'json'])
    assert args.dry_run is True


def test_repo_root_drift_check_for_set_matches_expected_workflow() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    repo_root = Path(__file__).resolve().parents[1]
    plan = planner.build_plan(config_path, data, repo_root=repo_root)
    assert plan['workflow_check']['status'] == 'matches'
    assert plan['workflow_check']['workflow_path'] == '.github/workflows/set.yml'
