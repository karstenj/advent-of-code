import sys
import unittest
import re
import functools

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
    #print(workflows)
    #print(ratings)
    for line in ratings:
        act_workflow = 'in'
        for rating in line:
            #print(rating)
            exec(rating)
        while act_workflow != 'A' and act_workflow != 'R':
            prev_workflow = act_workflow
            for check in workflows[act_workflow]['checks']:
                #print(check)
                if eval(check):
                    act_workflow = workflows[act_workflow]['checks'][check]
                    break
            if prev_workflow == act_workflow:
                act_workflow = workflows[act_workflow]['default']
        if act_workflow == 'A':
            exec('result += x + m + a + s')


    return eval('result')

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
