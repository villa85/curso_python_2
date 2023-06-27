import pandas  as pd

def consultar_comentarios_fecha(conexion, p_clave, f_ini, f_fin):
    query = "SELECT nick_usuario " \
            "FROM usuario " \
            "WHERE id_usuario in " \
            "(SELECT id_usuario " \
            "FROM mensaje " \
            "WHERE text_mensaje like '%{}%' " \
            "AND f_mensaje >= DATE('{}') " \
            "AND f_mensaje <= DATE('{}'))".format(p_clave, f_ini, f_fin)

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