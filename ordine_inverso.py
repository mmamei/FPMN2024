# Scrivere un programma che legga N numberi e li stampi in ordine inverso.
# Ad esempio, se N=5 e i numeri letti sono 1, 2, 3, 4, 5, il programma
# deve stampare 5, 4, 3, 2, 1.

N = int(input('inserisci quanti numeri '))

a = []

for i in range(N):
    x = int(input('inserisci numero '))
    a.append(x)


for i in range(N):
    print(a[-1-i])

