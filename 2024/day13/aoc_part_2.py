
from sympy import symbols, solve, Eq


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    token = 0
    for i in range(0, len(lines), 4):
        button_a_x = int(lines[i].split(':')[1].split(',')[0].split('+')[1])
        button_a_y = int(lines[i].split(':')[1].split(',')[1].split('+')[1])
        button_b_x = int(lines[i+1].split(':')[1].split(',')[0].split('+')[1])
        button_b_y = int(lines[i+1].split(':')[1].split(',')[1].split('+')[1])
        price_x = int(lines[i+2].split(':')[1].split(',')[0].split('=')[1]) + 10000000000000
        price_y = int(lines[i+2].split(':')[1].split(',')[1].split('=')[1]) + 10000000000000
        print(button_a_x, button_a_y, button_b_x, button_b_y, price_x, price_y)
        a, b = symbols('a b')
        eq1 = Eq(a * button_a_x + b * button_b_x, price_x)
        eq2 = Eq(a * button_a_y + b * button_b_y, price_y)
        sol_dict = solve((eq1, eq2), (a, b))
        sol_a = str(sol_dict[a])
        sol_b = str(sol_dict[b])
        if '/' not in sol_a and '/' not in sol_b:
            token += int(sol_a) * 3 + int(sol_b)
        print(eval(str(sol_dict[a])), eval(str(sol_dict[b])))
    return token


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
