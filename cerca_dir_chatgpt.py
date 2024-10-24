'''
Scrivi un progrmma python che legge una stringa da input 
e cerca in tutti i file presenti in una cartella e nelle 
sue sottocartelle tutti i file che contengono la stringa inserita
Non usare le funzioni e non usare funzioni ricorsive
'''

import os

# Legge la stringa da cercare dall'utente
stringa_cercata = input("Inserisci la stringa da cercare: ")

# Legge il percorso della cartella di base dall'utente
percorso_base = input("Inserisci il percorso della cartella: ")

# Inizializza una lista per memorizzare i file trovati
file_trovati = []

# Stack per simulare la ricorsione
stack = [percorso_base]

# Ciclo principale per visitare tutti i file e cartelle
while len(stack) > 0:
    # Estrae l'elemento in cima allo stack
    percorso_corrente = stack.pop()

    # Se l'elemento corrente è una directory, aggiungi i suoi contenuti allo stack
    if os.path.isdir(percorso_corrente):
        elementi = os.listdir(percorso_corrente)
        for elemento in elementi:
            stack.append(os.path.join(percorso_corrente, elemento))
    # Se l'elemento corrente è un file, controlla se contiene la stringa
    elif os.path.isfile(percorso_corrente):
        # Prova ad aprire il file e cercare la stringa
        try:
            with open(percorso_corrente, 'r', encoding='utf-8') as file:
                contenuto = file.read()
                if stringa_cercata in contenuto:
                    file_trovati.append(percorso_corrente)
        except:
            # Se il file non può essere letto, continua con il prossimo
            continue

# Stampa i file trovati
if len(file_trovati) > 0:
    print("File trovati che contengono la stringa:")
    for file in file_trovati:
        print(file)
else:
    print("Nessun file trovato che contenga la stringa.")
