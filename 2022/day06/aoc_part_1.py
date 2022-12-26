
def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    line = lines[0]
    for i in range(4, len(line)):
        window = line[i-4:i]
        buffer = set(window)
        if len(buffer) == 4:
            result = i
            break
    #print(result)
    return result
