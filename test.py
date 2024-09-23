
op = int(input('inserisci numero '))
# stampa ok se op è > 3 e < 10

if 3 < op < 10:
    print('ok')

if op > 3:
    if op < 10:
        print('ok')
    else:
        print('non ok')
else:
    print('non ok')