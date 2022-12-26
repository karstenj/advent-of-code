def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for l in lines:
        a, b = l.strip().split(' ')
        i_a = ord(a) - ord('A')
        i_b = ord(b) - ord('X')
        if i_a == i_b:
            w = i_b + 1 + 3
        elif i_a == (i_b - 1) % 3:
            w = i_b + 1 + 6
        elif i_a == (i_b + 1) % 3:
            w = i_b + 1
        result += w
    return result
