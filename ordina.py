# [2,3,1]
# cerco l'elemento più piccolo = 1
# scambio l'elemento più piccolo e lo metto all'inizio
# [1,3,2]
# [1,    3,2]
# [1,    2,3]


lista = [2,3,1,7,1,1,3]
print(lista)
for start in range(len(lista)):
    a = lista[start:]
    imin = a.index(min(a))
    print(imin)
    #tmp = a[0]
    #a[0] = a[imin] 
    #a[imin] = tmp
    lista[0+start],lista[imin+start] = (lista[imin+start], lista[0+start])


    print(lista)