from pathlib import Path

data_folder = Path(__file__).parent.parent / "data"
real_input = data_folder / "day20_input.txt"
fake_input = data_folder / "day20_fake.txt"


def parse_data(input):
    data = []
    new_order = []
    with open(input, "r") as file:
        for idx, line in enumerate(file):
            item = int(line.strip())
            data.append(item)
            new_order.append((idx, item))
    return data, new_order


def calculat_new_index(pos: int, number: int, maxi: int) -> int:
    total = (pos + number) % (maxi - 1)
    if total == 0:
        return maxi
    else:
        return total


data, new_order = parse_data(real_input)
length = len(data)


for idx, item in enumerate(data):
    position = next(
        new_order.index(item) for item in new_order if item[0] == idx
    )
    element = new_order.pop(position)

    new_index = calculat_new_index(position, item, length)

    new_order.insert(new_index, element)

    # print(element[1], "goes from", position, "to", new_index)
    index, order = zip(*new_order)
    # print(order)


zero_at = order.index(0)
print("index of zero is", zero_at)
coord_1 = order[(zero_at + 1000) % (length)]
coord_2 = order[(zero_at + 2000) % (length)]
coord_3 = order[(zero_at + 3000) % (length)]

print(coord_1 + coord_2 + coord_3)

# 0 -> 1 (item = 1)
# 1 -> 3 (item = 2)
# 1 -> 4 (item = -3) ## %len-1 if neg-
# 5 -> 3 (item = 4)
