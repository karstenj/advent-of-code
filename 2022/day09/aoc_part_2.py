
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

    def set(self, pos):
        self.x = pos.x
        self.y = pos.y

    def set_delta(self, pos):
        if self.x != pos.x:
            self.x += 1 if self.x < pos.x else -1
        if self.y != pos.y:
            self.y += 1 if self.y < pos.y else -1

    def __str__(self):
        return f"x={self.x} y={self.y}"


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    steps = set()
    h = Position()
    tails = []
    for i in range(9):
        tails.append(Position())
    for l in lines:
        l = l.strip()
        d, s = l.split(' ')
        s = int(s)
        for i in range(s):
            if d == 'L':
                h.step_left()
            elif d == 'R':
                h.step_right()
            elif d == 'U':
                h.step_up()
            elif d == 'D':
                h.step_down()
            t_head = h
            for t in tails:
                if not t_head.is_adjentend(t):
                    t.set_delta(t_head)
                t_head = t
            steps.add((tails[-1].x, tails[-1].y))
        print(len(steps))
    return len(steps)
