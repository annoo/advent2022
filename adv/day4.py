from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
input = data_folder / "day4_input.txt"


def pick_start_and_stop(two_numbers: str):
    start, stop = two_numbers.split("-")
    return int(start), (int(stop) + 1)


def is_range_completely_in_the_other(A, B) -> bool:
    return (set(range(*A)) == set(range(*A)).intersection(range(*B))) or (
        set(range(*B)) == set(range(*A)).intersection(range(*B))
    )


def are_overlapping(A, B) -> bool:
    return not not set(range(*A)).intersection(range(*B))


with open(input, "r") as file:
    overlaps_completely = []
    overlaps = []
    for i, line in enumerate(file):
        section_A, section_B = line.strip().split(",")
        rangeA = pick_start_and_stop(section_A)
        rangeB = pick_start_and_stop(section_B)
        if is_range_completely_in_the_other(rangeA, rangeB):
            overlaps_completely.append(i)
        if are_overlapping(rangeA, rangeB):
            overlaps.append(i)
    print(len(overlaps_completely))
    print(len(overlaps))
