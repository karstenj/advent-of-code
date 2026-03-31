from collections import deque


def read_input(file_path):
    """Reads the racetrack map from the input file."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]


def find_positions(grid):
    """Find the start (S) and end (E) positions in the grid."""
    start, end = None, None
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
            elif cell == 'E':
                end = (x, y)
    return start, end


def neighbors(x, y, grid):
    """Generate valid neighbors for a given position."""
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            yield nx, ny


def bfs_with_cheat(grid, start, end):
    """Perform BFS to find all cheats and their time savings."""
    queue = deque([(start, 0, False)])  # (position, time, used_cheat)
    visited = {}
    cheats = []

    while queue:
        (x, y), time, used_cheat = queue.popleft()

        if (x, y, used_cheat) in visited and visited[(x, y, used_cheat)] <= time:
            continue
        visited[(x, y, used_cheat)] = time

        if (x, y) == end:
            continue

        for nx, ny in neighbors(x, y, grid):
            if grid[ny][nx] != '#' or used_cheat:
                queue.append(((nx, ny), time + 1, used_cheat))

        if not used_cheat:
            # Try using a cheat
            for cheat_x, cheat_y in neighbors(x, y, grid):
                if grid[cheat_y][cheat_x] == '#':
                    for nx, ny in neighbors(cheat_x, cheat_y, grid):
                        if grid[ny][nx] != '#':
                            cheat_time = time + 2
                            if (nx, ny, True) not in visited or visited[(nx, ny, True)] > cheat_time:
                                queue.append(((nx, ny), cheat_time, True))
                                cheats.append((time + 1, cheat_time))

    return cheats


def count_cheats(cheats, min_savings):
    """Count the number of cheats that save at least the given amount of time."""
    return sum(1 for original, cheat in cheats if original - cheat >= min_savings)


def main(file_path):
    grid = read_input(file_path)
    start, end = find_positions(grid)
    cheats = bfs_with_cheat(grid, start, end)
    result = count_cheats(cheats, 100)
    print(f"Number of cheats that save at least 100 picoseconds: {result}")


if __name__ == "__main__":
    import sys

    main('input2.txt')
