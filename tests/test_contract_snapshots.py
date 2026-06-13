from __future__ import annotations

import json
from pathlib import Path

import scripts.plan_config_apply as planner


def _fixture(name: str) -> dict[str, object]:
    path = Path(__file__).parent / 'fixtures' / name
    return json.loads(path.read_text())


def _plan_signature(plan: dict[str, object]) -> dict[str, object]:
    workflow = plan['proposed_changes'][0]['workflow']
    return {
        'version': plan['version'],
        'mode': plan['mode'],
        'dry_run': plan['dry_run'],
        'repo': plan['repo'],
        'review_payload_version': plan['review_payload']['version'],
        'review_payload_dry_run': plan['review_payload']['dry_run'],
        'workflow_path': workflow['path'],
        'workflow_with_key_count': len(workflow['with']),
        'workflow_with_keys': sorted(workflow['with'].keys()),
        'unmapped_count': len(plan.get('unmapped', [])),
        'capability_count': len(plan['review_payload']['capabilities']),
        'repomap_policy_mode': plan['repomap_policy_mode'],
        'would_write': workflow['path'],
        'apply_readiness': plan['review_payload']['apply_readiness'],
    }


def _knowledge_signature(payload: dict[str, object]) -> dict[str, object]:
    return {
        'version': payload['version'],
        'repo_path': payload['repo_path'],
        'file_count': len(payload['files']),
        'entrypoint_count': len(payload['entrypoints']),
        'entrypoint_file_count': len(payload['entrypoint_files']),
        'changed_file_count': len(payload['changed_files']),
        'slice_changed_only': payload['slice']['changed_only'],
        'top_relevance_path': payload['relevance'][0]['path'],
    }


def _evidence_signature(payload: dict[str, object]) -> dict[str, object]:
    return {
        'version': payload['version'],
        'generated_by': payload['generated_by'],
        'task_id': payload['task_id'],
        'evidence_status': payload['evidence_status'],
        'check_summary_total': payload['check_summary']['total'],
        'artifact_summary_total': payload['artifact_summary']['total'],
    }


def _verdict_signature(payload: dict[str, object]) -> dict[str, object]:
    return {
        'version': payload['version'],
        'generated_by': payload['generated_by'],
        'status': payload['status'],
        'task_id': payload['task_id'],
        'decision': payload['decision'],
        'review_ready': payload['review_ready'],
        'ready_for_apply': payload['ready_for_apply'],
    }


def test_plan_snapshot_contract_for_set() -> None:
    config_path, data = planner.load_config('markoblogo/SET')
    plan = planner.build_plan(config_path, data)
    assert _plan_signature(plan) == _fixture('plan_set_signature.json')


def test_agents_knowledge_snapshot_contract() -> None:
    knowledge = json.loads(Path(__file__).resolve().parents[1].joinpath('agents.knowledge.json').read_text())
    assert _knowledge_signature(knowledge) == _fixture('agents_knowledge_signature.json')


def test_proof_artifacts_snapshot_contract() -> None:
    evidence = json.loads(
        Path(__file__).resolve().parents[1].joinpath('docs/ai/tasks/proof-loop-blocked/evidence.json').read_text()
    )
    verdict = json.loads(
        Path(__file__).resolve().parents[1].joinpath('docs/ai/tasks/proof-loop-blocked/verdict.json').read_text()
    )
    assert _evidence_signature(evidence) == _fixture('proof_evidence_signature.json')
    assert _verdict_signature(verdict) == _fixture('proof_verdict_signature.json')
