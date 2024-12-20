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


'''messaggi = [
    {'data':'14-10-2024','da':'marco','a':'franco','testo':'ciao!'},
    {'data':'14-10-2024','da':'franco','a':'marco','testo':'ciao! tutto bene?'},
    {'data':'15-10-2024','da':'franco','a':'robby','testo':'ciao!'},
]
'''
messaggi = []
with open('esame1/dati.txt') as f:
    for l in f:
        l = l.strip()
        l = l.split(' ')
        data = l[0].split(':')[1]
        da = l[1].split(':')[1]
        a = l[2].split(':')[1]
        testo = ' '.join(l[3:]) 
        messaggi.append({'data':data,'da':da,'a':a,'testo':testo})

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

print('---------------------------------')

pers2pers = {} # associo ad ogni persona la lista di persone con cui comunica
for p in persone:
    pers2pers[p] = []
for x in messaggi:
    pers2pers[x['da']].append(x['a'])
    pers2pers[x['a']].append(x['da'])

for k,v in pers2pers.items():
    print(k,'comunica con',len(set(v)),'persone')

print('---------------------------------')

pers2x = {}
for p in persone:
    pers2x[p] = {p:0 for p in persone}
for x in messaggi:
    pers2x[x['da']][x['a']] += 1
#print(pers2x)

def print_tab(filep,s='',nspace=10,end=''):
    s = str(s)
    space=''
    for i in range(nspace - len(s)):
        space += ' '
    filep.write(f'{s}{space}{end}')


with open('esame1/tab.txt','w') as f:
    sep = '\t\t'
    print('Da\\a', end=sep)
    print_tab(f,'Da\\a')
    for p in persone:
        print(p,end=sep)
        print_tab(f,p)
    print()
    print_tab(f,end='\n')
    for da in persone:
        print(da,end=sep)
        print_tab(f,da)
        for a in persone:
            print(pers2x[da][a], end=sep)
            print_tab(f,pers2x[da][a])
        print()
        print_tab(f,end='\n')
