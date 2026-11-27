import pytest

from utils import factorial


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120)])
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_factorial_rejects_negative():
    with pytest.raises(ValueError):
        factorial(-1)
