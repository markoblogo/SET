from __future__ import annotations

import json
from pathlib import Path

ALLOWED_PRESETS = {'minimal', 'repo-docs', 'site-ai'}
ALLOWED_TOP_LEVEL = {'version', 'repo', 'site', 'tools', 'presets'}
ALLOWED_SITE_KEYS = {'url'}
ALLOWED_TOOL_BLOCKS = {'agentsgen', 'git_tweet'}
ALLOWED_AGENTSGEN_KEYS = {
    'init',
    'pack',
    'check',
    'repomap',
    'repomap_policy',
    'snippets',
    'analyze_url',
    'meta_url',
}
ALLOWED_GIT_TWEET_KEYS = {'enabled'}


def _fail(message: str) -> SystemExit:
    return SystemExit(message)


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise _fail(message)


def _validate_bool_or_none(value: object, field: str) -> None:
    _require(value is None or isinstance(value, bool), f'{field} must be boolean or null')


def _validate_url_or_none(value: object, field: str) -> None:
    _require(value is None or isinstance(value, str), f'{field} must be string or null')


def _validate_positive_int(value: object, field: str) -> None:
    _require(isinstance(value, int) and value > 0, f'{field} must be a positive integer')


def validate_config(path: Path) -> dict[str, object]:
    data = json.loads(path.read_text())
    _require(isinstance(data, dict), f'{path.name}: config must be an object')
    unknown_top = set(data) - ALLOWED_TOP_LEVEL
    _require(not unknown_top, f"{path.name}: unknown top-level keys: {', '.join(sorted(unknown_top))}")
    _require(data.get('version') == 1, f'{path.name}: version must be 1')
    repo = data.get('repo')
    _require(isinstance(repo, str) and '/' in repo, f'{path.name}: repo must be owner/name')

    site = data.get('site')
    if site is not None:
        _require(isinstance(site, dict), f'{path.name}: site must be an object')
        unknown_site = set(site) - ALLOWED_SITE_KEYS
        _require(not unknown_site, f"{path.name}: unknown site keys: {', '.join(sorted(unknown_site))}")
        if 'url' in site:
            _require(isinstance(site['url'], str) and site['url'].startswith('http'), f'{path.name}: site.url must be http(s) string')

    tools = data.get('tools')
    _require(isinstance(tools, dict), f'{path.name}: tools must be an object')
    unknown_tools = set(tools) - ALLOWED_TOOL_BLOCKS
    _require(not unknown_tools, f"{path.name}: unknown tool blocks: {', '.join(sorted(unknown_tools))}")

    agentsgen = tools.get('agentsgen')
    if agentsgen is not None:
        _require(isinstance(agentsgen, dict), f'{path.name}: tools.agentsgen must be an object')
        unknown_agentsgen = set(agentsgen) - ALLOWED_AGENTSGEN_KEYS
        _require(not unknown_agentsgen, f"{path.name}: unknown agentsgen keys: {', '.join(sorted(unknown_agentsgen))}")
        for key in ('init', 'pack', 'check', 'repomap', 'snippets'):
            if key in agentsgen:
                _validate_bool_or_none(agentsgen[key], f'{path.name}: agentsgen.{key}')
        for key in ('analyze_url', 'meta_url'):
            if key in agentsgen:
                _validate_url_or_none(agentsgen[key], f'{path.name}: agentsgen.{key}')
        repomap_policy = agentsgen.get('repomap_policy')
        if repomap_policy is not None:
            _require(isinstance(repomap_policy, dict), f'{path.name}: agentsgen.repomap_policy must be an object')
            unknown_policy = set(repomap_policy) - {'compact_budget', 'top_ranked_files'}
            _require(not unknown_policy, f"{path.name}: unknown repomap_policy keys: {', '.join(sorted(unknown_policy))}")
            if 'compact_budget' in repomap_policy:
                _validate_positive_int(repomap_policy['compact_budget'], f'{path.name}: agentsgen.repomap_policy.compact_budget')
            if 'top_ranked_files' in repomap_policy:
                _validate_positive_int(repomap_policy['top_ranked_files'], f'{path.name}: agentsgen.repomap_policy.top_ranked_files')

    git_tweet = tools.get('git_tweet')
    if git_tweet is not None:
        _require(isinstance(git_tweet, dict), f'{path.name}: tools.git_tweet must be an object')
        unknown_git_tweet = set(git_tweet) - ALLOWED_GIT_TWEET_KEYS
        _require(not unknown_git_tweet, f"{path.name}: unknown git_tweet keys: {', '.join(sorted(unknown_git_tweet))}")
        if 'enabled' in git_tweet:
            _validate_bool_or_none(git_tweet['enabled'], f'{path.name}: git_tweet.enabled')

    presets = data.get('presets', [])
    _require(isinstance(presets, list), f'{path.name}: presets must be a list')
    for preset in presets:
        _require(isinstance(preset, str), f'{path.name}: preset names must be strings')
        _require(preset in ALLOWED_PRESETS, f'{path.name}: unsupported preset {preset!r}')

    return data


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    registry_dir = root / 'registry' / 'repos'
    configs = sorted(registry_dir.glob('*.json'))
    if not configs:
        print('No registry configs found.')
        return 0

    print('SET registry validation')
    for config_path in configs:
        data = validate_config(config_path)
        repo = data['repo']
        presets = ', '.join(data.get('presets', [])) or 'none'
        print(f'- ok: {config_path.name} -> {repo} (presets: {presets})')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
