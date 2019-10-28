from appmodules.state import State
from appmodules.state import State
from appmodules.edge import Edge
from appmodules.transition import Transition
from typing import List
from tkinter import messagebox
from appmodules.visualState import VisualState
from appmodules.gtt import Synthesis_voice
from appmodules.pytt import Pytt
import time


class StateGenerator:
    def __init__(self):
        self.word = None
        self.alphabet = None
        self.state = None
        self.last_state = None
        self.show_graphics = None
        self.visual_state = VisualState()

    def set_word(self, word):
        self.word = word
        self.alphabet = self.get_alphabet(self.word)
        self.state = None

    def generate(self):
        if len(self.word) % 2 == 0:
            Pytt('error, la palabra debe ser palindrome impar por favor intente de nuevo')
            raise Exception('ERROR: La palabra debe ser impar')

        aux_alphabet = self.alphabet.copy()
        aux_alphabet.insert(0, '#')

        # Estados
        state = State('q0')
        state2 = State('q1')
        state3 = State('q2', True)

        # Aristas
        edge1_1 = Edge(state)
        edge1_2 = Edge(state2)
        edge2_2 = Edge(state2)
        edge2_3 = Edge(state3)

        # Agregando transiciones

        for x in self.alphabet:
            for y in aux_alphabet:
                edge1_1.transitions.append(Transition(x, y))

        middle_caracter = self.get_middle_caracter()

        for x in aux_alphabet:
            edge1_2.transitions.append(Transition(middle_caracter, x, [x]))

        for x in self.alphabet:
            edge2_2.transitions.append(Transition(x, x, ['λ']))

        edge2_3.transitions.append(Transition('λ', '#', ['#']))

        # Agregando Aristas

        state.add_edge(edge1_1)
        state.add_edge(edge1_2)

        state2.add_edge(edge2_2)
        state2.add_edge(edge2_3)

        self.last_state = state3.name

        # retorno estado inicial
        self.state = state

    def generate_graphics(self):
        self.generate()

    def exec(self):
        self.generate()
        try:
            is_valid = self.validate(['#'], list(self.word), self.state)
            if is_valid:
                Pytt('es un palindromo impar')
        except:
            Pytt("ERROR, La palabra no es palindrome por favor intente de nuevo")


    def validate(self, pile: List[str], word: List[str], state: State):

        let = 'λ'
        if len(word) > 0:
            let = word.pop()

        edge, transition = self.find_transition(state, pile.pop(), let)

        if transition is None:
            return False

        if transition.push[0] != 'λ':
            pile += transition.push

        next_state = edge.next_state

        if next_state.accept:
            return True

        return self.validate(pile, word, next_state)

    def run_graphic_validate(self, mode):
        self.visual_state.set_var(self.window.paint)
        self.visual_state.paint_states(self.state)
        is_valid = self.graphic_validate(['#'], list(self.word), self.state, mode)

    def graphic_validate(self, pile: List[str], word: List[str], state: State, mode):
        let = 'λ'
        if len(word) > 0:
            let = word.pop()

        pile_clone = pile.copy()
        edge, transition = self.find_transition(state, pile.pop(), let)
        t_graphic = "[{}] -> {}, {} / ".format(state.name, transition.entry, transition.extract)

       #pintando transicion
        self.window.label_transition.set(transition.get())


#pintando la palabra

        b = 0
        size = len(self.word) - len(word)
        print(size)
        for i in range(size):
            self.window.paint.create_rectangle(400 + b, 60, 430 + b, 90, fill='red')
            self.window.paint.create_text(415 + b, 75, text=self.word[i], font=('calibri', 18))
            b = b+30

#----------------------------------------------------------------------



#pintando pila
        p = 0
        for i in range(len(self.word)):

            self.window.paint.create_rectangle(650, 480 - p, 700, 450 - p, fill='white')
            if i<len(pile):
                self.window.paint.create_text(675, 465 - p, text=pile[i], tag='pile', font=('calibri', 18))

            p = p + 30

        if len(pile) == 0:
            self.window.paint.create_text(675, 465, text='#', tag='pile', font=('calibri', 18))

#------------------------------------------------------------------------------------------------
        print(state.name,edge.next_state.name)


        for tr in transition.push:
            t_graphic += "{}".format(tr)
        t_graphic += " -> [{}]".format(edge.next_state.name)

        items2 = self.window.paint.find_withtag(state.name if state.name != edge.next_state.name else '')
        for i in range(0, len(items2)):
            if i != 1:
                self.window.paint.itemconfigure(items2[i], fill='green')

        time.sleep(2 if mode == 1 else 0.3)

        items = self.window.paint.find_withtag(edge.next_state.name)
        for i in range(0, len(items)):
            if i != 1:
                self.window.paint.itemconfigure(items[i], fill='red')

        if transition is None:
            return False

        if transition.push[0] != 'λ':
            pile += transition.push

        next_state = edge.next_state

        if next_state.accept:
            return True

        return self.graphic_validate(pile, word, next_state, mode)

    @staticmethod
    def find_transition(state: State, let_pile: str, let: str):
        for e in state.edges:
            for t in e.transitions:
                if t.equals(let, let_pile):
                    return e, t
        return None

    @staticmethod
    def get_alphabet(word: str):
        alphabet = []
        middle_l = int((len(word) / 2))
        for l in word:
            if l not in alphabet and l != word[middle_l]:
                alphabet.append(l)

        return alphabet

    def get_middle_caracter(self):
        return self.word[int(len(self.word) / 2)]

    def set_show_graphics(self, window):
        self.window = window
