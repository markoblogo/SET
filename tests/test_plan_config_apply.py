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
    profile = bundle['context_package']['capability_profile']
    assert profile['selected'] == 'governed-runner'
    assert profile['exports'] == [
        'context_budget_hint',
        'context_degradation_review',
        'loop_readiness_hint',
        'memory_capability',
        'agent_governance_capability',
    ]
    assert profile['selection_scope'] == 'planning-only context package'
    memory = bundle['context_package']['memory_capability']
    assert memory['enabled'] is False
    assert memory['scope']['model'] == 'per-project'
    assert memory['retrieval']['modes'] == ['full_text', 'semantic']
    assert memory['operations']['write']['policy'] == 'audit-gated-proposal-first'
    governance = bundle['context_package']['agent_governance_capability']
    assert governance['enabled'] is False
    assert governance['mode'] == 'shadow-first'
    assert governance['decision']['outcomes'] == ['allow', 'deny', 'require_approval']
    assert governance['telemetry']['fields'] == ['tool_calls', 'tokens', 'estimated_cost', 'latency_ms']
    assert 'SET does not execute or proxy tool calls' in governance['non_goals']
    assert 'research_diversity_hint' not in bundle['context_package']
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


def test_capability_profile_exports_are_snapshot_stable() -> None:
    expected_exports = {
        'baseline': [
            'context_budget_hint',
            'context_degradation_review',
            'loop_readiness_hint',
        ],
        'research': [
            'context_budget_hint',
            'context_degradation_review',
            'loop_readiness_hint',
            'research_diversity_hint',
            'memory_capability',
        ],
        'governed-runner': [
            'context_budget_hint',
            'context_degradation_review',
            'loop_readiness_hint',
            'memory_capability',
            'agent_governance_capability',
        ],
        'loop-readiness': [
            'context_budget_hint',
            'loop_readiness_hint',
            'loop_readiness_contract',
        ],
        'loop-hardening': [
            'context_budget_hint',
            'context_degradation_review',
            'loop_hardening_contract',
        ],
        'design-taste-review': [
            'context_budget_hint',
            'context_degradation_review',
            'design_taste_review_contract',
        ],
    }
    for name, exports in expected_exports.items():
        package = planner.build_profile_context_package({'capability_profile': name})
        assert package['capability_profile']['selected'] == name
        assert package['capability_profile']['exports'] == exports
        assert [key for key in package if key != 'capability_profile'] == exports


def test_loop_readiness_profile_exports_l1_l2_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'loop-readiness'})
    contract = package['loop_readiness_contract']
    assert contract['enabled'] is False
    assert contract['kind'] == 'optional-loop-readiness-contract'
    assert contract['default_level'] == 'L1'
    assert contract['levels']['L1']['authority'] == 'report-only'
    assert contract['levels']['L2']['authority'] == 'proposal-first-assisted'
    assert 'maker-checker verification' in contract['levels']['L2']['required_controls']
    assert 'SET does not schedule or execute loops' in contract['non_goals']


def test_loop_hardening_profile_exports_bounded_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'loop-hardening'})
    contract = package['loop_hardening_contract']
    assert contract['enabled'] is False
    assert contract['harness_stripping']['outcomes'] == ['REMOVE', 'RESTORE', 'HARMFUL', 'INCONCLUSIVE']
    assert 'human gates' in contract['harness_stripping']['protected_controls']
    assert contract['runtime_path_sprint']['required_fields'][0] == 'sprint_id'
    assert contract['runtime_path_sprint']['acceptance_rule'].startswith('the executor cannot self-accept')
    assert contract['broken_window_revalidation']['statuses'] == ['STILL_GREEN', 'REOPENED', 'INCONCLUSIVE']
    assert contract['broken_window_revalidation']['auto_revert'] is False
    assert contract['root_verification']['required'] is True


def test_design_taste_review_profile_exports_review_only_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'design-taste-review'})
    contract = package['design_taste_review_contract']
    assert contract['enabled'] is False
    assert contract['authority'] == 'review-and-proposal-only'
    assert contract['routing']['marketing_editorial'] == 'frontend-taste-layer'
    assert contract['routing']['product_ui'].startswith('Lazyweb')
    assert contract['relative_axes'] == ['composition_variance', 'motion', 'density']
    assert contract['redesign_audit']['required_before_changes'] is True
    assert contract['verification']['required'] is True
    assert contract['non_goals'][-1].startswith('the contract defines no universal aesthetic bans')


def test_bounded_orchestration_profile_exports_fail_closed_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'bounded-orchestration'})
    contract = package['bounded_orchestration_contract']
    assert contract['enabled'] is False
    assert contract['plan_protocol']['states'] == ['PLAN_DRAFT', 'PLAN_REVISE', 'PLAN_APPROVED']
    assert contract['plan_protocol']['maximum_review_rounds'] == 5
    assert contract['finding_protocol']['id_pattern'] == 'F-[0-9]{3}'
    assert contract['finding_protocol']['statuses'] == ['OPEN', 'INCORPORATED', 'REJECTED']
    assert contract['executor_packet']['ownership_rule'].startswith('parallel executors must have non-overlapping')
    assert list(contract['route_states']['rules']) == ['route accepted', 'used and confirmed', 'unavailable']
    assert contract['root_verification']['required'] is True
    assert 'SET does not spawn, schedule, or route agents' in contract['non_goals']


def test_git_native_context_profile_exports_minimal_human_gated_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'git-native-context'})
    contract = package['git_native_context_contract']
    assert contract['enabled'] is False
    assert contract['document_types']['allowed'] == ['adr', 'rfc', 'rule', 'spec', 'plan', 'rnd', 'cpat']
    assert contract['lifecycle']['statuses'] == ['draft', 'accepted', 'rejected']
    assert contract['lifecycle']['acceptance_gate']['human_approval_required'] is True
    assert contract['relations']['types'] == ['implements', 'depends_on', 'extends', 'related']
    assert contract['cpat']['required_sections'] == [
        'symptom',
        'root_cause',
        'change',
        'scope',
        'verification',
        'prevention',
    ]
    assert contract['storage']['write_policy'] == 'proposal -> inspect -> apply'
    assert 'SET does not install Archcore, hooks, MCP servers, or session-start injection' in contract['non_goals']


def test_bug_evidence_profile_exports_captured_red_to_green_contract() -> None:
    package = planner.build_profile_context_package({'capability_profile': 'bug-evidence'})
    contract = package['bug_evidence_contract']
    assert contract['enabled'] is False
    assert contract['ownership']['diagnosis'] == 'diagnose'
    assert contract['ownership']['implementation_loop'] == 'test-driven-execution'
    assert contract['statuses'][-3:] == ['FIX_UNVERIFIED', 'FIX_REGRESSION', 'FIX_PROVEN']
    assert contract['evidence_packet']['route_states'] == [
        'route accepted',
        'used and confirmed',
        'unavailable',
    ]
    assert 'command_sha256' in contract['evidence_packet']['command_record_fields']
    assert contract['evidence_packet']['optional_relation'] == 'cpat_id'
    assert contract['classification_rules']['FIX_PROVEN'].startswith('same command hash')
    assert contract['classification_rules']['manual_flag_rule'].startswith('manual claims')
    assert 'production or device writes' in contract['approval_policy']['explicit_approval_required_for']
    assert 'SET does not scan repositories for bugs or execute tests' in contract['non_goals']


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
