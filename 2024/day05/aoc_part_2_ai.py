from collections import defaultdict, deque


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


def topological_sort(rules, update):
    # Create a graph from the rules that only considers the pages in the update
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_in_update = set(update)

    for x, y in rules:
        if x in pages_in_update and y in pages_in_update:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Topological sort using Kahn's algorithm
    sorted_pages = []
    zero_in_degree = deque([node for node in pages_in_update if in_degree[node] == 0])

    while zero_in_degree:
        current = zero_in_degree.popleft()
        sorted_pages.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    return sorted_pages


def correct_updates_and_calculate_middle_sum(rules, updates):
    middle_sum = 0
    for update in updates:
        if not is_update_in_order(update, rules):
            # Correct the update using topological sort
            sorted_update = topological_sort(rules, update)
            # Find the middle page number
            middle_index = len(sorted_update) // 2
            middle_sum += sorted_update[middle_index]
    return middle_sum


if __name__ == "__main__":
    # Input file path
    file_path = "input2.txt"

    # Parse the input file
    rules, updates = parse_input(file_path)

    # Calculate the sum of middle page numbers for corrected updates
    result = correct_updates_and_calculate_middle_sum(rules, updates)

    print(f"The sum of the middle page numbers of corrected updates is: {result}")
