import json
import math
import urllib
def parseData():
    with open('chatbot/restaurant_bot/data.json') as f:
        data = json.load(f)
    restaurants = []
    for r in data:
        restaurants.append({
            'name':r['name'],
            'lat':float(r['lat']),
            'lon':float(r['lon']),
            'address':r['display_name']
        })
    return restaurants


def crea_link_google_maps(lat,lon):
    coordinate = f"{lat},{lon}"
    # Crea il link di navigazione
    link = f"https://www.google.com/maps/dir/?api=1&destination={coordinate}"
    return link




def haversine(lat1, lon1, lat2, lon2):
    lon1, lat1, lon2, lat2 = [math.radians(x) for x in [lon1, lat1, lon2, lat2]]
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2.0) ** 2
    c = 2 * math.asin(math.sqrt(a))
    m = 6367 * c * 1000
    return m

def search(restaurants,lat,lon,radius=500):
    result = []
    for r in restaurants:
        if haversine(lat,lon,r['lat'],r['lon']) < radius:
            result.append(r)
    return result

if __name__ == '__main__':
    resturants = parseData()
    result = search(resturants,45.1592619, 10.7880548) 
    for r in result:
        print(r['name'])