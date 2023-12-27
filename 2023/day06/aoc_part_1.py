import unittest
import re



def get_number_part1(input_file_name):
    result = 1
    with open(input_file_name) as fh:
        lines = fh.readlines()
    time = [int(n) for n in lines[0].split(':')[1].split()]
    dist = [int(n) for n in lines[1].split(':')[1].split()]
    for (t, ds) in zip(time, dist):
        n_dist = 0
        for s in range(1, t-1):
            di = s * (t - s)
            if di > ds:
                n_dist += 1
        #print(n_dist)
        result *= n_dist


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
