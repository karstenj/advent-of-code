import unittest
import re

# 31372422
def get_adjacent_symbol(row, start, end, lines):
    ret = []
    if row > 0:
        #print(lines[row-1][max(0, start-1):min(len(lines[row-1]), end+1)])
        for m in re.finditer(r'[\*]', lines[row-1][max(0, start-1):min(len(lines[row-1]), end+1)]):
            ret.append((row-1, m.start(0)+max(0, start-1)))
    if row < len(lines)-1:
        #print(lines[row+1][max(0, start-1):min(len(lines[row+1]), end+1)])
        for m in re.finditer(r'[\*]', lines[row+1][max(0, start-1):min(len(lines[row+1]), end+1)]):
            ret.append((row+1, m.start(0)+max(0, start-1)))
    if start > 0:
        #print(lines[row][start-1])
        if lines[row][start-1] == '*':
            ret.append((row, start-1))
    if end < len(lines[row]):
        #print(lines[row][end])
        if lines[row][end] == '*':
            ret.append((row, end))
    return ret

def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [l.strip() for l in lines]
    gears = {}
    for row, l in enumerate(lines):
        for m in re.finditer(r'\d+', l):
            #print(m.group(0))
            for (r, c) in get_adjacent_symbol(row, m.start(0), m.end(0), lines):
                g = gears.setdefault((r, c), [])
                g.append(int(m.group(0)))
                #print(row, col)
            #else:
            #    print(row, m.start(0), m.end(0), m.group(0))
    for g in gears:
        if len(gears[g]) == 2:
            result += gears[g][0] * gears[g][1]
        elif len(gears[g]) > 2:
            print(g, gears[g])
    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part('input1.txt')
        solution_2 = get_number_part('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
