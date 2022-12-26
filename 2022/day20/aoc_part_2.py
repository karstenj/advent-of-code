import copy

def move_number(t, numbers_out):
    id, n = t
    if n != 0:
        i_old = numbers_out.index(t)
        numbers_out.pop(i_old)
        if n > 0:
            i_new = (i_old + n)
            i_new = i_new % len(numbers_out)
        elif n < 0:
            i_new = i_old + n
            fak = abs(i_new) // len(numbers_out)
            i_new += fak * len(numbers_out)
        numbers_out.insert(i_new, (id, n))


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    numbers_in_raw = []
    numbers_in = []
    for l in lines:
        numbers_in_raw.append(int(l.strip()))
    for i, n in enumerate(numbers_in_raw):
        numbers_in.append((i, n * 811589153))
        if n == 0:
            t_0 = (i, n)
    #print(numbers_in)
    #numbers = [n[1] for n in numbers_in]
    #print(numbers)
    numbers_out = copy.copy(numbers_in)
    for r in range(10):
        for t in numbers_in:
            move_number(t, numbers_out)
        #numbers = [n[1] for n in numbers_out]
        #print(numbers)
    i_0 = numbers_out.index(t_0)
    i_1 = (i_0 + 1000) % len(numbers_out)
    i_2 = (i_0 + 2000) % len(numbers_out)
    i_3 = (i_0 + 3000) % len(numbers_out)
    #print(f'{numbers_out[i_1][1]} {numbers_out[i_2][1]} {numbers_out[i_3][1]}')
    result = numbers_out[i_1][1] + numbers_out[i_2][1] + numbers_out[i_3][1]
    #print(numbers_out)
    #print(len(numbers_in))
    #print(len(numbers_out))
    return result
