input = "/Users/annpeeters/advent/data/day2_input.txt"


def determine_score_for_a_shape(letter: str) -> int:
    if letter in ['A', 'X']:
        return 1
    if letter in ['B', 'Y']:
        return 2
    if letter in ['C', 'Z']:
        return 3


def calculate_score_of_a_round(play1, play2) -> int:
    your_score = determine_score_for_a_shape(play2)
    their_score = determine_score_for_a_shape(play1)
    wintable = [1, 2, 3]

    i = wintable.index(their_score)
    """
    look your number (eg paper) -> wins from i + 1
                                -> draw i
                                -> looses from i - 1
    """

    if your_score == wintable[(i + 1) % len(wintable)]:
        return 6 + your_score
    elif your_score == wintable[(i - 1) % len(wintable)]:
        return 0 + your_score
    else:       # draw
        return 3 + your_score


with open(input, 'r') as file:
    sum = 0
    for line in file:
        play = tuple(line.strip().split(' '))
        sum += calculate_score_of_a_round(*play)
    print(sum)
