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

        self.caselle = [[None,None,None],
                        [None,None,None],
                        [None,None,None]]
        for i in range(3):
            for j in range(3):
                self.caselle[i][j] = PushButton(self.app,grid=(i,j),command=self.click,args=(i,j), width=10,height=5, text="")
    


    def cambio_turno(self):
        if self.turno is not None:
            self.turno = self.giocatore2 if self.turno == self.giocatore1 else self.giocatore1
            if type(self.turno) is GiocatoreComputer:
                self.app.after(1000,self.click)

    def fine(self):
        if self.scacchiera.tris(self.turno.id):
            self.app.info("info", f"Giocatore {self.turno.id} ha vinto!")
            self.turno = None
            return True
        if not self.scacchiera.ce_spazio():
            self.app.info("info", "Pareggio")
            self.turno = None
            return True
        return False

    
    def click(self,i=-1,j=-1):

        if type(self.turno) is Giocatore:
            if self.scacchiera.metti_pedina(i,j,self.turno.id):
                self.caselle[i][j].text = self.turno.id
                if not self.fine():
                    self.cambio_turno()
        
        if type(self.turno) is GiocatoreComputer:
            i,j = self.turno.gioca()
            self.caselle[i][j].text = self.turno.id
            if not self.fine():
                self.cambio_turno()


    def gioca(self):
        if type(self.giocatore1) is GiocatoreComputer:
            self.app.after(1000,self.click)
        self.app.display()

if __name__ == '__main__':
    t = Tris()
    g1 = GiocatoreComputer('X',t)
    g2 = GiocatoreComputer('O',t)
    game = GamePlay(g1,g2,t)
    game.gioca()
