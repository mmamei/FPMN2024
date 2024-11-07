
'''
scrivi una classe in python per rappresentare la scacchiera del gioco del tris.
La classe deve fornire le seguenti funzioni:
- metti_pedina(i,j,id) riceve le coordinate dove mettere la pedina: i,j e l'id del giocatore/tipo di pedina che tipicamente sarà 'X' o 'O'. la funzione ritorna True se la mossa è valida, False altrimenti
- tris(id) riceve l'id di un giocatore e rispode True o False a seconda che sia verifcato un tris
- ce_spazio() dice se la scacchiera è piena e quindi non si può più goicare.
Questa classe non deve stampare niente, gestisce solo lo stato della scacchiera e le funzioni corrispondenti

scrivi la classe in python per rappresentare un giocatore umano del gioco del tris.
La classe ha un costruttore che imposta l'id del goicaotre che tipicamente sarà 'X' o 'O' e lo mette in collegamento con un oggetto della classe schacchiera.
La classe giocatore ha una funzione gioca() per chiedere tramite input e trasmette la mossa alla scacchiera

Scrivi la stessa cosa per rappresentare il giocatore computer. il computer è simile al giocaotre umano ma genera delle mosse casuali generando i nell'intervallo [0,2] e j nell'intervallo [0,2]

Scrivi la classe gameplay the viene inizializzata con i giocatori che si vuole far giocare e la scacchiera.
La classe gameplay si occupa della visualizzazione trmaite print
e del ciclo del gioco
'''

class Tris:
    def __init__(self):
        # La scacchiera è rappresentata come una lista di liste (matrice 3x3)
        # Ogni cella può essere 'X', 'O', oppure ' ' (spazio vuoto)
        self.scacchiera = [[' ' for _ in range(3)] for _ in range(3)]

    def metti_pedina(self, i, j, id):
        """
        Metti una pedina sulla scacchiera nella posizione (i, j)
        id: 'X' o 'O' per il tipo di pedina
        Ritorna True se la mossa è valida, False altrimenti.
        """
        if 0 <= i < 3 and 0 <= j < 3 and self.scacchiera[i][j] == ' ':
            self.scacchiera[i][j] = id
            return True
        return False

    def tris(self, id):
        """
        Controlla se il giocatore con l'id ('X' o 'O') ha fatto un tris
        Ritorna True se il giocatore ha fatto tris, False altrimenti.
        """
        # Controlliamo tutte le righe, colonne e le due diagonali
        for i in range(3):
            # Controlla righe
            if self.scacchiera[i][0] == self.scacchiera[i][1] == self.scacchiera[i][2] == id:
                return True
            # Controlla colonne
            if self.scacchiera[0][i] == self.scacchiera[1][i] == self.scacchiera[2][i] == id:
                return True

        # Controlla le due diagonali
        if self.scacchiera[0][0] == self.scacchiera[1][1] == self.scacchiera[2][2] == id:
            return True
        if self.scacchiera[0][2] == self.scacchiera[1][1] == self.scacchiera[2][0] == id:
            return True

        return False

    def ce_spazio(self):
        """
        Controlla se ci sono ancora spazi vuoti sulla scacchiera.
        Ritorna True se ci sono spazi vuoti, False se la scacchiera è piena.
        """
        for i in range(3):
            for j in range(3):
                if self.scacchiera[i][j] == ' ':
                    return True
        return False



class Giocatore:
    def __init__(self, id, scacchiera):
        """
        Costruttore che imposta l'id del giocatore ('X' o 'O') 
        e lo collega ad un oggetto della classe Tris (scacchiera).
        """
        self.id = id
        self.scacchiera = scacchiera

    def gioca(self):
        """
        La funzione chiede al giocatore umano di inserire una mossa
        e la invia alla scacchiera, assicurandosi che la mossa sia valida.
        """
        while True:
            try:
                # Chiede le coordinate della mossa (i, j)
                i, j = map(int, input(f"Giocatore {self.id}, inserisci la mossa (riga,colonna): ").split(','))
                if self.scacchiera.metti_pedina(i, j, self.id):
                    return
                else:
                    print('mossa non valida')
            except ValueError:
                print("Input non valido. Inserisci le coordinate nel formato 'riga,colonna' (es. 0,1).")


import random

class GiocatoreComputer:
    def __init__(self, id, scacchiera):
        """
        Costruttore che imposta l'id del giocatore ('X' o 'O') 
        e lo collega ad un oggetto della classe Tris (scacchiera).
        """
        self.id = id
        self.scacchiera = scacchiera

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
                return  # La mossa è stata eseguita, esce dal ciclo


class GamePlay:
    def __init__(self, giocatore1, giocatore2, scacchiera):
        """
        Inizializza la classe GamePlay con i due giocatori e la scacchiera.
        """
        self.giocatore1 = giocatore1
        self.giocatore2 = giocatore2
        self.scacchiera = scacchiera
        self.turno = giocatore1  # Il primo turno sarà per giocatore1

    def stampa_scacchiera(self):
        """
        Stampa la scacchiera attuale del gioco.
        """
        print("\nScacchiera:")
        for i in range(3):
            print(" | ".join(self.scacchiera.scacchiera[i]))
            if i < 2:
                print("-" * 10)
        print()

    def gioca(self):
        """
        Gestisce il ciclo del gioco: alterna i turni, verifica la vittoria o il pareggio.
        """
        while True:
            # Stampa la scacchiera prima di ogni mossa
            self.stampa_scacchiera()

            # Il giocatore corrente fa la mossa
            self.turno.gioca()

            # Verifica se il giocatore corrente ha vinto
            if self.scacchiera.tris(self.turno.id):
                self.stampa_scacchiera()
                print(f"Il giocatore {self.turno.id} ha vinto!")
                break

            # Verifica se la scacchiera è piena (pareggio)
            if not self.scacchiera.ce_spazio():
                self.stampa_scacchiera()
                print("La partita è finita in pareggio!")
                break

            # Passa al prossimo giocatore
            self.turno = self.giocatore1 if self.turno == self.giocatore2 else self.giocatore2



if __name__ == '__main__':
    t = Tris()
    g1 = GiocatoreComputer('X',t)
    g2 = GiocatoreComputer('O',t)
    gameplay = GamePlay(g1,g2,t)
    gameplay.gioca()