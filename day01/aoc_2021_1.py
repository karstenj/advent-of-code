def get_numbers(input_file_name):
    fh = open(input_file_name)
    lines = fh.readlines()
    fh.close()
    return [int(l) for l in lines]


def get_number_part1(input_file_name):
    numbers = get_numbers(input_file_name)
    increased = [1 if numbers[i] > numbers[i - 1] else 0 for i in range(1, len(numbers))]
    return sum(increased)


def get_number_part2(input_file_name):
    numbers = get_numbers(input_file_name)
    numbers = [sum(numbers[i - 2:i + 1]) for i in range(2, len(numbers))]
    # print(numbers)
    increased = [1 if numbers[i] > numbers[i - 1] else 0 for i in range(1, len(numbers))]
    return sum(increased)