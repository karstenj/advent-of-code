from functools import cmp_to_key

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


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    pairs = []
    for l in lines:
        l = l.strip()
        if l != '':
            pairs.append(eval(l))
    pairs.append([[2]])
    pairs.append([[6]])
    pairs = sorted(pairs, key=cmp_to_key(check_order), reverse=True)
    #print(pairs)
    result = 1
    for i, p in enumerate(pairs):
        if str(p) == '[[2]]':
            result *= (i + 1)
        if str(p) == '[[6]]':
            result *= (i + 1)
    return result
