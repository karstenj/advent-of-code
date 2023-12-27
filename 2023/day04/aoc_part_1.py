import unittest
import re

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    for l in lines:
        winning_numbers, my_numbers = l.split(':')[1].split('|')
        winning_numbers = set([int(n) for n in winning_numbers.split()])
        my_numbers = set([int(n) for n in my_numbers.split()])
        won_numbers = winning_numbers.intersection(my_numbers)
        #print(winning_numbers, my_numbers, won_numbers, pow(2, len(won_numbers)-1))
        result += pow(2, len(won_numbers)-1) if len(won_numbers) >= 1 else 0
    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input1.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
