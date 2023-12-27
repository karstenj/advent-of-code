import copy
import sys
import unittest
import re
import functools

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    queue = []
    lines = [list(l.strip()) for l in lines]
    for r, l in enumerate(lines):
        for c, char in enumerate(l):
            if char == 'S':
                queue.append((r, c))
                break
        if len(queue) > 0:
            break
    for i in range(64):
        new_queue = []
        plot = copy.deepcopy(lines)
        while len(queue) > 0:
            (r, c) = queue.pop()
            moves = [(r, c-1), (r,c+1), (r-1,c), (r+1,c)]
            for rn, cn in moves:
                if rn >= 0 and rn < len(plot) and cn >= 0 and cn < len(plot[r]):
                    if plot[rn][cn] in ['.', 'S']:
                        plot[rn][cn] = 'O'
                        new_queue.append((rn, cn))
        #print(len(new_queue))
        queue = new_queue

    result = len(new_queue)

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
