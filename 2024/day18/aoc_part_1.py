import heapq


def valid_position(maze, x, y):
    """Checks if a position is valid (within bounds and not a wall)."""
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and maze[y][x] != '#'


def solve_maze(maze, width, height):
    """Finds the lowest score to navigate the maze."""
    start = (0, 0)
    end = (width-1, height-1)

    # Directions: (dx, dy) and their corresponding indices
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

    # Priority queue: (steps, x, y)
    pq = []
    heapq.heappush(pq, (0, start[0], start[1]))

    # Visited set: (x, y, facing_direction)
    visited = set()

    while pq:
        steps, x, y = heapq.heappop(pq)

        # If we've reached the end, return the score
        if (x, y) == end:
            return steps

        # Skip if already visited with the same direction
        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore all possible moves
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # Check if the next position is valid
            if valid_position(maze, nx, ny):
                # Calculate the cost of moving to this position
                heapq.heappush(pq, (steps + 1, nx, ny))

def get_number_part(input_file_name, width, height, n_locations):
    print(input_file_name)
    with open(input_file_name) as fh:
        lines = fh.readlines()
    locations = []
    for l in lines:
        row, col = map(int, l.strip().split(','))
        locations.append((row, col))
    maze = []
    for y in range(height):
        l = []
        for x in range(width):
            if (x, y) in locations[:n_locations]:
                l.append('#')
            else:
                l.append('.')
        maze.append(l)

    return solve_maze(maze, width, height)

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt', 7, 7, 12)
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt', 71, 71, 1024)
    print(f'Solution part 1: {solution_2}')
