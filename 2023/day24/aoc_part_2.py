import copy
import sys
import unittest
import re
import itertools
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
    x, y, z, vx, vy, vz = sy.symbols('x y z vx vy vz')

    equations = []
    syms = []
    for i, p in enumerate(points[:3]):
        t = sy.Symbol('t' + str(i))
        equations.append(p.p.x + t * p.v.x - x - t * vx)
        equations.append(p.p.y + t * p.v.y - y - t * vy)
        equations.append(p.p.z + t * p.v.z - z - t * vz)
        syms.append(t)
    result = sy.solve_poly_system(equations, *([x, y, z, vx, vy, vz] + syms))
    print(result)
    result = result[0][0] + result[0][1] + result[0][2]
    print(result)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
