from __future__ import annotations

import json
import re
from pathlib import Path


ETH_RE = re.compile(r"0x[a-fA-F0-9]{40}")
GITHUB_RE = re.compile(r"(https?://github\.com/[A-Za-z0-9_.-]+/?|[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def parse_line(line: str) -> dict | None:
    line = line.strip()
    if not line or line.lower().startswith("name\t"):
        return None

    # Split by tabs first; if source is space-separated it still works as fallback.
    parts = [p.strip() for p in re.split(r"\t+", line) if p.strip()]
    if len(parts) < 2:
        return None

    name = parts[0]
    student_id = parts[1]
    github = ""
    eth_matches = ETH_RE.findall(line)
    eth_address = eth_matches[0] if eth_matches else ""

    for p in parts[2:]:
        gh = GITHUB_RE.search(p)
        if gh:
            github = gh.group(1)
            break

    if github and github.startswith("http") and github.endswith("/"):
        github = github[:-1]

    return {
        "name": name,
        "student_id": student_id,
        "github": github,
        "eth_address": eth_address,
        "eth_addresses_all": eth_matches,
        "missing_github": github == "",
        "missing_eth": eth_address == "",
        "multiple_eth": len(eth_matches) > 1,
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    input_path = root / "submissions/input/students_raw.txt"
    output_path = root / "submissions/output/students_clean.json"

    rows = []
    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            parsed = parse_line(line)
            if parsed:
                rows.append(parsed)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"Parsed {len(rows)} students")
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
