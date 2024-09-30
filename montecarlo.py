# voglio generare N = 100000 punti casuali con
# x = [-1,1]
# y = [-1,1]
# conto quanti di questi punti stanno nel cerchio di 
# raggio 1, cioè la distanza del punto dal centro è <= 1
# calcolo pi = 4 * numero punti dentro cerchio / N

import random
N = 100000000
NC = 0
for i in range(N):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2+y**2)**0.5 < 1:
        NC += 1
print(4*NC/N)