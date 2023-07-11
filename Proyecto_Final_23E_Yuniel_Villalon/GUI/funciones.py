from tkinter import *
from tkinter import messagebox

from procesar_mensajes import procesar_mensaje_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play


def pregunta():
    # Mensaje de Error
    messagebox.showinfo("Juegos cargados con exito")

def carga_datos_inicial(conexion):
    """
    carga_datos_inicial: Carga inicial de datos de juegos
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    """
    try:
        meta.cargar_video_juegos(conexion)
        play.cargar_comentario_playstore(conexion)
        meta.cargar_comentario_metacritic(conexion, "The Legend of Zelda: Ocarina of Time", "Nintendo64")
        meta.cargar_comentario_metacritic(conexion, "Super Mario 64", "Nintendo64")
        meta.cargar_comentario_metacritic(conexion, "Minecraft", "PC")
        conexion.commit()
        messagebox.showinfo('Información','Juegos cargados con exito')
    except Exception as error:
        messagebox.showerror("ERROR","Lo sentimos algo ha ido realmente mal")
        print("Lo sentimos algo ha ido realmente mal", str(error))


def eliminar_datos(conexion):
    """
    eliminar_datos: Se borran todos las tablas
    Parameters
    ----------
    conexion
        objeto conexion a la BD
    """
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM mensaje"
        cursor.execute(query)
        query = "DELETE FROM usuario"
        cursor.execute(query)
        query = "DELETE FROM juegos"
        cursor.execute(query)
        conexion.commit()
        messagebox.showinfo('Información','La Base de datos ha sido borrada con exito')
        return "La Base de datos ha sido borrada con exito"
    except Exception as error:
        messagebox.showerror("ERROR","Lo sentimos algo ha ido realmente mal")
        print("Lo sentimos algo ha ido realmente mal", str(error))