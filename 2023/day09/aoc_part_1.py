import unittest
import re

def get_diff(num):
    diff_num = [num[i+1]-num[i] for i in range(len(num)-1)]
    #print(diff_num)
    if diff_num.count(0) != len(diff_num):
        last_value = get_diff(diff_num)
        return last_value + diff_num[-1]
    return 0

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    for l in lines:
        num = [int(n) for n in l.strip().split()]
        #print(num)
        new_value = get_diff(num) + num[-1]
        #print(new_value)
        result += new_value



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
