
from utils import read_template,write_file

class GPSLogger():
    def __init__(self,user):
        self.user = user
        self.log = []
    def run(self):
        for i in range(100):
            lat,lon = self.user.get_pos(i)
            self.log.append((lat,lon))
    def print_html(self):
        t = read_template()
        t = t.replace('{{center}}',f'{list(self.log[0])}')
        
        placemark = []
        for lat,lon in self.log:
            placemark.append(f'L.marker([{lat}, {lon}]).addTo(map)')
        placemark = '\n'.join(placemark)

        t = t.replace('{{placemark}}',placemark)

        write_file(t)

class User():
    def __init__(self,x=10,y=40,vx=0.1,vy=0.1):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def get_pos(self,time):
        return (self.y + time*self.vy, self.x + time*self.vx)

if __name__ == '__main__':
    user = User()
    gps = GPSLogger(user)
    gps.run()
    gps.print_html()