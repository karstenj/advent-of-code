import unittest
import re

def get_length(pipes, start_pos, prev_pos, act_pos):
    length = 0
    while act_pos != start_pos:
        if act_pos in pipes:
            try:
                i = pipes[act_pos].index(prev_pos)
                length += 1
                prev_pos = act_pos
                act_pos = pipes[act_pos][0 if i == 1 else 1]
            except ValueError:
                return 0
        else:
            return 0
    return length

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    pipes = {}
    connections = {
        '|': [(-1, 0), (1, 0)],
        '-': [(0, -1), (0, 1)],
        'L': [(-1, 0), (0, 1)],
        'J': [(-1, 0), (0, -1)],
        '7': [(1, 0), (0, -1)],
        'F': [(1, 0), (0, 1)]
    }
    for r, l in enumerate(lines):
        for c, p in enumerate(l.strip()):
            if p == 'S':
                start = (r, c)
            elif p != '.':
                pipes[(r, c)] = []
                for (dr, dc) in connections[p]:
                    pipes[(r, c)].append((r+dr, c+dc))

    #print(pipes)
    #print(start)
    for (dr, dc) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = start
        act_pos = (r+dr, c+dc)
        l = get_length(pipes, start, start, act_pos)
        result = max(result, l)

    result = result // 2 + 1

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
