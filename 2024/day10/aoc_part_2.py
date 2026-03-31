
import re

def find_path(row, col, grid):
    queue = [(row, col)]
    result = []
    while len(queue) > 0:
        row, col = queue.pop()
        if grid[row][col] == 9:
            result.append((row, col))
        else:
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            for dr, dc in directions:
                if (row + dr) >= 0 and (row + dr) < len(grid) and (col + dc) >= 0 and (col + dc) < len(grid[0]):
                    if (grid[(row + dr)][(col + dc)] - grid[row][col]) == 1:
                        queue.append(((row + dr), (col + dc)))
    return len(result)

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    start = []
    grid = []
    for row, l in enumerate(lines):
        for col, c in enumerate(l.strip()):
            if c == '0':
                start.append((row, col))
        grid.append([int(v) for v in l.strip()])
    for row, col in start:
        v = find_path(row, col, grid)
        print(row, col, v)
        result += v
    return result


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
