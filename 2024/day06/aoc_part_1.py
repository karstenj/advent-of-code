
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    grid = []
    for r, l in enumerate(lines):
        grid.append(l.strip())
        c = grid[-1].find('^')
        if c >= 0:
            start = (r, c)
    print(start)
    row, col = start
    dr, dc = (-1, 0)
    path = set()
    while row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
        path.add((row, col))
        if (row+dr) >= 0 and (row+dr) < len(grid) and (col+dc) >= 0 and (col+dc) < len(grid[0]):
            if grid[(row+dr)][(col+dc)] == '#':
                if dr == -1:
                    dr = 0
                    dc = 1
                elif dc == 1:
                    dr = 1
                    dc = 0
                elif dr == 1:
                    dr = 0
                    dc = -1
                elif dc == -1:
                    dr = -1
                    dc = 0
                continue
            else:
                row += dr
                col += dc
        else:
            break

    return len(path)


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
