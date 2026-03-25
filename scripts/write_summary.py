from __future__ import annotations

import json
import os
from pathlib import Path


def _enabled(name: str) -> bool:
    return os.environ.get(name, '').strip() == 'true'


def _line(label: str, value: str) -> str:
    return f'- **{label}:** {value}\n'


def _repomap_mode(focus: str, changed: str) -> str:
    focus_value = focus.strip()
    changed_enabled = changed.strip() == 'true'
    if focus_value and changed_enabled:
        return 'focus+changed'
    if focus_value:
        return 'focus'
    if changed_enabled:
        return 'changed'
    return 'full'


def _repomap_label(mode: str) -> str:
    return {
        'full': 'Full Repo Slice',
        'focus': 'Focused Code Slice',
        'changed': 'Changed Files Slice',
        'focus+changed': 'Hybrid Slice',
    }.get(mode, 'Full Repo Slice')


def _load_json(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding='utf-8'))
    except Exception:
        return None
    return payload if isinstance(payload, dict) else None


def main() -> int:
    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', '').strip()
    if not summary_path:
        print('SET summary skipped: GITHUB_STEP_SUMMARY is not available.')
        return 0

    workflow_preset = os.environ.get('INPUT_WORKFLOW_PRESET', '').strip() or 'none'
    path_value = os.environ.get('INPUT_PATH', '.').strip() or '.'
    autodetect = os.environ.get('INPUT_AUTODETECT', 'true').strip() or 'true'
    init_preset = os.environ.get('INPUT_PRESET', '').strip() or 'none'

    operations: list[str] = []
    if _enabled('SET_RESOLVED_INIT'):
        operations.append('init')
    if _enabled('SET_RESOLVED_PACK') and _enabled('SET_RESOLVED_SITE_PACK'):
        operations.append('pack --site')
    elif _enabled('SET_RESOLVED_PACK'):
        operations.append('pack')
    if _enabled('SET_RESOLVED_CHECK'):
        operations.append('check --all --ci')
    if _enabled('SET_RESOLVED_REPOMAP'):
        operations.append('understand')
    if _enabled('SET_RESOLVED_SNIPPETS'):
        operations.append('snippets')
    if _enabled('SET_RESOLVED_ANALYZE'):
        operations.append('analyze')
    if _enabled('SET_RESOLVED_META'):
        operations.append('meta')
    if _enabled('SET_RESOLVED_PROOF_LOOP'):
        operations.append('proof-loop')

    body = []
    body.append('## SET execution summary\n\n')
    body.append(_line('workflow preset', workflow_preset))
    body.append(_line('path', f'`{path_value}`'))
    body.append(_line('autodetect', autodetect))
    body.append(_line('init preset', init_preset))
    body.append(_line('agentsgen ref', os.environ.get('INPUT_AGENTSGEN_REF', 'main').strip() or 'main'))
    body.append(_line('operations', ', '.join(operations) if operations else 'none'))

    site_url = os.environ.get('SET_RESOLVED_SITE_URL', '').strip()
    analyze_url = os.environ.get('SET_RESOLVED_ANALYZE_URL', '').strip()
    meta_url = os.environ.get('SET_RESOLVED_META_URL', '').strip()
    repomap_budget = os.environ.get('INPUT_REPOMAP_COMPACT_BUDGET', '').strip() or '4000'
    repomap_focus = os.environ.get('INPUT_REPOMAP_FOCUS', '').strip()
    repomap_changed = os.environ.get('INPUT_REPOMAP_CHANGED', '').strip()
    if _enabled('SET_RESOLVED_REPOMAP'):
        repomap_mode = _repomap_mode(repomap_focus, repomap_changed)
        body.append(_line('repomap compact budget', repomap_budget))
        body.append(_line('repomap policy mode', repomap_mode))
        body.append(_line('repomap policy label', _repomap_label(repomap_mode)))
        body.append(_line('repomap slice', repomap_focus if repomap_focus else ('changed' if repomap_changed == 'true' else 'full')))
    if _enabled('SET_RESOLVED_PROOF_LOOP'):
        body.append(_line('proof loop', 'enabled'))
        proof_task_id = os.environ.get('SET_RESOLVED_PROOF_TASK_ID', '').strip() or 'missing'
        body.append(_line('proof task id', proof_task_id))
        repo_root = Path(path_value)
        proof_dir = repo_root / 'docs' / 'ai' / 'tasks' / proof_task_id
        evidence = _load_json(proof_dir / 'evidence.json') or _load_json(proof_dir / 'evidence.generated.json')
        verdict = _load_json(proof_dir / 'verdict.json') or _load_json(proof_dir / 'verdict.generated.json')
        if isinstance(evidence, dict):
            body.append(_line('proof evidence status', str(evidence.get('evidence_status', 'unknown'))))
            check_summary = evidence.get('check_summary')
            artifact_summary = evidence.get('artifact_summary')
            if isinstance(check_summary, dict):
                body.append(
                    _line(
                        'proof checks',
                        f"passed {check_summary.get('passed', 0)}, failed {check_summary.get('failed', 0)}, pending {check_summary.get('pending', 0)}",
                    )
                )
            if isinstance(artifact_summary, dict):
                body.append(
                    _line(
                        'proof artifacts',
                        f"present {artifact_summary.get('present', 0)} / total {artifact_summary.get('total', 0)}",
                    )
                )
        if isinstance(verdict, dict):
            body.append(_line('proof verdict', str(verdict.get('status', 'unknown'))))
            body.append(_line('proof decision', str(verdict.get('decision', 'unknown'))))
            body.append(_line('proof ready for apply', str(verdict.get('ready_for_apply', False)).lower()))

    if site_url:
        body.append(_line('site url', site_url))
    if _enabled('SET_RESOLVED_ANALYZE') and analyze_url:
        body.append(_line('analyze url', analyze_url))
    if _enabled('SET_RESOLVED_META') and meta_url:
        body.append(_line('meta url', meta_url))

    with Path(summary_path).open('a', encoding='utf-8') as fh:
        fh.writelines(body)

    print('SET execution summary written.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
