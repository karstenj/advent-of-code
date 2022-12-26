import sys

def show_grid(grid):
    for i, r in enumerate(grid):
        print(f"{i:02d} {''.join(r)}")


def get_number_part1(input_file_name, row):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    rows = []
    for l in lines:
        l = l.strip()
        coord = list(map(int, l.split(',')))
        rows.append(coord)
    #row = 2000000
    xr1 = None
    xr2 = None
    for r in rows:
        x1, y1, x2, y2 = r
        d = abs(x1 - x2) + abs(y1 - y2)
        #print(str(r) + " d=" + str(d))
        d2 = d * 2 + 1
        w = d2 - abs(row - y1) * 2
        if w > 0:
            if xr1 is None and xr2 is None:
                xr1 = x1 - w//2
                xr2 = x1 + w//2
            else:
                xr1 = min(x1 - w//2, xr1)
                xr2 = max(x1 + w//2, xr2)
    result = xr2 - xr1
    return result
