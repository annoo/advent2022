import pytest

input = "/Users/annpeeters/advent/data/day3_input.txt"
# I've been struggling with Path
# I saw you have a way of oAuth working with request @ Maarten?


# TESTS
@pytest.mark.parametrize(
    "given, expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", ("vJrwpWtwJgWr", "hcsFMMfFFhFp")),
        (
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            ("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"),
        ),
        ("PmmdzqPrVvPwwTWBwg", ("PmmdzqPrV", "vPwwTWBwg")),
    ],
)
def test_get_items_in_2_compartments(given, expected):
    content = given
    comp1, comp2 = split_in_half(content)
    assert comp1, comp2 == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        ("vJrwpWtwJgWrhcsFMMfFFhFp", "p"),
        ("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "L"),
        ("PmmdzqPrVvPwwTWBwg", "P"),
        ("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn", "v"),
        ("ttgJtRGJQctTZtZT", "t"),
        ("CrZsJsPPZsGzwwsLwLmpwMDw", "s"),
    ],
)
def test_detect_similar_items(given, expected):
    content = given
    same_item = look_for_same_item(content)
    assert same_item == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        ("p", 16),
        ("L", 38),
        ("P", 42),
        ("v", 22),
    ],
)
def test_lookup_priority_number(given, expected):
    letter = given
    priority_number = lookup_priority_number(letter)
    assert priority_number == expected


# CODE
def split_in_half(content: str) -> tuple[str, str]:
    i = len(content) // 2
    comp1 = content[:i]
    comp2 = content[i:]
    return comp1, comp2


def look_for_same_item(content: str) -> str:
    comp1, comp2 = split_in_half(content)
    same = "".join(set(comp1) & set(comp2))
    return same


def lookup_priority_number(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96  # using ASCII values ot set 'a' as 1
    else:
        return ord(letter) - 38  # using ASCII values ot set 'A' as 27


with open(input, "r") as file:
    numbers = []
    for line in file:
        number = lookup_priority_number(look_for_same_item(line))
        numbers.append(number)
    print(sum(numbers))
