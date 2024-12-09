from datetime import datetime, timedelta
s = datetime.strptime('19092022 08:00:00', '%d%m%Y %H:%M:%S')
e = datetime.strptime('19092022 18:00:00', '%d%m%Y %H:%M:%S')
d = datetime.strptime('19092022 10:00:00', '%d%m%Y %H:%M:%S')

if s < d < e:
    print('ciao')

s = datetime.strftime(s,'%d %B %Y')
print(s)

print(d.weekday())

print(d + timedelta(days=1))