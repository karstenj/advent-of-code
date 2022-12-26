import re
import copy

def get_value(var, expr):
    e = expr[var]
    if 'value' not in e:
        v1 = get_value(e['var1'], expr)
        v2 = get_value(e['var2'], expr)
        e['expr'] = e['expr'].replace(e['var1'], v1)
        e['expr'] = e['expr'].replace(e['var2'], v2)
        e['value'] = str(eval(e['expr']))
    return e['value']

def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    expr = {}
    for l in lines:
        m = re.match(r'([a-z]+):\s+([0-9]+)\s*', l)
        if m:
            expr[m.group(1)] = {'value': m.group(2)}
        else:
            m = re.match(r'([a-z]+):\s*(.*)\s*', l)
            if m:
                ops = re.split(r'\*|\+|\/|\-', m.group(2))
                expr[m.group(1)] = {'expr': m.group(2), 'var1': ops[0].strip(), 'var2': ops[1].strip()}
    human = 0
    old_delta_value = None
    old_v1 = None
    while True:
        e = copy.deepcopy(expr)
        e['humn']['value'] = str(human)
        v1 = get_value(e['root']['var1'], e)
        v2 = get_value(e['root']['var2'], e)
        if float(v1) == float(v2):
            break
        delta_value = float(v2) - float(v1)
        if old_delta_value is not None:
            delta_v1 = float(v1) - old_v1
            delta_human_v1 = delta_v1 / delta_human
            delta_human = delta_value / delta_human_v1
            human += delta_human
            #print(f'{delta_value} {delta_human} {human}')
        else:
            delta_human = 1
            human += delta_human
        old_delta_value = delta_value
        old_v1 = float(v1)
    #print(human)
    return int(float(human))
