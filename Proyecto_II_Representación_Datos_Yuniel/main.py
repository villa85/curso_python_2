from tabulate import tabulate
from funtions import funciones as f

if __name__ == '__main__':
    print("\n")
    print('Proyecto "MusicPlayList en MongoDB" por Yuniel Villalón.', end= "\n\n")
    print('Elija la "opción" a realizar, escribiendo el Número correspondiente o fin para terminar.', end= "\n\n")
    print('1- Crear estrutura de la base de datos', end= "\n")
    print('2- Generar archivo Json de canciones', end= "\n")
    print('3- Crear Usuario', end= "\n")
    print('4- Mostrar sugencias de canciones', end= "\n")
    print('5- Crear PlayList', end= "\n\n")

    opcion = "0"

    while opcion.lower() != "fin":
        opcion = input("Escriba la opción deseada o fin para salir: ")
        print("\n")
        if opcion == "1":
            f.extrutura_BD()
        elif opcion == "2":
            f.crear_json_canciones()
        elif opcion == "3":
            l = f.valida_user()
            f.crear_user(l[0],l[1],l[2],l[3])
        elif opcion == "4":
            twenty_random_songs = f.lista_canciones()
            s = f.PlayList("PlayListGeneral", "admin", twenty_random_songs)
            s.mostrar_sugerencias()
        elif opcion == "5":
            if 'twenty_random_songs' not in locals():
                print("Error, Antes debes mostrar las sugerencias de canciones (Paso 4)")
                print("\n")
            else:
                f.valida_playlist(twenty_random_songs)
        elif opcion != "fin" and f.if_integer(opcion) and int(opcion) not in range(1,4) or opcion != "fin" and not f.if_integer(opcion):
                print('Opción no válida, Por favor Introduzca un número del (1-5) o "fin" para salir')
                print("\n")
    else:
        print("Muchas Gracias")





