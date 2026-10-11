# CI Build Performance & Delivery Tracker

A small Python project that treats CI as something a technical project manager can measure and manage. Every push runs the test suite on GitHub Actions, records how long it took, and produces a short delivery report with the numbers engineering leads care about: average build time, failure rate, slowest run and flagged risks.

## Why

Slow or flaky CI quietly drains engineering momentum: people wait for builds, retry failures and lose focus. You can't manage what you don't measure, so this project makes build performance visible on every commit.

## How it works

1. `.github/workflows/ci.yml` runs on every push and pull request.
2. `scripts/run_timed_tests.py` runs the tests with pytest and appends commit, branch, status and duration to `data/build_times.csv`.
3. `scripts/report.py` turns that data into `reports/ci_report.md` and shows it on the workflow run summary.
4. The data and report are uploaded as a build artifact.

`src/delivery_metrics.py` is the code under test: cycle time and at-risk task calculations used in delivery reporting.

## Run locally

```bash
pip install -r requirements.txt
python scripts/run_timed_tests.py
python scripts/report.py
```

## Project management docs

- [Project plan](docs/project-plan.md): goals, scope, milestones, resources
- [Roadmap](docs/roadmap.md): phased delivery
- [Risk register](docs/risk-register.md): risks, owners and mitigations

## Next steps

- Persist run history across CI runs (commit to a data branch or use the GitHub API)
- Add per-step timing and caching impact
- Chart build-time trends
