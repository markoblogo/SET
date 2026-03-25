from __future__ import annotations

import os
from pathlib import Path


def _read_preset(name: str) -> dict[str, str]:
    if not name:
        return {}
    preset_path = Path(__file__).resolve().parents[1] / 'presets' / f'{name}.env'
    if not preset_path.exists():
        available = ', '.join(sorted(p.stem for p in preset_path.parent.glob('*.env')))
        raise SystemExit(f"Unknown workflow_preset '{name}'. Available presets: {available}")
    values: dict[str, str] = {}
    for line in preset_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        key, _, value = line.partition('=')
        values[key.strip()] = value.strip()
    return values


def _resolve_flag(explicit: str, preset: dict[str, str], key: str, fallback: str) -> str:
    if explicit in {'true', 'false'}:
        return explicit
    if key in preset:
        return preset[key]
    return fallback


def main() -> int:
    preset_name = os.environ.get('INPUT_WORKFLOW_PRESET', '').strip()
    preset = _read_preset(preset_name)

    resolved = {
        'SET_RESOLVED_AGENTSGEN': _resolve_flag(os.environ.get('INPUT_AGENTSGEN', ''), preset, 'AGENTSGEN', 'true'),
        'SET_RESOLVED_INIT': _resolve_flag(os.environ.get('INPUT_INIT', ''), preset, 'INIT', 'true'),
        'SET_RESOLVED_PACK': _resolve_flag(os.environ.get('INPUT_PACK', ''), preset, 'PACK', 'false'),
        'SET_RESOLVED_SITE_PACK': _resolve_flag(os.environ.get('INPUT_SITE_PACK', ''), preset, 'SITE_PACK', 'false'),
        'SET_RESOLVED_CHECK': _resolve_flag(os.environ.get('INPUT_CHECK', ''), preset, 'CHECK', 'false'),
        'SET_RESOLVED_REPOMAP': _resolve_flag(os.environ.get('INPUT_REPOMAP', ''), preset, 'REPOMAP', 'false'),
        'SET_RESOLVED_SNIPPETS': _resolve_flag(os.environ.get('INPUT_SNIPPETS', ''), preset, 'SNIPPETS', 'false'),
        'SET_RESOLVED_ANALYZE': _resolve_flag(os.environ.get('INPUT_ANALYZE', ''), preset, 'ANALYZE', 'false'),
        'SET_RESOLVED_META': _resolve_flag(os.environ.get('INPUT_META', ''), preset, 'META', 'false'),
    }

    site_url = os.environ.get('INPUT_SITE_URL', '').strip()
    analyze_url = os.environ.get('INPUT_ANALYZE_URL', '').strip()
    meta_url = os.environ.get('INPUT_META_URL', '').strip()
    default_site_url = site_url or preset.get('SITE_URL', '')
    resolved['SET_RESOLVED_SITE_URL'] = default_site_url
    resolved['SET_RESOLVED_ANALYZE_URL'] = analyze_url or default_site_url
    resolved['SET_RESOLVED_META_URL'] = meta_url or default_site_url

    output_path = os.environ['GITHUB_ENV']
    with open(output_path, 'a', encoding='utf-8') as fh:
        for key, value in resolved.items():
            fh.write(f'{key}={value}\n')

    summary = (
        'SET preset resolution: '
        f"workflow_preset={preset_name or 'none'}, "
        f"agentsgen={resolved['SET_RESOLVED_AGENTSGEN']}, "
        f"init={resolved['SET_RESOLVED_INIT']}, "
        f"pack={resolved['SET_RESOLVED_PACK']}, "
        f"site_pack={resolved['SET_RESOLVED_SITE_PACK']}, "
        f"check={resolved['SET_RESOLVED_CHECK']}, "
        f"repomap={resolved['SET_RESOLVED_REPOMAP']}, "
        f"snippets={resolved['SET_RESOLVED_SNIPPETS']}, "
        f"analyze={resolved['SET_RESOLVED_ANALYZE']}, "
        f"meta={resolved['SET_RESOLVED_META']}"
    )
    print(summary)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
