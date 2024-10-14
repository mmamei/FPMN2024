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