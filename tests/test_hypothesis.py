import pytest

from hypothesis import given, strategies


def increment(num: int) -> int:
    return num + 1


@pytest.mark.parametrize(
    "number, result",
    [
        (-2, -1),
        (0, 1),
        (3, 4),
        (101234, 101235),
    ],
)
def test_increment(number, result):
    assert increment(number) == result


@given(strategies.integers())
def test_increment_using_hypothesis(number):
    assert increment(number) == number + 1
