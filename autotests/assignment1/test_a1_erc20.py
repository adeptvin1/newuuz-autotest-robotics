from __future__ import annotations

import pytest
from web3 import Web3

from common.eth_client import contract


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_erc20_total_supply(submission: dict, web3_client, erc20_abi: list[dict]) -> None:
    token = contract(web3_client, submission["contracts"]["erc20"], erc20_abi)
    expected_supply = 1_000_000 * 10**18
    assert token.functions.totalSupply().call() == expected_supply


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_erc20_decimals(submission: dict, web3_client, erc20_abi: list[dict]) -> None:
    token = contract(web3_client, submission["contracts"]["erc20"], erc20_abi)
    assert token.functions.decimals().call() == 18


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_erc20_deployer_has_tokens(submission: dict, web3_client, erc20_abi: list[dict]) -> None:
    token = contract(web3_client, submission["contracts"]["erc20"], erc20_abi)
    student_wallet = Web3.to_checksum_address(submission["eth_address"])
    assert token.functions.balanceOf(student_wallet).call() > 0
