import unittest
import re
import functools

#@functools.cache
def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    for l in lines:
        for p in l.split(','):
            hash = 0
            for c in p:
                hash += ord(c)
                hash *= 17
                hash %= 256
            result += hash

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
