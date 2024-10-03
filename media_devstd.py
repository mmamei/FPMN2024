'''
N = int(input('quanti numeri? '))
a = []
for i in range(N):
    a.append(int(input('inserisci numero ')))
'''
#a = [18,30,18,30]
a = [2]
m = 0
for i in range(len(a)):
    m += a[i]
m = m / len(a)
print('la media è', m)

sd = 0
for i in range(len(a)):
    sd += (a[i]-m)**2
sd = (sd/len(a))**0.5
print('deviaizone standrad', sd)