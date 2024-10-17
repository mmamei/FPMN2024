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

# trovate tutte le persone
persone = []
for x in messaggi:
    persone.append(x['da'])
    persone.append(x['a'])
persone = set(persone)

# inizializzo persN a zero
persN = {}
for p in persone:
    persN[p] = 0

# per ogni persona conto i messaggi
for x in messaggi:
    persN[x['da']] += 1

print(persN)

persMax = sorted(persN.items(), key=lambda kv:kv[1])[-1][0]
print(persMax)