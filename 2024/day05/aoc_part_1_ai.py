def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()

    # Separate rules and updates
    rules = []
    updates = []
    for line in lines:
        if "|" in line:
            rules.append(tuple(map(int, line.split("|"))))
        elif line:
            updates.append(list(map(int, line.split(","))))

    return rules, updates


def is_update_in_order(update, rules):
    # Create a position map for the current update
    position = {page: idx for idx, page in enumerate(update)}

    for x, y in rules:
        if x in position and y in position:
            # x must appear before y in the update
            if position[x] >= position[y]:
                return False
    return True


def calculate_middle_sum(rules, updates):
    middle_sum = 0
    for update in updates:
        if is_update_in_order(update, rules):
            # Find the middle page number
            middle_index = len(update) // 2
            middle_sum += update[middle_index]
    return middle_sum


if __name__ == "__main__":
    # Input file path
    file_path = "input2.txt"

    # Parse the input file
    rules, updates = parse_input(file_path)

    # Calculate the sum of middle page numbers for correctly ordered updates
    result = calculate_middle_sum(rules, updates)

    print(f"The sum of the middle page numbers of correctly ordered updates is: {result}")
