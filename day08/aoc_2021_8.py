def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input_data = []
    output_data = []
    for l in lines:
        d = l.split(' | ')
        input_data.append([x.strip() for x in d[0].split(' ')])
        output_data.append([x.strip() for x in d[1].split(' ')])
    return input_data, output_data


def get_number_part1(input_file_name):
    input_data, output_data = get_numbers(input_file_name)
    instance = 0
    for l in output_data:
        for o in l:
            #print(o)
            if len(o) in [2, 3, 4, 7]:
                instance += 1
    return instance


def get_number_part2(input_file_name):
    pass
