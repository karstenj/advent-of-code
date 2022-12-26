
class Position:
    def __init__(self, pos=None):
        self.x = pos.x if pos is not None else 0
        self.y = pos.y if pos is not None else 0

    def is_adjentend(self, pos):
        return abs(self.x - pos.x) <= 1 and abs(self.y - pos.y) <= 1

    def step_left(self):
        self.x -= 1

    def step_right(self):
        self.x += 1

    def step_up(self):
        self.y += 1

    def step_down(self):
        self.y -= 1

    def __str__(self):
        return f"x={self.x} y={self.y}"


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    steps = set()
    h = Position()
    t = Position()
    for l in lines:
        l = l.strip()
        d, s = l.split(' ')
        s = int(s)
        for i in range(s):
            o = Position(h)
            if d == 'L':
                h.step_left()
            elif d == 'R':
                h.step_right()
            elif d == 'U':
                h.step_up()
            elif d == 'D':
                h.step_down()
            if not h.is_adjentend(t):
                t = o
            steps.add((t.x, t.y))

    #print(steps)
    return len(steps)
