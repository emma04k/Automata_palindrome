from typing import List
from appmodules.edge import Edge


class State:
    def __init__(self, name: str, accept=False):
        self.name = name
        self.edges: List[Edge] = []
        self.accept = accept

    def add_edge(self, edge: Edge):
        self.edges.append(edge)

    def show_edges(self):
        for e in self.edges:
            print("{} -> {}".format(self.name, e.next_state.name))