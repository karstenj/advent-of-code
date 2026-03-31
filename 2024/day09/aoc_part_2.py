
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    line = lines[0].strip()
    id = 0
    file = True
    disk = []
    free_space = []
    used_space = []
    for c in line:
        if not file:
            if int(c) > 0:
                free_space.append((int(c), len(disk)))
        else:
            used_space.append((int(c), len(disk), id))
        for i in range(int(c)):
            disk.append(id if file else -1)
        if file:
            id = id + 1
        file = not file
    #free_space.sort(key=lambda e: (e[0], -e[1]), reverse=True)
    print(free_space)
    print(used_space)
    print(disk)
    compact_used_space = []
    while len(used_space) > 0:
        len_used, index_used, id_used = used_space[-1]
        print(len_used, index_used, id_used)
        used_space = used_space[:-1]
        for i, (len_free, index_free) in enumerate(free_space):
            if index_free < index_used:
                if len_free >= len_used:
                    index_used = index_free
                    len_free -= len_used
                    index_free += len_used
                    free_space[i] = (len_free, index_free)
        compact_used_space.append((len_used, index_used, id_used))
    compact_used_space.sort(key=lambda e: e[1])
    for len_used, index_used, id_used in compact_used_space:
        for i in range(len_used):
            result += (index_used + i) * id_used
    return result


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
