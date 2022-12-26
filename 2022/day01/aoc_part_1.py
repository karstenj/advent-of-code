def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    s = 0
    max = []
    for l in lines:
        l = l.strip()
        if l == '':
            max.append(s)
            s = 0
        else:
            s += int(l)
    max.append(s)
    result = sorted(max)
    print(result[-1])
    return result[-1]
