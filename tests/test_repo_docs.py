from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def test_custom_repo_docs_keep_required_sections_and_references():
    text = (ROOT / 'AGENTS.md').read_text()
    for section in ('agentsgen_contract', 'task_contract', 'verification'):
        assert re.search(rf'<!-- AGENTSGEN:START section={section} -->\s*\S[\s\S]+?<!-- AGENTSGEN:END section={section} -->', text)
    assert (ROOT / 'RUNBOOK.md').read_text().strip()
    assert (ROOT / 'docs/ai/task-contract.json').is_file()
