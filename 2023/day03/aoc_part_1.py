import unittest
import re

# 532870
def has_adjacent_symbol(row, start, end, lines):
    if row > 0:
        #print(lines[row-1][max(0, start-1):min(len(lines[row-1]), end+1)])
        if len(re.findall('[^\.]', lines[row-1][max(0, start-1):min(len(lines[row-1]), end+1)])) > 0:
            return True
    if row < len(lines)-1:
        #print(lines[row+1][max(0, start-1):min(len(lines[row+1]), end+1)])
        if len(re.findall('[^\.]', lines[row+1][max(0, start-1):min(len(lines[row+1]), end+1)])) > 0:
            return True
    if start > 0:
        #print(lines[row][start-1])
        if lines[row][start-1] != '.':
            return True
    if end < len(lines[row]):
        #print(lines[row][end])
        if lines[row][end] != '.':
            return True
    return False

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [l.strip() for l in lines]
    for row, l in enumerate(lines):
        for m in re.finditer(r'\d+', l):
            #print(m.group(0))
            if has_adjacent_symbol(row, m.start(0), m.end(0), lines):
                result += int(m.group(0))
            #else:
            #    print(row, m.start(0), m.end(0), m.group(0))
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
