from loan_simulator.domain import calc
from datetime import date


def test_calc() -> None:
    assert calc(500, 0.10, 5) == 491.67
