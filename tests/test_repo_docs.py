from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_custom_repo_docs_keep_required_sections_and_references():
    text = (ROOT / 'AGENTS.md').read_text()
    for section in ('agentsgen_contract', 'task_contract', 'verification'):
        assert re.search(rf'<!-- AGENTSGEN:START section={section} -->\s*\S[\s\S]+?<!-- AGENTSGEN:END section={section} -->', text)
    assert (ROOT / 'RUNBOOK.md').read_text().strip()
    assert (ROOT / 'docs/ai/task-contract.json').is_file()


def test_action_and_docs_pin_supported_agentsgen_release():
    action = (ROOT / 'action.yml').read_text()
    guard = (ROOT / '.github/workflows/agentsgen-pr-guard.yml').read_text()
    integration = (ROOT / 'docs/integration-testing.md').read_text()

    assert "default: 'v0.5.1'" in action
    assert 'agentsgen==0.5.1' in guard
    assert 'SET 0.5.0 + agentsgen 0.5.1' in integration
