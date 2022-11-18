def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    numbers = [[int(c) for c in l.strip()] for l in lines]
    return numbers


def increase_adjacent(i, j, numbers):
    if i > 0:
        numbers[i-1][j] += 1
    if i < 9:
        numbers[i+1][j] += 1
    if j > 0:
        numbers[i][j-1] += 1
    if j < 9:
        numbers[i][j+1] += 1
    if i > 0 and j > 0:
        numbers[i-1][j-1] += 1
    if i < 9 and j < 9:
        numbers[i+1][j+1] += 1
    if i > 0 and j < 9:
        numbers[i-1][j+1] += 1
    if i < 9 and j > 0:
        numbers[i+1][j-1] += 1


def get_number_part1(input_file_name):
    numbers = get_numbers(input_file_name)
    flashes = 0
    for step in range(100):
        #print(f"Step {step+1}")
        # step 1 increase numbers
        for i, row in enumerate(numbers):
            for j, col in enumerate(row):
                numbers[i][j] += 1
        # step 2 check for numbers > 9
        flashed = [[False for j in range(10)] for i in range(10)]
        check = True
        while check:
            check = False
            for i, row in enumerate(numbers):
                for j, col in enumerate(row):
                    if numbers[i][j] > 9 and not flashed[i][j]:
                        increase_adjacent(i, j, numbers)
                        flashed[i][j] = True
                        check = True
                        flashes += 1
        for i, row in enumerate(numbers):
            for j, col in enumerate(row):
                if numbers[i][j] > 9:
                    numbers[i][j] = 0
        #for row in numbers:
        #    print(row)
    return flashes


def get_number_part2(input_file_name):
    numbers = get_numbers(input_file_name)
    step = 1
    while True:
        flashes = 0
        #print(f"Step {step+1}")
        # step 1 increase numbers
        for i, row in enumerate(numbers):
            for j, col in enumerate(row):
                numbers[i][j] += 1
        # step 2 check for numbers > 9
        flashed = [[False for j in range(10)] for i in range(10)]
        check = True
        while check:
            check = False
            for i, row in enumerate(numbers):
                for j, col in enumerate(row):
                    if numbers[i][j] > 9 and not flashed[i][j]:
                        increase_adjacent(i, j, numbers)
                        flashed[i][j] = True
                        check = True
                        flashes += 1
        for i, row in enumerate(numbers):
            for j, col in enumerate(row):
                if numbers[i][j] > 9:
                    numbers[i][j] = 0
        if flashes == 100:
            return step
        step += 1
        #for row in numbers:
        #    print(row)
    return 0
