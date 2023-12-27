import copy
import itertools
import sys
import unittest
import re
import functools

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    queue = {}
    plots = set()
    lines = [list(l.strip()) for l in lines]
    for r, l in enumerate(lines):
        for c, char in enumerate(l):
            if char == 'S':
                queue[(r, c)] = 0
                plots.add((r, c))
                lines[r][c] = '.'
            if char == '.':
                plots.add((r, c))
    width = len(lines[0])
    height = len(lines)
    print(height, width)
    diff = [0] * width
    diff_diff = [0] * width
    last_diff_diff = [0] * width
    last_length = 0
    for count in itertools.count(1):
        new_queue = {}
        for (r, c) in queue:
            moves = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
            for rn, cn in moves:
                rp = rn % height
                cp = cn % width
                if lines[rp][cp] == '.' and (rn, cn) not in new_queue:
                    new_queue[(rn, cn)] = 0

        index = count % width
        act_diff = len(new_queue) - last_length
        diff_diff[index] = act_diff - diff[index]
        diff[index] = act_diff
        #print(len(new_queue)-last_length)
        last_length = len(new_queue)
        if count % width == 0 and count > 0:
            if all([a == b for a, b in zip(diff_diff, last_diff_diff)]):
                break

            last_diff_diff = diff_diff
            diff_diff = [0] * width
        queue = new_queue

    length = len(new_queue)
    print(count, length, diff_diff)
    for i in itertools.count(count+1):
        index = i % width
        diff[index] += diff_diff[index]
        length += diff[index]

        if i in [100, 500, 1000, 5000]:
            print(i, length)

        if i == 26501365:
            print(length)
            break


    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
