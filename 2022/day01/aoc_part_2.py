def get_number_part2(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    v = []
    s = 0
    for l in lines:
        l = l.strip()
        if l != '':
            s += int(l)
        else:
            v.append(s)
            s = 0
    v.append(s)
    v = sorted(v)
    #print(v)
    return sum(v[-3:])