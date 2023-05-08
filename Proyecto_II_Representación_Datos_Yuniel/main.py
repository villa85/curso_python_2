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
        if opcion == "1":
            f.extrutura_BD()
            e.opciones(opcion)
        elif opcion == "2":
            f.crear_json_canciones()
            e.opciones(opcion)
        elif opcion == "3":
            l = f.valida_user()
            f.crear_user(l[0],l[1],l[2],l[3])
            e.opciones(opcion)
        elif opcion == "4":
            if 'hr' not in locals() and 'sr' not in locals() and 'rs' not in locals():
                hr = f.PlayList("Hard Rock", "admin", f.lista_canciones(cant = 5))
                sr = f.PlayList("Soft Rock", "admin", f.lista_canciones(cant = 5))
                rs = f.PlayList("Rock Start", "admin", f.lista_canciones(cant = 5))
                hr.crearplaylist()
                sr.crearplaylist()
                rs.crearplaylist()
            twenty_random_songs = f.lista_canciones()
            s = f.PlayList("PlayListGeneral", "admin", twenty_random_songs)
            s.mostrar_sugerencias()
            e.opciones(opcion)
        elif opcion == "5":
            if 'twenty_random_songs' not in locals():
                print("Error, Antes debes mostrar las sugerencias de canciones (Paso 4)")
                print("\n")
            else:
                f.valida_playlist(twenty_random_songs)
                e.opciones(opcion)
        elif opcion == "6":
            i = f.valida_user_consultar_playlists()
            s = f.PlayList("PlayListGeneral", i, [])
            songs_list_playlist = s.consultar_playlists()
            e.lista_tabular(songs_list_playlist[0], 0)
            e.opciones(opcion)
        elif opcion == "7":
            if 'songs_list_playlist' not in locals():
                print("Error, Antes debes Consultar las PlaysList (Paso 6)")
                print("\n")
            else:
                f.get_playlist(songs_list_playlist[1])
                e.opciones(opcion)
        elif opcion == "8":
            if 'songs_list_playlist' not in locals():
                print("Error, Antes debes Consultar las PlaysList (Paso 6)")
                print("\n")
            else:
                f.get_playlist(songs_list_playlist[1], playlist = True)
                e.opciones(opcion)
        elif opcion != "fin" and e.if_integer(opcion) and int(opcion) not in range(1,7) or opcion != "fin" and not e.if_integer(opcion):
                print('Opción no válida, Por favor Introduzca un número del (1-7) o "fin" para salir')

    else:
        print("Muchas Gracias")





