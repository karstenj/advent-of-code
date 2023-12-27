import sys
import unittest
import re
import functools
import heapq


def get_number_part(input_file_name):
    result = sys.maxsize
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    heatloss = {}
    current_path = []
    heapq.heappush(current_path, (0, 1, 'e', 1, int(lines[0][1])))
    heapq.heappush(current_path, (1, 0, 's', 1, int(lines[1][0])))
    rt, ct = (len(lines)-1, len(lines[-1])-1)
    max_length = 0
    while len(current_path) > 0:
        max_length = max(max_length, len(current_path))
        r, c, d, steps, hl = heapq.heappop(current_path)
        key = (r, c, d, steps)
        if key not in heatloss or heatloss[key] > hl:
            heatloss[key] = hl
        else:
            continue
        #print(r, c, d, hl, steps, path)
        if r == rt and c == ct:
            result = min(hl, result)
            #print(hl, result, max_length)
            continue
        moves = {
            'e': [(r, c + 1, 'e'), (r - 1, c, 'n'), (r + 1, c, 's')],
            'w': [(r, c - 1, 'w'), (r - 1, c, 'n'), (r + 1, c, 's')],
            'n': [(r - 1, c, 'n'), (r, c - 1, 'w'), (r, c + 1, 'e')],
            's': [(r + 1, c, 's'), (r, c - 1, 'w'), (r, c + 1, 'e')]
        }
        for m in moves[d]:
            rn, cn, dn = m
            if rn >= 0 and rn < len(lines) and cn >= 0 and cn < len(lines[rn]):
                if dn == d:
                    if steps < 3:
                        heapq.heappush(current_path, (rn, cn, dn, steps+1, hl+int(lines[rn][cn])))
                else:
                    heapq.heappush(current_path, (rn, cn, dn, 1, hl + int(lines[rn][cn])))

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
