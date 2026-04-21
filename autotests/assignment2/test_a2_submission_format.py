from __future__ import annotations

import pytest


@pytest.mark.assignment2
@pytest.mark.required
def test_a2_required_fields_present(submission: dict) -> None:
    required_top_level = ["github", "eth_address", "ethernaut_levels"]
    for key in required_top_level:
        assert key in submission, f"Missing required field: {key}"
    assert isinstance(submission["ethernaut_levels"], list), "ethernaut_levels must be a list"
