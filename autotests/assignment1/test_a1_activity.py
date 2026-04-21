from __future__ import annotations

import pytest
from web3 import Web3


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_wallet_has_onchain_activity(submission: dict, web3_client) -> None:
    wallet = Web3.to_checksum_address(submission["eth_address"])
    tx_count = web3_client.eth.get_transaction_count(wallet)
    assert tx_count > 0, "Wallet has no on-chain transactions"
