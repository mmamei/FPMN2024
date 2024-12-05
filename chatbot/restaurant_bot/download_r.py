from requests import get
import json
url = 'https://nominatim.openstreetmap.org/search.php?q=restaurants&viewbox=10.784,45.158,10.799,45.165&bounded=1&limit=1000&format=jsonv2'
headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'marco.mamei@gmail.com'
}
r = get(url, headers=headers)

with open('chatbot/restaurant_bot/data.json','w') as f:
    json.dump(r.json(),f)