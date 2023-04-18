import os
import json
import requests
import pymongo
import random
from tabulate import tabulate

def conexion_BD():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client

def extrutura_BD():
    client = conexion_BD()
    db = client.MusicPlayList
    l = db.list_collection_names()
    if "usuario" not in l:
        db.create_collection("usuario")
        print("Colección usuario creado con exito")
    else:
        print("La colección usuario ya existe")
    if "playlist" not in l:
        db.create_collection("playlist")
        print("Colección usuario creado con exito")
    else:
        print("La colección playlist ya existe")
    if "canciones" not in l:
        db.create_collection("canciones")
        print("Colección usuario creado con exito")
    else:
        print("La colección canciones ya existe")
        print("\n")

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

    l = ['https://itunes.apple.com/search?term=System+of+a+Down&limit=5',
        'https://itunes.apple.com/search?term=Marilyn+Manson&limit=5',
        'https://itunes.apple.com/search?term=Audioslave&limit=5',
        'https://itunes.apple.com/search?term=LINKIN+PARK&limit=5',
        'https://itunes.apple.com/search?term=Muse&limit=5',
        'https://itunes.apple.com/search?term=Gorillaz&limit=5',
        'https://itunes.apple.com/search?term=Rammstein&limit=5',
        'https://itunes.apple.com/search?term=Avenged+Sevenfold&limit=5',
        'https://itunes.apple.com/search?term=The+Rolling+Stonesd&limit=5',
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
        x = {
            "nombre": i.get('trackName', i["collectionName"]),
            "cantante": i.get('artistName', None),
            "genero": i.get('primaryGenreName', None),
            "album": i.get('collectionName', None),
            "url": i.get('trackViewUrl', None)
            }
        d.append(x)

    file_name = "data.json"
    with open(file_name, 'w') as file:
        json.dump(d, file, indent=4)
    print(f'Archivo "{file_name}" creado con exito en el directorio de trabajo: {os.getcwd()}')
    print("\n")

def lista_canciones(): # Una lista de todas las canciones (_ids)
    l = []
    client = conexion_BD()
    db = client.MusicPlayList
    cursor = db.canciones.find()
    for i in cursor:
        l.append(i["_id"])
        # l.append(str(i["_id"]))
    return l

def list_random_music(lista, cant = 20): # Una lista de canciones aletorias con cantidad predefinida (_ids)
    l = random.SystemRandom().sample(lista, cant)
    return l

def mostrar_sugerencias(lista): # Una lista de canciones aletorias con (nombre, grupo, id)
    l = []
    client = conexion_BD()
    db = client.MusicPlayList
    for i in lista:
        cursor = db.canciones.find({"_id": i})
        if cursor:
            for j in cursor:
                t = j["nombre"], j["cantante"], i
                l.append(t)
    return l



p = lista_canciones()
d = list_random_music(p)
m = mostrar_sugerencias(d)

e = list(enumerate(m, start=1))
# print(tabulate(e, headers=['Número', 'Canción / Banda Rock / Id']))

# print(len(m))

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

class PlayList:

    def __init__(self, nombre, usuario, canciones):
        self.name = nombre
        self.user = usuario
        self.songs = canciones

    def crearplaylist (self):
        client = conexion_BD()
        db = client.MusicPlayList
        playlist = ([{
            "nombre":self.name,
            "username":self.user,
            "canciones":[self.songs]
            }])
        db.playlist.insert_many(playlist)

def if_integer(string):

    if string[0] == ('+'):
        return string[1:].isdigit()

    else:
        return string.isdigit()

# string1 = '132'
# string2 = '-132'
# string3 = 'abc'

# print(if_integer(string1))
# print(if_integer(string2))
# print(if_integer(string3))