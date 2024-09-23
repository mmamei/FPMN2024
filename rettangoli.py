xa = int(input('xa ')) # rettangolo 1, punto basso sinistra
ya = int(input('ya '))

xb = int(input('xb ')) # rettangolo 1, punto alto destra
yb = int(input('yb '))

xc = int(input('xc ')) # rettangolo 2, punto basso sinistra
yc = int(input('yc '))

xd = int(input('xd ')) # rettangolo 2, punto alto destra
yd = int(input('yd '))

if xa == xc and ya == yc and xb == xd and yb == yd:
    print('conicidenti')
elif xc > xb or xa > xd or ya > yd or yc > yb:
    print('disgiunti')
else:
    print('sovrapposti')


