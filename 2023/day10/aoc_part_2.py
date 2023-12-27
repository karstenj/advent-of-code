import unittest
import re

def get_length(pipes, start_pos, prev_pos, act_pos):
    path = []
    while act_pos != start_pos:
        if act_pos in pipes:
            try:
                i = pipes[act_pos].index(prev_pos)
                path.append(act_pos)
                prev_pos = act_pos
                act_pos = pipes[act_pos][0 if i == 1 else 1]
            except ValueError:
                return None
        else:
            return None
    return path

def ray_tracing(x,y,poly):
    n = len(poly)
    inside = False
    xints = 0.0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


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
        path = get_length(pipes, start, start, act_pos)
        if path is not None:
            path.append(start)
            break
    #print(path)

    for r, l in enumerate(lines):
        s = ''
        for c, p in enumerate(l.strip()):
            if p == '.' or (r, c) not in path:
                if ray_tracing(r, c, path):
                    p = 'I'
                    result += 1
                else:
                    p = 'O'
            s += p
        #print(s)


    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input3.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
