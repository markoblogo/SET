from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "export_id_bootstrap.py"


class ExportIdBootstrapTests(unittest.TestCase):
    def test_export_writes_json_and_prompt_packet(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp) / "repo"
            repo_root.mkdir(parents=True, exist_ok=True)
            env = os.environ.copy()
            env.update(
                {
                    "INPUT_PATH": str(repo_root),
                    "SET_RESOLVED_ID_OWNER_ID": "markoblogo",
                    "SET_RESOLVED_ID_TARGET": "set",
                    "SET_ID_PRIMARY_BOOTSTRAP": "profiles/markoblogo/soul.md",
                    "SET_ID_PREFERRED_BOOTSTRAP": "profiles/markoblogo/soul.md|profiles/markoblogo/profile.core.md|profiles/markoblogo/handshake.md",
                    "SET_ID_PROFILE_CORE": "profiles/markoblogo/profile.core.md",
                    "SET_ID_HANDSHAKE": "profiles/markoblogo/handshake.md",
                    "SET_ID_SOUL_PATH": "profiles/markoblogo/soul.md",
                    "SET_ID_INTEGRATION_GUIDE": "integrations/set/README.md",
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
            json_path = repo_root / "docs" / "ai" / "id-bootstrap.json"
            prompt_path = repo_root / "docs" / "ai" / "id-bootstrap.prompt.md"
            self.assertTrue(json_path.exists())
            self.assertTrue(prompt_path.exists())

            payload = json.loads(json_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["id"]["primary_human_bootstrap"], "profiles/markoblogo/soul.md")
            self.assertEqual(
                payload["id"]["preferred_human_bootstrap"][0],
                "profiles/markoblogo/soul.md",
            )
            prompt = prompt_path.read_text(encoding="utf-8")
            self.assertIn("`profiles/markoblogo/soul.md`", prompt)
            self.assertIn("Downstream Agent Instructions", prompt)


if __name__ == "__main__":
    unittest.main()
