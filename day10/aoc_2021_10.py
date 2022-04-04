def get_numbers(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    return lines


def get_number_part1(input_file_name):
    data = get_numbers(input_file_name)
    result = 0
    stack = []
    for l in data:
        matching = {'{': '}', '[': ']', '(': ')', '<': '>'}
        score = {'}': 1197, ']': 57, ')': 3, '>': 25137}
        for c in l.strip():
            if c in ['{', '[', '(', '<']:
                stack.append(c)
            else:
                t = stack.pop(-1)
                if c != matching[t]:
                    result += score[c]
                    break

    return result


def get_number_part2(input_file_name):
    data = get_numbers(input_file_name)
    result = []
    for l in data:
        matching = {'{': '}', '[': ']', '(': ')', '<': '>'}
        score = {'}': 3, ']': 2, ')': 1, '>': 4}
        stack = []
        res = 0
        failure = False
        for c in l.strip():
            if c in ['{', '[', '(', '<']:
                stack.append(c)
            else:
                t = stack.pop(-1)
                if c != matching[t]:
                    failure = True
                    break
        if failure: continue
        for i in range(len(stack)):
            t = stack.pop(-1)
            res *= 5
            res += score[matching[t]]
        result.append(res)
    result.sort()
    #print(result)
    return result[int(len(result)/2)]
