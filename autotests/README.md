# Blockchain homework autotests (pytest)

## Install

```bash
cd autotests
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Required environment

- `SEPOLIA_RPC_URL` - HTTP RPC URL for Sepolia checks.
- `GITHUB_TOKEN` - optional GitHub token to avoid strict API rate limits.

## Submission format

Use `submissions/example_submission.json` as a template.

## Run checks

Run all required checks:

```bash
cd autotests
pytest -m required --submission submissions/example_submission.json
```

Run only assignment 1:

```bash
pytest assignment1 -m required --submission submissions/example_submission.json
```

Run only assignment 2:

```bash
pytest assignment2 -m required --submission submissions/example_submission.json
```

## Batch processing students

1) Put the raw table into `submissions/input/students_raw.txt`.

2) Build normalized JSON:

```bash
python tools/build_students_json.py
```

3) Run batch status checks (`СДАН / НЕ СДАН / НЕТ ДАННЫХ`):

```bash
export SEPOLIA_RPC_URL="https://your-sepolia-rpc"
python tools/run_batch.py
```

Output report is written to `submissions/output/batch_report.json`.
Current batch mode ignores GitHub and uses ETH checks only.
