import copy
import sys
import unittest
import re
import functools
from collections import namedtuple

C = namedtuple('C', 'x y z')
CUBE = namedtuple('CUBE', 's e n')


def get_n_fall(s1, support_to, support_by, fall):
    if s1 in support_to:
        for s2 in support_to[s1]:
            if s1 in support_by[s2]:
                support_by[s2].remove(s1)
                if len(support_by[s2]) == 0:
                    fall.add(s2)
                    get_n_fall(s2, support_to, support_by, fall)


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    cubes = []
    for i, l in enumerate(lines):
        start, end = l.split('~')
        start = tuple([int(v) for v in start.split(',')])
        end = tuple([int(v) for v in end.split(',')])
        c = (CUBE(C(*start), C(*end), i))
        #print(c)
        cubes.append(c)

    min_x = lambda a: min(a.s.x, a.e.x)
    max_x = lambda a: max(a.s.x, a.e.x)
    min_y = lambda a: min(a.s.y, a.e.y)
    max_y = lambda a: max(a.s.y, a.e.y)
    min_z = lambda a: min(a.s.z, a.e.z)
    max_z = lambda a: max(a.s.z, a.e.z)
    cubes.sort(key=min_z)
    #print(cubes)

    def intersects(a, b):
        return (max_x(a) >= min_x(b)
            and min_x(a) <= max_x(b)
            and max_y(a) >= min_y(b)
            and min_y(a) <= max_y(b))

    stack = []
    for c in cubes:
        if min_z(c) == 1:
            stack.append(c)
            continue
        z = 1
        for s in stack:
            if intersects(c, s):
                z = max(z, max_z(s) + 1)
        d = max_z(c) - min_z(c)
        c = c._replace(s = c.s._replace(z = z if c.s.z == min_z(c) else z + d))
        c = c._replace(e = c.e._replace(z = z if c.e.z == min_z(c) else z + d))
        stack.append(c)
    #print(stack)
    support_by = {}
    support_to = {}
    for s1 in stack:
        for s2 in stack:
            if s1.n != s2.n:
                if max_z(s1)+1 == min_z(s2) and intersects(s1, s2):
                    support_by.setdefault(s2, [])
                    support_by[s2].append(s1)
                    support_to.setdefault(s1, [])
                    support_to[s1].append(s2)
    #print(support_to)
    #print(support_by)
    for s1 in stack:
        fall = set()
        get_n_fall(s1, copy.deepcopy(support_to), copy.deepcopy(support_by), fall)
        result += len(fall)
        #print(len(fall))

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
