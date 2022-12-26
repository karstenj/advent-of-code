def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    item = []
    for l in lines:
        l = l.strip()
        l1 = l[:len(l)//2]
        l2 = l[len(l) // 2:]
        for c1 in l1:
            if c1 in l2:
                item.append(c1)
                #print(c1)
                break
    for i in item:
        if i >= 'a' and i <= 'z':
            result += ord(i) - ord('a') + 1
        else:
            result += ord(i) - ord('A') + 27
    return result
