'''
N = int(input('quanti numeri? '))
a = []
for i in range(N):
    a.append(int(input('inserisci numero ')))
'''
#a = [18,30,18,30]
a = [2,2,1,2,2,3,5,6]
m = sum(a) / len(a)
print('la media è', m)
sd = (sum([(x-m)**2 for x in a])/len(a))**0.5
print('deviaizone standrad', sd)