def is_visible(t, x, y, grid):
    if x == 0 or y == 0 or x == (len(grid)-1) or y == (len(grid[x])-1):
        return True
    visible = True
    for i in range(x-1, -1, -1):
        if grid[i][y] >= t:
            visible = False
            break
    if visible:
        return True
    visible = True
    for i in range(x+1, len(grid)):
        if grid[i][y] >= t:
            visible = False
            break
    if visible:
        return True
    visible = True
    for i in range(y-1, -1, -1):
        if grid[x][i] >= t:
            visible = False
            break
    if visible:
        return True
    visible = True
    for i in range(y+1, len(grid[x])):
        if grid[x][i] >= t:
            visible = False
            break
    if visible:
        return True
    return False

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    grid = []
    for l in lines:
        l = l.strip()
        row = [int(x) for x in l]
        grid.append(row)
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            t = grid[x][y]
            if is_visible(t, x, y, grid):
                #if not (x == 0 or y == 0 or x == (len(grid) - 1) or y == (len(grid[x]) - 1)):
                #    print(f'{x} {y}')
                result += 1

    return result
