input = "/Users/annpeeters/advent/data/day1_input.txt"

with open(input, 'r') as file:
    most_calories = []
    current_calories = 0
    for line in file:
        data = line.strip()
        if data != '':
            data = int(data)
            current_calories += data
        else:
            most_calories.append(current_calories)
            current_calories = 0
    top3 = sorted(most_calories)[-3:]
    print(sum(top3))
