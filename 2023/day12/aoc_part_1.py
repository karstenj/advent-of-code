import unittest
import re
import functools

@functools.cache
def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    for l in lines:
        part1, part2 = l.split()
        part2 = [int(i) for i in part2.split(',')]
        quest = [i for i, c in enumerate(part1) if c == '?']
        #print(quest)
        hash = part1.count('#')
        damaged = sum(part2)
        #print(part1, part2, len(quest), hash, damaged)
        part1 = list(part1)
        for v in range(pow(2, len(quest))):
            b = bin(v)[2:].zfill(len(quest))
            #print(b)
            for i, q in enumerate(quest):
                part1[q] = '.' if b[i] == '0' else '#'
            #print(part1)
            parts = ''.join(part1)
            #print(parts)
            sizes = []
            #print(parts)
            for p in parts.split('.'):
                if len(p) > 0:
                    sizes.append(len(p))
            #print(sizes)
            if len(sizes) == len(part2):
                compare = [i for i, j in zip(sizes, part2) if i == j]
                if len(compare) == len(part2):
                    #print('found')
                    result += 1




        #s = ['#' * i for i in part2]
        #s = '.'.join(s)
        #print(s)
        #if len(s) == len(part1):
        #    print(s)




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
