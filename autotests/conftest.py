from __future__ import annotations

import os
from pathlib import Path

import pytest
import yaml

from common.eth_client import build_web3, load_abi
from common.github_client import GitHubClient
from common.submission_loader import load_submission


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        "--submission",
        action="store",
        default="submissions/example_submission.json",
        help="Path to a student's submission JSON (relative to autotests/).",
    )


@pytest.fixture(scope="session")
def submission(pytestconfig: pytest.Config) -> dict:
    submission_option = pytestconfig.getoption("--submission")
    submission_path = Path(submission_option)
    if not submission_path.is_absolute():
        submission_path = Path(__file__).parent / submission_path
    return load_submission(submission_path)


@pytest.fixture(scope="session")
def github_client() -> GitHubClient:
    return GitHubClient(token=os.getenv("GITHUB_TOKEN"))


@pytest.fixture(scope="session")
def web3_client():
    rpc_url = os.getenv("SEPOLIA_RPC_URL")
    if not rpc_url:
        pytest.skip("SEPOLIA_RPC_URL is not configured")
    return build_web3(rpc_url)


@pytest.fixture(scope="session")
def erc20_abi() -> list[dict]:
    return load_abi(Path(__file__).parent / "common/abi/erc20.json")


@pytest.fixture(scope="session")
def erc721_abi() -> list[dict]:
    return load_abi(Path(__file__).parent / "common/abi/erc721.json")


@pytest.fixture(scope="session")
def level_complexity() -> dict[str, int]:
    levels_file = Path(__file__).parent / "assignment2/levels_complexity.yaml"
    with levels_file.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
