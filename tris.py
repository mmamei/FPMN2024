
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