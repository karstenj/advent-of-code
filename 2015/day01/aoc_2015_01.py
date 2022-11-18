def get_input(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input = [l for l in lines]
    return input


def get_number_part1(input_file_name):
    result = 0
    input = get_input(input_file_name)
    for c in input [0]:
        if c == '(':
            result += 1
        if c == ')':
            result -= 1
    return result


def get_number_part2(input_file_name):
    result = 0
    input = get_input(input_file_name)
    for i, c in enumerate(input [0]):
        if c == '(':
            result += 1
        if c == ')':
            result -= 1
        if result == -1:
            result = i+1
            break
    return result
