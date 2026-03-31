import heapq


def valid_position(maze, x, y, allow_blocked):
    """Checks if a position is valid (within bounds and not a wall)."""
    return 0 <= y < len(maze) and 0 <= x < len(maze[0]) and (maze[y][x] != '#' or allow_blocked)


def solve_maze_normal(maze, start, end):
    """Finds the lowest score to navigate the maze."""
    results = []

    # Directions: (dx, dy) and their corresponding indices
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

    # Priority queue: (steps, x, y, bx, by)
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], []))

    # Visited set: (x, y, bx, by)
    visited = set()

    while pq:
        steps, x, y, path = heapq.heappop(pq)

        # If we've reached the end, return the score
        if (x, y) == end:
            print(steps, path)
            return steps, path

        # Skip if already visited with the same direction

        if (x, y) in visited:
            continue
        visited.add((x, y))

        # Explore all possible moves
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # Check if the next position is valid
            if valid_position(maze, nx, ny, False):
                heapq.heappush(pq, (steps + 1, nx, ny, path + [(nx, ny)]))
    return results

def solve_maze(maze, start, end, allow_blocked, max_steps, path):
    """Finds the lowest score to navigate the maze."""
    results = {}

    # Directions: (dx, dy) and their corresponding indices
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # East, South, West, North

    # Priority queue: (steps, x, y, bx, by)
    pq = []
    heapq.heappush(pq, (0, start[0], start[1], False, 20, []))

    # Visited set: (x, y, bx, by)
    visited = {}

    while pq:
        steps, x, y, used_cheat, cheat_time, blocked = heapq.heappop(pq)

        # If we've reached the end, return the score
        if (x, y) == end:
            print(steps, cheat_time, blocked)
            results.setdefault(steps, set())
            results[steps].add(tuple(blocked))
            continue

        # Skip if already visited with the same direction

        key = tuple([(x, y)] + blocked)
        if key in visited:
            continue
        visited[key] = steps
        if steps > max_steps:
            continue

        # Explore all possible moves
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy

            # Check if the next position is valid
            if cheat_time > 0 and valid_position(maze, nx, ny, True):
                if used_cheat:
                    b = blocked[:]
                    b[-1] = (nx, ny)
                    if (nx, ny) in path:
                        heapq.heappush(pq, (steps + 1, nx, ny, True, 0, b))
                    else:
                        heapq.heappush(pq, (steps + 1, nx, ny, True, cheat_time - 1, blocked))
                elif maze[ny][nx] == '#':
                    heapq.heappush(pq, (steps + 1, nx, ny, True, cheat_time - 1, [(x, y), (x, y)]))
                else:
                    heapq.heappush(pq, (steps + 1, nx, ny, False, cheat_time, blocked))
            elif valid_position(maze, nx, ny, False):
                heapq.heappush(pq, (steps + 1, nx, ny, used_cheat, cheat_time, blocked))
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
    steps, path = solve_maze_normal(maze, start, end)
    results_blocked = solve_maze(maze, start, end, True, steps-allowed_diff, path)
    result = 0
    for r in results_blocked:
        print(steps - r, len(results_blocked[r]))
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt', 50)
    print(f'Test solution part 1: {solution_1}')
    #solution_2 = get_number_part('input2.txt', 100)
    #print(f'Solution part 1: {solution_2}')
