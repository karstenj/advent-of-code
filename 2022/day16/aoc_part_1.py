import heapq
import sys


def delete_obsolete_nodes(edges, valves, start_valve):
    del_edges = []
    for n in edges:
        if len(edges[n]) == 2 and valves[n] == 0 and n != start_valve:
            keys = list(edges[n].keys())
            n1 = keys[0]
            n2 = keys[1]
            edges[n1][n2] = edges[n1][n] + edges[n2][n]
            edges[n2][n1] = edges[n1][n] + edges[n2][n]
            del edges[n1][n]
            del edges[n2][n]
            del_edges.append(n)
    for n in del_edges:
        del edges[n]


class Node:
    def __init__(self, name, distance=sys.maxsize):
        self.name = name
        self.distance=distance
        self.prev=None

    def __lt__(self, other):
        self.distance < other.distance


def init_nodes(edges):
    all_nodes = {}
    for n in edges:
        all_nodes[n] = Node(n)
    return all_nodes


def calc_closest_distance(edges):
    new_edges = {}
    for start_node in edges:
        all_nodes = init_nodes(edges)
        all_nodes[start_node].distance = 0
        act_nodes = [all_nodes[start_node]]
        while len(act_nodes) > 0:
            q = heapq.heappop(act_nodes)
            for n in edges[q.name]:
                c = edges[q.name][n] + all_nodes[q.name].distance
                if c < all_nodes[n].distance:
                    all_nodes[n].distance = c
                    all_nodes[n].prev = q.name
                    heapq.heappush(act_nodes, all_nodes[n])
        new_edges[start_node] = {}
        for n in all_nodes:
            if n != start_node:
                new_edges[start_node][n] = all_nodes[n].distance
    return new_edges


class PermNode:
    def __init__(self, n, t, s):
        self.nodes = []
        self.nodes.extend(n)
        self.time = t
        self.score = s


def process_nodes(nodes, edges, start_valve, valves):
    act_nodes = []
    max_score = 0
    act_nodes.append(PermNode([start_valve], 30, 0))
    while len(act_nodes) > 0:
        node = act_nodes.pop()
        n1 = node.nodes[-1]
        added = False
        for n2 in nodes:
            if n2 not in node.nodes:
                if edges[n1][n2] < node.time and valves[n2] > 0:
                    t = node.time-edges[n1][n2]-1
                    score = node.score + (valves[n2] * t)
                    new_node = PermNode(node.nodes, t, score)
                    new_node.nodes.append(n2)
                    act_nodes.append(new_node)
                    added = True
        if not added:
            if node.score > max_score:
                max_score = node.score
                #print(max_score)
    return max_score


def get_input(input_file_name):
    with open(input_file_name) as fh:
        lines = fh.readlines()
    valves = {}
    edges = {}
    for l in lines:
        l = l.strip()
        valve,way = l.split(';')
        valve = valve.split('=')
        valves[valve[0]] = int(valve[1])
        edges[valve[0]] = {}
        for w in way.split(','):
            edges[valve[0]][w] = 1
    return edges, valves


def get_number_part1(input_file_name):
    start_valve = 'AA'
    edges, valves = get_input(input_file_name)
    delete_obsolete_nodes(edges, valves, start_valve)
    edges = calc_closest_distance(edges)

    nodes = list(edges.keys())
    nodes.remove(start_valve)
    result = process_nodes(nodes, edges, start_valve, valves)
    #print(result)

    return result
