def get_number_part2(input_file_name):
    result = []
    with open(input_file_name) as fh:
        lines = fh.readlines()
    x = 1
    c = 0
    crt = ''
    for l in lines:
        l = l.strip()
        if l.startswith('noop'):
            cyc = 1
            value = 0
        else:
            _, value = l.split(' ')
            value = int(value)
            cyc = 2
        for i in range(cyc):
            crt += '#' if c in [x-1, x, x+1] else ' '
            c += 1
            if c >= 40:
                c = 0
                result.append(crt)
                crt = ''
        if value != 0:
            x += value
    for r in result:
        print(r)
    return result
