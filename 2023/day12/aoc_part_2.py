import unittest
import re
import functools

@functools.cache
def process_part(part1, part2, hash_count):
    ret = 0
    if len(part1) == 0:
        if len(part2) == 0 and (hash_count is None or hash_count == 0):
            return 1
        else:
            return 0
    else:
        if part1[0] == '?':
            part1 = list(part1)
            part1[0] = '#'
            ret += process_part(tuple(part1), part2, hash_count)
            part1[0] = '.'
            ret += process_part(tuple(part1), part2, hash_count)
        elif part1[0] == '#':
            part1 = part1[1:]
            if hash_count is None:
                if len(part2) > 0:
                    hash_count = part2[0] - 1
                    part2 = part2[1:]
                else:
                    return 0
            else:
                hash_count -= 1
            ret += process_part(part1, part2, hash_count)
        elif part1[0] == '.':
            part1 = part1[1:]
            if hash_count is not None:
                if hash_count == 0:
                    hash_count = None
                    ret += process_part(part1, part2, hash_count)
                else:
                    return 0
            else:
                ret += process_part(part1, part2, hash_count)
    return ret

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    for l in lines:
        part1, part2 = l.split()
        part1 = '?'.join([part1]*5)
        part2 = ','.join([part2]*5)
        #print(part1, part2)
        part2 = [int(i) for i in part2.split(',')]
        ret = process_part(tuple(list(part1)), tuple(part2), None)
        #print(part1, part2, ret)
        result += ret

        #quest = [i for i, c in enumerate(part1) if c == '?']
        #min_part = ['#' * i for i in part2]
        #print(part1)
        #min_part = '.'.join(min_part)
        #print(min_part)
        #shift = len(part1) - len(min_part)
        #print(len(part1) - len(min_part))
        #point = [0] + [i for i, c in enumerate(min_part) if c == '.']
        #print(point)





    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
