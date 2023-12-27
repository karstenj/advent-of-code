import sys
import unittest
import re as regex
import functools

def get_area(edges):
    A = 0
    for (r1, c1), (r2, c2) in edges:
        A += (c1*r2) - (c2*r1)
    A *= 0.5
    return A

def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    r, c = 0, 0
    coords = []
    edge_points = 0
    for l in lines:
        m = regex.match(r'(\w) (\d+) \(\#(.*)\)', l)
        if m:
            dir_map = ['R', 'D', 'L', 'U']
            dir = dir_map[int(m.group(3)[5:])]
            dist = int(m.group(3)[:5], 16)
            #print(dir, dist)
            if dir == 'R':
                c += dist
            elif dir == 'L':
                c -= dist
            elif dir == 'U':
                r -= dist
            elif dir == 'D':
                r += dist
            edge_points += dist
            coords.append((r, c))
    edges = []
    for i in range(len(coords)-1):
        edges.append((coords[i], coords[i+1]))
    edges.append((coords[-1], coords[0]))
    A = get_area(edges)
    #print(coords)
    #print(A)
    #print(edge_points)
    #print(A - edge_points*0.5 + 1)
    I = A - edge_points*0.5 + 1
    result = int(I + edge_points)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
