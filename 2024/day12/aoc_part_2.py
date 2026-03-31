
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    line = lines[0].strip()
    stones = {}
    for v in line.strip().split():
        stones[v] = 1
    stone_map = {}
    for i in range(75):
        print(stones)
        #print(i)
        next_stones = {}
        for s in stones:
            #print('miss')
            if s == '0':
                next_stones.setdefault('1', 0)
                next_stones['1'] += stones[s]
            elif len(s) % 2 == 0:
                m = len(s) // 2
                k = s[:m]
                next_stones.setdefault(k, 0)
                next_stones[k] += stones[s]
                k = str(int(s[m:]))
                next_stones.setdefault(k, 0)
                next_stones[k] += stones[s]
                #print(s[:m], str(int(s[m:])))
            else:
                k = str(int(s)*2024)
                next_stones.setdefault(k, 0)
                next_stones[k] += stones[s]
                #print(str(int(s)*2024))
        stones = next_stones

    return sum(stones.values())


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
