class Monkey:
    def __init__(self, number, items, op, test, test_true, test_false):
        self.number = number
        self.items = items
        self.operation = op
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.inspected = 0

    def handle_items(self, monkeys, limit):
        self.inspected += len(self.items)
        for item in self.items:
            old = item
            new = eval(self.operation)
            new %= limit
            if (new % self.test) == 0:
                m = monkeys[self.test_true]
            else:
                m = monkeys[self.test_false]
            m.items.append(new)
        self.items = []

    def __str__(self):
        s = f'Monkey {self.number}: items=str{self.items} inspected={self.inspected}'
        return s


def get_number_part2(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    monkeys = []
    for i, l in enumerate(lines):
        l = l.strip()
        if l.startswith('Monkey'):
            number = int(lines[i].replace('Monkey', '').replace(':', ''))
            items = list(map(int, lines[i + 1].replace('Starting items: ', '').split(',')))
            op = lines[i + 2].replace('Operation: ', '').replace('new = ', '')
            test = int(lines[i + 3].replace('Test: divisible by', ''))
            test_true = int(lines[i + 4].replace('If true: throw to monkey', ''))
            test_false = int(lines[i + 5].replace('If false: throw to monkey', ''))
            monkeys.append(Monkey(number, items, op, test, test_true, test_false))
    limit = 1
    for m in monkeys:
        limit *= m.test
    for r in range(1, 10001):
        for m in monkeys:
            m.handle_items(monkeys, limit)
        #print(r)
        #for m in monkeys:
        #    print(m)
    inspected = []
    for m in monkeys:
        #print(m)
        inspected.append(m.inspected)
    inspected = sorted(inspected, reverse=True)
    return inspected[0] * inspected[1]
