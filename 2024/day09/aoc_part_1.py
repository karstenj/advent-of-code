
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
    for c in line:
        for i in range(int(c)):
            disk.append(id if file else -1)
        if file:
            id = id + 1
        file = not file
    #print(disk)
    i = disk.index(-1)
    while i >= 0:
        while disk[-1] == -1:
            disk = disk[:-1]
        disk[i] = disk[-1]
        disk = disk[:-1]
        try:
            i = disk.index(-1)
        except ValueError:
            break
    #print(disk)
    for i, v in enumerate(disk):
        result += i * v
    return result


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
