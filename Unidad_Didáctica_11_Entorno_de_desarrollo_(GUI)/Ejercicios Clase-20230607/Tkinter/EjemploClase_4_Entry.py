from tkinter import *

# Función para obtener los datos
def obtener_datos():
    nombre = usuario.get()
    passw = password.get()

    print("El nombre es : " + nombre)
    print("La contraseña es : " + passw)

    usuario.set("")
    password.set("")

# Crear la ventana principal para la aplicación GUI
root = Tk()

# Insertar widgets a la aplicación
# Titulo de la ventana
root.title("Validación de usuario")

# Declarar variable para almacenar el usuario y la contraseña
usuario = StringVar()
password = StringVar()

# Etiquetas de controles Usuario y Contraseña
l_usuario = Label(root, text="Usuario: ", font=('calibre',10, 'bold'))
l_password = Label(root, text="Contraseña: ", font=('calibre',10, 'bold'))

# Entrada de Datos
e_usuario = Entry(root, textvariable = usuario, font=('calibre',10, 'bold'))
e_password = Entry(root, textvariable = password, show="*", font=('calibre',10, 'bold'))

# Botones Aceptar y Cancelar
boton_aceptar = Button(root, text="Aceptar", command = obtener_datos)
boton_cancelar = Button(root, text="Cancelar", command=root.quit)

# Ordenar los controles en un grid
l_usuario.grid(row=0,column=0)
e_usuario.grid(row=0,column=1)
l_password.grid(row=1,column=0)
e_password.grid(row=1,column=1)
boton_aceptar.grid(row=2,column=1)
boton_cancelar.grid(row=2,column=2)

root.mainloop()