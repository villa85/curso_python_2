import os
import json
import requests
import pymongo
import random
import funtions.extra as e
from tabulate import tabulate

def conexion_BD():
    """
    conexion_BD _summary_
    función que realiza la conexion con la BD local de Mongo

    Returns
    -------
    retorna cursor con la conexion a la BD
    """
    client = pymongo.MongoClient("mongodb://localhost:27017")
    return client


def extrutura_BD():
    """
    extrutura_BD _summary_
    crea la estrutura de la BD MusicPlayList, con las colecciones (usuario, playlist, canciones). Y controla que no creen
    las colecciones ya que son ya existen.
    """
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
        print("\n")
    else:
        print("La colección canciones ya existe")
        print("\n")

def crear_json_canciones():
    """
    crear_json_canciones _summary_
    Genera un arichivo JSON de 10 artistas con 5 canciones cada una

    _extended_summary_
    """

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

    m = e.une_listas(data['s'])

    for i in m:
        x = {
            "nombre": i.get('trackName', i["collectionName"]), # se valida que si el nombre de la cancion esta vacion la sustituya por el nombre del album
            "cantante": i.get('artistName', None), # premite que el nombre del artista pueda ser nulo
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

class PlayList(object):
    """
    Clase PlayList: Clase principal PlayList, encargada del tratamiendo de datos realicionados a Lista de Reprodución

    Parameters
    Nombre de Playlist, Nombre de Usuario, Listado de Caciniones
    """

    def __init__(self, nombre, usuario, canciones):
        self.name = nombre
        self.user = usuario
        self.songs = canciones

    def __str__(self, lista, playlist = False):
        """
        __str__ _summary_
        Permite mostrar PlaysList en diferentes formatos dependiendo el valor de playlist

        Parameters
        ----------
        lista
            lista de reprodución.
        playlist, optional
            _description_, by default False
            controlamos al si queremos ver la playlist o solo las canciones

        Returns
        -------
            lista de reprocdución o solo canciones
        """
        if playlist:
            print(f"Nombre del PlayList: {self.songs[0]}")
            return e.lista_tabular(lista, 2)
        else:
            print("Listado de Canciones")
            return e.lista_tabular(lista, 3)

    def mostrar_sugerencias(self): # Una lista de canciones aletorias con (nombre, grupo)
        """
        mostrar_sugerencias: Muestra un listado de 20 canciones aletorias.
        """
        l = []
        client = conexion_BD()
        db = client.MusicPlayList
        if self.songs != []:
            for i in self.songs:
                cursor = db.canciones.find({"_id": i})
                if cursor:
                    for j in cursor:
                        t = j["nombre"], j["cantante"]
                        l.append(t)
            e.lista_tabular(l, sugerencias = 1)
        else:
            print('ERROR, la colleción "canciones" no ha sido creada o se encuatra vacia. Ejecute las opciones (1 y 2) y asegurese que el archivo JSON ha sido importado correctamente en la BD.')
            print("\n")

    def crearplaylist (self, notification = True):
        """
        crearplaylist: Función mediante la que se crea las Playlist
        Parameters
        ----------
        notification, optional
            _description_, by default True
            Según el valores de la variable "notification" (True o False), se muestran notificaciones de extio o no
        """
        client = conexion_BD()
        db = client.MusicPlayList
        cursor = db.playlist.find_one({"nombre":self.name, "username":self.user})
        if cursor is None:
            playlist = ([{
                "nombre":self.name,
                "username":self.user,
                "canciones":[self.songs]
                }])
            db.playlist.insert_many(playlist)
            if notification:
                print("\n")
                print(f'Lista de reproducción "{self.name}" creada con exito')
                print("\n")

    def consultar_playlists(self):
        """
        consultar_playlists:Funcion que devuelve las listas de reproducción de un usuario a la vez.

        _extended_summary_

        Returns
        -------
            Devuelve una lista que contiene 2 listas embebidas, la primera "Nombre PlayList y cantida de canciones"
            y  la segunda "Nombre PlayList y listado de canciones"
        """
        l = []
        s = []
        lista_general = []
        client = conexion_BD()
        db = client.MusicPlayList
        if self.user:
            cursor = db.playlist.find({"username":self.user})
            if cursor:
                for i in cursor:
                    c = i["nombre"], i["canciones"][0]
                    t = i["nombre"], len(i["canciones"][0])
                    l.append(t)
                    s.append(c)
            elif not cursor:
                print(f'El usuario "{self.user}" no existe')

            lista_general.append(l)
            lista_general.append(s)
            return lista_general

        else:
            print('ERROR, la colleción "playlist" no ha sido creada o se encuatra vacia. Ejecute las opciones (1 y 2) y asegurese que el archivo JSON ha sido importado correctamente en la BD.')
            print("\n")


    def works_for_all(func):
        def mostrar_canciones(self, playlist = False):
            """
            mostrar_canciones: Funcion que muestra las canciones de una playlist

            Parameters
            ----------
            playlist, optional
                _description_, by default False
                Muestra solo las "canciones y el grupo" de una lista o  "las canciones, el grupo, el nombre del playlis y el genero de cada cancion"

            Returns
            -------
                Listado de canciones en direntes formatos
            """
            l = []
            client = conexion_BD()
            db = client.MusicPlayList
            if self.songs[1] != []:
                for i in self.songs[1]:
                    cursor = db.canciones.find({"_id": i})
                    if cursor:
                        for j in cursor:
                            t = j["nombre"], j["cantante"], j["genero"]
                            l.append(t)
                if playlist == True:
                    return self.__str__(l, playlist)
                else:
                    return self.__str__(l, playlist)
            else:
                print('ERROR, la colleción "canciones" no ha sido creada o se encuatra vacia. Ejecute las opciones (1 y 2) y asegurese que el archivo JSON ha sido importado correctamente en la BD.')
                print("\n")
            return func(self, playlist)
        return mostrar_canciones

    @works_for_all
    def mostrar_playlists(self, playlist):
        """
        mostrar_playlists: Decorador para extender la funcionalidad del método
        mostrar_Canciones
        """
        if playlist:
            print(f"Nombre de la PlayList: {self.songs[0]}")
        else:
            print("Listado de Canciones")

def get_playlist(lista, playlist = False):
    """
    get_playlist: Se valida que le usuario introduzca un número valido de lista de reproduccion que va a visualizar

    Parameters
    ----------
    lista
        listado de listas de un usuario
    playlist, optional
        _description_, by default False
        Muestra la playlist en diferentes formatos
    Returns
    -------
        Playslist de usuario
    """
    playlist_numb = "0"
    print("Elija el número correspondiente a la PlayList")
    playlist_numb = input(f'Introduzca un número: ')
    print("\n")
    para = True
    bad = e.if_integer(playlist_numb) and int(playlist_numb) not in range(1,len(lista)+1) or not e.if_integer(playlist_numb)
    good = e.if_integer(playlist_numb) and int(playlist_numb) in range(1,len(lista)+1) and not playlist_numb == ""
    while para:
        if bad:
            print(f'Opción no válida, Por favor Introduzca un número (1-{len(lista)})')
            print("Elija el número correspondiente a la PlayList")
            playlist_numb = input(f'Introduzca un número: ')
            print("\n")
            if e.if_integer(playlist_numb) and int(playlist_numb) in range(1,len(lista)+1) and not playlist_numb == "":
                position = int(playlist_numb) - 1
                para = False
        elif good:
            position = int(playlist_numb) - 1
            para = False
    s = PlayList("PlayListGeneral", "admin", lista[position])
    if playlist:
        return s.mostrar_playlists(playlist = True)
    else:
        return s.mostrar_playlists()

def valida_user_consultar_playlists():
    """
    valida_user_consultar_playlists: Valida que usuario este en BD usuarios para poder crear una playlist

    Returns
    -------
        devuelve el usuario
    """
    user_name = ""
    while not user_name:
        print("Por favor introduzca username registrado")
        user_name = input("Introduzca username: ")
    else:
        client = conexion_BD()
        db = client.MusicPlayList
        cursor = db.usuario.find_one({"username":user_name})
        if cursor:
            return user_name
        elif cursor is None:
            print("\n")
            print(f"El usuario ({user_name}) no exite en la Base de Datos")
            print('Rectifique, username no registrado')
            user_name = input('Introduzca username: ')
            cursor = db.usuario.find_one({"username":user_name})
            while cursor is None:
                print('Rectifique, username no registrado')
                user_name = input("Introduzca username: ")
                cursor = db.usuario.find_one({"username":user_name})
            return user_name

def lista_canciones(cant = 20): # Una lista de 20 las canciones aleatorias (_ids)
    """
    lista_canciones: Genera una lista de ids correspondiente a los ids de canciones

    Parameters
    ----------
    cant, optional
        la lista contara son 20 cancione por defecto, by default 20
    Returns
    -------
        lista de ids(canciones)
    """
    l = []
    client = conexion_BD()
    db = client.MusicPlayList
    n = db.list_collection_names()
    cursor = db.canciones.find()
    if "canciones" in n and cursor.count() > 0:
        for i in cursor:
            l.append(i["_id"])
        l = random.SystemRandom().sample(l, cant)
        return l
    else:
        return l

def valida_user():
    """
    valida_user: Hace las validaciones de cada uno de los atributos de un usuario

    para que se inserte un usuario "válido"

    Returns
    -------
        Devuelve una lista donde cada uno de los valores es un atributo valido de la colección usuario
    """
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
        l.append(valida_user_name(user_name)) # se verifica que el usuario ya no se encuentre creado
    while not e.es_correo_valido(email) or not email:
        print("Por favor introduzca un correo válido")
        email = input("Introduzca dirección de correo: ")
    else:
        l.append(email)
    return l

def valida_user_name(usuario, play_list = False):
    """
    valida_user_name: Metod que busca en la BD si exite el usuario que se quiere crear
    en caso de que si se encuentre se vuelve a pedir que introduz otro nombre de usuario.
    Logrando que el user name sea unico

    Parameters
    ----------
    usuario
        Nombre de usuario que se quiere crear
    play_list, optional
        si play_list "play_list=True" devuelve el user_name si esta en la BD usuario justo lo que
        se necesita para crear una PlayList, si "play_list=False" la funcion se esta usando para validar
        un usuario y crearlo, y si esta le BD usuario se le pide que cree otro

    Returns
    -------
        Devuelve un usuario o Inserta el usuario en la BD
    """
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

def crear_user(nombre, apellido, usuario, email, notification = True):
    """
    crear_user: Funcion que inserta un usuario en la BD

    Parameters
    ----------
    nombre
        _description_
    apellido
        _description_
    usuario
        _description_
    email
        _description_
    notification, optional
        _description_, by default True
    """
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
        if notification:
            print("\n")
            print("Usuario creado con exito")
            print("\n")
    else:
        if notification:
            print("\n")
            print(f"Ya existe un usuario ({usuario}) ")
            print("Por favor inténte con otro username")

def lista_canciones_playlist(list_sugerencias, userlist):
    """
    lista_canciones_playlist: Busca en la lista de 20 sugerencias de canciones las que el usuario a elegido

    Parameters
    ----------
    list_sugerencias
        lista de 20 canciones (ids)
    userlist
        lista de numeros corespondientes a las canciones seleccionadas

    Returns
    -------
        lista de canciones (ids) del usuario
    """
    l = []
    for i in userlist:
        l.append(list_sugerencias[i])
    return l

def valida_playlist(list_sugerencias):
    """
    valida_playlist: Funcion que primero valida los datos y luego crea la Playlist
    Parameters
    ----------
    list_sugerencias
        lista de 20 canciones
    """
    l = []
    playlist_name = ""
    user_name = ""
    song = "0"
    songs_list = []
    while not playlist_name:
        print("Por favor introduzca nombre para la Playlist")
        playlist_name = input("Introduzca el nombre de la PlayList: ")
    else:
        n = playlist_name.capitalize()
        l.append(n)
    while not user_name.isalnum() or not user_name:
        print("Por favor introduzca username válido (Sin signos de puntuación)")
        user_name = input("Introduzca username: ")
    else:
        l.append(valida_user_name(user_name, play_list=True))

    while song.lower() != "save":
        print("Elija el número correspondiente a la canción")
        song = input('Introduzca un número cada vez, del (1-20) y "save" para guardar: ')
        if e.if_integer(song) and int(song) in range(1,20) and not song == "":
            songs_list.append(int(song) - 1)
        elif song != "save" and e.if_integer(song) and int(song) not in range(1,20) or song != "save" and not e.if_integer(song):
                print('Opción no válida, Por favor Introduzca un número del (1-20) y "save" para guardar')
                print("\n")
    else:
        if songs_list == []:
            print("ERROR, una lista de reproducción no se puede guardar vacia")
        elif songs_list != []:
            l.append(lista_canciones_playlist(list_sugerencias, list(set(songs_list))))
    p = PlayList(l[0], l[1], l[2])
    p.crearplaylist()