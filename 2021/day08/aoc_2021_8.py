from itertools import permutations

def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    input_data = []
    output_data = []
    for l in lines:
        d = l.split(' | ')
        input_data.append(sorted([''.join(sorted(x.strip())) for x in d[0].split(' ')], key=len))
        output_data.append([''.join(sorted(x.strip())) for x in d[1].split(' ')])
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
    input_data, output_data = get_numbers(input_file_name)
    numbers = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }
    segments = [c for c in 'abcdefg']
    perms = [p for p in permutations([i for i in range(7)])]
    configs = []
    for perm in perms:
        mapping = {}
        for i, p in enumerate(perm):
            mapping[segments[i]] = segments[p]
        new_numbers = {}
        for key in numbers:
            new_key = ''
            for d in key:
                new_key += mapping[d]
            new_key = ''.join(sorted(new_key))
            new_numbers[new_key] = numbers[key]
        configs.append(new_numbers)
    #print(configs)
    result = 0
    for i, data in enumerate(input_data):
        #print(data)
        for c in configs:
            found = [1 if d in c else 0 for d in data]
            if sum(found) == 10:
                number = int(''.join([c[o] for o in output_data[i]]))
                result += number
                #print(data)
                #print(str(output_data[i]) + ' ' + str(number))
    print(result)
    return result
