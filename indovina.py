import random
import math
'''
0 ----> 100
1 ----> 100/2
2 ----> 100/4
n ---> 100/2**n

100/2^n = 1
n = log2(100) --> 6

'''

'''
crea in python senza usare le funzioni il gioco indovina numero
il computer genera un numero casuale tra 1 e 100
il goicatore tramite input inserisce tentativi
il computer risponde troppo grande o troppo piccolo o hai indovinato a
seconda dei casi
Dopo 10 mosse, se non è stato indovinato, stampa hai perso
'''


x = random.randint(1,100)
#print(x)
vinto = False
for i in range(int(math.log2(100))):
    y = int(input('inserisci un numero '))
    if x < y:
        print('troppo grande')
    elif x > y:
        print('troppo piccolo')
    else:
        print('hai indovinato')
        vinto = True
        break
else:
    print('hai perso')