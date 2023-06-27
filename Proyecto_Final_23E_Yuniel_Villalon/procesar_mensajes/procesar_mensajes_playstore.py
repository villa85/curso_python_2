import json
from datetime import datetime
from cargar_datos import cargar_datos_bbdd as bd


def cargar_comentario_playstore(conexion):

    with open("datos/PlayStoreGameAppInfoReview.json") as file:
        json_data = json.load(file)

    fecha_actual = bd.FECHA_P
    id_red_social = bd.find_social_network(conexion, "Playstore")

    juegos = ["com.redantz.game.za3p", "com.imcrazy.ds2"]

    for juego in juegos:
        tit_juego = json_data[juego]["appInfo"]["title"]
        f_publicacion = json_data[juego]["appInfo"]["released"][-4]
        id_juego = bd.find_game(conexion, juego, "Mobile")
        if id_juego is None:
            id_juego = bd.insert_game(conexion, tit_juego, "Mobile")

        for i in range(5):
            nick_usuario = json_data[juego]['reviews'][i]['userName']
            id_usuario = bd.find_user(conexion, nick_usuario)
            if id_usuario is None:
                id_usuario = bd.insert_user(conexion, nick_usuario, nick_usuario, "sin email")
            mensaje = json_data[juego]["reviews"][i]["content"]
            try:
                bd.insert_mensaje(conexion, mensaje, id_juego, id_usuario, id_red_social)
            except Exception as e:
                print(f"Ha ocurrido un error al insertar los comentarios {e}")
