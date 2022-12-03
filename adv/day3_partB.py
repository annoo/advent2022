import pytest
input = ("/Users/annpeeters/advent/data/day3_input.txt")
# somthing wrong with the cache and the poetry venv?


@pytest.mark.parametrize("given, expected", [
             (('vJrwpWtwJgWrhcsFMMfFFhFp',
               'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
               'PmmdzqPrVvPwwTWBwg'
               ),
              'r'),
             (('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
               'ttgJtRGJQctTZtZT',
               'CrZsJsPPZsGzwwsLwLmpwMDw'
               ),
              'Z'),
            ]
            )
def test_detect_similar_items(given, expected):
    content = given
    same_item = look_for_same_item_in_rucksacks(content)
    assert same_item == expected


@pytest.mark.parametrize("given, expected", [
                                            ('p', 16),
                                            ('L', 38),
                                            ('P', 42),
                                            ('v', 22),
                                            ]
                         )
def test_lookup_priority_number(given, expected):
    letter = given
    priority_number = lookup_priority_number(letter)
    assert priority_number == expected


# CODE
def split_in_half(content: str) -> tuple[str, str]:
    pass


# @Maarten: very similar function, how would I best "reuse it"
# there must be a better way than c/p and adapt :)
# != input: from str to list(str) as input; so feeding it split input in a list
# using all to complete more arguments
def look_for_same_item(content: str) -> str:
    comp1, comp2 = split_in_half(content)
    same = ''.join(set(comp1) & set(comp2))
    return same


def look_for_same_item_in_rucksacks(rucksack_of_team: list[str]) -> str:
    return ''.join(set(rucksack_of_team[0])
                   .intersection(*set(rucksack_of_team)))
    # is ther another fuctional way to do this properly?


def lookup_priority_number(letter: str) -> int:
    if letter.islower():
        return ord(letter) - 96     # using ASCII values ot set 'a' as 1
    else:
        return ord(letter) - 38     # using ASCII values ot set 'A' as 27


with open(input, 'r') as file:
    numbers = []
    three_rucksacks = []
    for i, line in enumerate(file):
        if (i+1) % 3 != 0:
            three_rucksacks.append(line.strip())
        else:
            three_rucksacks.append(line.strip())
            number = lookup_priority_number(
                look_for_same_item_in_rucksacks(three_rucksacks))
            numbers.append(number)
            three_rucksacks = []
            break
    print(sum(numbers))
