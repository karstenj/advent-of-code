def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    return [int(c) for c in lines[0].split(',')]


def get_number_part1(input_file_name):
    positions = get_numbers(input_file_name)
    max_pos = max(positions)
    fuel = []
    for i in range(max_pos+1):
        fuel.append(sum([abs(p-i) for p in positions]))
    return min(fuel)


def get_number_part2(input_file_name):
    positions = get_numbers(input_file_name)
    max_pos = max(positions)
    fuel = []
    for i in range(max_pos+1):
        fuel.append(sum([(abs(p-i)*(abs(p-i)+1))/2 for p in positions]))
    return int(min(fuel))
