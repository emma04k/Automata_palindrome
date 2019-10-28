from appmodules.state import State


class VisualState:
    SPACE = 25

    def __init__(self):
        self.paint = None
        self.state = None

    def set_var(self, paint):
        self.paint = paint

    def paint_states(self, state: State, x=140, y=350, mode=1):

        for ed in state.edges:

            if ed.next_state.name == 'Q2':
                y = 420

            for t in ed.transitions:
                self.paint.create_text(x, y, text=t.get(), font=('calibri', 16))
                y -= self.SPACE

            x += 100
            mode = mode * (-1)

            y = 420 if mode == -1 else 350

            if state != ed.next_state:
                self.paint_states(ed.next_state, x - 5, y, mode)
