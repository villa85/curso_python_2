import re

def une_listas(l):
    p = 0
    c = len(l)

    while c > 0:
        for i in l:
            if isinstance(i, list):
                p = l.index(i)
                lv = l.pop(p)
                for j in range(len(lv)):
                    l.insert(p, lv[j])
                    p +=1
        c -= 1
    return l

def if_integer(string):
        return string.isdigit()

def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

def opciones(option):
    if option =="":
        print('1- Crear estrutura de la base de datos. ', end= "\n")
        print('2- Generar archivo Json de canciones.', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones.', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="1":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U00002714")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="2":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "")
        print("\U00002714")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="3":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario. ', end= "")
        print("\U00002714")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="4":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "")
        print("\U00002714")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="5":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "")
        print("\U00002714")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="6":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "")
        print("\U00002714")
        print('7- Mostrar Canciones. ', end= "\n\n")
    elif option =="7":
        print('1- Crear estrutura de la base de datos. ', end= "")
        print("\U000026A0")
        print('2- Generar archivo Json de canciones. ', end= "\n")
        print('3- Crear Usuario.', end= "\n")
        print('4- Mostrar sugencias de canciones. ', end= "\n")
        print('5- Crear PlayList. ', end= "\n")
        print('6- Consultar PlayList. ', end= "\n")
        print('7- Mostrar Canciones. ', end= "")
        print("\U00002714")
        print("\n")