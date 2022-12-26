import sys

WATER = 2
ROCK = 1
AIR = 0

def get_number_part2(input_file_name):
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
    # fill outer sides with water if AIR
    greedy = []
    for x in range(mx):
        for y in range(my):
            if space[x][y][0] == AIR:
                greedy.append((x, y, 0))
            if space[x][y][mz-1] == AIR:
                greedy.append((x, y, mz-1))
    for x in range(mx):
        for z in range(mz):
            if space[x][0][z] == AIR:
                greedy.append((x, 0, z))
            if space[x][my-1][z] == AIR:
                greedy.append((x, my-1, z))
    for y in range(my):
        for z in range(mz):
            if space[0][y][z] == AIR:
                greedy.append((0, y, z))
            if space[mx-1][y][z] == AIR:
                greedy.append((mx-1, y, z))
    # fill water from surface
    while len(greedy) > 0:
        (x, y, z) = greedy.pop()
        space[x][y][z] = WATER
        if x > 0 and space[x-1][y][z] == AIR:
            greedy.append((x-1, y, z))
        if x < (mx-1) and space[x+1][y][z] == AIR:
            greedy.append((x+1, y, z))
        if y > 0 and space[x][y-1][z] == AIR:
            greedy.append((x, y-1, z))
        if y < (my-1) and space[x][y+1][z] == AIR:
            greedy.append((x, y+1, z))
        if z > 0 and space[x][y][z-1] == AIR:
            greedy.append((x, y, z-1))
        if z < (mz-1) and space[x][y][z+1] == AIR:
            greedy.append((x, y, z+1))
    for x in range(mx):
        for y in range(my):
            for z in range(mz):
                if space[x][y][z] == ROCK:
                    if (x > 0 and space[x - 1][y][z] == WATER) or x == 0:
                        surface += 1
                    if (x < (mx - 1) and space[x + 1][y][z] == WATER) or x == (mx-1):
                        surface += 1
                    if (y > 0 and space[x][y - 1][z] == WATER) or y == 0:
                        surface += 1
                    if (y < (my - 1) and space[x][y + 1][z] == WATER) or y == (my-1):
                        surface += 1
                    if (z > 0 and space[x][y][z - 1] == WATER) or z == 0:
                        surface += 1
                    if (z < (mz - 1) and space[x][y][z + 1] == WATER) or z == (mz-1):
                        surface += 1
    result = surface
    return result
