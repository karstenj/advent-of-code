


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    left = [int(l.strip().split()[0]) for l in lines]
    right = [int(l.strip().split()[1]) for l in lines]
    score = [l * right.count(l) for l in left]
    print(score)
    return sum(score)

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
