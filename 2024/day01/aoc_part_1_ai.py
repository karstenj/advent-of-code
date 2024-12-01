def calculate_total_distance(file_path):
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []

        # Read input file
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Sort both lists
    left_list.sort()
    right_list.sort()

    # Calculate total distance
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance


# Replace 'input.txt' with your actual file path
file_path = 'input2.txt'
total_distance = calculate_total_distance(file_path)
print(total_distance)
