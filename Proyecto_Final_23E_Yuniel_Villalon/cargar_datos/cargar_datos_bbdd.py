"""
Módulo para conexión y carga inicial de datos
"""
import sqlite3
from sqlite3 import Error
from datetime import datetime

FORMATO = "%d-%m-%y %H:%M:%S"
FORMATO2 = "%Y"
hoy = datetime.today()
FECHA_P = hoy.strftime(FORMATO)
FECHA_YEAR = hoy.strftime(FORMATO2)


def conexion_bd(archivo):
    """Conexión a la BD video juegos
    Args:
        archivo (URL): ruta de la base de datos
    Return:
    conn conexión a la BD
    """
    conn = None
    try:
        conn = sqlite3.connect(archivo)
        print(f"Versión de Sqlite: {sqlite3.version}")
    except Error as error:
        print(f"Error al intentar conectarse a la Base de Datos: {error}")
        if conn:
            conn.close()
    return conn

def find_social_network(conexion, social_network_name):
    """
    find_social_network: Busca red social y retorna id
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    social_network_name
        nombre red social
    Returns: id de la red social si existe y None sino existe
    """
    cursor = conexion.cursor()
    query = "SELECT id_red_social FROM red_social WHERE nom_red_social = '{}'".format(social_network_name.capitalize())
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id

def find_user(conexion, nick_name):
    """
    find_user: Busca usuario y retorna id
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    user_name
        nombre usuario
    Returns: id del usuario si existe y None sino existe
    """
    cursor = conexion.cursor()
    query = 'SELECT id_usuario FROM usuario WHERE nick_usuario = "{}"'.format(nick_name)
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id

def find_game(conexion, game_name, plataforma):
    """
    find_game: Busca juego y retorna id
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    game_name
        titulo de juego
    plataforma
        plataforma de juegos
    Returns: id del juego si existe y None sino existe
    """
    cursor = conexion.cursor()
    query = "SELECT id_juego FROM juegos WHERE tit_juego = '{}' AND plataforma = '{}'".format(game_name.capitalize(), plataforma.capitalize())
    cursor.execute(query)
    res = cursor.fetchone()
    if res is None:
        id = None
    else:
        if type(res) == int:
            id = res
        else:
            id = res[0]
    return id

def insert_game(conexion, game_name, plataforma):
    """
    insert_game: Inserción de juego en la BD
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    game_name
        titulo de juego
    plataforma
        plataforma de juegos
    """
    fecha_p = FECHA_YEAR
    id_game = find_game(conexion, game_name, plataforma)
    if id_game is None:
        query = "INSERT INTO juegos (tit_juego, plataforma, f_publicacion) VALUES(?,?,?)"
        data = (game_name.capitalize(), plataforma.capitalize(), fecha_p)
        insertar = conexion.cursor()
        insertar.execute(query, data)
        conexion.commit()
        return insertar.lastrowid
    else:
        print(f"El juego {game_name} ya existe en la Base de datos")
        return None

def insert_user(conexion, nick_name, user_name, email_user):
    """
    insert_user: Inserción de usuario en la BD
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    nick_name
        sobre-nombre del usuario
    user_name
        nombre del usuario
    email_user
        correo electronico
    """
    id_user = find_user(conexion, user_name)
    if id_user is None:
        query = "INSERT INTO usuario (nick_usuario, nom_usuario, email_usuario) VALUES(?,?,?)"
        data = (nick_name.capitalize(), user_name.capitalize(), email_user)
        insertar = conexion.cursor()
        insertar.execute(query, data)
        conexion.commit()
        return insertar.lastrowid
    else:
        print(f"El usuario {user_name} ya existe en la Base de datos")
        return None

def insert_social_network(conexion, social_network_name, social_network_url):
    """
    insert_social_network: Inserción de red social en la BD
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    social_network_name
        nombre red social
    social_network_url
        url red social
    """
    id_social_network = find_social_network(conexion, social_network_name)
    if id_social_network is None:
        query = "INSERT INTO red_social (nom_red_social, url_red_social) VALUES(?,?)"
        data = (social_network_name.capitalize(), social_network_url)
        insertar = conexion.cursor()
        insertar.execute(query, data)
        conexion.commit()
        return insertar.lastrowid
    else:
        print(f"La red social {social_network_name} ya existe en la Base de datos")
        return None

def insert_mensaje(conexion, mensaje, id_juego, id_usuario, id_red_social):
    """
    insert_mensaje: Inserción de comentario sobre un juego en la BD
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    mensaje
        cometario acerca del juego
    juego
        nombre del juego
    plataforma
        nombre de la plataforma
    usuario
        nick name del usuario
    red_social
        nombre de la red social

    Returns
    -------
        id del mensaje creado
    """

    fecha_mensaje = FECHA_P

    query = "INSERT INTO mensaje (f_mensaje, text_mensaje, id_juego, id_usuario, id_red_social) VALUES(?,?,?,?,?)"
    data = (fecha_mensaje, mensaje.capitalize(), id_juego, id_usuario, id_red_social)
    insertar = conexion.cursor()
    insertar.execute(query, data)
    conexion.commit()
    return insertar.lastrowid
