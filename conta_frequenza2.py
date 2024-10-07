# data una lista
a = [1,2,3,4,4,4,3,2,7]
# voglio stampare:
# 1 --> non duplicato
# 2 --> duplicato, 2 volte
# 3 --> duplicato, 2 volte
# ...
# per farlo:
# prima trovo gli elementi unici
# u = [1,2,3,4,7]
# inserisco in u un elemento di a se non è già contenuto in u
# poi per ogni elemento unico vedo quante volte compare in a
u = set(a)
for x in u:
    c = a.count(x)
    if c == 1:
        print(x,'non è duplicato')
    if c > 1:
        print(x,'è duplicato e compare',c,'volte')
