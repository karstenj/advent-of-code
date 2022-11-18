def get_numbers(input_file_name):
    fh = open(input_file_name)
    lines = fh.readlines()
    fh.close()
    return [(l.split(' ')[0], int(l.split(' ')[1])) for l in lines]


def get_dx(cmd, step):
    dx = step if cmd == 'forward' else 0
    return


def get_number_part1(input_file_name):
    numbers = get_numbers(input_file_name)
    x = [step if cmd == 'forward' else 0 for (cmd, step) in numbers]
    y = [step if cmd == 'down' else -step if cmd == 'up' else 0 for (cmd, step) in numbers]
    return sum(x) * sum(y)


def get_number_part2(input_file_name):
    numbers = get_numbers(input_file_name)
    aim = [step if cmd == 'down' else -step if cmd == 'up' else 0 for (cmd, step) in numbers]
    aim = [sum(aim[:i + 1]) for i in range(len(aim))]
    y = [step * aim[i] if cmd == 'forward' else 0 for i, (cmd, step) in enumerate(numbers)]
    x = [step if cmd == 'forward' else 0 for i, (cmd, step) in enumerate(numbers)]
    return sum(x) * sum(y)