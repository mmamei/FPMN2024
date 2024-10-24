'''
Prompt:

Realizzare un programma in python che presenti all'utente il seguente menu:

1.Inserisci Studente
2.Inserisci voto studente
3.Stampa tutto
4.Calcola media voti della studnete
5.Esci

La classe è un dizionaroi che associa al nome di uno studente, la sua lista dei voti
Il menu continua a chiedere operazioni, tramite commando input, all'utente finché l'utente non esegue l’operazione “5”.
L'operazione 1 permette di inserire il nome e cognome dello studente.
L'operazione 2 chiede il nome e il cognome di uno studente, quindi chiede il valore della media di quello studente.
L'operazione 3 stampa tutti gli studenti e la loro media.
L'operazione 4 stampa la media voti della classe.

Non usare le funzioni, usa solo le due liste indicate

'''

import json


# Liste per memorizzare gli studenti e i loro voti
studenti_voti = {}
try:
    with open('menu-diz-list-save.json') as f:
        studenti_voti = json.load(f)
except:
    pass



while True:
    # Mostra il menu
    print("\nMenu:")
    print("1. Inserisci Studente")
    print("2. Inserisci un voto a uno studente")
    print("3. Stampa tutto")
    print("4. Calcola media voti di uno studnete")
    print("5. Esci")
    
    # Leggi la scelta dell'utente
    scelta = input("Scegli un'opzione (1-5): ")
    
    # Opzione 1: Inserisci studente
    if scelta == '1':
        nome = input("Inserisci nome e cognome dello studente: ")
        studenti_voti[nome] = []
        
    # Opzione 2: Inserisci voti studente
    elif scelta == '2':
        nome = input("Inserisci nome e cognome dello studente per aggiungere un voto: ")
        if nome in studenti_voti:
            voto = float(input("Inserisci voto"))
            studenti_voti[nome].append(voto)
        else:
            print("Studente non trovato!")
    
    # Opzione 3: Stampa tutto
    elif scelta == '3':
        print("\nElenco studenti e voti:")
        for n, lv in studenti_voti.items():
            #media = medie[i] if medie[i] is not None else "Non assegnata"
            print(n,'-->',lv)
    
    # Opzione 4: Calcola media voti della studnete
    elif scelta == '4':
        nome = input("Inserisci nome e cognome dello studente per calcolare la media: ")
        if nome in studenti_voti:
            lv = studenti_voti[nome]
            if len(lv) > 0:
                print(nome,sum(lv)/len(lv))
            else:
                print(nome,'non ha voti assegnati')
    # Opzione 5: Esci
    elif scelta == '5':
        print("Uscita dal programma.")
        with open('menu-diz-list-save.json','w') as f:
            json.dump(studenti_voti,f)
        break
    
    # Opzione non valida
    else:
        print("Scelta non valida! Riprova.")
