from tkinter import *
import threading
from appmodules.stateGenerator import StateGenerator
from appmodules.recognition import Recognition
from functools import partial


state_generator = StateGenerator()


class MainWindow:
    WIDTH = 1000
    HEIGHT = 700

    def __init__(self):
        self.root = Tk()
        self.root.resizable(0,0)
        self.root.title('Automata palindromo impar')
        self.root.geometry("{}x{}".format(self.WIDTH, self.HEIGHT))


        self.paint = Canvas(self.root, width=self.WIDTH, height=self.HEIGHT)
        self.paint.place(x=-1, y=70)

        self.text_entry = StringVar()
        self.label_transition =StringVar()
        self.label_state = StringVar()
        self.text_entry.set("abbcbba")

        Entry(self.root, width=40, textvariable=self.text_entry).place(x=305, y=15)
        Button(self.root, text='Validar', command=self.on_click_validate).place(x=631, y=10)
        Label(self.root,textvariable=self.label_transition,bg='blue',font=('calibri',18)).place(x=450,y=250)
        Label(self.root, textvariable=self.label_state, bg='blue', font=('calibri', 18)).place(x=450, y=290)

        Button(self.root, text='Visualizar Lento', command=lambda: self.on_click_show_validate(1)).place(x=370, y=90)
        Button(self.root, text='Visualizar Rapido', command=lambda: self.on_click_show_validate(2)).place(x=510, y=90)
        state_generator.set_show_graphics(self)
        self.init_components()

    def init_components(self):
        # estado 1
        self.paint.create_line(50, 450, 94, 450, width=3.0, arrow=LAST)
        self.paint.create_arc(105, 375, 175.5, 470, star=0, extent=180, style='arc', width=3.0)
        self.paint.create_line(165, 405, 175, 420, widt=3)
        self.paint.create_line(185, 405, 175, 420, widt=3)
        self.paint.create_oval(95, 495, 185, 405, width=1.5, tag='q0',fill='green')
        self.paint.create_text(140, 450, text='q0', tag='q0', font=('calibri', 20))

        # estado2
        self.paint.create_line(185, 450, 284, 450, width=3.0, arrow=LAST)
        self.paint.create_oval(285, 495, 375, 405, width=1.5, tag='q1', fill='green')
        self.paint.create_text(330, 450, text='q1', tag='q1', font=('calibri', 20))
        self.paint.create_arc(295, 375, 365.5, 470, star=0, extent=180, style='arc', width=3.0)
        self.paint.create_line(355, 405, 365, 420, widt=3, )
        self.paint.create_line(375, 405, 365, 420, widt=3,)

        # estado3
        self.paint.create_line(375, 450, 474, 450, width=3.0, arrow=LAST)
        self.paint.create_oval(475, 495, 565, 405, width=1.5,tag='q2',fill='green')
        self.paint.create_oval(485, 485, 555, 415, width=1.5)
        self.paint.create_text(520, 450, text='q2', font=('calibri', 20))

        #palabra
        word = self.text_entry.get()
        b = 0
        for i in range(len(word)):

            self.paint.create_rectangle(400+b, 60,430+b,90, fill='white')
            self.paint.create_text(415+b, 75, text=word[i], tag='pile', font=('calibri', 18))


            b = b + 30

    #pila

        p = 0
        for i in range(len(word)):

            self.paint.create_rectangle(650, 480 - p, 700, 450 - p, fill='white')

            p = p + 30

        self.paint.create_text(675, 465, text='#', font=('calibri', 18))


    def run(self):
        self.root.mainloop()

    def on_click_validate(self):
        self.paint.delete('all')
        self.label_transition.set('')
        self.label_state.set('')
        self.init_components()
        state_generator.set_word(self.text_entry.get())
        state_generator.exec()

    def on_click_show_validate(self, mode):
        self.paint.delete('all')
        self.init_components()
        thread_validate = threading.Thread(target=state_generator.run_graphic_validate, args=(mode,))
        thread_validate.start()








window = MainWindow()
window.run()
