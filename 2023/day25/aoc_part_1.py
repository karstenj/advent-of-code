import copy
import sys
import unittest
import re
import functools
from collections import namedtuple
import sympy as sy
import networkx as nx

def get_number_part(input_file_name):
    print(input_file_name)
    result = 0
    with open(input_file_name) as fh:
        lines = fh.readlines()
    lines = [l.strip() for l in lines]
    edges = {}
    nodes = set()
    G = nx.Graph()
    for l in lines:
        src, dest = l.split(':')
        dest = [d.strip() for d in dest.split()]
        for d in dest:
            G.add_edge(src, d)
    cliques = [c for c in nx.k_edge_components(G, 4)]
    result = len(cliques[0]) * len(cliques[1])
    print(cliques, len(cliques), result)
    #print(nx.is_k_edge_connected(G, 3))
    #cluster = nx.clustering(G)
    #print(cluster)
    #sorted_cluster = sorted(nx.clustering(G), key=lambda x: cluster[x])
    #for sc in sorted_cluster:
    #    print(sc, cluster[sc])
    #print(sorted(nx.clustering(G), key=lambda x: cluster[x]))



    print(len(edges), len(nodes))
    return result

if __name__ == '__main__':
    solution_1 = get_number_part('input1.txt')
    print(f'Test solution part 1: {solution_1}')
    solution_2 = get_number_part('input2.txt')
    print(f'Solution part 1: {solution_2}')
