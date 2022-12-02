input = "/Users/annpeeters/advent/data/day1_input.txt"

with open(input, 'r') as file:
    most_calories = 0
    current_calories = 0
    for line in file:
        data = line.strip()
        if data != '':
            data = int(data)
            current_calories += data
        else:
            if current_calories > most_calories:
                most_calories = current_calories
            current_calories = 0
    print(most_calories)
