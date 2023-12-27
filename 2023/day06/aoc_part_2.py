import unittest
import re



def get_number_part1(input_file_name):
    result = 1
    with open(input_file_name) as fh:
        lines = fh.readlines()
    total_time = 71530
    total_dist = 940200
    total_time = 49877895
    total_dist = 356137815021882
    n_dist = 0
    for s in range(1, total_time-1):
        di = s * (total_time - s)
        if di > total_dist:
            n_dist += 1
    print(n_dist)
    result = n_dist


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
