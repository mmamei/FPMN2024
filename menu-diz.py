'''
Prompt:

Realizzare un programma in python che presenti all’utente il seguente menu:

1.Inserisci Studente
2.Inserisci media voti studente
3. Stampa tutto
4.Calcola media voti della classe
5.Esci

Gli studenti sono rappresentati da una lista di stringhe.
Le medie degli studenti sono rappresentati da una lista di float.
Il menu continua a chiedere operazioni, tramite commando input, all’utente finché l’utente non esegue l’operazione “5”.
L’operazione 1 permette di inserire il nome e cognome dello studente.
L’operazione 2 chiede il nome e il cognome di uno studente, quindi chiede il valore della media di quello studente.
L’operazione 3 stampa tutti gli studenti e la loro media.
L’operazione 4 stampa la media voti della classe.

Non usare le funzioni, usa solo le due liste indicate

'''


# Liste per memorizzare gli studenti e le loro medie
studenti_medie = {}

while True:
    # Mostra il menu
    print("\nMenu:")
    print("1. Inserisci Studente")
    print("2. Inserisci media voti studente")
    print("3. Stampa tutto")
    print("4. Calcola media voti della classe")
    print("5. Esci")
    
    # Leggi la scelta dell'utente
    scelta = input("Scegli un'opzione (1-5): ")
    
    # Opzione 1: Inserisci studente
    if scelta == '1':
        nome = input("Inserisci nome e cognome dello studente: ")
        studenti_medie[nome] = None
        
    # Opzione 2: Inserisci media voti studente
    elif scelta == '2':
        nome = input("Inserisci nome e cognome dello studente per aggiungere la media: ")
        if nome in studenti_medie:
            media = float(input("Inserisci la media voti"))
            studenti_medie[nome] = media
        else:
            print("Studente non trovato!")
    
    # Opzione 3: Stampa tutto
    elif scelta == '3':
        print("\nElenco studenti e medie:")
        for n, m in studenti_medie.items():
            #media = medie[i] if medie[i] is not None else "Non assegnata"
            
            if m is not None:
                media = m
            else:
                media = "Non assegnata"

            print(f"{n} - Media: {media}")
    
    # Opzione 4: Calcola media voti della classe
    elif scelta == '4':
        mediev = [m for m in studenti_medie.values() if m is not None]
        if len(mediev) > 0:
            media_classe = sum(mediev) / len(mediev)
            print(f"La media della classe è: {media_classe:.2f}")
        else:
            print("Non ci sono medie disponibili per calcolare la media della classe.")
    
    # Opzione 5: Esci
    elif scelta == '5':
        print("Uscita dal programma.")
        break
    
    # Opzione non valida
    else:
        print("Scelta non valida! Riprova.")
