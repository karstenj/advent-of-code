def get_input(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input = [int(l) for l in lines]
    return input


def get_number_part1(input_file_name):
    result = 0
    input = get_input(input_file_name)
    return result


def get_number_part2(input_file_name):
    result = 0
    input = get_input(input_file_name)
    return result
