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


def bfs_with_cheat(grid, start, end, max_cheat_time):
    """Perform BFS to find all cheats and their time savings with the updated rules."""
    queue = deque([(start, 0, False, 0)])  # (position, time, used_cheat, cheat_time)
    visited = {}
    cheats = []

    while queue:
        (x, y), time, used_cheat, cheat_time = queue.popleft()

        if (x, y, used_cheat, cheat_time) in visited and visited[(x, y, used_cheat, cheat_time)] <= time:
            continue
        visited[(x, y, used_cheat, cheat_time)] = time

        if (x, y) == end:
            print(time)
            continue

        for nx, ny in neighbors(x, y, grid):
            if grid[ny][nx] != '#' or used_cheat:
                queue.append(((nx, ny), time + 1, used_cheat, cheat_time))

        if not used_cheat:
            # Try using a cheat for up to max_cheat_time
            for cheat_duration in range(1, max_cheat_time + 1):
                cheat_path = [(x, y)]
                cx, cy = x, y
                valid_cheat = True
                for _ in range(cheat_duration):
                    next_positions = [(nx, ny) for nx, ny in neighbors(cx, cy, grid) if grid[ny][nx] == '#']
                    if not next_positions:
                        valid_cheat = False
                        break
                    cx, cy = next_positions[0]  # Move to the first valid wall position
                    cheat_path.append((cx, cy))

                if valid_cheat:
                    for nx, ny in neighbors(cx, cy, grid):
                        if grid[ny][nx] != '#':
                            cheat_time = time + cheat_duration
                            if (nx, ny, True, cheat_time) not in visited or visited[
                                (nx, ny, True, cheat_time)] > cheat_time:
                                queue.append(((nx, ny), cheat_time, True, cheat_duration))
                                cheats.append((time + 1, cheat_time))

    return cheats


def count_cheats(cheats, min_savings):
    """Count the number of cheats that save at least the given amount of time."""
    return sum(1 for original, cheat in cheats if original - cheat >= min_savings)


def main(file_path):
    grid = read_input(file_path)
    start, end = find_positions(grid)
    max_cheat_time = 20
    cheats = bfs_with_cheat(grid, start, end, max_cheat_time)
    result = count_cheats(cheats, 50)
    print(f"Number of cheats that save at least 100 picoseconds: {result}")


if __name__ == "__main__":
    import sys

    main('input1.txt')
