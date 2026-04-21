from __future__ import annotations

import pytest


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_required_fields_present(submission: dict) -> None:
    required_top_level = ["github", "eth_address", "contracts"]
    for key in required_top_level:
        assert key in submission, f"Missing required field: {key}"

    assert "erc20" in submission["contracts"], "Missing contracts.erc20"
    assert "erc721" in submission["contracts"], "Missing contracts.erc721"
