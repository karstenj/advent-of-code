import unittest
import re


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input = [int(l) for l in lines]
    return result


class TestAOC(unittest.TestCase):
    def test_aoc_part1(self):
        solution_1 = get_number_part2('input1.txt')
        solution_2 = get_number_part2('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)


if __name__ == '__main__':
    unittest.main()