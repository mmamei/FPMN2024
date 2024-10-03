# Lettura della lista di numeri dall'utente
numeri = []
print("Inserisci i numeri uno per uno. Digita 'fine' per terminare.")

while True:
    numero = input("Inserisci un numero: ")
    if numero == 'fine':
        break
    numeri.append(int(numero))

# Lettura del numero x
x = int(input("Inserisci il numero da cercare: "))

# Variabile per indicare se x è stato trovato
trovato = False

# Ciclo for per scorrere gli elementi della lista
for numero in numeri:
    if numero == x:
        trovato = True
        break  # Esci dal ciclo se il numero è trovato

# Stampa del risultato
if trovato:
    print("trovato")
else:
    print("non trovato")
