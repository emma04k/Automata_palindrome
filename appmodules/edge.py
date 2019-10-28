from typing import List
from appmodules.transition import Transition


class Edge:
    def __init__(self, next_state):
        self.transitions: List[Transition] = []
        self.next_state = next_state

    def show_transitions(self):
        for t in self.transitions:
            print("{},{}/{}".format(t.entry, t.extract, t.push))

    def get_transitions(self):
        transitions = ''
        for t in self.transitions:
            p = ''
            for elm in t.push:
                p += "{}".format(elm)
            transitions += "{}, {}/ {}\n".format(t.entry, t.extract, p)
        return transitions