import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt


def consultar_comentarios_fecha(conexion, p_clave, f_ini, f_fin):
        query = "SELECT nick_usuario " \
                "FROM usuario " \
                "WHERE id_usuario in " \
                "(SELECT id_usuario " \
                "FROM mensaje " \
                "WHERE text_mensaje like '%{}%' " \
                "AND f_mensaje >= DATE('{}') " \
                "AND f_mensaje <= DATE('{}')) ".format(p_clave, f_ini, f_fin)

        df = pd.read_sql_query(query, conexion)
        print(df)

def consultar_comentarios_cantidad(conexion, p_clave):
        query = "SELECT usuario.nick_usuario, count(mensaje.text_mensaje) as cantidad " \
                "FROM mensaje " \
                "INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario " \
                "GROUP BY mensaje.id_usuario " \
                "HAVING text_mensaje like '%{}%' " \
                "ORDER BY cantidad DESC".format(p_clave)

        df = pd.read_sql_query(query, conexion)
        print(df)

def consultar_media_mensajes(conexion, f_ini, f_fin):
        query = "SELECT (red_social.nom_red_social) as Red_Social, avg(mensaje.text_mensaje) as Media " \
                "FROM mensaje " \
                "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
                "WHERE f_mensaje >= DATE('{}') " \
                "AND f_mensaje <= DATE('{}') " \
                "GROUP BY mensaje.id_red_social " \
                "ORDER BY Media DESC".format(f_ini, f_fin)

        df = pd.read_sql_query(query, conexion)
        ax = sb.catplot(x = "Red_Social", y="Media", data=df, kind="bar")
        plt.legend(
        loc='best',
        fontsize='small',
        frameon=False
        )
        plt.title("Media de Mensajes Diarios.", size=18)

def stadisticas_mensaje(conexion, word):
        query= "SELECT (red_social.nom_red_social) as Red_Social, count(mensaje.text_mensaje) as Cantidad " \
                "FROM mensaje " \
                "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
                "WHERE mensaje.text_mensaje like '%{}%' " \
                "GROUP BY red_social.nom_red_social".format(word)

        df= pd.read_sql_query(query, conexion)
        print(df)
