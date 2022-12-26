from collections import deque

def get_snafu(value):
    fak = 1
    digit = 1
    s = ''
    while True:
        if (fak - fak//2) < value and (fak + fak//2) > value:
            a = 1
            break
        if (2*fak - fak//2) < value and (2*fak + fak//2) > value:
            a = 2
            break
        fak *= 5
        digit += 1
    act_value = a * fak
    fak = fak // 5
    s = str(a)
    value_map = {-2: '=', -1: '-', 0: '0', 1: '1', 2:'2'}
    for d in range(digit-1):
        for a in range(-2, 3):
            b = act_value + a * fak
            if (b - fak // 2) <= value and (b + fak // 2) >= value:
                s = s + value_map[a]
                act_value = b
                break
        fak = fak // 5
    return s


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.read()
    values = []
    for l in lines.split('\n'):
        digit = 1
        value = 0
        for c in l[::-1]:
            if c == '-':
                value += -1 * digit
            elif c == '=':
                value += -2 * digit
            else:
                value += int(c) * digit
            digit *= 5
        values.append(value)
    total = sum(values)
    print(total)

    snafu = get_snafu(total)
    print(snafu)

    return snafu
