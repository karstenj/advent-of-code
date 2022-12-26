import sys
from collections import deque

def show_grid(grid):
    for i, r in enumerate(grid):
        print(''.join(r))

class Rock:
    def __init__(self, shape):
        self.shape = [[c for c in l.strip()] for l in shape]
        self.width = len(shape[0])
        self.height = len(shape)

    def can_move_rock(self, rock_x, rock_y, new_grid):
        y = rock_y - self.height + 1
        x = rock_x
        if y < 0 or (x+self.width) > 7:
            print('error')
        for h in range(self.height):
            for w in range(self.width):
                if self.shape[h][w] == '#' and new_grid[y+h][x+w] == '#':
                    return False
        return True

    def put_rock(self, rock_x, rock_y, new_grid):
        y = rock_y - self.height + 1
        x = rock_x
        if y < 0 or (x+self.width) > 7:
            print('error')
        for h in range(self.height):
            for w in range(self.width):
                if self.shape[h][w] == '#' and new_grid[y + h][x + w] == '#':
                    print(f"error x={rock_x} y={rock_y} w={self.width} h={self.height}")
                    show_grid(new_grid)
                    sys.exit(1)
                if self.shape[h][w] == '#':
                    new_grid[y+h][x+w] = self.shape[h][w]


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    jet_stream = lines[0].strip()
    rocks_file_names = [
        'rock_line_horz.txt',
        'rock_cross.txt',
        'rock_l.txt',
        'rock_line_vert.txt',
        'rock_square.txt'
    ]
    rocks = []
    for file_name in rocks_file_names:
        with open(file_name) as fh:
            lines = fh.readlines()
            lines = [l.strip() for l in lines]
            rocks.append(Rock(lines))
    rock_index = 0
    jet_index = 35
    grid = deque([])
    empty_line = ['.'] * 7
    old_height = 0
    old_round = 0
    remaining = 1000000000000 % 1740
    fak = 1000000000000 // 1740
    height = 2724 * fak - 7
    #height = 0
    for r in range(remaining):
        if (r % 1740) == 0:
            y = 0
            while y < len(grid) and '#' not in grid[y]:
                y += 1
            act_height = len(grid) - y
            delta_round = r - old_round
            old_round = r
            delta_height = act_height - old_height
            old_height = act_height
            print(f'{r} {act_height} {delta_height} {delta_round} {jet_index} {rock_index}')

        y = 0
        rock = rocks[rock_index]
        rock_index = (rock_index+1) % len(rocks)
        while y < len(grid) and '#' not in grid[y]:
            y += 1
        for j in range(y, 3+rock.height):
            grid.appendleft(empty_line.copy())
            y += 1
        #new_grid = new_grid + grid[:10]
        #height += len(grid[10:])
        rock_x = 2
        rock_y = y - 4
        while True:
            jet = jet_stream[jet_index]
            jet_index = (jet_index+1) % len(jet_stream)
            #print(jet_index)
            # move lef or right
            if jet == '>' and (rock_x + rock.width) < 7 and rock.can_move_rock(rock_x + 1, rock_y, grid):
                rock_x += 1
            elif jet == '<' and rock_x > 0 and rock.can_move_rock(rock_x - 1, rock_y, grid):
                rock_x -= 1
            # move down
            if rock_y == (len(grid)-1):
                rock.put_rock(rock_x, rock_y, grid)
                break
            if rock.can_move_rock(rock_x, rock_y + 1, grid):
                rock_y += 1
            else:
                rock.put_rock(rock_x, rock_y, grid)
                break
        #print(i)
        #show_grid(new_grid)
        #grid = new_grid
    y = 0
    while y < len(grid) and '#' not in grid[y]:
        y += 1
    result = len(grid)-y+height
    #print(len(grid)-y+height)
    #show_grid(grid)
    return result
