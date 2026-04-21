from __future__ import annotations

import pytest


@pytest.mark.assignment2
@pytest.mark.required
def test_a2_complexity_at_least_7(submission: dict, level_complexity: dict[str, int]) -> None:
    total = sum(level_complexity[level] for level in submission["ethernaut_levels"] if level in level_complexity)
    assert total >= 7, f"Total complexity is {total}, expected at least 7"
