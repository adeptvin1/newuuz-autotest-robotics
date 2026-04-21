from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from web3 import Web3


def build_web3(rpc_url: str) -> Web3:
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise RuntimeError(f"Unable to connect to RPC endpoint: {rpc_url}")
    return w3


def load_abi(path: str | Path) -> list[dict[str, Any]]:
    abi_path = Path(path)
    with abi_path.open("r", encoding="utf-8") as f:
        return json.load(f)


def contract(w3: Web3, address: str, abi: list[dict[str, Any]]):
    return w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)
