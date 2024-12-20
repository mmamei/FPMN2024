
import json

def read_loc_history(file):
    data = []

    with open(file) as f:
        h = json.load(f)
    print(len(h['timelineObjects']))
    for x in h['timelineObjects']:
        if 'placeVisit' in x:
            lat = x['placeVisit']['location']['latitudeE7'] / 10000000
            lon = x['placeVisit']['location']['longitudeE7'] / 10000000
            name = x['placeVisit']['location']['name']
            #print(name,lat,lon)
            data.append({'name':name,'lat':lat,'lon':lon})
    return data

def read_template(file='leaf/leaflet.html'):
    with open(file) as f:
        t = f.read()
    return t

def write_file(file, testo):
    with open(file, 'w') as f:
        f.write(testo)


data = read_loc_history('leaf/data.json')
template = read_template()
name, lat, lon = data[0].values()
mappa = template.replace('{{center}}',f'[{lat},{lon}]')

# L.marker([51.5, -0.09]).addTo(map).bindPopup('Ciao.')
placemark = []
for p in data:
    name, lat, lon = p.values()
    name = name.replace('"','\'')
    placemark.append(f'L.marker([{lat}, {lon}]).addTo(map).bindPopup("{name}")')
placemark = '\n'.join(placemark)

mappa = mappa.replace('{{placemark}}',placemark)


write_file('leaf/mappa.html',mappa)



