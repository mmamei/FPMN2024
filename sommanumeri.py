

n = int(input('quanti numeri vuoi sommare?\n'))

'''
somma = 0

x = 0
while x < n:
    a = int(input('inserisci numero '))
    somma += a
    x += 1
print('la somma è',somma)
'''
somma = 0
for i in range(n):
    i = int(input('inserisci numero '))
    somma += i
print('la somma è',somma)
