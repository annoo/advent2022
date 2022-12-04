from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
input = data_folder / "day4_input.txt"


def pick_start_and_stop(two_numbers: str):
    start, stop = two_numbers.split("-")
    return int(start), (int(stop) + 1)


def is_range_completely_in_the_other(
    A: tuple[int, int], B: tuple[int, int]
) -> bool:
    intersection = set(range(*A)).intersection(range(*B))
    return (set(range(*A)) == intersection) or (set(range(*B)) == intersection)


def are_overlapping(A: tuple[int, int], B: tuple[int, int]) -> bool:
    return not not set(range(*A)).intersection(range(*B))


def determine_kind_of_overlap(A: tuple[int, int], B: tuple[int, int]) -> str:
    intersection = set(range(*A)).intersection(range(*B))
    if (set(range(*A)) == intersection) or (set(range(*B)) == intersection):
        return "A or B completely in intersection"
    elif not not set(range(*A)).intersection(range(*B)):
        return "some overlap"
    else:
        return "no overlap"


with open(input, "r") as file:
    overlaps_completely = []
    overlaps = []
    for i, line in enumerate(file):
        section_A, section_B = line.strip().split(",")
        rangeA = pick_start_and_stop(section_A)
        rangeB = pick_start_and_stop(section_B)
        overlap = determine_kind_of_overlap(rangeA, rangeB)
        if overlap == "A or B completely in intersection":
            overlaps_completely.append(i)
        elif overlap == "some overlap":
            overlaps.append(i)
        else:
            continue
    print(len(overlaps_completely))
    print(len(overlaps + overlaps_completely))
