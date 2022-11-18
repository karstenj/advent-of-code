from itertools import permutations

def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    numbers = [[int(c) for c in l.strip()] for l in lines]
    return numbers


def get_number_part1(input_file_name):
    numbers = get_numbers(input_file_name)
    #print(numbers)
    risk = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            n = numbers[i][j]
            if i == 0 or numbers[i-1][j] > n:
                if i+1 == len(numbers) or numbers[i + 1][j] > n:
                    if j == 0 or numbers[i][j-1] > n:
                        if j + 1 == len(numbers[i]) or numbers[i][j+1] > n:
                            #print(n+1)
                            risk += n + 1
    print(risk)
    return risk

def scan_area(numbers, visited, i, j, area):
    n = numbers[i][j]
    if not visited[i][j] and n < 9:
        visited[i][j] = True
        area.append([i, j])
        if i+1 < len(numbers):
            scan_area(numbers, visited, i+1, j, area)
        if i > 0:
            scan_area(numbers, visited, i-1, j, area)
        if j+1 < len(numbers[0]):
            scan_area(numbers, visited, i, j+1, area)
        if j > 0:
            scan_area(numbers, visited, i, j-1, area)


def get_number_part2(input_file_name):
    numbers = get_numbers(input_file_name)
    visited = [[False for j in numbers[0]] for i in numbers]
    area_size = []
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            area = []
            scan_area(numbers, visited, i, j, area)
            if len(area) > 0:
                area_size.append(len(area))
    area_size.sort()
    #print(area_size[-3:])
    value = area_size[-3] * area_size[-2] * area_size[-1]
    return value
