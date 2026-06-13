from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "write_summary.py"


class WriteSummaryTests(unittest.TestCase):
    def test_summary_includes_resolved_id_bootstrap(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary_path = Path(tmp) / "summary.md"
            env = os.environ.copy()
            env.update(
                {
                    "GITHUB_STEP_SUMMARY": str(summary_path),
                    "INPUT_PATH": ".",
                    "INPUT_AUTODETECT": "true",
                    "INPUT_AGENTSGEN_REF": "main",
                    "SET_RESOLVED_ID_ENABLED": "true",
                    "SET_RESOLVED_ID_PRE_TASK": "true",
                    "SET_RESOLVED_ID_WEEKLY_REVIEW": "false",
                    "SET_RESOLVED_ID_OWNER_ID": "markoblogo",
                    "SET_RESOLVED_ID_TARGET": "set",
                    "SET_ID_PRIMARY_BOOTSTRAP": "profiles/markoblogo/soul.md",
                    "SET_ID_PREFERRED_BOOTSTRAP": "profiles/markoblogo/soul.md|profiles/markoblogo/profile.core.md|profiles/markoblogo/handshake.md",
                }
            )

            completed = subprocess.run(
                [sys.executable, str(SCRIPT)],
                cwd=REPO_ROOT,
                env=env,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            body = summary_path.read_text(encoding="utf-8")
            self.assertIn("**id primary bootstrap:** `profiles/markoblogo/soul.md`", body)
            self.assertIn("`profiles/markoblogo/profile.core.md`", body)
            self.assertIn("`profiles/markoblogo/handshake.md`", body)


if __name__ == "__main__":
    unittest.main()
