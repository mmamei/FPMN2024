
from menuoo import Studente, Menu

class StudenteUniv(Studente):
    def __init__(self,nome,matricola):
        super().__init__(nome)
        self.matricola = matricola
    1
    def __str__(self):
        return f'{self.matricola} {super()}'
    
    def calcola_media():
        return super().calcola_media() * 110 / 30


class MenuUniv(Menu):
    def esegui(self):
        while(True):
            self.stampa()
            op = input('Inserisci operazione ')
            if op == '1':
                nome = input('Inserisci nome: ')
                matr = input('Inserisci matr: ')
                s = StudenteUniv(nome,matr)
                self.aula.aggiungi(s)
            if op == '2':
                nome = input('Inserisci nome: ')
                s = self.aula.cerca(nome)
                v = int(input('Inserisci voto: '))
                s.aggiungi_voto(v)
            if op == '3':
                for s in self.aula.lista():
                    print(s)
            if op == '4':
                nome = input('Inserisci nome: ')
                s = self.aula.cerca(nome)
                print(s.calcola_media())
            if op == '5':
                break


m = MenuUniv()
m.esegui()
    
        

