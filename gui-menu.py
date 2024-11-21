from guizero import App, Box, PushButton, TextBox, Text
from menuoo import Studente, Aula

class Menu():
    def __init__(self):
        self.aula = Aula()
        self.app = App('menu',layout='grid')
        PushButton(self.app,text='inserisci studente', command=self.op1, grid=(0,0))
        PushButton(self.app,text='aggiungi voto', command=self.op2, grid=(0,1))
        PushButton(self.app,text='stampa tutto', command=self.op3, grid=(0,2))
        PushButton(self.app,text='calcola media', command=self.op4, grid=(0,3))

    def op1(self):
        def insert():
            s = Studente(nome.value)
            self.aula.aggiungi(s)
            box.destroy()
        box = Box(self.app, grid=(1,0))
        nome = TextBox(box)
        p1 = PushButton(box,command=insert)
    def op2(self):
        def close():
            p1.destroy()
        p1 = PushButton(self.app,grid=(1,0),command=close)
    def op3(self):
            box = Box(self.app, grid=(1,0), width=200, height=200)
            t = "\n".join([str(s) for s in self.aula.lista()])
            print(t)
            Text(box,text=t)
            PushButton(box,command=lambda : box.destroy())
    def op4(self):
        ...

    def esegui(self):
        self.app.display()


if __name__ == '__main__':
    m = Menu()
    m.esegui()