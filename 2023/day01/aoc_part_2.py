import re
import unittest


def get_first_digit(l):
    index = len(l)
    digit = ''
    for s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        act_index = l.find(s)
        if act_index >= 0 and act_index < index:
            index = act_index
            digit = s
    return digit


def get_last_digit(l):
    index = -1
    digit = ''
    for s in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']:
        act_index = l.rfind(s)
        if act_index >= 0 and act_index > index:
            index = act_index
            digit = s
    return digit


def get_value(first, last):
    value = 0
    digit_name = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    try:
        value += digit_name.index(first) * 10
    except ValueError:
        value += int(first) * 10
    try:
        value += digit_name.index(last)
    except ValueError:
        value += int(last)
    return value


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    for l in lines:
        digits = re.findall('\d|zero|one|two|three|four|five|six|seven|eight|nine', l)
        first = get_first_digit(l)
        last = get_last_digit(l)
        value1 = get_value(first, last)
        value2 = get_value(digits[0], digits[-1])
        #if value1 != value2:
        #    print(l.strip())
        #    print(first, last, value1)
        #    print(digits[0], digits[-1], value2)
        result += value1
    return result


class TestAOC(unittest.TestCase):
    def test_aoc_part1(self):
        solution_1 = get_number_part2('input3.txt')
        solution_2 = get_number_part2('input2.txt')
        print(f'Test solution part 1: {solution_1}')
        print(f'Solution part 1: {solution_2}')
        self.assertEqual(281, solution_1)
        self.assertEqual(53515, solution_2)


if __name__ == '__main__':
    unittest.main()