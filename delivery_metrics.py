"""Small delivery-metrics library used as the project under test.

Computes cycle time and flags at-risk tasks, the kind of numbers a
technical project manager reports to engineering leadership.
"""
from datetime import date


def cycle_time_days(started: date, finished: date) -> int:
    """Days between work starting and finishing."""
    if finished < started:
        raise ValueError("finished date is before started date")
    return (finished - started).days


def average_cycle_time(tasks: list[dict]) -> float:
    """Average cycle time across tasks that have both start and finish dates."""
    done = [cycle_time_days(t["started"], t["finished"]) for t in tasks if t.get("finished")]
    return sum(done) / len(done) if done else 0.0


def at_risk(tasks: list[dict], today: date, threshold_days: int = 10) -> list[str]:
    """Names of unfinished tasks open longer than the threshold."""
    return [
        t["name"]
        for t in tasks
        if not t.get("finished") and (today - t["started"]).days > threshold_days
    ]
