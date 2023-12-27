import unittest
import re

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    exp_lines = []
    empty_rows = []
    for r, l in enumerate(lines):
        if l.count('#') == 0:
            empty_rows.append(r)
        exp_lines.append(l.strip())

    exp_lines = [''.join(list(i)) for i in zip(*exp_lines)]
    lines = exp_lines
    exp_lines = []
    empty_cols = []
    for c, l in enumerate(lines):
        if l.count('#') == 0:
            empty_cols.append(c)
        exp_lines.append(l.strip())
    exp_lines = [''.join(list(i)) for i in zip(*exp_lines)]
    #for l in exp_lines:
    #    print(l)
    print(empty_rows)
    print(empty_cols)
    galaxies = []
    for r, l in enumerate(exp_lines):
        for c, x in enumerate(l):
            if x == '#':
                galaxies.append((r, c))
    for g1 in range(len(galaxies)-1):
        r1, c1 = galaxies[g1]
        for g2 in range(g1+1, len(galaxies)):
            r2, c2 = galaxies[g2]
            dist = abs(r1-r2) + abs(c1-c2)
            for r in empty_rows:
                if r > min(r1, r2) and r < max(r1, r2):
                    dist += 1000000-1
            for c in empty_cols:
                if c > min(c1, c2) and c < max(c1, c2):
                    dist += 1000000-1
            result += dist
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
