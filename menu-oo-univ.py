
from menuoo import Studente, Menu

class StudenteUniv(Studente):
    def __init__(self,nome,matricola):
        super().__init__(nome)
        self.matricola = matricola
    1
    def __str__(self):
        return f'{self.matricola} {super().__str__()}'
    def calcola_media(self):
        return super().calcola_media() * 110 / 30

class MenuUniv(Menu):
    def menu_crea_studente(self):
        nome = input('Inserisci nome: ')
        matr = input('Inserisci matr: ')
        s = StudenteUniv(nome,matr)
        self.aula.aggiungi(s)



if __name__ == '__main__':
    m = MenuUniv()
    m.esegui()
    
        

