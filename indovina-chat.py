import random

# Il computer genera un numero casuale tra 1 e 100
numero_casuale = random.randint(1, 100)
tentativi = 0

print("Benvenuto al gioco 'Indovina il numero'!")
print("Il computer ha generato un numero tra 1 e 100. Hai 10 tentativi per indovinarlo.")

# Loop per 10 tentativi
while tentativi < 10:
    # L'utente inserisce un numero
    print(f"Tentativo {tentativi + 1}: ")
    tentativo_utente = int(input("Inserisci un numero: "))
    
    tentativi += 1
    
    # Controlla se il numero inserito è corretto
    if tentativo_utente == numero_casuale:
        print("Hai indovinato!")
        break
    elif tentativo_utente < numero_casuale:
        print("Troppo piccolo!")
    else:
        print("Troppo grande!")

# Se i 10 tentativi sono stati esauriti senza indovinare
if tentativi == 10 and tentativo_utente != numero_casuale:
    print(f"Hai perso! Il numero corretto era {numero_casuale}.")
