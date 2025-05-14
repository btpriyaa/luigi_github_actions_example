# Luigi GitHub Actions Example

This project demonstrates:
- A simple Luigi pipeline
- GitHub Actions for CI (linting, testing, and running Luigi)
- Use of `pre-commit` for local linting

## To Use

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run Luigi: `luigi --module luigi_pipeline.tasks PrintDateTask --local-scheduler`

## Pre-commit

Install and run pre-commit:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```
