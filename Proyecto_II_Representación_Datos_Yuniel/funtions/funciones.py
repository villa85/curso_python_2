from bson.objectid import ObjectId

from pymongo import IndexModel, ASCENDING, DESCENDING

import pymongo
from pymongo import MongoClient

def conexion_BD():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client

def extrutura_BD():
    client = conexion_BD()
    db = client.MusicPlayList
    db.create_collection("usuario")
    db.create_collection("playlist")
    db.create_collection("canciones")



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