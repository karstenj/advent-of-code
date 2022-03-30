from aoc_2021_7 import get_number_part1, get_number_part2
import unittest

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):        
        self.assertEqual(37, get_number_part1('input1.txt'))
        self.assertEqual(348664, get_number_part1('input2.txt'))
 
    def test_aoc_part2(self):        
        self.assertEqual(168, get_number_part2('input1.txt'))
        self.assertEqual(100220525, get_number_part2('input2.txt'))


if __name__ == '__main__':
    unittest.main()