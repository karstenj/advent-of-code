import re
import unittest


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    for l in lines:
        digits = re.findall(r'\d', l)
        result += int(digits[0]) * 10 + int(digits[-1])
    return result


class TestAOC(unittest.TestCase):
    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        self.assertEqual(142, solution_1)
        self.assertEqual(54388, solution_2)

if __name__ == '__main__':
    unittest.main()