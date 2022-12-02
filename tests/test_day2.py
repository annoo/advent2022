import pytest

from adv.day2_part1 import (
                        determine_score_for_a_shape,
                        calculate_score_of_a_round
)

expected_points = [('A', 1),
                   ('B', 2),
                   ('C', 3),
                   ('X', 1),
                   ('Y', 2),
                   ('Z', 3)
                   ]


@pytest.mark.parametrize("letter, expected_point", expected_points)
def test_A_letters_get_assigned_the_right_weight(letter, expected_point):
    assert determine_score_for_a_shape(letter) == expected_point


scoretable = [(('A', 'Y'), 8),
              (('B', 'X'), 1),
              (('C', 'Z'), 6),
              ]


@pytest.mark.parametrize("play", "expected_score", scoretable)
def test_A_returns_winning_score(play, expexted_score):
    score = calculate_score_of_a_round(play)

    assert score == expexted_score
