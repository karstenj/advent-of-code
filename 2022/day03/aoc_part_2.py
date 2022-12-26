def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    item = []
    for i in range(0, len(lines), 3):
        l1 = lines[i].strip()
        l2 = lines[i+1].strip()
        l3 = lines[i+2].strip()
        for c1 in l1:
            if c1 in l2 and c1 in l3:
                item.append(c1)
                #print(c1)
                break
    for i in item:
        if i >= 'a' and i <= 'z':
            result += ord(i) - ord('a') + 1
        else:
            result += ord(i) - ord('A') + 27
    return result
