import unittest
import re
import functools

def get_hash(v):
    hash = 0
    for c in v:
        hash += ord(c)
        hash *= 17
        hash %= 256
    return hash

#@functools.cache
def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()


    lines = [l.strip() for l in lines]
    boxes = [[] for i in range(256)]
    for l in lines:
        for p in l.split(','):
            #print(p)
            if p.endswith('-'):
                label = p[:-1]
                hash = get_hash(label)
                found = False
                for i, (lens, values) in enumerate(boxes[hash]):
                    if lens == label:
                        found = True
                        break
                if found:
                    boxes[hash] = boxes[hash][:i] + boxes[hash][i+1:]
            else:
                label, value = p.split('=')
                hash = get_hash(label)
                found = False
                for i, (lens, values) in enumerate(boxes[hash]):
                    if lens == label:
                        boxes[hash][i] = (label, value)
                        found = True
                        break
                if not found:
                    boxes[hash].append((label, value))
            #for i, b in enumerate(boxes):
            #    if len(b) > 0:
            #        print(i, b)
    for i, b in enumerate(boxes):
        for j, (label, value) in enumerate(b):
            result += (i + 1) * (j + 1) * int(value)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
