import unittest
import re
import functools


@functools.cache
def get_move(r, c, d, field):
    move_dict = {
        'e': {'.': [(r, c + 1, 'e')], '\\': [(r + 1, c, 's')], '/': [(r - 1, c, 'n')],
              '|': [(r - 1, c, 'n'), (r + 1, c, 's')], '-': [(r, c + 1, 'e')]},
        'w': {'.': [(r, c - 1, 'w')], '\\': [(r - 1, c, 'n')], '/': [(r + 1, c, 's')],
              '|': [(r - 1, c, 'n'), (r + 1, c, 's')], '-': [(r, c - 1, 'w')]},
        'n': {'.': [(r - 1, c, 'n')], '\\': [(r, c - 1, 'w')], '/': [(r, c + 1, 'e')], '|': [(r - 1, c, 'n')],
              '-': [(r, c - 1, 'w'), (r, c + 1, 'e')]},
        's': {'.': [(r + 1, c, 's')], '\\': [(r, c + 1, 'e')], '/': [(r, c - 1, 'w')], '|': [(r + 1, c, 's')],
              '-': [(r, c - 1, 'w'), (r, c + 1, 'e')]},
    }
    return move_dict[d][field]


def get_energy(r, c, d, lines):
    result = 0
    beams = [(r, c, d)]
    energized = set([(r, c, d)])
    count = 0
    max_count = 0
    while len(beams) > 0:
        energized_length = len(energized)
        beams_length = len(beams)
        r, c, d = beams.pop(0)
        moves = get_move(r, c, d, lines[r][c])
        for m in moves:
            rn, cn, dn = m
            if rn >= 0 and rn < len(lines) and cn >= 0 and cn < len(lines[rn]) and (rn, cn, dn) not in energized:
                beams.append(m)
                energized.add((rn, cn, dn))

        if energized_length == len(energized):
            count += 1
            if count > 1000000:
                break
        else:
            max_count = max(count, max_count)
            #print(len(energized), len(beams), count, max_count)
            count = 0

    for r, l in enumerate(lines):
        s = ''
        for c, char in enumerate(l):
            if (r, c, 'n') in energized or (r, c, 's') in energized or (r, c, 'e') in energized or (r, c, 'w') in energized:
                s += '#'
                result += 1
            else:
                s += char
        #print(s)

    return result

def get_number_part(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]

    for r in range(len(lines)):
        res = get_energy(r, 0, 'e', lines)
        result = max(res, result)
        res = get_energy(r, len(lines[r])-1, 'w', lines)
        result = max(res, result)
    for c in range(len(lines[0])):
        res = get_energy(0, c, 's', lines)
        result = max(res, result)
        res = get_energy(len(lines)-1, c, 'n', lines)
        result = max(res, result)



    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
