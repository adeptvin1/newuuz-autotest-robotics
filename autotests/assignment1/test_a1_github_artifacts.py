from __future__ import annotations

import re

import pytest
import requests


def _parse_repo(full_name_or_url: str) -> tuple[str, str]:
    if full_name_or_url.startswith("https://github.com/"):
        clean = full_name_or_url.removeprefix("https://github.com/").strip("/")
    else:
        clean = full_name_or_url.strip()
    match = re.match(r"^([^/]+)/([^/]+)$", clean)
    if not match:
        raise ValueError("github must be owner/repo or full GitHub URL")
    return match.group(1), match.group(2)


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_github_repo_exists(submission: dict, github_client) -> None:
    owner, repo = _parse_repo(submission["github"])
    try:
        repo_data = github_client.get_repo(owner, repo)
    except requests.RequestException as exc:
        pytest.skip(f"GitHub API unavailable in current environment: {exc}")
    assert repo_data["archived"] is False, "Repository is archived"


@pytest.mark.assignment1
@pytest.mark.required
def test_a1_github_has_commits(submission: dict, github_client) -> None:
    owner, repo = _parse_repo(submission["github"])
    try:
        commits = github_client.list_commits(owner, repo, per_page=5)
    except requests.RequestException as exc:
        pytest.skip(f"GitHub API unavailable in current environment: {exc}")
    assert len(commits) > 0, "No commits found in repository"
