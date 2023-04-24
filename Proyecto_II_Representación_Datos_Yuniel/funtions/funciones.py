import os
import json
import requests
import pymongo
import random
import re
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
        print("La Base de Datos MusicPlayList ha sido creada exitosamente")
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

def if_integer(string):
        return string.isdigit()


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

def lista_canciones(cant = 20): # Una lista de 20 las canciones aleatorias (_ids)
    l = []
    n = []
    client = conexion_BD()
    db = client.MusicPlayList
    cursor = db.canciones.find()
    for i in cursor:
        l.append(i["_id"])
    l = random.SystemRandom().sample(l, cant)
    return l

def mostrar_sugerencias(lista): # Una lista de canciones aletorias con (nombre, grupo, id)
    l = []
    client = conexion_BD()
    db = client.MusicPlayList
    for i in lista:
        cursor = db.canciones.find({"_id": i})
        if cursor:
            for j in cursor:
                t = j["nombre"], j["cantante"]
                l.append(t)
    return l

def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def valida_user():
    l = []
    name = ""
    last_name = ""
    user_name = ""
    email = ""
    while not name.isalpha() or not name:
        print("Por favor introduzca un nombre válido (Solo Letras)")
        name = input("Introduzca nombre: ")
    else:
        n = name.capitalize()
        l.append(n)
    while not last_name.isalpha() or not last_name:
        print("Por favor introduzca un apellido válido (Solo Letras)")
        last_name = input("Introduzca apellido: ")
    else:
        a = last_name.capitalize()
        l.append(a)
    while not user_name.isalnum() or not user_name:
        print("Por favor username válido (Sin signos de puntuación)")
        user_name = input("Introduzca username: ")
    else:
        l.append(valida_user_name(user_name))
    while not es_correo_valido(email) or not email:
        print("Por favor introduzca un correo válido")
        email = input("Introduzca dirección de correo: ")
    else:
        l.append(email)
    return l

def valida_user_name(usuario, play_list = False):
    client = conexion_BD()
    db = client.MusicPlayList
    cursor = db.usuario.find_one({"username":usuario})
    user_name = ""
    if cursor is None and play_list == False:
        return usuario
    if cursor and play_list == False:
        print("\n")
        print(f"Ya existe un usuario ({usuario}) ")
        print("Por favor inténte con otro username")
        while not user_name.isalnum() or not user_name:
            print("Por favor username válido (Sin signos de puntuación)")
            user_name = input("Introduzca username: ")
        return user_name
    if cursor and play_list:
        return usuario
    if cursor is None and play_list:
        print("\n")
        print(f"El usuario ({usuario}) no exite en la Base de Datos")
        print(f'Rectifique el username o cree un nuevo usuario tecleando número "3"')
        user_name = input('Introduzca username o "3" para crear un nuevo usuario: ')
        cursor = db.usuario.find_one({"username":user_name})
        if user_name != "3":
            while not user_name.isalnum() or not user_name or (cursor is None):
                print("Por favor username válido o que este registrado (Sin signos de puntuación)")
                user_name = input("Introduzca username: ")
            return user_name
        else:
            l = valida_user()
            crear_user(l[0],l[1],l[2],l[3])
            return l[2]

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
        print("\n")
        print("Usuario creado con exito")
        print("\n")
    else:
        print("\n")
        print(f"Ya existe un usuario ({usuario}) ")
        print("Por favor inténte con otro username")

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

def valida_playlist():
    l = []
    playlist_name = ""
    user_name = ""
    song = "0"
    songs_list = []
    while not playlist_name:
        print("\n")
        print("Por favor introduzca nombre para la Playlist")
        playlist_name = input("Introduzca el nombre de la PlayList: ")
    else:
        l.append(playlist_name)
    while not user_name.isalnum() or not user_name:
        print("Por favor introduzca username válido (Sin signos de puntuación)")
        user_name = input("Introduzca username: ")
    else:
        l.append(valida_user_name(user_name, play_list=True))

    while song.lower() != "save":
        print("Elija el número correspondiente a la canción")
        song = input('Introduzca un número cada vez, del (1-20) y "save" para guardar: ')
        if if_integer(song) and int(song) in range(1,20) and not song == "":
            songs_list.append(int(song) - 1)
        elif song != "sabe" and if_integer(song) and int(song) not in range(1,20) or song != "sabe" and not if_integer(song):
                print('Opción no válida, Por favor Introduzca un número del (1-20) o "save" para guardar')
                print("\n")
    else:
        if songs_list == []:
            print("Error, una lista de reproducción no se puede guardar vacia")
        elif songs_list != []:
            l.append(list(set(songs_list)))
            return l

l = valida_playlist()
print(l)

class PlayList(object):

    def __init__(self, nombre, usuario, canciones):
        self.name = nombre
        self.user = usuario
        self.songs = canciones


    def mostrar_sugerencias(self): # Una lista de canciones aletorias con (nombre, grupo, id)
        l = []
        client = conexion_BD()
        db = client.MusicPlayList
        for i in self.songs:
            cursor = db.canciones.find({"_id": i})
            if cursor:
                for j in cursor:
                    t = j["nombre"], j["cantante"]
                    l.append(t)
        l = list(enumerate(l, start=1))
        print(tabulate(l, headers=['Número', 'Nombre Canción  -  Banda Rock']))
        print("\n")
        # return l

    def crearplaylist (self):
        client = conexion_BD()
        db = client.MusicPlayList
        playlist = ([{
            "nombre":self.name,
            "username":self.user,
            "canciones":[self.songs]
            }])
        db.playlist.insert_many(playlist)