"""
# THOUGHT PROCESS
______________
| [D]        |
| [N] [C]    |
| [Z] [M] [P]|
|  1   2   3 |
|____________|

## 1. structure crates to get from input
' 1   2   3   4   5   6   7   8   9 '
 012345678901234567890 
 one space LETTER two spaces * 9
 important to get the "nothing on the stack"-space
 in example:
 ".x.." * 3
 line 1 --> "D.."
 line 2 --> "NC."

## 2. crate_stack
top to bottom --> so I can use `pop`
stack1 = 'ZND'
stack2 = 'MC'

## 3. kind of input
line 1 --> 8 (incl.) represents the crates
line 11 --> end (inlc. ) represents the movements

"""
from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
input = data_folder / "day5_input.txt"


with open(input, "r") as file:
    stacks = []
    location_of_s = [
        x for x in range(1, 36, 4)
    ]  # the 9 stacks are located here

    for i, line in enumerate(file):
        if i < 8:  # stack data
            for s in range(len(location_of_s)):
                box = "{:<36}".format(line.strip())[location_of_s[s]]
                if i == 0:
                    stacks.append([])
                stacks[s].append(box)
        if i > 9:  # move data
            how_many_text, what_stacks_text = line.strip().split("from ")
            how_many_boxes = int(how_many_text.strip("move "))
            from_stack, to_stack = what_stacks_text.split(" to")
            from_stack, to_stack = int(from_stack) - 1, int(to_stack) - 1
            for box in range(how_many_boxes):
                box_on_crane = stacks[from_stack].pop(0)
                stacks[to_stack].insert(0, box_on_crane)

top = []
for stack in stacks:
    print(stack)
    top_box = stack.pop(0)
    top.append(top_box)
print("".join(top))
