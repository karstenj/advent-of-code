
def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    line = lines[0]
    for i in range(14, len(line)):
        window = line[i-14:i]
        buffer = set(window)
        if len(buffer) == 14:
            result = i
            break
    #print(result)
    return result
