import unittest
import re

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    steps = lines[0].strip()
    elements = {}
    for l in lines[2:]:
        #print(l)
        m = re.match(r'(\w+) \= \((\w+)\, (\w+)\)', l)
        elements[m.group(1)] = {'L': m.group(2), 'R': m.group(3)}
    elem = 'AAA'
    while elem != 'ZZZ':
        for s in steps:
            result += 1
            elem = elements[elem][s]
            if elem == 'ZZZ':
                break

    return result

class TestAOC(unittest.TestCase):

    def test_aoc_part1(self):
        solution_1 = get_number_part1('input3.txt')
        solution_2 = get_number_part1('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        #self.assertEqual(0, solution_1)
        #self.assertEqual(0, solution_2)

if __name__ == '__main__':
    unittest.main()
