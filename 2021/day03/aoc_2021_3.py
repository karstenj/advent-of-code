def get_numbers(input_file_name):
    fh = open(input_file_name)
    lines = fh.readlines()
    fh.close()
    return [[int(lines[r][c]) for r in range(len(lines))] for c in range(len(lines[0]) - 1)]


def get_number_part1(input_file_name):
    numbers = get_numbers(input_file_name)
    count = [sum(n) for n in numbers]
    gamma = int(''.join(['1' if c > (len(numbers[0]) / 2) else '0' for c in count]), 2)
    epsilon = int(''.join(['1' if c < (len(numbers[0]) / 2) else '0' for c in count]), 2)
    return gamma * epsilon


def get_value_part2(numbers, cmp_fnc):
    for i in range(len(numbers)):
        count = sum(numbers[i])
        bit_value = 1 if cmp_fnc(count, (len(numbers[i]) / 2)) else 0
        new_numbers = []
        for j in range(len(numbers)):
            bit_pos = []
            for k in range(len(numbers[i])):
                if numbers[i][k] == bit_value:
                    bit_pos.append(numbers[j][k])
            new_numbers.append(bit_pos)
        numbers = new_numbers
        if len(numbers[0]) <= 1:
            break
    value = int(''.join([str(n[0]) for n in numbers]), 2)
    print(value)
    return value


def get_number_part2(input_file_name):
    numbers = get_numbers(input_file_name)
    oxygen = get_value_part2(numbers, lambda x, y: x >= y)
    co2 = get_value_part2(numbers, lambda x, y: x < y)
    return oxygen * co2