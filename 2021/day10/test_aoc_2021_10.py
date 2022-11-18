from aoc_2021_10 import get_number_part1, get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):        
        self.assertEqual(26397, get_number_part1('input1.txt'))
        self.assertEqual(288291, get_number_part1('input2.txt'))
 
    def test_aoc_part2(self):        
        self.assertEqual(288957, get_number_part2('input1.txt'))
        self.assertEqual(820045242, get_number_part2('input2.txt'))


if __name__ == '__main__':
    unittest.main()