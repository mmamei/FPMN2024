from datetime import datetime
s = datetime.strptime('09-19-2022 08:00:00', '%m-%d-%Y %H:%M:%S')
e = datetime.strptime('09-19-2022 18:00:00', '%m-%d-%Y %H:%M:%S')
d = datetime.strptime('09-19-2022 10:00:00', '%m-%d-%Y %H:%M:%S')
if s < d < e:
    print('ciao')