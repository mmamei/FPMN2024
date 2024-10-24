import os
dir  = 'test'
cerca = input('Inserisci stringa ')
for f in os.listdir(dir):
    if os.path.isfile(f'{dir}/{f}'):
        with open(f'{dir}/{f}') as fp:
            c = fp.read()
            if cerca.lower() in c.lower():
                print(f)
    else:
        dir2 = f'{dir}/{f}'
        # copio il pezzo di codice precedenet

