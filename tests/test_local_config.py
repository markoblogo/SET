import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_external_repo_config_exports_without_registry_or_target_writes(tmp_path):
    config = tmp_path / '.set.json'
    config.write_text(json.dumps({'version': 1, 'repo': 'outside/project', 'tools': {'agentsgen': {'init': True, 'pack': True, 'check': True}}, 'presets': ['repo-docs']}))
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/plan_config_apply.py'), '--config', str(config), '--repo-root', str(tmp_path), '--format', 'json', '--export-dir', str(tmp_path / 'review')], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    plan = json.loads(result.stdout)
    assert plan['repo'] == 'outside/project'
    assert plan['dry_run'] is True
    assert plan['proposed_changes'][0]['workflow']['uses'] == 'markoblogo/SET@v0.3.0'
    assert (tmp_path / 'review/workflow.set.yml').exists()
    assert not (tmp_path / '.github').exists()


def test_invalid_local_config_fails_before_export(tmp_path):
    config = tmp_path / '.set.json'
    config.write_text('{"version": 99}')
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/plan_config_apply.py'), '--config', str(config), '--export-dir', str(tmp_path / 'review')], capture_output=True, text=True)
    assert result.returncode != 0
    assert not (tmp_path / 'review').exists()
