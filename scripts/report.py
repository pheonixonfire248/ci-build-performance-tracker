"""Turn data/build_times.csv into a short markdown delivery report."""
import csv
import sys
from pathlib import Path

CSV_PATH = Path("data/build_times.csv")
OUT_PATH = Path("reports/ci_report.md")


def build_report(rows: list[dict]) -> str:
    if not rows:
        return "# CI Delivery Report\n\nNo runs recorded yet.\n"
    durations = [float(r["duration_s"]) for r in rows]
    fails = [r for r in rows if r["status"] == "fail"]
    slowest = max(rows, key=lambda r: float(r["duration_s"]))
    avg = sum(durations) / len(durations)
    risk = []
    if len(fails) / len(rows) > 0.2:
        risk.append("Failure rate above 20%: investigate flaky or broken tests.")
    if len(durations) >= 4 and durations[-1] > 1.5 * avg:
        risk.append("Latest run is 50% slower than average: check for a build-time regression.")
    lines = [
        "# CI Delivery Report",
        "",
        f"- Runs recorded: {len(rows)}",
        f"- Average duration: {avg:.2f}s",
        f"- Failure rate: {len(fails) / len(rows):.0%}",
        f"- Slowest run: {slowest['duration_s']}s (commit {slowest['commit']}, {slowest['timestamp_utc']})",
        "",
        "## Risks",
        *(f"- {r}" for r in risk or ["None flagged."]),
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    rows = list(csv.DictReader(CSV_PATH.open())) if CSV_PATH.exists() else []
    report = build_report(rows)
    OUT_PATH.parent.mkdir(exist_ok=True)
    OUT_PATH.write_text(report)
    print(report)
    return 0


if __name__ == "__main__":
    sys.exit(main())
