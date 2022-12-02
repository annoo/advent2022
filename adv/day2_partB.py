input = "/Users/annpeeters/advent/data/day2_input.txt"


def determine_score_for_a_shape(letter: str) -> int:
    return ['A', 'B', 'C'].index(letter) + 1


def calculate_score_of_a_round(play: tuple) -> int:
    play1, your_shape = play

    their_score = determine_score_for_a_shape(play1)
    wintable = [1, 2, 3]
    i = their_score - 1

    if your_shape == 'X':       # loose
        points = 0
        yi = ((i - 1) % len(wintable))
    elif your_shape == 'Y':     # draw
        points = 3
        yi = i
    elif your_shape == 'Z':    # win
        points = 6
        yi = ((i + 1) % len(wintable))

    your_score = wintable[yi]

    return points + your_score


with open(input, 'r') as file:
    sum = 0
    for line in file:
        play = tuple(line.strip().split(' '))
        sum += calculate_score_of_a_round(play)
    print(sum)
