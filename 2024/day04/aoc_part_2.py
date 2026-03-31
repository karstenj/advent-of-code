
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    enabled = True
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for l in lines:
        muls = re.findall(r"(mul\(([0-9]+)\s*\,\s*([0-9]+)\)|don\'t\(\)|do\(\))", l)
        for m in muls:
            print(m)
            if m[0] == 'do()':
                enabled = True
            elif m[0] == 'don\'t()':
                enabled = False
            elif enabled:
                result += int(m[1]) * int(m[2])
        print(muls)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
