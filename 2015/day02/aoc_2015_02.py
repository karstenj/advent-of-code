def get_input(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input = [[int(n) for n in l.strip().split('x')] for l in lines]
    return input


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        for l in fh.readlines():
            l, w, h = [int(x) for x in l.split('x')]
            area = 2*l*w + 2*w*h + 2*l*h
            area += min(l*w, w*h, l*h)
            result += area
    return result


def get_number_part2(input_file_name):
    result = 0
    input = get_input(input_file_name)
    for l in input:
        area = 0
        area += 2 * min(l[0] + l[1], l[1] + l[2], l[0] + l[2])
        area += l[0] * l[1] * l[2]
        result += area

    return result
