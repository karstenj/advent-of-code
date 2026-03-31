
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for l in lines:
        muls = re.findall(r"mul\(([0-9]+)\s*\,\s*([0-9]+)\)", l)
        for m in muls:
            result += int(m[0]) * int(m[1])
        print(muls)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
