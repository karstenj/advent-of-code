import re
import copy

RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
SIZE = 4

def get_face(coord):
    r, c = coord
    faces = [
        (0, 8),
        (4, 0),
        (4, 4),
        (4, 8),
        (8, 8),
        (8, 12)
    ]
    for i, (fr, fc) in enumerate(faces):
        if r >= fr and c >= fc and r < (fr + SIZE) and c < (fc + SIZE):
            return (i + 1, fr, fc, fr+SIZE-1, fc+SIZE-1)
    print(f'Wrong coordinate {r} {c}')
    return (0, 0, 0, 0, 0)

def get_next_coord(current, facing, grid):
    row, col = current
    (cube_face, top, left, bottom, right) = get_face(current)
    layout = {
        1: {LEFT: (3, DOWN), RIGHT: (6, LEFT), UP: (2, DOWN), DOWN: (4, DOWN)},
        2: {LEFT: (6, UP), RIGHT: (3, RIGHT), UP: (1, DOWN), DOWN: (5, UP)},
        3: {LEFT: (2, LEFT), RIGHT: (4, RIGHT), UP: (1, RIGHT), DOWN: (5, RIGHT)},
        4: {LEFT: (3, LEFT), RIGHT: (6, DOWN), UP: (1, UP), DOWN: (5, DOWN)},
        5: {LEFT: (3, UP), RIGHT: (6, RIGHT), UP: (4, UP), DOWN: (2, UP)},
        6: {LEFT: (5, LEFT), RIGHT: (1, LEFT), UP: (4, LEFT), DOWN: (2, RIGHT)}
    }
    (new_face, new_facing) = layout[cube_face][facing]
    if facing == LEFT:
        if col > left:
            if grid[row][col-1] != '#':
                return (row, col-1, LEFT)
        if new_facing == LEFT and grid[row][col-1] != '#':
            return (row, col - 1, LEFT)
        if new_facing == RIGHT and grid[row][col - 1] != '#':
            return (row, col - 1, LEFT)
    elif facing == RIGHT:
        if col < right:
            if grid[row][col+1] != '#':
                return (row, col+1, RIGHT)
    elif facing == UP:
        if row > top:
            if grid[row-1][col] != '#':
                return (row-1, col, UP)
    elif facing == DOWN:
        if row < bottom:
            if grid[row+1][col] != '#':
                return (row+1, col, UP)




def get_number_part2(input1_file_name, input2_file_name):
    result = 0
    with open(input1_file_name) as fh:
        lines = fh.read()
    grid = lines.split('\n')
    with open(input2_file_name) as fh:
        lines = fh.readlines()
    cmd = lines[0].strip()
    row = 0
    col = grid[row].find('.')
    facing = RIGHT
    while len(cmd) > 0:
        if cmd[0] == 'R':
            facing = (facing + 1) % 4
            cmd = cmd[1:]
        elif cmd[0] == 'L':
            facing = (facing - 1) if facing > 0 else 3
            cmd = cmd[1:]
        else:
            i_r = cmd.find('R')
            i_l = cmd.find('L')
            if i_r == -1 and i_l == -1:
                steps = int(cmd)
                cmd = []
            elif (i_r < i_l or i_l == -1) and i_r >= 0:
                steps = int(cmd[:i_r])
                cmd = cmd[i_r:]
            elif (i_l < i_r or i_r == -1) and i_l >= 0:
                steps = int(cmd[:i_l])
                cmd = cmd[i_l:]
            else:
                print('error')
            for s in range(steps):
                if facing == RIGHT:
                    if col < (len(grid[row]) - 1) and grid[row][col+1] != ' ':
                        if grid[row][col+1] == '.':
                            col += 1
                    elif col == 49 and row >= 150 and row < 200:
                        # change from 6 => 5
                        nr = 149
                        nc = 50 + row - 150
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = UP
                    elif col == 99 and row >= 50 and row < 100:
                        # change from 3 => 2
                        nr = 49
                        nc = 100 + row - 50
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = UP
                    elif col == 99 and row >= 100 and row < 150:
                        # change from 5 => 2
                        nr = 49 - (row - 100)
                        nc = 149
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = LEFT
                    elif col == 149 and row >= 0 and row < 50:
                        # change from 2 => 5
                        nr = 149 - row
                        nc = 99
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = LEFT
                    else:
                        raise Exception
                elif facing == LEFT:
                    if col > 0 and grid[row][col - 1] != ' ':
                        if grid[row][col - 1] == '.':
                            col -= 1
                    elif col == 0 and row >= 100 and row < 150:
                        # change from 4 => 1
                        nr = 49 - (row - 100)
                        nc = 50
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = RIGHT
                    elif col == 50 and row >= 0 and row < 50:
                        # change from 1 => 4
                        nr = 149 - row
                        nc = 0
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = RIGHT
                    elif col == 0 and row >= 150 and col < 200:
                        # change from 6 => 1
                        nr = 0
                        nc = 50 + row - 150
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = DOWN
                    elif col == 50 and row >= 50 and col < 100:
                        # change from 3 => 4
                        nr = 100
                        nc = row - 50
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = DOWN
                    else:
                        raise Exception
                elif facing == UP:
                    if row > 0 and grid[row - 1][col] != ' ':
                        if grid[row - 1][col] == '.':
                            row -= 1
                    elif row == 0 and col >= 50 and col < 100:
                        # change from 1 => 6
                        nr = 150+(col-50)
                        nc = 0
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = RIGHT
                    elif row == 100 and col >= 0 and col < 50:
                        # change from 4 => 3
                        nr = 50 + col
                        nc = 50
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = RIGHT
                    elif row == 0 and col >= 100 and col < 150:
                        # change from 2 => 6
                        nr = 199
                        nc = col - 100
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = UP
                    else:
                        raise Exception
                elif facing == DOWN:
                    if row < (len(grid)-1) and grid[row + 1][col] != ' ':
                        if grid[row + 1][col] == '.':
                            row += 1
                    elif row == 149 and col >= 50 and col < 100:
                        # change from 5 => 6
                        nr = 150 + col - 50
                        nc = 49
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = LEFT
                    elif row == 199 and col >= 0 and col < 50:
                        # change from 6 => 2
                        nr = 0
                        nc = 100 + col
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = DOWN
                    elif row == 49 and col >= 100 and col < 150:
                        # change from 2 => 3
                        nr = 50 + col - 100
                        nc = 99
                        if grid[nr][nc] != '#':
                            row = nr
                            col = nc
                            facing = LEFT
                    else:
                        raise Exception
                if row < 0 or col < 0:
                    raise Exception
    # find start point
    #print(grid)
    #print(cmd)
    result = 1000 * (row+1) + 4 * (col+1) + facing
    return result
