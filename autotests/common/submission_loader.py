from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def load_submission(path: str | Path) -> dict[str, Any]:
    submission_path = Path(path)
    if not submission_path.exists():
        raise FileNotFoundError(
            f"Submission file was not found: {submission_path}. "
            "Pass a valid file via --submission=..."
        )
    with submission_path.open("r", encoding="utf-8") as f:
        return json.load(f)
