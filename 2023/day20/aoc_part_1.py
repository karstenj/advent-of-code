import sys
import unittest
import re
import functools

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()

    lines = [l.strip() for l in lines]
    elements = {}
    for l in lines:
        module, dest = l.split('->')
        module = module.strip()
        dest = [d.strip() for d in dest.split(',')]
        if module[0] in ['%', '&']:
            module_type = module[0]
            module = module[1:]
        elif module == 'broadcaster':
            module_type = 'broadcaster'
        else:
            module_type = 'unknown'
        elements[module] = {'dest': dest, 'type': module_type}
        if module_type == '%':
            elements[module]['state'] = False

    for e in elements:
        for d in elements[e]['dest']:
            if d not in elements: continue
            if elements[d]['type'] == '&':
                elements[d].setdefault('state', {})
                elements[d]['state'][e] = False
    #print(elements)

    pulses = []
    for i in range(1000):
        queue = [('', 'broadcaster', False)]
        while len(queue) > 0:
            module_src, module_dst, state = queue.pop(0)
            pulses.append(state)
            if module_dst not in elements:
                continue
            if module_dst == 'broadcaster':
                for d in elements[module_dst]['dest']:
                    #print(f'{module_dst} {state} -> {d}')
                    queue.append((module_dst, d, state))
            elif elements[module_dst]['type'] == '%':
                if not state:
                    elements[module_dst]['state'] = not elements[module_dst]['state']
                    for d in elements[module_dst]['dest']:
                        #print(f'{module_dst} {elements[module_dst]["state"]} -> {d}')
                        queue.append((module_dst, d, elements[module_dst]['state']))
            elif elements[module_dst]['type'] == '&':
                elements[module_dst]['state'][module_src] = state
                final_state = False
                for s in elements[module_dst]['state'].values():
                    if not s:
                        final_state = True
                for d in elements[module_dst]['dest']:
                    #print(f'{module_dst} {final_state} -> {d}')
                    queue.append((module_dst, d, final_state))

    low_pulses = pulses.count(False)
    high_pulses = pulses.count(True)
    result = low_pulses * high_pulses


    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_3 = get_number_part('input3.txt')
    print(f'Test solution part 1: {solution_3}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
