import pytest
from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
input = data_folder / "day6_input.txt"


@pytest.mark.parametrize(
    "given, expected",
    [
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_position_of_the_marker_is_detected_correctly(given, expected):
    input = given
    position = detect_position_of_marker(input)
    assert position == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ],
)
def test_position_of_the_start_of_msg_is_detected_correctly(given, expected):
    input = given
    position = detect_position_of_marker(input, 14)
    assert position == expected


def detect_position_of_marker(input: str, length=4) -> int:
    from_ = 0
    to_ = length
    for i in input:
        test = input[from_:to_]
        if len(set(test)) == length:
            return to_
        else:
            from_ += 1
            to_ += 1


with open(input, "r") as file:
    for line in file:
        input = line.strip()

print(detect_position_of_marker(input, 14))
