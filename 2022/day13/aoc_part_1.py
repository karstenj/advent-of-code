def check_order(part1, part2):
    for i1 in range(len(part1)):
        if i1 < len(part2):
            p1 = part1[i1]
            p2 = part2[i1]
            if type(p1) == int and type(p2) == int:
                if p1 < p2:
                    return 1
                elif p1 > p2:
                    return -1
            elif type(p1) == int and type(p2) == list:
                p1 = [p1]
                ret = check_order(p1, p2)
                if ret != 0:
                    return ret
            elif type(p1) == list and type(p2) == int:
                p2 = [p2]
                ret = check_order(p1, p2)
                if ret != 0:
                    return ret
            elif type(p1) == list and type(p2) == list:
                ret = check_order(p1, p2)
                if ret != 0:
                    return ret
    if type(part1) == list and type(part2) == list:
        if len(part1) < len(part2):
            return 1
        elif len(part1) > len(part2):
            return -1
    return 0

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    pairs = []
    for l in lines:
        l = l.strip()
        if l != '':
            pairs.append(eval(l))
    #print(pairs)
    count = 1
    for i in range(0,len(pairs),2):
        p1 = pairs[i]
        p2 = pairs[i+1]
        if check_order(p1, p2) == 1:
            #print(count)
            result += count
        count += 1
    return result
