q1 = input('is the color red? (y/n)\n')
if q1 == 'y':
    if input('is the model newer than 2010? (y/n)\n') == 'y':
        print('buy!')
    else:
        if input('is mileage fewer than 50000 km? (y/n)\n') == 'y':
            print('buy!')
        else:
            print('don\'t buy!')
else:
    if input('is the color yellow? (y/n)\n') == 'y':
        if input('is the car a Ferrari? (y/n)\n') == 'y':
            print('buy!')
        else:
            print('don\'t buy!')
    else:
        print('don\'t buy!')