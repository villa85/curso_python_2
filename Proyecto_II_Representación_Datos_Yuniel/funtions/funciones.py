import json
import requests
import pymongo

def conexion_BD():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client

def extrutura_BD():
    client = conexion_BD()
    db = client.MusicPlayList
    l = db.list_collection_names()
    if "usuario" not in l:
        db.create_collection("usuario")
    else:
        print("La colección usuario ya existe")
    if "playlist" not in l:
        db.create_collection("playlist")
    else:
        print("La colección playlist ya existe")
    if "canciones" not in l:
        db.create_collection("canciones")
    else:
        print("La colección canciones ya existe")

def une_listas(l):
    p = 0
    c = len(l)

    while c > 0:
        for i in l:
            if isinstance(i, list):
                p = l.index(i)
                lv = l.pop(p)
                for j in range(len(lv)):
                    l.insert(p, lv[j])
                    p +=1
        c -= 1
    return l

def crear_json_canciones():

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

    m = une_listas(data['s'])

    for i in m:
        x = {"nombre": i.get('trackName', i["collectionName"]), "cantante": i.get('artistName', None),
            "genero": i.get('primaryGenreName', None),
            "album": i.get('collectionName', None), "url": i.get('trackViewUrl', None)}
        d.append(x)

    file_name = "data\\data.json"
    with open(file_name, 'w') as file:
        json.dump(d, file, indent=4)


def crear_user(nombre, apellido, usuario, email):
    client = conexion_BD()
    db = client.MusicPlayList
    cursor = db.usuario.find_one({"username":usuario})
    if cursor is None:
        user = ([{
                "nombre":nombre,
                "apellido":apellido,
                "username":usuario,
                "email":email

            }])
        db.usuario.insert_many(user)
    else:
        print("El usuario ya existe...")

def une_listas(l):
    p = 0
    c = len(l)

    while c > 0:
        for i in l:
            if isinstance(i, list):
                p = l.index(i)
                lv = l.pop(p)
                for j in range(len(lv)):
                    l.insert(p, lv[j])
                    p +=1
        c -= 1
    return l