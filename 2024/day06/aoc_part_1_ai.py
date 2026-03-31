def load_map(file_path):
    """Load the map from the input file."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def get_guard_start_position(grid):
    """Find the guard's starting position and direction."""
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in directions:
                return (r, c), directions[cell]
    return None, None

def turn_right(direction):
    """Turn right 90 degrees."""
    if direction == (-1, 0):  # Up
        return (0, 1)  # Right
    elif direction == (0, 1):  # Right
        return (1, 0)  # Down
    elif direction == (1, 0):  # Down
        return (0, -1)  # Left
    elif direction == (0, -1):  # Left
        return (-1, 0)  # Up

def simulate_guard_path(grid):
    """Simulate the guard's path."""
    start_pos, direction = get_guard_start_position(grid)
    if not start_pos or not direction:
        raise ValueError("Guard start position or direction not found in the map.")

    rows, cols = len(grid), len(grid[0])
    visited = set()
    current_pos = start_pos

    while True:
        visited.add(current_pos)
        r, c = current_pos
        dr, dc = direction
        next_pos = (r + dr, c + dc)

        # Check if next position is out of bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check if next position is an obstacle
        if grid[next_pos[0]][next_pos[1]] == '#':
            direction = turn_right(direction)
        else:
            current_pos = next_pos

    return visited

def count_visited_positions(file_path):
    """Count the number of distinct positions visited by the guard."""
    grid = load_map(file_path)
    visited_positions = simulate_guard_path(grid)
    return len(visited_positions)

if __name__ == "__main__":
    input_file = "input2.txt"  # Replace with your input file path
    visited_count = count_visited_positions(input_file)
    print(f"Number of distinct positions visited: {visited_count}")
