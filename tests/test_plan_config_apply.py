from __future__ import annotations

from pathlib import Path

import scripts.plan_config_apply as planner


def test_build_plan_for_set_is_planning_only() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    plan = planner.build_plan(config_path, data)
    assert plan['dry_run'] is True
    assert plan['mode'] == 'planning-only'
    assert plan['review_payload']['dry_run'] is True
    assert 'workflow_preset' in plan['proposed_changes'][0]['workflow']['with']
    assert isinstance(plan['review_payload']['capabilities'], list)


def test_plan_dry_run_flag_is_parsed_explicitly() -> None:
    args = planner.parse_args(['markoblogo/SET', '--dry-run', '--format', 'json'])
    assert args.dry_run is True


def test_repo_root_drift_check_for_set_matches_expected_workflow() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    repo_root = Path(__file__).resolve().parents[1]
    plan = planner.build_plan(config_path, data, repo_root=repo_root)
    assert plan['workflow_check']['status'] == 'matches'
    assert plan['workflow_check']['workflow_path'] == '.github/workflows/set.yml'
