
def get_number_part2(input_file_name):
    result = ''
    with open(input_file_name) as fh:
        lines = fh.readlines()
    n_stacks = 9
    stacks = [[] for i in range(n_stacks)]
    for l in lines:
       if len(l) >= 1 and l[1] == '1':
           break
       for i in range(n_stacks):
           ind = i * 4 + 1
           if ind < len(l) and l[ind] != ' ':
               stacks[i].append(l[ind])
    for l in lines:
        if l.startswith('move'):
            l = l.strip().replace('move ', '').replace(' from ', ',').replace(' to ', ',')
            n, f, t = map(int, l.split(','))
            #print(f'{n} {f} {t}')
            items = stacks[f-1][:n]
            stacks[f-1] = stacks[f-1][n:]
            stacks[t-1] = items + stacks[t-1]
    for s in stacks:
        if len(s) > 0:
            result += s[0]
    #print(stacks)
    #print(result)
    return result
