def get_score(t, x, y, grid):
    result = 1
    score = 0
    for i in range(x-1, -1, -1):
        score += 1
        if grid[i][y] >= t:
            break
    result *= score
    score = 0
    for i in range(x+1, len(grid)):
        score += 1
        if grid[i][y] >= t:
            break
    result *= score
    score = 0
    for i in range(y-1, -1, -1):
        score += 1
        if grid[x][i] >= t:
            break
    result *= score
    score = 0
    for i in range(y+1, len(grid[x])):
        score += 1
        if grid[x][i] >= t:
            break
    result *= score
    return result

def get_number_part2(input_file_name):
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
            score = get_score(t, x, y, grid)
            #print(f'{x} {y} {score}')
            if score > result:
                result = score
                #if not (x == 0 or y == 0 or x == (len(grid) - 1) or y == (len(grid[x]) - 1)):
                #    print(f'{x} {y}')

    return result
