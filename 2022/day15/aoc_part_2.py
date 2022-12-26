import sys


def show_grid(grid):
    for i, r in enumerate(grid):
        print(f"{i:02d} {r}")


def process_row(xs, xe, y, grid):
    new_row = []
    for c in grid[y]:
        x1, x2 = c
        if xs <= x1 and xe >= x2:
            # fully covered => remove (x1, x2)
            pass
        else:
            partial = False
            if x1 < xs and x2 >= xs:
                # partial
                new_row.append((x1, xs - 1))
                partial = True
            if x1 <= xe and x2 > xe:
                # partial
                new_row.append((xe + 1, x2))
                partial = True
            if not partial:
                new_row.append(c)
    grid[y] = new_row

def get_number_part2(input_file_name, dim):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    rows = []
    for l in lines:
        l = l.strip()
        coord = list(map(int, l.split(',')))
        rows.append(coord)

    #dim = 4000000
    grid = []
    for y in range(dim+1):
        grid.append([(0, dim)])
    for r in rows:
        x1, y1, x2, y2 = r
        d = abs(x1 - x2) + abs(y1 - y2)
        #print(str(r) + " d=" + str(d))
        d2 = d * 2 + 1
        for i in range(0, d+1):
            w = d2 - i * 2
            xs = min(max(x1 - w//2, 0), dim)
            xe = min(max(x1 + w//2, 0), dim)
            y = min(max(y1 + i, 0), dim)
            process_row(xs, xe, y, grid)
            y = min(max(y1 - i, 0), dim)
            process_row(xs, xe, y, grid)

    #show_grid(grid)
    for y, r in enumerate(grid):
        if len(r) == 1:
            x,_ = r[0]
            result = x * 4000000 + y
            break
    return result
