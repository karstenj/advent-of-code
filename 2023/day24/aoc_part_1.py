import copy
import sys
import unittest
import re
import functools
from collections import namedtuple
import sympy as sy

V = namedtuple('V', 'x y z')
P = namedtuple('P', 'p v')

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [l.strip() for l in lines]
    points = []
    for l in lines:
        p, v = l.split('@')
        p = tuple([int(x.strip()) for x in p.split(',')])
        v = tuple([int(x.strip()) for x in v.split(',')])
        points.append(P(V(*p), V(*v)))
    #print(points)

    for i in range(len(points) - 1):
        print(i)
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]
            s, t = sy.symbols("s t")
            equations = [
                sy.Eq(p1.p.x + t * p1.v.x, p2.p.x + s * p2.v.x),
                sy.Eq(p1.p.y + t * p1.v.y, p2.p.y + s * p2.v.y)
            ]
            f = sy.solve(equations)
            #print(f)
            if len(f) == 2:
                x1 = p1.p.x + float(f[t]) * p1.v.x
                y1 = p1.p.y + float(f[t]) * p1.v.y
                #print(f)
                ll = 200000000000000
                ul = 400000000000000
                if x1 >= ll and x1 <= ul and y1 >= ll and y1 <= ul and float(f[s]) >= 0 and float(f[t]) >= 0:
                    result += 1
                #print(x1, y1, x2, y2, result)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
