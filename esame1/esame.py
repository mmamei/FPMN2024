'''
Data una lista di messaggi rappresentati da un una lista di dizionari del tipo:
{'data':'14-10-2024','da':'marco','a':'franco','testo':'ciao!'}
Creare un programma python, senza usare le funzioni, che esegua i seguenti punti:
1. Trovare la persona che scrive più messaggi
2. Per ogni persona, stamapre il numero di persone con cui comunica
3. Scrivere la tabella che riassume il numero di messaggi inviati da una persona all'altra

Da\A    Marco   Matteo  Luca
Marco   0       1       2
Matteo  2       0       1       
Luca    3       1       0
'''



messaggi = [
    {'data':'14-10-2024','da':'marco','a':'franco','testo':'ciao!'},
    {'data':'14-10-2024','da':'franco','a':'marco','testo':'ciao! tutto bene?'},
    {'data':'15-10-2024','da':'franco','a':'robby','testo':'ciao!'},
]

# trovare la persona che scrive più messaggi
'''
persN = {
    'marco':1,
    'franco':2,
    'robby':0
}
'''
persN = {}
for x in messaggi:
    mittente = x['da']
    print(mittente)
    if mittente in persN:
        persN[mittente] += 1
    else:
        persN[mittente] = 1 
print(persN)