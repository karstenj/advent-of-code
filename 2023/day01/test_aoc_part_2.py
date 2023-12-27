from aoc_part_2 import get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part2(self):
        solution_3 = get_number_part2('input3.txt')
        solution_1 = get_number_part2('input1.txt')
        solution_2 = get_number_part2('input2.txt')
        print(f'Test solution part 2: {solution_3}')
        print(f'Test solution part 2: {solution_1}')
        print(f'Solution part 2: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)


if __name__ == '__main__':
    unittest.main()
