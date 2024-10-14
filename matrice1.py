N = 3
'''
m = []
for i in range(N):
    r = []
    m.append(r)
    for j in range(N):
        r.append(int(input('Inserisci numero ')))
'''
m = [[1,2,3],
     [4,5,6],
     [7,8,9]]
for r in m:
    for x in r:
        print(x,end='  ')
    print()    

s = sum([sum(r) for r in m])
print('somma',s)

# riga di somma massima

sr = [sum(r) for r in m]
maxi = sr.index(max(sr))
print('la riga massima ha indice', maxi)

sc = [0 for _ in m[0]]
for r in m:
    #for j in range(len(r)):
    for j,x in enumerate(r):
        sc[j] += x
print(sc)
maxi = sc.index(max(sc))
print('la colonna massima ha indice', maxi)