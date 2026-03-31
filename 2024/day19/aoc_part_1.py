
def find_design(l, designs):
    #print(l, designs)
    if len(l) == 0:
        return True
    possible_designs = []
    for d in designs:
        if d in l:
            possible_designs.append(d)
    for d in possible_designs:
        if l.startswith(d):
            if find_design(l[len(d):], possible_designs):
                return True
    return False

def get_number_part(input_file_name, width, height, n_locations):
    result = 0
    print(input_file_name)
    with open(input_file_name) as fh:
        lines = fh.readlines()
    stripped_lines = []
    for l in lines:
        stripped_lines.append(l.strip())
    designs = [d.strip() for d in stripped_lines[0].split(',')]
    designs.sort(key=lambda e: len(e), reverse=True)
    print(designs)
    for l in stripped_lines[2:]:
        print(l)
        if find_design(l, designs):
            result += 1
        else:
            print(l)
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt', 7, 7, 12)
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt', 71, 71, 1024)
    print(f'Solution part 1: {solution_2}')
