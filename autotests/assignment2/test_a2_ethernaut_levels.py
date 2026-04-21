from __future__ import annotations

import pytest


@pytest.mark.assignment2
@pytest.mark.required
def test_a2_all_declared_levels_are_known(submission: dict, level_complexity: dict[str, int]) -> None:
    declared_levels = submission["ethernaut_levels"]
    unknown = [level for level in declared_levels if level not in level_complexity]
    assert not unknown, f"Unknown Ethernaut levels: {unknown}"
