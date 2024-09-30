# Inizializza una variabile per rappresentare i numeri da 2 a 100
somma = 0
for numero in range(1, 101):
    # Variabile di controllo per verificare se il numero è primo
    primo = True

    # Controllo se il numero ha divisori (escluso 1 e se stesso)
    for divisore in range(2, numero):
        if numero % divisore == 0:
            primo = False
            break

    # Se il numero è primo, lo stampa
    if primo:
        #print(numero)
        somma += 1

print('i numeri primi tra 1 e 100 sono',somma)

