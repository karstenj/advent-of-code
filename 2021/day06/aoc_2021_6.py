def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    return [int(c) for c in lines[0].split(',')]


def get_number_part1(input_file_name, rounds):
    fishes = get_numbers(input_file_name)
    counts = [0] * 9
    for f in fishes:
        counts[f] += 1
    for r in range(rounds):
        count_0 = counts[0]
        counts = counts[1:] + [count_0]
        counts[6] += count_0
    return sum(counts)


def get_number_part2(input_file_name, rounds):
    return get_number_part1(input_file_name, rounds)