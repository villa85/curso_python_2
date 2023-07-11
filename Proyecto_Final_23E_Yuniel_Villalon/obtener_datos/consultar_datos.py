import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
import sqlite3

def busca_fecha_menor_mensaje():
        conexion = sqlite3.connect('bbdd/video_juegos.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT MIN(f_mensaje) AS fecha_menor FROM mensaje")
        query = cursor.fetchone()
        fecha = query[0]
        conexion.close()
        return fecha


def consultar_comentarios_fecha(conexion, p_clave, f_ini, f_fin):
        query = "SELECT nick_usuario as Usuario " \
                "FROM usuario " \
                "WHERE id_usuario in " \
                "(SELECT id_usuario " \
                "FROM mensaje " \
                "WHERE text_mensaje like '%{}%' " \
                "AND f_mensaje >= DATE('{}') " \
                "AND f_mensaje <= DATE('{}')) ".format(p_clave, f_ini, f_fin)

        df = pd.read_sql_query(query, conexion)
        if not df.empty:
                print(df)
                return df
        else:
                messagebox.showerror("Error","No hay datos para mostrar. Primero cargar la Base de Datos")
                return("Error: No hubo coincidencia con tu búsqueda")

def consultar_comentarios_cantidad(conexion, p_clave):
        query = "SELECT usuario.nick_usuario, count(mensaje.text_mensaje) as cantidad " \
                "FROM mensaje " \
                "INNER JOIN usuario ON usuario.id_usuario = mensaje.id_usuario " \
                "GROUP BY mensaje.id_usuario " \
                "HAVING text_mensaje like '%{}%' " \
                "ORDER BY cantidad DESC".format(p_clave)

        df = pd.read_sql_query(query, conexion)
        if not df.empty:
                return df
        else:
                messagebox.showerror("Error","No hay datos para mostrar. Primero cargar la Base de Datos")
                return("Error: No hubo coincidencia con tu búsqueda")

def consultar_media_mensajes(conexion, f_ini, f_fin):
        query = "SELECT red_social.nom_red_social, mensaje.f_mensaje " \
                "FROM mensaje " \
                "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
                "WHERE f_mensaje >= DATE('{}') " \
                "AND f_mensaje <= DATE('{}') ".format(f_ini, f_fin)

        df = pd.read_sql_query(query, conexion)
        if not df.empty:
                df["f_mensaje"] = pd.to_datetime(df["f_mensaje"])
                df["dia"] = df["f_mensaje"].dt.date
                df = df.loc[:, ["nom_red_social", "dia"]]
                m_dia = df.groupby(["nom_red_social", "dia"])["dia"].count().reset_index(name='Mensajes')
                total_mensajes = m_dia["Mensajes"].sum()
                m_dia['media_mensajes'] = m_dia['Mensajes']/total_mensajes
                print(m_dia)
                m_dia.plot(x='dia', y="media_mensajes", kind='bar', figsize=(12, 8))
                plt.xticks(rotation=30)
                plt.xlabel('Días')
                plt.ylabel('Porcentaje')
                plt.title('Media de mensajes por día', size=18)
                plt.show()
        else:
                messagebox.showerror("Error","No hay datos para mostrar. Primero cargar la Base de Datos")
                return("Error: No hubo coincidencia con tu búsqueda")

def stadisticas_mensaje(conexion, word):
        query= "SELECT (red_social.nom_red_social) as Red_Social, count(mensaje.text_mensaje) as Cantidad " \
                "FROM mensaje " \
                "INNER JOIN red_social ON red_social.id_red_social = mensaje.id_red_social " \
                "WHERE mensaje.text_mensaje like '%{}%' " \
                "GROUP BY red_social.nom_red_social".format(word)

        df= pd.read_sql_query(query, conexion)
        if not df.empty:
                return df
        else:
                messagebox.showerror("Error","No hay datos para mostrar. Primero cargar la Base de Datos")
                return("Error: No hubo coincidencia con tu búsqueda")