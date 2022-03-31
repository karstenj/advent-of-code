from aoc_2021_6 import get_number_part1, get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):        
        self.assertEqual(26, get_number_part1('input1.txt', 18))
        self.assertEqual(5934, get_number_part1('input1.txt', 80))
        self.assertEqual(352195, get_number_part1('input2.txt', 80))
 
    def test_aoc_part2(self):        
        self.assertEqual(26984457539, get_number_part2('input1.txt', 256))
        self.assertEqual(1600306001288, get_number_part2('input2.txt', 256))


if __name__ == '__main__':
    unittest.main()