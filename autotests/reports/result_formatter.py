from __future__ import annotations


def pass_fail_from_required(failed_required_count: int) -> str:
    return "PASS" if failed_required_count == 0 else "FAIL"
