class Studente():
    def __init__(self,nome):
        self.nome = nome
        self.voti = []
    def aggiungi_voto(self,v):
        self.voti.append(v)
    def stampa(self):
        return f'{self.nome} {self.voti}'
    def calcola_media(self):
        return sum(self.voti) / len(self.voti)

class Aula():
    def __init__(self):
        self.__studenti = {}
    def aggiungi(self,s):
        self.__studenti[s.nome] = s
    def cerca(self,nome):
        if nome in self.__studenti:
            return self.__studenti[nome]
        return None
    def lista(self):
        return self.__studenti.values()

class Menu():
    def __init__(self):
        self.aula = Aula()
    def stampa(self):
        print("1. Inserisci studente")
        print("2. Inserisci voto studente")
        print("3. Stampa tutto")
        print("4. Calcola media voti studente")
        print("5. Esci")
    def esegui(self):
        while(True):
            self.stampa()
            op = input('Inserisci operazione ')
            if op == '1':
                nome = input('Inserisci nome: ')
                s = Studente(nome)
                self.aula.aggiungi(s)
            if op == '2':
                nome = input('Inserisci nome: ')
                s = self.aula.cerca(nome)
                v = int(input('Inserisci voto: '))
                s.aggiungi_voto(v)
            if op == '3':
                for s in self.aula.lista():
                    print(s.stampa())
            if op == '4':
                nome = input('Inserisci nome: ')
                s = self.aula.cerca(nome)
                print(s.calcola_media())
            if op == '5':
                break


m = Menu()
m.esegui()