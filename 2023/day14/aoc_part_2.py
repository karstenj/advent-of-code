import unittest
import re
import functools
import copy

def move_north(r, c, lines):
    if lines[r][c] == 'O' and r > 0 and lines[r-1][c] == '.':
        lines[r][c] = '.'
        lines[r-1][c] = 'O'
        move_north(r-1, c, lines)

def move_south(r, c, lines):
    if lines[r][c] == 'O' and r < len(lines)-1 and lines[r+1][c] == '.':
        lines[r][c] = '.'
        lines[r+1][c] = 'O'
        move_south(r+1, c, lines)

def move_west(r, c, lines):
    if lines[r][c] == 'O' and c > 0 and lines[r][c-1] == '.':
        lines[r][c] = '.'
        lines[r][c-1] = 'O'
        move_west(r, c-1, lines)

def move_east(r, c, lines):
    if lines[r][c] == 'O' and c < len(lines[r])-1 and lines[r][c+1] == '.':
        lines[r][c] = '.'
        lines[r][c+1] = 'O'
        move_east(r, c+1, lines)

def print_matrix(lines):
    count = 0
    for l in lines:
        print(''.join(l))
        count += l.count('O')
    print(count)

def lines_to_string(lines):
    return '\n'.join([''.join(l) for l in lines])

def string_to_lines(lines):
    return [list(l) for l in lines.split('\n')]

def get_result(lines):
    result = 0
    for r, l in enumerate(lines):
        for c, char in enumerate(l):
            if char == 'O':
                result += len(lines) - r
    return result

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [list(l.strip()) for l in lines]

    cache = {}
    for i in range(1000000000):
        #print(i)
        lines_str = lines_to_string(lines)
        if lines_str in cache:
            print('cache', i)
            keys = set()
            while i < 1000000000:
                #print(lines_str)
                x, lines_str = cache[lines_str]
                old_length = len(keys)
                keys.add(x)
                if len(keys) == old_length and x == min(keys):
                    i += ((1000000000 - i) // len(keys)) * len(keys) + 1
                else:
                    i += 1
            lines = string_to_lines(lines_str)
            break
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                move_north(r, c, lines)
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                move_west(r, c, lines)
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                move_south(len(lines) - r - 1, c, lines)
        for r in range(len(lines)):
            for c in range(len(lines[r])):
                move_east(r, len(lines[r]) - c - 1, lines)
        cache[lines_str] = (i, lines_to_string(lines))


    result = get_result(lines)



    return result

if __name__ == '__main__':
    solution_1 = get_number_part1('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part1('input2.txt')
    print(f'Solution part 1: {solution_2}')
