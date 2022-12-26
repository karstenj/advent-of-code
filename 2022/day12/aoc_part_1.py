
def find_path(nodes, costs, grid):
    node = nodes.pop()
    x, y = node
    c = costs[f'{x}:{y}']
    next_nodes = []
    if x > 0:
        next_nodes.append((x-1, y))
    if x < len(grid)-1:
        next_nodes.append((x + 1, y))
    if y < len(grid[x])-1:
        next_nodes.append((x, y+1))
    if y > 0:
        next_nodes.append((x, y-1))
    prev = grid[x][y]
    for xn, yn in next_nodes:
        act = grid[xn][yn]
        if (act == 'E' and prev == 'z') or (act == 'a' and prev == 'S') or (act not in ['S', 'E'] and ord(act)-ord(prev) <= 1):
            # valid edge
            key = f'{xn}:{yn}'
            if not key in costs or costs[key] > (c + 1):
                #print(f"{xn} {yn} {prev} {act} {c+1}")
                nodes.add((xn, yn))
                costs[key] = c + 1


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    grid = []
    nodes = set()
    costs = {}
    for i, l in enumerate(lines):
        l = l.strip()
        if 'S' in l:
            x, y = i, l.find('S')
            nodes.add((x, y))
            costs[f'{x}:{y}'] = 0
        if 'E' in l:
            xe, ye = i, l.find('E')
        grid.append(l)
    while len(nodes) > 0:
        find_path(nodes, costs, grid)
    #print(costs[f'{xe}:{ye}'])
    return costs[f'{xe}:{ye}']
