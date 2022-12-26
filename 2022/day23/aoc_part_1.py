from collections import deque

def show_grid(grid):
    for i, r in enumerate(grid):
        print(''.join(r))

def count_seed(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                count += 1
    return count

def extend_grid(grid):
    left = False
    right = False
    w = len(grid[0])
    h = len(grid)
    for r in range(h):
        if grid[r][w-1] == '#':
            right = True
        if grid[r][0] == '#':
            left = True
        if left and right:
            break
    if left:
        w += 1
    if right:
        w += 1
    new_grid = []
    if '#' in grid[0]:
        new_grid.append(['.' for i in range(w)])
    for r in range(len(grid)):
        line = []
        if left:
            line.append('.')
        for c in grid[r]:
            line.append(c)
        if right:
            line.append('.')
        new_grid.append(line)
    if '#' in grid[h-1]:
        new_grid.append(['.' for i in range(w)])
    return new_grid


def move(grid, checks):
    valid_moves = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                # look north
                count = 0
                for check, coord in checks:
                    #print(f'{r} {c} {len(grid)} {len(grid[0])} {check}')
                    if eval(check):
                        count += 1
                if count < len(checks):
                    for check, coord in checks:
                        #print(f'{r} {c} {check}')
                        if eval(check):
                            new_coord = eval(coord)
                            if new_coord not in valid_moves:
                                valid_moves[new_coord] = []
                            valid_moves[new_coord].append((r, c))
                            break
    for dest in valid_moves:
        if len(valid_moves[dest]) == 1:
            r1, c1 = valid_moves[dest][0]
            r2, c2 = dest
            grid[r1][c1] = '.'
            if  grid[r2][c2] == '#':
                print(f'Error {r2} {c2}')
            grid[r2][c2] = '#'

def calculate_free_space(grid):
    min_r = len(grid)
    max_r = 0
    min_c = len(grid[0])
    max_c = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    free_space = 0
    for r in range(min_r, max_r+1):
        for c in range(min_c, max_c + 1):
            if grid[r][c] != '#':
                free_space += 1
    return free_space

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.read()
    grid = lines.split('\n')
    grid = [[c for c in l] for l in grid]
    #show_grid(grid)
    checks = [
        ('grid[r-1][c-1] != "#" and grid[r-1][c] != "#" and grid[r-1][c+1] != "#"', '(r-1, c)'),
        ('grid[r+1][c-1] != "#" and grid[r+1][c] != "#" and grid[r+1][c+1] != "#"', '(r+1, c)'),
        ('grid[r-1][c-1] != "#" and grid[r][c-1] != "#" and grid[r+1][c-1] != "#"', '(r, c-1)'),
        ('grid[r-1][c+1] != "#" and grid[r][c+1] != "#" and grid[r+1][c+1] != "#"', '(r, c+1)')
    ]
    checks = deque(checks)
    for round in range(10):
        #print(f'Round {round+1}')
        grid = extend_grid(grid)
        move(grid, checks)
        #show_grid(grid)
        #print(f'Seeds {count_seed(grid)}')
        checks.append(checks.popleft())
    result = calculate_free_space(grid)
    return result
