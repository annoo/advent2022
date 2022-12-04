from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
input = data_folder / "day4_input.txt"


def pick_start_and_stop(two_numbers: str):
    start, stop = two_numbers.split("-")
    return int(start), (int(stop) + 1)  # range function doesn't include stop


def determine_kind_of_overlap(A: tuple[int, int], B: tuple[int, int]) -> str:
    intersection = set(range(*A)).intersection(range(*B))
    if (set(range(*A)) == intersection) or (set(range(*B)) == intersection):
        return "A or B completely in intersection"
    elif not not intersection:  # not an empty set # not set().isempty
        return "some overlap"
    else:
        return "no overlap"


with open(input, "r") as file:
    overlaps_completely = 0
    overlaps = 0
    for i, line in enumerate(file):
        section_A, section_B = line.strip().split(",")
        rangeA = pick_start_and_stop(section_A)
        rangeB = pick_start_and_stop(section_B)
        overlap = determine_kind_of_overlap(rangeA, rangeB)
        if overlap == "A or B completely in intersection":
            overlaps_completely += 1
        elif overlap == "some overlap":
            overlaps += 1
        else:
            continue
    print(overlaps_completely)
    print(overlaps + overlaps_completely)
