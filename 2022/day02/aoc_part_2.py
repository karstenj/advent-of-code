def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for l in lines:
        a, b = l.strip().split(' ')
        i_a = ord(a) - ord('A')
        i_b = ord(b) - ord('X')
        if b == 'X':
            w = ((i_a - 1) % 3) + 1
        elif b == 'Y':
            w = i_a + 1 + 3
        elif b == 'Z':
            w = ((i_a + 1) % 3) + 1 + 6
        result += w
    return result
