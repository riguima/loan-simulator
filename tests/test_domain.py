from loan_simulator.domain import calc
from datetime import date


def test_calc() -> None:
    assert calc('37,03', '2,05', '1', '03/03/2023', '96') == 'R$ 1.534,24'
