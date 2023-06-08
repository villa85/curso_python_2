# Importar los módulos o  librerías Tkinter
from tkinter import *
from tkinter.ttk import *
#from tkinter import ttk

# Crear la ventana principal para la aplicación GUI
root = Tk()
root.geometry(newGeometry='800x600')
root.resizable(width=False, height=False)

# Insertar widgets a la aplicación
# Titulo de la ventana
root.title("Primer GUI en Python")
root.iconbitmap('python.ico')

# Etiqueta
label = Label(root, text="¡Bienvenidos!").pack()
#label = ttk.Label(v_principal, text="¡Bienvenidos!").pack() #from tkinter import ttk

# Crear el loop del programa principal (Main)
root.mainloop()