from aoc_2021_8 import get_number_part1, get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):        
        self.assertEqual(26, get_number_part1('input1.txt'))
        self.assertEqual(284, get_number_part1('input2.txt'))
 
    def test_aoc_part2(self):        
        self.assertEqual(5353, get_number_part2('input3.txt'))
        self.assertEqual(61229, get_number_part2('input1.txt'))
        self.assertEqual(973499, get_number_part2('input2.txt'))


if __name__ == '__main__':
    unittest.main()