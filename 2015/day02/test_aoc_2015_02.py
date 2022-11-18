from aoc_2015_02 import get_number_part1, get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):        
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        self.assertEqual(101, solution_1)
        self.assertEqual(1606483, solution_2)
 
    def test_aoc_part2(self):        
        solution_1 = get_number_part2('input1.txt')
        solution_2 = get_number_part2('input2.txt')
        print(f'Test solution part 2: {solution_1}')
        print(f'Solution part 2: {solution_2}')
        self.assertEqual(48, solution_1)
        self.assertEqual(3842356, solution_2)


if __name__ == '__main__':
    unittest.main()