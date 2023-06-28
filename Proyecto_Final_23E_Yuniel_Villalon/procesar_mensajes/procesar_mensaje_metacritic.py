import pandas as pd
from cargar_datos import cargar_datos_bbdd as bd


def cargar_video_juegos(conexion):
    df_juegos = pd.read_csv("datos/metacritic_game_info.csv",
                            header=0,
                            index_col=0,
                            names=["tit_juego", "f_publicacion", "Publisher",
                                "Genre", "plataforma", "PMetascore", "Avg", "NoPlayers"]
                            )

    df_juegos = df_juegos.loc[0:500,["tit_juego", "plataforma", "f_publicacion"]]
    df_juegos.to_sql( name = "juegos", con = conexion, if_exists="append", index=False)

def cargar_comentario_metacritic(conexion, juego, plataformma):
    df_cometarios = pd.read_csv("datos/metacritic_game_user_comments.csv",
                                header=0,
                                index_col=0,
                                names=["Title", "Platform", "Userscore", "Comment", "UserName"]
                                )
    df_cometarios = (df_cometarios.loc[(df_cometarios["Title"] == juego) & (df_cometarios["Platform"] == plataformma), ["Title", "Platform", "Comment", "UserName"]])
    id_red_social = bd.find_social_network(conexion, "Metacritic")
    id_juego = bd.find_game(conexion, juego, plataformma)

    if id_juego is None:
        id_juego = bd.insert_game(conexion, juego, plataformma)

    for fila in df_cometarios.itertuples():
        nick_name = str(fila.UserName)
        id_usuario = bd.find_user(conexion, nick_name)
        if id_usuario is None:
            id_usuario = bd.insert_user(conexion, nick_name, nick_name, "sin email")
        try:
            bd.insert_mensaje(conexion, fila.Comment, id_juego, id_usuario, id_red_social)
        except Exception as e:
            print(f"Ha ocurrido un error al insertar los comentarios {e}")
