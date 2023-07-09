from procesar_mensajes import procesar_mensaje_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play

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
        meta.cargar_comentario_metacritic(conexion, "God of War", "PlayStation4")
        conexion.commit()
        return "Juegos cargados con exito"
    except Exception as error:
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
    except Exception as error:
        print("Lo sentimos algo ha ido realmente mal", str(error))