from datetime import date
from tkinter import *
from PIL import Image, ImageTk

# Crear la ventana principal para la aplicación GUI
root = Tk()
root.geometry(newGeometry='420x200')
root.resizable(width=False, height=False)

# Insertar widgets a la aplicación
# Titulo de la ventana
root.title("Validación de usuario")

# Etiquetas de controles Usuario y Contraseña
l_usuario = Label(root, text="Usuario: ").place(x=40,y=60)  # , bg="blue"
l_contrasena = Label(root, text="Contraseña: ").place(x=40, y=100) #,relief="solid", font="Times 8 bold"

# Etiquetas generadas en tiempo de ejecución (Variables)
fecha = StringVar()
Label(root, text="Fecha: ").place(x=300,y=20)
Label(root,  textvariable=fecha).place(x=340,y=20)
fecha.set(date.today()) # Asignamos el texto en tiempo de ejecución

# Etiquetas con imágenes
imagen = Image.open("perfil.png")
imagen = imagen.resize((100, 100))
imagen = ImageTk.PhotoImage(imagen)
Label(root, image=imagen).place(x=300, y=40)  #

# Botones Aceptar y Cancelar
boton_aceptar = Button(root, text="Aceptar").place(x=170, y=150)
boton_cancelar = Button(root, text="Cancelar").place(x=230, y=150)

# Entrada de Datos
e_usuario = Entry(root, width=30).place(x=110,  y=60)
e_contrasena = Entry(root, width=30).place(x=110, y=100)

root.mainloop()