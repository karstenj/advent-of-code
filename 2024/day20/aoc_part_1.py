import heapq


def valid_position(maze, x, y, allow_blocked):
    """Checks if a position is valid (within bounds and not a wall)."""
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and (maze[y][x] != '#' or allow_blocked)


def solve_maze(maze, start, end, allow_blocked, max_steps):
    """Finds the lowest score to navigate the maze."""
    results = []

    # Directions: (dx, dy) and their corresponding indices
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

    # Priority queue: (steps, x, y, bx, by)
    pq = []
    if allow_blocked:
        heapq.heappush(pq, (0, start[0], start[1], -1, -1))
    else:
        heapq.heappush(pq, (0, start[0], start[1], 0, 0))

    # Visited set: (x, y, bx, by)
    visited = set()

    while pq:
        steps, x, y, bx, by = heapq.heappop(pq)

        # If we've reached the end, return the score
        if (x, y) == end:
            print(steps, bx, by)
            results.append(steps)
            continue

        # Skip if already visited with the same direction
        if (x, y, bx, by) in visited:
            continue
        visited.add((x, y, bx, by))
        if allow_blocked and steps > max_steps:
            continue

        # Explore all possible moves
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # Check if the next position is valid
            if valid_position(maze, nx, ny, bx == -1 and by == -1):
                if maze[ny][nx] == '#':
                    # Calculate the cost of moving to this position
                    heapq.heappush(pq, (steps + 1, nx, ny, nx, ny))
                else:
                    heapq.heappush(pq, (steps + 1, nx, ny, bx, by))
    return results
def get_number_part(input_file_name, allowed_diff):
    print(input_file_name)
    with open(input_file_name) as fh:
        lines = fh.readlines()
    maze = []
    for y, l in enumerate(lines):
        l = l.strip()
        if (x := l.find('S')) >= 0:
            start = (x, y)
        if (x := l.find('E')) >= 0:
            end = (x, y)
        maze.append([c for c in l])

    print(start)
    print(end)
    print(maze)
    results_wo_blocked = solve_maze(maze, start, end, False, None)
    results_blocked = solve_maze(maze, start, end, True, results_wo_blocked[0]-100)
    diff = {}
    result = 0
    for r in results_blocked:
        if results_wo_blocked[0] > r:
            d = results_wo_blocked[0] - r
            if d >= 100:
                result += 1
            diff.setdefault(d, 0)
            diff[d] += 1
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt', 7, 7, 12)
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt', 71, 71, 1024)
    print(f'Solution part 1: {solution_2}')
