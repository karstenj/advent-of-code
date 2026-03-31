
import re


def check_xmas(row, col, dr, dc, expected, lines):
    #print(row, col, dr, dc, expected)
    if row >= 0 and row < len(lines) and col >= 0 and col < len(lines[row]) and lines[row][col] == expected[0]:
        if len(expected) == 1:
            return 1
        return check_xmas(row+dr, col+dc, dr, dc, expected[1:], lines)
    return 0
def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for row, l in enumerate(lines):
        for col, c in enumerate(l.strip()):
            directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1,-1)]
            for dr, dc in directions:
                if check_xmas(row, col, dr, dc, 'XMAS', lines):
                    #print(row, col, dr, dc, 'XMAS')
                    result += 1
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
