import unittest
import re

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    exp_lines = []
    for l in lines:
        if l.count('#') == 0:
            exp_lines.append(l.strip())
            exp_lines.append(l.strip())
        else:
            exp_lines.append(l.strip())

    exp_lines = [''.join(list(i)) for i in zip(*exp_lines)]
    lines = exp_lines
    exp_lines = []
    for l in lines:
        if l.count('#') == 0:
            exp_lines.append(l.strip())
            exp_lines.append(l.strip())
        else:
            exp_lines.append(l.strip())
    exp_lines = [''.join(list(i)) for i in zip(*exp_lines)]
    #for l in exp_lines:
    #    print(l)
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
