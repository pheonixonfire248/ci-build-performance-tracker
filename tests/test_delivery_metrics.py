from datetime import date

import pytest

from src.delivery_metrics import at_risk, average_cycle_time, cycle_time_days

TASKS = [
    {"name": "API", "started": date(2026, 1, 1), "finished": date(2026, 1, 5)},
    {"name": "UI", "started": date(2026, 1, 2), "finished": date(2026, 1, 12)},
    {"name": "Docs", "started": date(2026, 1, 3), "finished": None},
]


def test_cycle_time():
    assert cycle_time_days(date(2026, 1, 1), date(2026, 1, 4)) == 3


def test_cycle_time_rejects_reversed_dates():
    with pytest.raises(ValueError):
        cycle_time_days(date(2026, 1, 5), date(2026, 1, 1))


def test_average_cycle_time():
    assert average_cycle_time(TASKS) == 7.0


def test_average_cycle_time_empty():
    assert average_cycle_time([]) == 0.0


def test_at_risk_flags_old_open_tasks():
    assert at_risk(TASKS, today=date(2026, 1, 20)) == ["Docs"]


def test_at_risk_ignores_recent_tasks():
    assert at_risk(TASKS, today=date(2026, 1, 6)) == []
