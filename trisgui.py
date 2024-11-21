from tris import Giocatore,Tris
from tris2 import GiocatoreComputer
from guizero import App, PushButton

class GamePlay():
    def __init__(self,giocatore1, giocatore2, scacchiera):
        
        self.giocatore1 = giocatore1
        self.giocatore2 = giocatore2
        self.scacchiera = scacchiera
        self.turno = giocatore1

        self.app = App(layout='grid')
        for i in range(3):
            for j in range(3):
                PushButton(self.app,grid=(i,j),command=self.click,args=(i,j))
    def click(self,i,j):
        print(i,j)
        # devo passare il turno al computer

    def gioca(self):
        self.app.display()

if __name__ == '__main__':
    t = Tris()
    g1 = Giocatore('X',t)
    g2 = GiocatoreComputer('O',t)
    game = GamePlay(g1,g2,t)
    game.gioca()
