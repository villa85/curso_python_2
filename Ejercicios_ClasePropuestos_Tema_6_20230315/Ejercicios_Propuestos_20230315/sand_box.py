# import pywhatkit as whatsapp

# whatsapp.sendwhatmsg("+34655062310", "Esto es un mensaje de amor automatico, mamita", 10, 8)

import json
import os

print(f"Directorio de Trabajo: {os.getcwd()}")

PATH_FILE = os.getcwd()

PATH_IMAGES = PATH_FILE + "\Ejercicios_ClasePropuestos_Tema_6_20230315\Ejercicios_Propuestos_20230315"

print(PATH_IMAGES)
if os.path.isdir(PATH_IMAGES):
    os.chdir(PATH_IMAGES)
else:
    print("La ruta no existe")

print(f"Directorio de Trabajo se cambio a: {os.getcwd()}")


# file_name = "data\\yelp_academic_dataset_business.json"
# file_name = "recipes.json"
file_name = "data\\pokedex.json"

with open(file_name, "r", encoding = "utf-8") as file:
    my_file = file.readlines()
    mis_datos = []
    for linea in my_file:
        mis_datos.append(json.loads(linea))

print(mis_datos)