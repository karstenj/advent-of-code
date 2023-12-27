import sys
import unittest
import re
import functools

def check_workflow(act_workflow, checks, workflows):
    result = 0
    if act_workflow == 'A':
        vars = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}
        for c in checks:
            if '>=' in c:
                var, value = c.replace('>=', ':').split(':')
                vars[var][0] = max(vars[var][0], int(value))
            elif '<=' in c:
                var, value = c.replace('<=', ':').split(':')
                vars[var][1] = min(vars[var][1], int(value))
            elif '>' in c:
                var, value = c.split('>')
                vars[var][0] = max(vars[var][0], int(value)+1)
            else:
                var, value = c.split('<')
                vars[var][1] = min(vars[var][1], int(value)-1)
        result = 1
        for v in vars.values():
            result *= (v[1] - v[0] + 1)
        #print('A', checks, vars, result)
        return result
    if act_workflow == 'R':
        #print('R', checks)
        return 0
    for c in workflows[act_workflow]['checks']:
        result += check_workflow(workflows[act_workflow]['checks'][c], checks + [c], workflows)
        if '<' in c:
            checks.append(c.replace('<', '>='))
        else:
            checks.append(c.replace('>', '<='))
    result += check_workflow(workflows[act_workflow]['default'], checks[:], workflows)
    return result


def get_number_part(input_file_name):
    exec('result = 0')
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    workflows = {}
    ratings = []
    parse_workflows = True
    for l in lines:
        if len(l) == 0:
            parse_workflows = False
            continue
        if parse_workflows:
            mx = re.match(r'(\w+)\{(.*)\}', l)
            if mx:
                key = mx.group(1)
                checks = mx.group(2).split(',')
                workflows[key] = {}
                workflows[key]['checks'] = {}
                for c in checks:
                    parts = c.split(':')
                    if len(parts) == 2:
                        workflows[key]['checks'][parts[0]] = parts[1]
                    else:
                        workflows[key]['default'] = c
        else:
            assignments = []
            mx = re.match(r'\{(.*)\}', l)
            if mx:
                for r in mx.group(1).split(','):
                    assignments.append(r)
            ratings.append(assignments)

    result = check_workflow('in', [], workflows)

    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
    #solution_3 = get_number_part('input3.txt')
    #print(f'Solution part 1: {solution_3}')
