
import re


def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    first = True
    page_order = {}
    for l in lines:
        if l == '\n':
            first = False
        elif first:
            p, q = map(int, l.strip().split('|'))
            pages = page_order.setdefault(q, [])
            pages.append(p)
        else:
            pages = [int(v) for v in l.strip().split(',')]
            wrong = False
            for i, p1 in enumerate(pages):
                if p1 in page_order:
                    for p2 in pages[i+1:]:
                        if p2 in page_order[p1]:
                            wrong = True
            if not wrong:
                result += pages[len(pages)//2:len(pages)//2+1][0]
    return result


if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
