import unittest
import re
import functools

#@functools.cache
def move(r, c, lines):
    if r > 0 and lines[r-1][c] == '.':
        lines[r][c] = '.'
        lines[r-1][c] = 'O'
        move(r-1, c, lines)

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [list(l.strip()) for l in lines]
    for r, l in enumerate(lines):
        for c, char in enumerate(l):
            if char == 'O':
                move(r, c, lines)
    for r, l in enumerate(lines):
        #print(l)
        for c, char in enumerate(l):
            if char == 'O':
                result += len(lines) - r


    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
