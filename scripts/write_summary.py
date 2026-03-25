from __future__ import annotations

import os
from pathlib import Path


def _enabled(name: str) -> bool:
    return os.environ.get(name, '').strip() == 'true'


def _line(label: str, value: str) -> str:
    return f'- **{label}:** {value}\n'


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
