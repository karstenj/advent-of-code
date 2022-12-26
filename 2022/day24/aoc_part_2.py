import sys
import heapq
from collections import deque

class Grid:
    def __init__(self, lines):
        grid = lines.split('\n')
        grid = [[[c] for c in l] for l in grid]
        self.grid_t = [grid]

    def show_grid(self, t):
        for r in self.grid_t[t]:
            s = ''
            for c in r:
                if len(c) == 1:
                    s += c[0]
                else:
                    s += str(len(c))
            print(s)

    def get_grid(self, t):
        if t < len(self.grid_t):
            return self.grid_t[t]
        g = self.grid_t[t-1]
        ng = []
        self.grid_t.append(ng)
        for r in range(len(g)):
            line = []
            for c in range(len(g[r])):
                line.append([])
            ng.append(line)
        for r in range(len(g)):
            for c in range(len(g[r])):
                for x in g[r][c]:
                    if x == '#':
                        ng[r][c].append(x)
                    elif x == '<':
                        if g[r][c-1][0] != '#':
                            ng[r][c-1].append(x)
                        else:
                            ng[r][len(g[r])-2].append(x)
                    elif x == '>':
                        if g[r][c+1][0] != '#':
                            ng[r][c+1].append(x)
                        else:
                            ng[r][1].append(x)
                    elif x == '^':
                        if g[r-1][c][0] != '#':
                            ng[r-1][c].append(x)
                        else:
                            ng[len(g)-2][c].append(x)
                    elif x == 'v':
                        if g[r+1][c][0] != '#':
                            ng[r+1][c].append(x)
                        else:
                            ng[1][c].append(x)
        for r in range(len(ng)):
            for c in range(len(ng[r])):
                if len(ng[r][c]) == 0:
                    ng[r][c].append('.')
        return self.grid_t[t]


class Step:
    def __init__(self, r, c, t, tr, tc):
        self.r = r
        self.c = c
        self.t = t
        self.dist = abs(tr - r) + abs(tc - c)

    def __lt__(self, other):
        return self.dist < other.dist or (self.dist == other.dist and self.t < other.t)

    def __eq__(self, other):
        return isinstance(other, Step) and self.r == other.r and self.c == other.c and self.t == other.t

    def __hash__(self):
        return hash((self.r, self.c, self.t))

class Strategy:
    def __init__(self, start_time, grid, sr, sc, tr, tc):
        self.grid = grid
        self.min_time = sys.maxsize
        self.visited = set()
        self.next = []
        self.sr = sr
        self.sc = sc
        self.tr = tr
        self.tc = tc
        self.start_time = start_time

    def add(self, step):
        if (step.dist + step.t) <= self.max_depth:
            if step not in self.visited:
                self.visited.add(step)
                self.next.append(step)

    def find_steps(self, r, c, t):
        self.next = []
        g = self.grid.get_grid(t+1)
        if g[r][c + 1][0] == '.':
            self.add(Step(r, c + 1, t + 1, self.tr, self.tc))
        if r < (len(g)-1) and g[r + 1][c][0] == '.':
            self.add(Step(r + 1, c, t + 1, self.tr, self.tc))
        if r > 0 and g[r-1][c][0] == '.':
            self.add(Step(r-1, c, t+1, self.tr, self.tc))
        if g[r][c-1][0] == '.':
            self.add(Step(r, c-1, t+1, self.tr, self.tc))
        if g[r][c][0] == '.':
            self.add(Step(r, c, t+1, self.tr, self.tc))
        return self.next

    def start_find(self):
        steps = []
        self.max_depth = 500 + self.start_time
        heapq.heappush(steps, Step(self.sr, self.sc, self.start_time, self.tr, self.tc))
        while len(steps) > 0:
            step = heapq.heappop(steps)
            if step.r == self.tr and step.c == self.tc:
                if self.min_time > step.t:
                    self.min_time = step.t
                    self.max_depth = step.t
                    #print(f'Found {step.t} {step.r} {step.c}')
                continue
            next = self.find_steps(step.r, step.c, step.t)
            for n in next:
                heapq.heappush(steps, n)
        return self.min_time

def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.read()
    grid = Grid(lines)
    g = grid.get_grid(0)
    tr = len(g) - 1
    for c in range(len(g[tr])):
        if g[tr][c][0] == '.':
            break
    tc = c
    sr = 0
    for c in range(len(g[sr])):
        if g[sr][c][0] == '.':
            break
    sc = c
    print(input_file_name)
    strategy = Strategy(0, grid, sr, sc, tr, tc)
    strategy.start_find()
    strategy = Strategy(strategy.min_time, grid, tr, tc, sr, sc)
    strategy.start_find()
    strategy = Strategy(strategy.min_time, grid, sr, sc, tr, tc)
    result = strategy.start_find()

    return result
