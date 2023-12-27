import sys
import unittest
import re as regex
import functools

def is_inside(r, c, rs, cs, re, ce, poly):
    inside = False
    prev_poly = False
    if r == rs or r == re:
        return False
    for cp in range(c+1, ce+1):
        act_poly = (r, cp) in poly
        if not act_poly and prev_poly:
            inside = not inside
        prev_poly = act_poly
    return inside

def fill_poly(r, c, rs, cs, re, ce, not_inside, poly):
    queue = [(r, c)]
    while len(queue) > 0:
        r, c = queue.pop()
        if r >= rs and r <= re and c >= cs and c <= ce:
            if (r, c) not in poly and (r, c) not in not_inside:
                not_inside.add((r, c))
                queue.append((r-1, c))
                queue.append((r+1, c))
                queue.append((r, c-1))
                queue.append((r, c+1))

def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    r, c = 0, 0
    rs, re, cs, ce = 0, 0, 0, 0
    coords = set([(0,0)])
    for l in lines:
        m = regex.match(r'(\w) (\d+) .*', l)
        if m:
            #print(m.group(1), m.group(2))
            for i in range(int(m.group(2))):
                if m.group(1) == 'R':
                    c += 1
                    coords.add((r, c))
                elif m.group(1) == 'L':
                    c -= 1
                    coords.add((r, c))
                elif m.group(1) == 'U':
                    r -= 1
                    coords.add((r, c))
                elif m.group(1) == 'D':
                    r += 1
                    coords.add((r, c))
                rs = min(rs, r)
                re = max(re, r)
                cs = min(cs, c)
                ce = max(ce, c)
    height = re - rs + 1
    width = ce - cs + 1
    #print(len(coords)-1, height, width)
    #coords = list(coords)
    not_inside = set()
    for r in range(rs, re+1):
        fill_poly(r, cs, rs, cs, re, ce, not_inside, coords)
        fill_poly(r, ce, rs, cs, re, ce, not_inside, coords)
    for c in range(cs, ce+1):
        fill_poly(rs, c, rs, cs, re, ce, not_inside, coords)
        fill_poly(re, c, rs, cs, re, ce, not_inside, coords)

    #print((height*width) - len(not_inside))
    for r in range(rs, re+1):
        s = ''
        for c in range(cs, ce + 1):
            if (r, c) in not_inside:
                s += '.'
            else:
                s += '#'
                result += 1
        #print(s)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
