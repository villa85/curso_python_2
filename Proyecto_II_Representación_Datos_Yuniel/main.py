from funtions import funciones as f
from funtions import extra as e

if __name__ == '__main__':
    print("\n")
    print('Proyecto "MusicPlayList en MongoDB" por Yuniel Villalón.', end= "\n\n")
    print('Elija la "opción" a realizar, escribiendo el Número correspondiente o fin para terminar.', end= "\n\n")
    opcion = ""
    e.opciones(opcion)
    while opcion.lower() != "fin":
        opcion = input("Escriba la opción deseada o fin para salir: ")
        print("\n")
        if opcion == "1": # Crea la extrutura de Base Datos
            f.extrutura_BD()
            e.opciones(opcion)
        elif opcion == "2": # Crea el archivo Json que luego se debe importar
            f.crear_json_canciones()
            e.opciones(opcion)
        elif opcion == "3": # Carga inicial de datos, creacion del usuario Admin y 3 PlayList de 5 canciones cada una
            if "user" not in locals() and 'hr' not in locals() and 'sr' not in locals() and 'rs' not in locals():
                user = f.crear_user("Yuniel", "Villalón", "admin", "villalo2511@gmail.com", notification=False)
                hr = f.PlayList("Hard Rock", "admin", f.lista_canciones(cant = 5))
                sr = f.PlayList("Soft Rock", "admin", f.lista_canciones(cant = 5))
                rs = f.PlayList("Rock Start", "admin", f.lista_canciones(cant = 5))
                hr.crearplaylist(notification = False)
                sr.crearplaylist(notification = False)
                rs.crearplaylist(notification = False)
                print("Carga inicial de datos terminada con exito")
                print("\n")
            else:
                print("La carga incial de datos ya a sido realizada")
                print("\n")
            e.opciones(opcion)
        elif opcion == "4": # Crea usuario
            l = f.valida_user()
            f.crear_user(l[0],l[1],l[2],l[3])
            e.opciones(opcion)
        elif opcion == "5": # Muestra sugerencia de 20 canciones
            twenty_random_songs = f.lista_canciones()
            s = f.PlayList("PlayListGeneral", "admin", twenty_random_songs)
            s.mostrar_sugerencias()
            e.opciones(opcion)
        elif opcion == "6": # Crea PlayList de las sugerencias recomendadas
            if 'twenty_random_songs' not in locals():
                print("Error, Antes debes mostrar las sugerencias de canciones (Paso 5)")
                print("\n")
            else:
                f.valida_playlist(twenty_random_songs)
                e.opciones(opcion)
        elif opcion == "7": # Cosultar las PlayList de un Usuario
            i = f.valida_user_consultar_playlists()
            s = f.PlayList("PlayListGeneral", i, [])
            songs_list_playlist = s.consultar_playlists()
            e.lista_tabular(songs_list_playlist[0], 0)
            e.opciones(opcion)
        elif opcion == "8": # Muestra las canciones de la PlayList Seleccionada
            if 'songs_list_playlist' not in locals():
                print("Error, Antes debes Consultar las PlaysList (Paso 7)")
                print("\n")
            else:
                f.get_playlist(songs_list_playlist[1])
                e.opciones(opcion)
        elif opcion == "9": # Muestra la PlayList (Nombre de la PlayList y genero de cada canción)
            if 'songs_list_playlist' not in locals():
                print("Error, Antes debes Consultar las PlaysList (Paso 7)")
                print("\n")
            else:
                f.get_playlist(songs_list_playlist[1], playlist = True)
                e.opciones(opcion)
        elif opcion != "fin" and e.if_integer(opcion) and int(opcion) not in range(1,9) or opcion != "fin" and not e.if_integer(opcion):
                print('Opción no válida, Por favor Introduzca un número del (1-9) o "fin" para salir')

    else:
        print("Muchas Gracias")





