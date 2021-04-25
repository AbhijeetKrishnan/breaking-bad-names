#!/usr/bin/env python

from typing import List, Dict
import sys

import networkx as nx

def read_elements_list(filename: str = "elements.txt") -> List[str]:
    with open(filename, 'r') as fp:
        elements = fp.read().split('\n')
    return elements

def assign_elements(names: List[str], elements: List[str]) -> Dict[str, str]:
    graph = nx.Graph()
    graph.add_nodes_from(names, bipartite=0)
    graph.add_nodes_from(elements, bipartite=1)
    graph.add_edges_from([(name, ele) for ele in elements for name in names if ele in name])
    return nx.bipartite.maximum_matching(graph, top_nodes=names)

if __name__ == '__main__':
    elements = read_elements_list()
    names = [name.strip().lower() for name in sys.stdin.read().split('\n') if name]
    assignments = assign_elements(names, elements)
    print(assignments)