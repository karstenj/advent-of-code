def get_input(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input = [[int(n) for n in l.strip().split('x')] for l in lines]
    return input


def get_number_part1(input_file_name):
    result = 0
    h = {}
    with open(input_file_name) as fh:
        input = fh.read()
        y = 0
        x = 0
        h[f'{x}:{y}'] = 1
        result = 1
        for c in input:
            if c == '^': y += 1
            if c == 'v': y -= 1
            if c == '<': x -= 1
            if c == '>': x += 1
            if not f'{x}:{y}' in h:
                h[f'{x}:{y}'] = 1
                result += 1
    return result


def get_number_part2(input_file_name):
    result = 0
    h = {}
    with open(input_file_name) as fh:
        input = fh.read()
        y = 0
        x = 0
        y1 = 0
        x1 = 0
        y2 = 0
        x2 = 0
        h[f'{x1}:{y1}'] = 1
        result = 1
        for c in input:
            if c == '^': y1 += 1
            if c == 'v': y1 -= 1
            if c == '<': x1 -= 1
            if c == '>': x1 += 1
            if not f'{x1}:{y1}' in h:
                h[f'{x1}:{y1}'] = 1
                result += 1
            x, y = x1, y1
            x1, y1 = x2, y2
            x2, y2 = x, y

    return result
