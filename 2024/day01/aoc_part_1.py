


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    left = [int(l.strip().split()[0]) for l in lines]
    left.sort()
    right = [int(l.strip().split()[1]) for l in lines]
    right.sort()
    print(left)
    print(right)
    diff = [abs(l-r) for l, r in zip(left, right)]
    print(diff)
    return sum(diff)

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
