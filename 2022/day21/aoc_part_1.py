import re

def get_value(var, expr):
    e = expr[var]
    if 'value' not in e:
        v1 = get_value(e['var1'], expr)
        v2 = get_value(e['var2'], expr)
        e['expr'] = e['expr'].replace(e['var1'], v1)
        e['expr'] = e['expr'].replace(e['var2'], v2)
        e['value'] = str(eval(e['expr']))
    return e['value']

def get_number_part1(input_file_name):
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
    result = get_value('root', expr)
    return int(float(result))
