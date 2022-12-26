import re
import copy
import heapq

class State:
    def __init__(self, blueprint, buy_list):
        self.ore = 0
        self.clay = 0
        self.obsidian = 0
        self.geode = 0
        self.ore_robots = 1
        self.clay_robots = 0
        self.obsidian_robots = 0
        self.geode_robots = 0
        self.time = 0
        self.blueprint = blueprint
        self.buy_list = buy_list

    def collect(self):
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        self.geode += self.geode_robots
        self.time += 1

    def get_buy_list(self):
        buy_list = ['ore', 'clay']
        if self.clay_robots > 0:
            buy_list.append('obsidian')
        if self.obsidian_robots > 0:
            buy_list.append('geode')
        return buy_list

    def handle_state(self):
        new_states = []
        if self.ore >= self.blueprint['geode']['ore'] and self.obsidian >= self.blueprint['geode']['obsidian'] and 'geode' in self.buy_list:
            # build geode robot
            new_state = copy.copy(self)
            new_state.collect()
            new_state.ore -= self.blueprint['geode']['ore']
            new_state.obsidian -= self.blueprint['geode']['obsidian']
            new_state.geode_robots += 1
            new_state.buy_list = self.get_buy_list()
            new_states.append(new_state)
            self.buy_list.remove('geode')
        elif self.ore >= self.blueprint['obsidian']['ore'] and self.clay >= self.blueprint['obsidian']['clay'] and 'obsidian' in self.buy_list:
            # build obsidian robot
            new_state = copy.copy(self)
            new_state.collect()
            new_state.ore -= self.blueprint['obsidian']['ore']
            new_state.clay -= self.blueprint['obsidian']['clay']
            new_state.obsidian_robots += 1
            new_states.append(new_state)
            new_state.buy_list = self.get_buy_list()
            self.buy_list.remove('obsidian')
        else:
            if self.ore >= self.blueprint['clay']['ore'] and 'clay' in self.buy_list:
                # build clay robot
                new_state = copy.copy(self)
                new_state.collect()
                new_state.ore -= self.blueprint['clay']['ore']
                new_state.clay_robots += 1
                new_states.append(new_state)
                new_state.buy_list = self.get_buy_list()
                self.buy_list.remove('clay')
            if self.ore >= self.blueprint['ore']['ore'] and 'ore' in self.buy_list:
                # build ore robot
                new_state = copy.copy(self)
                new_state.collect()
                new_state.ore -= self.blueprint['ore']['ore']
                new_state.ore_robots += 1
                new_state.buy_list = self.get_buy_list()
                new_states.append(new_state)
                self.buy_list.remove('ore')
        self.collect()
        return new_states

    def __lt__(self, other):
        return -self.geode < -other.geode or \
               (self.geode == other.geode and -self.obsidian < -other.obsidian) or \
               (self.geode == other.geode and self.obsidian == other.obsidian and -self.clay < -other.clay)

class Strategy:
    def __init__(self, blueprint):
        self.act_states = []
        heapq.heappush(self.act_states, State(blueprint, ['ore', 'clay']))
        self.blueprint = blueprint
        self.finished_states = []
        self.max_geode = 0
        self.max_geode_r = 0

    def find(self):
        while len(self.act_states) > 0:
            state = heapq.heappop(self.act_states)
            if state.time >= 24:
                if state.geode > self.max_geode:
                    self.max_geode = state.geode
                    self.max_geode_r = state.geode_robots
                    #print(f'{self.max_geode} {len(self.act_states)}')
                #self.finished_states.append(state)
            elif (self.max_geode_r - state.geode_robots) > (24 - state.time):
                continue
            else:
                new_states = state.handle_state()
                if len(state.buy_list) > 0:
                    heapq.heappush(self.act_states, state)
                for s in new_states:
                    heapq.heappush(self.act_states, s)


def get_number_part1(input_file_name):
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    blueprints = []
    for l in lines:
        m = re.match(r'Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.\s*',l)
        if not m:
            print('error ' + l)
            continue
        #print(m.group(1))
        b = {
            'id': int(m.group(1)),
            'ore': {'ore': int(m.group(2))},
            'clay': {'ore': int(m.group(3))},
            'obsidian': {'ore': int(m.group(4)), 'clay': int(m.group(5))},
            'geode': {'ore': int(m.group(6)), 'obsidian': int(m.group(7))}
        }
        blueprints.append(b)
    print(blueprints)
    for b in blueprints:
        print(f'Start Blueprint {b["id"]}')
        strategy = Strategy(b)
        strategy.find()
        print(f'End Blueprint {b["id"]} {strategy.max_geode}')
        result += strategy.max_geode * b["id"]
    return result
