from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from web3 import Web3

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def check_wallet_activity(w3: Web3, address: str) -> tuple[bool, str]:
    if not address:
        return False, "missing_eth"
    try:
        tx_count = w3.eth.get_transaction_count(Web3.to_checksum_address(address))
        return tx_count > 0, f"tx_count={tx_count}"
    except Exception as exc:
        return False, f"eth_error={exc}"


def final_status(missing_eth: bool, wallet_ok: bool) -> str:
    if missing_eth:
        return "НЕТ ДАННЫХ"
    return "СДАН" if wallet_ok else "НЕ СДАН"


def main() -> None:
    root = ROOT
    students_path = root / "submissions/output/students_clean.json"
    report_path = root / "submissions/output/batch_report.json"

    with students_path.open("r", encoding="utf-8") as f:
        students = json.load(f)

    rpc = os.getenv("SEPOLIA_RPC_URL", "")
    if not rpc:
        raise RuntimeError("SEPOLIA_RPC_URL is required for batch run")
    w3 = Web3(Web3.HTTPProvider(rpc))
    if not w3.is_connected():
        raise RuntimeError("Failed to connect to Sepolia RPC")

    report = []
    for s in students:
        wallet_ok, wallet_note = check_wallet_activity(w3, s.get("eth_address", ""))
        status = final_status(s["missing_eth"], wallet_ok)
        report.append(
            {
                "student_id": s["student_id"],
                "name": s["name"],
                "github": s["github"],
                "eth_address": s["eth_address"],
                "status": status,
                "wallet_check": wallet_note,
                "github_check": "ignored",
                "multiple_eth": s["multiple_eth"],
            }
        )

    with report_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    total = len(report)
    passed = sum(1 for x in report if x["status"] == "СДАН")
    no_data = sum(1 for x in report if x["status"] == "НЕТ ДАННЫХ")
    failed = total - passed - no_data
    print(f"Total: {total} | СДАН: {passed} | НЕ СДАН: {failed} | НЕТ ДАННЫХ: {no_data}")
    print(f"Saved: {report_path}")


if __name__ == "__main__":
    main()
