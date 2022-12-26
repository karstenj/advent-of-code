def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    x = 1
    c = 0
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
            c += 1
            if c in [20, 60, 100, 140, 180, 220]:
                result += c * x
        x += value
    #print(result)
    return result
