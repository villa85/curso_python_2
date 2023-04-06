import json
import requests
from funtions import funciones as f

# f.crear_user("Yuniel", "Villalón", "villa85", "villalon2511@gmail.com")

l = ['https://itunes.apple.com/search?term=System+of+a+Down&limit=5', 'https://itunes.apple.com/search?term=Marilyn+Manson&limit=5','https://itunes.apple.com/search?term=Audioslave&limit=5',
    'https://itunes.apple.com/search?term=LINKIN+PARK&limit=5','https://itunes.apple.com/search?term=Muse&limit=5','https://itunes.apple.com/search?term=Gorillaz&limit=5',
    'https://itunes.apple.com/search?term=Rammstein&limit=5','https://itunes.apple.com/search?term=Avenged+Sevenfold&limit=5','https://itunes.apple.com/search?term=The+Rolling+Stonesd&limit=5',
    'https://itunes.apple.com/search?term=Limp+Bizkit&limit=5']

data = {}
data['s'] = []
x = {}
d= []

for j in l:
    response = requests.get(j)
    json_data = json.loads(response.content)
    data['s'].append(json_data["results"])

m = f.une_listas(data['s'])

for i in m:

    x = {"nombre": i.get('trackName', i["collectionName"]), "cantante": i["artistName"], "genero": i["primaryGenreName"], "album": i["collectionName"], "url": i.get('trackViewUrl', None)}
    d.append(x)

file_name = "data\\data.json"
with open(file_name, 'w') as file:
    json.dump(d, file, indent=4)
