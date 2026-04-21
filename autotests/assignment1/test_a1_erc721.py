from __future__ import annotations

import pytest

from common.eth_client import contract


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_erc721_token_uri_present(submission: dict, web3_client, erc721_abi: list[dict]) -> None:
    nft = contract(web3_client, submission["contracts"]["erc721"], erc721_abi)
    token_id = submission.get("nft_token_id_for_check", 1)
    token_uri = nft.functions.tokenURI(token_id).call()
    assert isinstance(token_uri, str) and token_uri.strip(), "tokenURI is empty"


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_erc721_owner_of_token(submission: dict, web3_client, erc721_abi: list[dict]) -> None:
    nft = contract(web3_client, submission["contracts"]["erc721"], erc721_abi)
    token_id = submission.get("nft_token_id_for_check", 1)
    owner = nft.functions.ownerOf(token_id).call()
    assert owner.startswith("0x"), "ownerOf returned invalid address"
