import copy
import sys
import unittest
import re
import functools
from collections import namedtuple
import heapq


def get_path_to_crossing(rs, cs, crossing, lines):
    queue = [(rs, cs, [])]
    path = []
    while len(queue) > 0:
        r, c, s = queue.pop()
        if (r, c) != (rs, cs) and (r, c) in crossing:
            path.append(s)
            continue
        move = [(r,c+1, '>'), (r,c-1,'<'), (r-1,c,'^'), (r+1,c,'v')]
        for rn, cn, dn in move:
            if (rn, cn) not in s and lines[rn][cn] in ['.', dn] and (rn, cn) != (rs, cs):
                sn = copy.deepcopy(s)
                sn.append((rn, cn))
                queue.append((rn, cn, sn))
    return path


def get_crossing(lines):
    crossing = []
    for r, l in enumerate(lines[1:-1]):
        for c, char in enumerate(l):
            if char == '.':
                move = [(r,c+1), (r,c-1), (r-1,c), (r+1,c)]
                count = 0
                for (rn, cn) in move:
                    if lines[rn+1][cn] in ['.', '<', '>', 'v', '^']:
                        count += 1
                if count > 2:
                    # crossing
                    crossing.append((r+1, c))
                elif count == 1:
                    # deadend
                    pass
    return crossing

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [l.strip() for l in lines]
    rs = 0
    cs = lines[0].find('.')
    re = len(lines)-1
    ce = lines[-1].find('.')
    #print(rs, cs, re, ce)
    lines[0] = lines[0].replace('.', '#')
    crossing = get_crossing(lines)
    crossing.append((re, ce))
    #print(len(crossing), crossing)
    paths = {}
    queue = [(rs, cs)]
    while len(queue) > 0:
        r, c = queue.pop()
        if (r, c) == (re, ce):
            continue
        path = get_path_to_crossing(r, c, crossing, lines)
        paths.setdefault((r, c), {})
        for p in path:
            rn, cn = p[-1]
            if (rn, cn) not in paths[(r, c)]:
                paths[(r, c)][(rn, cn)] = len(p)
                #paths.setdefault((rn, cn), {})
                #paths[(rn, cn)][(r, c)] = len(p)
                queue.append((rn, cn))

    queue = [(rs, cs, [], 0)]
    while len(queue) > 0:
        r, c, s, l = queue.pop()
        #print(r, c)
        if (r, c) == (re, ce):
            if result < l:
                #print(l)
                result = l
            continue
        for (rn, cn) in paths[(r, c)]:
            if (rn, cn) not in s:
                p = paths[(r, c)][(rn, cn)]
                queue.append((rn, cn, s + [(rn, cn)], l + p))

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
