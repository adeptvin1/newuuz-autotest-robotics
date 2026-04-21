from __future__ import annotations

from typing import Any

import requests


class GitHubClient:
    def __init__(self, token: str | None = None) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "User-Agent": "newuuz-autotest-robotics",
            }
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def get_repo(self, owner: str, repo: str) -> dict[str, Any]:
        resp = self.session.get(f"https://api.github.com/repos/{owner}/{repo}", timeout=20)
        resp.raise_for_status()
        return resp.json()

    def get_user(self, username: str) -> dict[str, Any]:
        resp = self.session.get(f"https://api.github.com/users/{username}", timeout=20)
        resp.raise_for_status()
        return resp.json()

    def list_commits(self, owner: str, repo: str, per_page: int = 10) -> list[dict[str, Any]]:
        resp = self.session.get(
            f"https://api.github.com/repos/{owner}/{repo}/commits",
            params={"per_page": per_page},
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()
