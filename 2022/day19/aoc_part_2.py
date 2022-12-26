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
        self.first_geode = None
        self.first_obsidian = None

    def collect(self):
        self.ore += self.ore_robots
        self.clay += self.clay_robots
        self.obsidian += self.obsidian_robots
        self.geode += self.geode_robots
        self.time += 1

    def get_buy_list(self):
        buy_list = []
        if self.clay_robots > 0:
            buy_list.append('obsidian')
        if self.obsidian_robots > 0:
            buy_list.append('geode')
        if self.geode_robots == 0:
            buy_list.append('ore')
            buy_list.append('clay')
        return buy_list

    def handle_state(self):
        new_states = []
        buy_remaining = True
        if self.ore >= self.blueprint['geode']['ore'] and self.obsidian >= self.blueprint['geode']['obsidian'] and 'geode' in self.buy_list:
            # build geode robot
            new_state = copy.copy(self)
            new_state.collect()
            new_state.ore -= self.blueprint['geode']['ore']
            new_state.obsidian -= self.blueprint['geode']['obsidian']
            if new_state.geode_robots == 0:
                new_state.first_geode = new_state.time + 1
            new_state.geode_robots += 1
            new_state.buy_list = self.get_buy_list()
            new_states.append(new_state)
            self.buy_list.remove('geode')
            buy_remaining = True
        if self.ore >= self.blueprint['obsidian']['ore'] and self.clay >= self.blueprint['obsidian']['clay'] and 'obsidian' in self.buy_list:
            # build obsidian robot
            new_state = copy.copy(self)
            new_state.collect()
            new_state.ore -= self.blueprint['obsidian']['ore']
            new_state.clay -= self.blueprint['obsidian']['clay']
            if new_state.obsidian_robots == 0:
                new_state.first_obsidian = new_state.time + 1
            new_state.obsidian_robots += 1
            new_states.append(new_state)
            new_state.buy_list = self.get_buy_list()
            self.buy_list.remove('obsidian')
            buy_remaining = True
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
        self.act_states = [State(blueprint, ['ore', 'clay'])]
        self.blueprint = blueprint
        self.finished_states = []
        self.max_geode = 0
        self.max_geode_r = 0

    def add_state(self, state):
        self.act_states.append(state)

    def get_buy_list(self, clay_r, obsidian_r, geode_r):
        buy_list = []
        if clay_r > 0:
            buy_list.append('obsidian')
        if obsidian_r > 0:
            buy_list.append('geode')
        if geode_r == 0:
            buy_list.append('ore')
            buy_list.append('clay')
        return buy_list

    def calculate(self, time, ore, clay, obsidian, geode, ore_r, clay_r, obsidian_r, geode_r, buy_list):
        if time >= 32:
            if geode_r > self.max_geode_r:
                self.max_geode_r = geode_r
                print(f'GeodeR {geode_r}')
            return geode
        if geode > self.max_geode:
            self.max_geode = geode
            print(f'Geode {geode}')
        if (self.max_geode_r - geode_r) > (32 - time):
            return 0
        geode_ret = []
        if ore >= self.blueprint['geode']['ore'] and obsidian >= self.blueprint['geode']['obsidian'] and 'geode' in buy_list:
            geode_ret.append(self.calculate(
                time+1,
                ore+ore_r-self.blueprint['geode']['ore'],
                clay+clay_r,
                obsidian+obsidian_r-self.blueprint['geode']['obsidian'],
                geode+geode_r,
                ore_r,
                clay_r,
                obsidian_r,
                geode_r+1,
                self.get_buy_list(clay_r, obsidian_r, geode_r+1)))
            buy_list.remove('geode')
        if ore >= self.blueprint['obsidian']['ore'] and clay >= self.blueprint['obsidian']['clay'] and 'obsidian' in buy_list:
            geode_ret.append(self.calculate(
                time+1,
                ore+ore_r-self.blueprint['obsidian']['ore'],
                clay+clay_r-self.blueprint['obsidian']['clay'],
                obsidian+obsidian_r,
                geode+geode_r,
                ore_r,
                clay_r,
                obsidian_r+1,
                geode_r,
                self.get_buy_list(clay_r, obsidian_r+1, geode_r)))
            buy_list.remove('obsidian')
        if ore >= self.blueprint['clay']['ore'] and 'clay' in buy_list:
            geode_ret.append(self.calculate(
                time+1,
                ore+ore_r-self.blueprint['clay']['ore'],
                clay+clay_r,
                obsidian+obsidian_r,
                geode+geode_r,
                ore_r,
                clay_r+1,
                obsidian_r,
                geode_r,
                self.get_buy_list(clay_r+1, obsidian_r, geode_r)))
            buy_list.remove('clay')
        if ore >= self.blueprint['ore']['ore'] and 'ore' in buy_list:
            geode_ret.append(self.calculate(
                time+1,
                ore+ore_r-self.blueprint['ore']['ore'],
                clay+clay_r,
                obsidian+obsidian_r,
                geode+geode_r,
                ore_r+1,
                clay_r,
                obsidian_r,
                geode_r,
                self.get_buy_list(clay_r, obsidian_r, geode_r)))
            buy_list.remove('ore')
        if len(buy_list) > 0:
            geode_ret.append(self.calculate(
                time+1,
                ore+ore_r,
                clay+clay_r,
                obsidian+obsidian_r,
                geode+geode_r,
                ore_r,
                clay_r,
                obsidian_r,
                geode_r,
                buy_list))
        return max(geode_ret)

    def find(self):
        return self.calculate(0, 0, 0, 0, 0, 1, 0, 0, 0, ['ore', 'clay'])

    def __find(self):
        while len(self.act_states) > 0:
            state = self.act_states.pop()
            if state.time >= 32:
                if state.geode > self.max_geode:
                    self.max_geode = state.geode
                    print(f'{self.max_geode} {len(self.act_states)}')
                #self.finished_states.append(state)
            else:
                new_states = state.handle_state()
                if len(state.buy_list) > 0:
                    self.add_state(state)
                for s in new_states:
                    self.add_state(s)


def get_number_part2(input_file_name):
    result = 1
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
        max_geode = strategy.find()
        print(f'End Blueprint {b["id"]} {max_geode}')
        result *= max_geode
    return result
