

def is_safe(l):
    increasing = 0
    decreasing = 0
    safe = False
    for i, v in enumerate(l):
        if i > 0 and l[i - 1] < l[i] and (l[i] - l[i - 1]) >= 1 and (l[i] - l[i - 1]) <= 3:
            increasing += 1
        if i > 0 and l[i - 1] > l[i] and (l[i - 1] - l[i]) >= 1 and (l[i - 1] - l[i]) <= 3:
            decreasing += 1
    if decreasing == len(l) - 1:
        safe = True
    if increasing == len(l) - 1:
        safe = True
    return safe

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [[int(v) for v in l.strip().split()] for l in lines]
    n_safe = 0
    for l in lines:
        if is_safe(l):
            n_safe +=1
        #print(increasing, decreasing)
    print(n_safe)
    return n_safe

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
