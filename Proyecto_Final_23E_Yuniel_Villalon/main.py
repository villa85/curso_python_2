# Proyecto Final 23E Yuniel Antonio Villalón Rosales

# Importar Librerias

#Importar modulos propios
from cargar_datos import cargar_datos_bbdd as bd
from procesar_mensajes import procesar_mensaje_metacritic as meta
from procesar_mensajes import procesar_mensajes_playstore as play
from obtener_datos import consultar_datos as cd

# Programa principal
conexion = bd.conexion_bd("bbdd/video_juegos.db")

# id_social_network = bd.find_social_network(conexion, "PLaysTore")
# print(f"Red Social: {id_social_network}")

# id_game = bd.insert_game(conexion, "Mario Bros", "steam")

# print(id_game)
# id_mensaje = bd.insert_mensaje(conexion, "Es una prueba", "Mario Bros", "steam", "villa","PLaysTore")
# print(id_mensaje)

# id_red_social = bd.insert_social_network(conexion, "Playstore", "twitter.com")
# print(id_red_social)



# id_usuario = bd.insert_user(conexion, "Villa", "Yuniel Villalón", "villalon2511@gmail.com")
# print(id_usuario)

# id_user = bd.find_user(conexion, "Burtq.")
# print(f"Usuario: {id_user}")

# meta.cargar_video_juegos(conexion) # 1
# play.cargar_comentario_playstore(conexion) # 2
# meta.cargar_comentario_metacritic(conexion, "The Legend of Zelda: Ocarina of Time", "Nintendo64") # 3
# cd.consultar_comentarios_fecha(conexion, "Zelda", "2020-06-28", "2023-06-29")
# cd.consultar_comentarios_cantidad(conexion, "Zelda")
cd.consultar_media_mensajes(conexion, "2023-06-28", "2023-06-29")
# cd.stadisticas_mensaje(conexion, "zelda")

