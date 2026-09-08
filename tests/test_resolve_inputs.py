from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "resolve_inputs.py"


def _resolve(tmp_path: Path, **inputs: str) -> dict[str, str]:
    output = tmp_path / "github-env"
    env = os.environ.copy()
    env.update({"GITHUB_ENV": str(output), **inputs})
    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr
    return dict(line.split("=", 1) for line in output.read_text().splitlines())


def test_web_ui_preset_focuses_changed_frontend_code(tmp_path: Path) -> None:
    resolved = _resolve(tmp_path, INPUT_WORKFLOW_PRESET="web-ui")

    assert resolved["SET_RESOLVED_INIT"] == "true"
    assert resolved["SET_RESOLVED_PACK"] == "true"
    assert resolved["SET_RESOLVED_CHECK"] == "true"
    assert resolved["SET_RESOLVED_REPOMAP"] == "true"
    assert resolved["SET_RESOLVED_REPOMAP_CHANGED"] == "true"
    assert "frontend" in resolved["SET_RESOLVED_REPOMAP_FOCUS"]
    assert resolved["SET_RESOLVED_ANALYZE"] == "false"
    assert resolved["SET_RESOLVED_META"] == "false"


def test_explicit_repomap_inputs_override_web_ui_defaults(tmp_path: Path) -> None:
    resolved = _resolve(
        tmp_path,
        INPUT_WORKFLOW_PRESET="web-ui",
        INPUT_REPOMAP_FOCUS="packages/admin",
        INPUT_REPOMAP_CHANGED="false",
    )

    assert resolved["SET_RESOLVED_REPOMAP_FOCUS"] == "packages/admin"
    assert resolved["SET_RESOLVED_REPOMAP_CHANGED"] == "false"


def test_multiline_repomap_focus_is_rejected_before_writing_github_env(tmp_path: Path) -> None:
    output = tmp_path / "github-env"
    env = os.environ.copy()
    env.update(
        {
            "GITHUB_ENV": str(output),
            "INPUT_WORKFLOW_PRESET": "web-ui",
            "INPUT_REPOMAP_FOCUS": "frontend\nSET_RESOLVED_ANALYZE=true",
        }
    )

    completed = subprocess.run(
        [sys.executable, str(SCRIPT)],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )

    assert completed.returncode != 0
    assert "single-line" in completed.stderr
