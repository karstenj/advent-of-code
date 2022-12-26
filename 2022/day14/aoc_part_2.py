def show_grid(grid):
    for i, r in enumerate(grid):
        print(f"{i:02d} {''.join(r)}")


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    rows = []
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0
    for l in lines:
        l = l.strip()
        coord = l.split('->')
        coord = [list(map(int, c.strip().split(','))) for c in coord]
        #print(coord)
        rows.append(coord)
        for c in coord:
            x, y = c
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            max_y = max(y, max_y)
    grid = []
    min_x = 0
    max_x = 1000
    max_y += 2
    w = (max_x - min_x + 1)
    h = max_y+1
    for y in range(h):
        grid.append(['.'] * w)
    for r in rows:
        for i in range(len(r)-1):
            x1, y1 = r[i]
            x2, y2 = r[i+1]
            x1 -= min_x
            x2 -= min_x
            if x1 == x2:
                if y1 < y2:
                    for y in range(y1, y2+1):
                        grid[y][x1] = '#'
                else:
                    for y in range(y2, y1+1):
                        grid[y][x1] = '#'
            elif y1 == y2:
                if x1 < x2:
                    for x in range(x1, x2+1):
                        grid[y1][x] = '#'
                else:
                    for x in range(x2, x1+1):
                        grid[y1][x] = '#'
            else:
                print('x1==x2 and y1==y2')
    for x in range(w):
        grid[h-1][x] = '#'
    #show_grid(grid)
    #print(f'min_x={min_x} max_x={max_x} min_y={min_y} max_y={max_y} w={w} h={h}')
    while True:
        x = 500 - min_x
        y = 0
        while True:
            # if x == 70 and y == 153:
            #     print(f'{x} {y}')
            if y < h:
                if grid[y+1][x] == '.':
                    y += 1
                elif x > 0 and grid[y+1][x-1] == '.':
                    x -= 1
                    y += 1
                elif x < (w-1) and grid[y+1][x+1] == '.':
                    x += 1
                    y += 1
                else:
                    break
            else:
                break
        if y == (h-1) or x == 0 or x == (w-1):
            break
        grid[y][x] = 'o'
        result += 1
        if x == 500 and y == 0:
            #show_grid(grid)
            break
    return result
