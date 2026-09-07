"""Check the installed planner outside its source checkout."""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--exe', default='set-plan-config-apply')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        (root / '.set.json').write_text(json.dumps({'version': 1, 'repo': 'external/example', 'tools': {'agentsgen': {'init': True, 'pack': True, 'check': True}}, 'presets': ['repo-docs']}))
        result = subprocess.run([args.exe, '--format', 'json', '--export-dir', 'review'], cwd=root, text=True, capture_output=True)
        if result.returncode:
            raise SystemExit(result.stderr)
        plan = json.loads(result.stdout)
        assert plan['repo'] == 'external/example'
        assert plan['dry_run'] is True
        assert (root / 'review/workflow.set.yml').is_file()
        assert 'markoblogo/SET@v0.3.0' in (root / 'review/workflow.set.yml').read_text()
        assert not (root / '.github').exists()
    print('Installed planner: local config, pinned workflow export, no target mutation: PASS')


if __name__ == '__main__':
    main()
