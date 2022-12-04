import pytest
from adv.day4 import (
    pick_start_and_stop,
    is_range_completely_in_the_other,
    are_overlapping,
)


@pytest.mark.parametrize(
    "given, expected",
    [
        ((((6, 7)), ((4, 7))), True),
        ((((2, 8)), ((3, 6))), True),
        ((((3, 6)), ((2, 8))), True),
        ((((1, 3)), ((2, 8))), True),
        ((((5, 8)), ((7, 9))), True),
        ((((5, 7)), ((8, 9))), False),
    ],
)
def test_are_overlapping(given, expected):
    overlap = are_overlapping(*given)
    assert overlap == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        (("2-4"), (2, 5)),
        (("6-8"), (6, 9)),
        (("2-3"), (2, 4)),
    ],
)
def test_pick_start_and_stop(given, expected):
    picked = pick_start_and_stop(given)
    assert picked == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        ((((6, 7)), ((4, 7))), True),
        ((((2, 8)), ((3, 6))), True),
        ((((3, 6)), ((2, 8))), True),
        ((((1, 3)), ((2, 8))), False),
    ],
)
def test_is_range_completely_in_the_other(given, expected):
    is_in = is_range_completely_in_the_other(*given)
    assert is_in == expected
