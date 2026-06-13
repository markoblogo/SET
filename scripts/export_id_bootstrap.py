from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _split_pipe(value: str) -> list[str]:
    return [item.strip() for item in value.split("|") if item.strip()]


def _require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"missing required environment variable: {name}")
    return value


def build_json_payload() -> dict[str, object]:
    owner_id = _require_env("SET_RESOLVED_ID_OWNER_ID")
    target = os.environ.get("SET_RESOLVED_ID_TARGET", "").strip() or "set"
    primary = _require_env("SET_ID_PRIMARY_BOOTSTRAP")
    preferred = _split_pipe(_require_env("SET_ID_PREFERRED_BOOTSTRAP"))
    payload: dict[str, object] = {
        "version": 1,
        "generated_by": "set",
        "generated_at": _utc_now_iso(),
        "id": {
            "owner_id": owner_id,
            "target": target,
            "primary_human_bootstrap": primary,
            "preferred_human_bootstrap": preferred,
            "profile_core": os.environ.get("SET_ID_PROFILE_CORE", "").strip(),
            "handshake": os.environ.get("SET_ID_HANDSHAKE", "").strip(),
            "soul": os.environ.get("SET_ID_SOUL_PATH", "").strip(),
            "integration_guide": os.environ.get("SET_ID_INTEGRATION_GUIDE", "").strip(),
        },
        "usage": {
            "purpose": "Resolved human bootstrap packet for downstream agent runs.",
            "instructions": [
                "Start with primary_human_bootstrap.",
                "Expand through preferred_human_bootstrap only when more human context is needed.",
                "Treat these files as human-context and operating-constraints inputs, not as repo evidence.",
            ],
        },
    }
    return payload


def build_prompt_packet(payload: dict[str, object]) -> str:
    id_block = payload["id"]
    primary = str(id_block["primary_human_bootstrap"])
    preferred = [str(item) for item in id_block["preferred_human_bootstrap"]]
    lines = [
        "# ID Bootstrap Packet",
        "",
        f"- owner_id: `{id_block['owner_id']}`",
        f"- target: `{id_block['target']}`",
        f"- primary_human_bootstrap: `{primary}`",
        "",
        "## Consumption Order",
        "",
    ]
    for index, item in enumerate(preferred, start=1):
        lines.append(f"{index}. `{item}`")
    lines.extend(
        [
            "",
            "## Downstream Agent Instructions",
            "",
            "- Start with the primary bootstrap file first.",
            "- Read deeper files in the listed order only if more human context is needed.",
            "- Use these files for style, constraints, and decision preferences.",
            "- Do not treat them as repo facts, market evidence, or verification artifacts.",
        ]
    )
    integration_guide = str(id_block.get("integration_guide", "") or "").strip()
    if integration_guide:
        lines.extend(["", f"- integration_guide: `{integration_guide}`"])
    return "\n".join(lines) + "\n"


def main() -> int:
    repo_root = Path(os.environ.get("INPUT_PATH", ".").strip() or ".")
    output_dir = repo_root / "docs" / "ai"
    output_dir.mkdir(parents=True, exist_ok=True)

    payload = build_json_payload()
    json_path = output_dir / "id-bootstrap.json"
    prompt_path = output_dir / "id-bootstrap.prompt.md"

    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    prompt_path.write_text(build_prompt_packet(payload), encoding="utf-8")

    print(f"id_bootstrap_json={json_path}")
    print(f"id_bootstrap_prompt={prompt_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
