from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_DIR = ROOT / 'registry' / 'repos'


def load_config(repo: str) -> tuple[Path, dict[str, object]]:
    for path in sorted(REGISTRY_DIR.glob('*.json')):
        data = json.loads(path.read_text())
        if data.get('repo') == repo:
            return path, data
    raise SystemExit(f'Repo config not found for {repo!r}')


def pick_workflow_preset(presets: list[str]) -> str | None:
    for name in ('site-ai', 'repo-docs', 'minimal'):
        if name in presets:
            return name
    return None


def build_plan(config_path: Path, data: dict[str, object]) -> dict[str, object]:
    tools = data.get('tools', {}) if isinstance(data.get('tools'), dict) else {}
    agentsgen = tools.get('agentsgen', {}) if isinstance(tools.get('agentsgen'), dict) else {}
    presets = data.get('presets', []) if isinstance(data.get('presets'), list) else []
    workflow_preset = pick_workflow_preset([p for p in presets if isinstance(p, str)])

    with_block: dict[str, str] = {'agentsgen': 'true', 'autodetect': 'true', 'path': '.'}
    if workflow_preset:
        with_block['workflow_preset'] = workflow_preset

    for key in ('init', 'pack', 'check'):
        if key in agentsgen and isinstance(agentsgen[key], bool):
            with_block[key] = 'true' if agentsgen[key] else 'false'

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

    unmapped = []
    for key in ('repomap', 'snippets'):
        if agentsgen.get(key) is True:
            unmapped.append(f'agentsgen.{key} is in registry but not yet wired into SET action inputs')

    workflow = {
        'path': '.github/workflows/set.yml',
        'uses': 'markoblogo/SET@main',
        'with': with_block,
    }
    return {
        'version': 1,
        'mode': 'planning-only',
        'repo': data['repo'],
        'source_config': str(config_path),
        'proposed_changes': [
            {
                'type': 'workflow',
                'workflow': workflow,
            }
        ],
        'unmapped': unmapped,
        'notes': [
            'This planner does not open a PR or write files.',
            'Use the output to review the intended SET workflow before any future apply step.',
        ],
    }


def render_text(plan: dict[str, object]) -> str:
    workflow = plan['proposed_changes'][0]['workflow']
    with_block = workflow['with']
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
    return '\n'.join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description='Planning-only SET config apply helper.')
    parser.add_argument('repo', help='Repo name in owner/name format')
    parser.add_argument('--format', choices=('text', 'json'), default='text')
    args = parser.parse_args()

    config_path, data = load_config(args.repo)
    plan = build_plan(config_path, data)
    if args.format == 'json':
        print(json.dumps(plan, indent=2))
    else:
        print(render_text(plan))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
