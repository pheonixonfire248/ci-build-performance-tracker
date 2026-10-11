"""Run the test suite, time it, and append the result to data/build_times.csv."""
import csv
import os
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CSV_PATH = Path("data/build_times.csv")
FIELDS = ["timestamp_utc", "commit", "branch", "status", "duration_s"]


def main() -> int:
    start = time.perf_counter()
    result = subprocess.run([sys.executable, "-m", "pytest", "-q"])
    duration = round(time.perf_counter() - start, 2)

    CSV_PATH.parent.mkdir(exist_ok=True)
    new_file = not CSV_PATH.exists()
    with CSV_PATH.open("a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "commit": os.getenv("GITHUB_SHA", "local")[:7],
            "branch": os.getenv("GITHUB_REF_NAME", "local"),
            "status": "pass" if result.returncode == 0 else "fail",
            "duration_s": duration,
        })
    print(f"Test run took {duration}s, status={'pass' if result.returncode == 0 else 'fail'}")
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
