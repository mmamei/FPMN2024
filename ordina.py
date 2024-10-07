# [2,3,1]
# cerco l'elemento più piccolo = 1
# scambio l'elemento più piccolo e lo metto all'inizio
# [1,3,2]
# [1,    3,2]
# [1,    2,3]


a = [2,3,1]
imin = a.index(min(a))
print(imin)
#tmp = a[0]
#a[0] = a[imin] 
#a[imin] = tmp

a[0],a[imin] = a[imin], a[0]


print(a)