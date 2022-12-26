from aoc_part_2 import get_number_part2
import unittest
import logging


class TestAOC(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger().setLevel(logging.DEBUG)

    def test_aoc_part2(self):
        solution_1 = get_number_part2('input1.txt')
        solution_2 = get_number_part2('input2.txt')
        logging.info(f'Test solution part 2: {solution_1}')
        logging.info(f'Solution part 2: {solution_2}')
        self.assertEqual(301, solution_1)
        self.assertEqual(3887609741189, solution_2)


if __name__ == '__main__':
    unittest.main()
