import unittest
import re


def check_mirror(idx, lines):
    r = min(idx+1, len(lines)-idx-1)
    for i in range(r):
        if lines[idx-i] != lines[idx+i+1]:
            return False
    return True


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    print(lines)
    pattern = []
    pattern_lines = []
    for l in lines:
        if len(l) == 0:
            pattern.append(pattern_lines)
            pattern_lines = []
        else:
            pattern_lines.append(l)
    pattern.append(pattern_lines)
    print(pattern)

    for lines in pattern:
        for i in range(len(lines)-1):
            if lines[i] == lines[i+1]:
                if check_mirror(i, lines):
                    result += (i + 1) * 100
        lines = [''.join(list(i)) for i in zip(*lines)]
        for i in range(len(lines)-1):
            if lines[i] == lines[i+1]:
                if check_mirror(i, lines):
                    result += (i + 1)

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
