from tris import Giocatore,Tris,GamePlay
import random

class GiocatoreComputer(Giocatore):
    def gioca(self):
        """
        La funzione genera una mossa casuale per il computer e la invia alla scacchiera.
        Il computer continua a generare mosse finché non trova una casella vuota.
        """
        while True:
            # Genera due numeri casuali nell'intervallo [0, 2]
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            
            # Verifica che la mossa sia valida (la casella deve essere vuota)
            if self.scacchiera.metti_pedina(i, j, self.id):
                #print(f"Il computer ({self.id}) ha messo la pedina in ({i},{j}).")
                return i,j  # La mossa è stata eseguita, esce dal ciclo

if __name__ == '__main__':
    t = Tris()
    g1 = Giocatore('X',t)
    g2 = GiocatoreComputer('O',t)
    game = GamePlay(g1,g2,t)
    game.gioca()
