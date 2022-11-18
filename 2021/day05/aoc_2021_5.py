def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    cords = [tuple([tuple([int(c) for c in p.split(',')]) for p in l.split(' -> ')]) for l in lines]
    return cords


def get_hor_ver(cords, counts):
    for c in cords:
        (x1,y1),(x2,y2) = c
        #print(f'{x1}{y1}{x2}{y2}')
        if x1 == x2:
            inc = 1 if y1 < y2 else -1
            for i in range(abs(y1-y2)+1):
                key = f'{x1},{y1+inc*i}'
                counts[key] = 1 if key not in counts else counts[key] + 1
        elif y1 == y2:
            inc = 1 if x1 < x2 else -1
            for i in range(abs(x1-x2)+1):
                key = f'{x1+i*inc},{y1}'
                counts[key] = 1 if key not in counts else counts[key] + 1

def get_number_part1(input_file_name):
    cords = get_numbers(input_file_name)
    #print(cords)
    counts = {}
    get_hor_ver(cords, counts)
    result = 0
    for key in counts:
        c = counts[key]
        result += 1 if c >= 2 else 0
        #if c >= 2: print(key)
    #print(result)
    return result


def get_number_part2(input_file_name):
    cords = get_numbers(input_file_name)
    counts = {}
    counts = {}
    get_hor_ver(cords, counts)
    for c in cords:
        (x1, y1), (x2, y2) = c
        #print(f'{x1}{y1}{x2}{y2}')
        if abs(x2 - x1) == abs(y2 - y1):
            ix = 1 if x1 < x2 else -1
            iy = 1 if y1 < y2 else -1
            for i in range(abs(x2 - x1)+1):
                key = f'{x1+ix*i},{y1+iy*i}'
                counts[key] = 1 if key not in counts else counts[key] + 1
    result = 0
    for key in counts:
        c = counts[key]
        result += 1 if c >= 2 else 0
        #if c >= 2: print(key)
    #print(result)
    return result