# Lista dei messaggi
lista_messaggi = [
    {'data': '14-10-2024', 'da': 'Marco', 'a': 'Franco', 'testo': 'Ciao!'},
    {'data': '14-10-2024', 'da': 'Marco', 'a': 'Matteo', 'testo': 'Come stai?'},
    {'data': '15-10-2024', 'da': 'Luca', 'a': 'Marco', 'testo': 'Ciao, tutto bene?'},
    {'data': '16-10-2024', 'da': 'Matteo', 'a': 'Luca', 'testo': 'Tutto ok!'},
    {'data': '16-10-2024', 'da': 'Marco', 'a': 'Luca', 'testo': 'Ciao di nuovo!'},
    {'data': '17-10-2024', 'da': 'Luca', 'a': 'Marco', 'testo': 'Come va?'},
    {'data': '17-10-2024', 'da': 'Marco', 'a': 'Luca', 'testo': 'Bene, grazie!'}
]

# 1. Trovare la persona che scrive più messaggi
conteggio_messaggi = {}
for messaggio in lista_messaggi:
    mittente = messaggio['da']
    if mittente in conteggio_messaggi:
        conteggio_messaggi[mittente] += 1
    else:
        conteggio_messaggi[mittente] = 1

# Trovare la persona con il massimo numero di messaggi
massimo_messaggi = 0
persona_con_piu_messaggi = None
for persona in conteggio_messaggi.keys():
    if conteggio_messaggi[persona] > massimo_messaggi:
        massimo_messaggi = conteggio_messaggi[persona]
        persona_con_piu_messaggi = persona

print("La persona che scrive più messaggi è:", persona_con_piu_messaggi)

# 2. Per ogni persona, stampare il numero di persone con cui comunica
comunicazioni = {}
for messaggio in lista_messaggi:
    mittente = messaggio['da']
    destinatario = messaggio['a']
    if mittente not in comunicazioni:
        comunicazioni[mittente] = set()
    comunicazioni[mittente].add(destinatario)

print("\nNumero di persone con cui comunica ogni persona:")
for persona in comunicazioni:
    print(persona, "comunica con", len(comunicazioni[persona]), "persone")

# 3. Creare la tabella del numero di messaggi inviati da una persona all'altra
persone = set()
for messaggio in lista_messaggi:
    persone.add(messaggio['da'])
    persone.add(messaggio['a'])

persone = sorted(list(persone)) # Ordinare le persone in ordine alfabetico

# Inizializzare la matrice dei messaggi
tabella_messaggi = {}
for mittente in persone:
    tabella_messaggi[mittente] = {}
    for destinatario in persone:
        tabella_messaggi[mittente][destinatario] = 0

# Popolare la matrice con i conteggi dei messaggi
for messaggio in lista_messaggi:
    mittente = messaggio['da']
    destinatario = messaggio['a']
    tabella_messaggi[mittente][destinatario] += 1

# Stampare la tabella
print("\nTabella dei messaggi inviati:")
print("Da/A", "\t", "\t".join(persone))
for mittente in persone:
    righe = [str(tabella_messaggi[mittente][destinatario]) for destinatario in persone]
    print(mittente, "\t", "\t".join(righe))
