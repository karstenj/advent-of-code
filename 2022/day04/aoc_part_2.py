def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    for l in lines:
        s1,s2 = l.strip().split(',')
        s1 = s1.split('-')
        s2 = s2.split('-')
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        if s1[0] <= s2[0] and s1[1] >= s2[0]:
            result += 1
        elif s2[0] <= s1[0] and s2[1] >= s1[0]:
            result += 1
    return result
