from aoc_part_1 import get_number_part1
import unittest
import logging


class TestAOC(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1_1.txt', 'input1_2.txt')
        solution_2 = get_number_part1('input2_1.txt', 'input2_2.txt')
        logging.info(f'Test solution part 1: {solution_1}')
        logging.info(f'Solution part 1: {solution_2}')
        self.assertEqual(6032, solution_1)
        self.assertEqual(117054, solution_2)

if __name__ == '__main__':
    unittest.main()
