dati = '''Marco,30
Matteo,28
Roberta,24
Roberta,28
Marco,28'''

d = {}
for l in dati.splitlines():
    n,v = l.split(',')
    if n not in d:
        d[n] = []
    d[n].append(int(v))
print(d)

for k,v in d.items():
    print(k, sum(v)/len(v))
