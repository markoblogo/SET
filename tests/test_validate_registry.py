from __future__ import annotations

from pathlib import Path

import json
import pytest

from scripts.validate_registry import validate_config


def write_json(path: Path, payload: dict[str, object]) -> Path:
    path.write_text(json.dumps(payload, indent=2) + '\n')
    return path


def valid_config() -> dict[str, object]:
    return {
        'version': 1,
        'repo': 'owner/name',
        'site': {'url': 'https://example.com'},
        'tools': {
            'agentsgen': {
                'init': True,
                'pack': False,
                'check': False,
                'repomap': False,
            },
            'id': {'enabled': True, 'owner_id': 'owner'},
        },
        'presets': ['minimal'],
    }


def test_validate_config_accepts_valid_payload(tmp_path: Path) -> None:
    path = write_json(tmp_path / 'repo.json', valid_config())
    assert validate_config(path) == valid_config()


def test_validate_config_rejects_unknown_top_level_keys(tmp_path: Path) -> None:
    invalid = valid_config()
    invalid['oops'] = 'boom'
    path = write_json(tmp_path / 'repo.json', invalid)
    with pytest.raises(SystemExit):
        validate_config(path)


def test_validate_config_rejects_unsupported_preset(tmp_path: Path) -> None:
    invalid = valid_config()
    invalid['presets'] = ['unsupported']
    path = write_json(tmp_path / 'repo.json', invalid)
    with pytest.raises(SystemExit):
        validate_config(path)


def test_validate_config_rejects_bad_repomap_policy(tmp_path: Path) -> None:
    invalid = valid_config()
    invalid['tools']['agentsgen'] = {
        'init': True,
        'repomap': True,
        'repomap_policy': {'compact_budget': -1},
    }
    path = write_json(tmp_path / 'repo.json', invalid)
    with pytest.raises(SystemExit):
        validate_config(path)
