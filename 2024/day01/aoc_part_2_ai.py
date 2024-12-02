from collections import Counter


def calculate_similarity_score(file_path):
    with open(file_path, 'r') as file:
        left_list = []
        right_list = []

        # Read input file
        for line in file:
            left, right = map(int, line.strip().split())
            left_list.append(left)
            right_list.append(right)

    # Count occurrences in the right list
    right_count = Counter(right_list)

    # Calculate similarity score
    similarity_score = sum(num * right_count[num] for num in left_list)
    return similarity_score


# Replace 'input.txt' with the path to your file
file_path = 'input2.txt'
similarity_score = calculate_similarity_score(file_path)
print(similarity_score)
