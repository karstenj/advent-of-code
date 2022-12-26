import sys

WATER = 2
ROCK = 1
AIR = 0

def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    cubes = []
    for l in lines:
        l = l.strip()
        x, y, z = map(int, l.split(','))
        cubes.append((x,y,z))
    surface = 0
    mx, my, mz = 0, 0, 0
    for c in cubes:
        (x, y, z) = c
        mx = max(mx, x+1)
        my = max(my, y+1)
        mz = max(mz, z+1)
    #print(f'{mx} {my} {mz}')
    space = []
    for x in range(mx):
        area = []
        for y in range(my):
            area.append([AIR]*mz)
        space.append(area)
    #print(space)
    for c in cubes:
        (x, y, z) = c
        space[x][y][z] = ROCK
    for x in range(mx):
        for y in range(my):
            for z in range(mz):
                if space[x][y][z] == ROCK:
                    if (x > 0 and space[x - 1][y][z] == AIR) or x == 0:
                        surface += 1
                    if (x < (mx - 1) and space[x + 1][y][z] == AIR) or x == (mx-1):
                        surface += 1
                    if (y > 0 and space[x][y - 1][z] == AIR) or y == 0:
                        surface += 1
                    if (y < (my - 1) and space[x][y + 1][z] == AIR) or y == (my-1):
                        surface += 1
                    if (z > 0 and space[x][y][z - 1] == AIR) or z == 0:
                        surface += 1
                    if (z < (mz - 1) and space[x][y][z + 1] == AIR) or z == (mz-1):
                        surface += 1
    result = surface
    return result
