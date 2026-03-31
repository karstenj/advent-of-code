def find_obstruction_positions(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    turns = {'+': {'^': '>', '>': 'v', 'v': '<', '<': '^'},
             '|': {'^': '^', 'v': 'v'},
             '-': {'>': '>', '<': '<'}}
    possible_positions = set()

    # Find the guard's initial position and direction
    guard_position = None
    guard_direction = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in directions:
                guard_position = (r, c)
                guard_direction = grid[r][c]
                break
        if guard_position:
            break

    if not guard_position:
        raise ValueError("No guard position found in the grid!")

    # Function to simulate the guard's movement
    def simulate_with_obstruction(obstruction):
        # Create a copy of the grid with the obstruction
        sim_grid = [list(row) for row in grid]
        sim_grid[obstruction[0]][obstruction[1]] = '#'

        visited = set()
        pos = guard_position
        direction = guard_direction

        while True:
            if pos in visited:
                # Guard is stuck in a loop
                return True
            visited.add(pos)

            # Compute next position
            dr, dc = directions[direction]
            next_row, next_col = pos[0] + dr, pos[1] + dc

            # Check bounds
            if not (0 <= next_row < rows and 0 <= next_col < cols):
                return False  # Guard moves out of bounds

            next_cell = sim_grid[next_row][next_col]

            if next_cell == '#':
                return False  # Guard encounters an obstacle

            if next_cell in directions:
                # Guard changes direction
                direction = next_cell
            elif next_cell in turns and direction in turns[next_cell]:
                # Guard moves through a turn
                direction = turns[next_cell][direction]
            elif next_cell == '.':
                # Guard continues forward
                pass
            else:
                return False  # Invalid movement

            pos = (next_row, next_col)

    # Test each open space on the grid as a potential obstruction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.' and (r, c) != guard_position:
                if simulate_with_obstruction((r, c)):
                    possible_positions.add((r, c))

    return len(possible_positions)


# Read the input from the file
with open("input1.txt", "r") as file:
    grid_input = [line.strip() for line in file.readlines()]

# Find possible obstruction positions
result = find_obstruction_positions(grid_input)

# Output the result
print(f"The number of possible obstruction positions is: {result}")
