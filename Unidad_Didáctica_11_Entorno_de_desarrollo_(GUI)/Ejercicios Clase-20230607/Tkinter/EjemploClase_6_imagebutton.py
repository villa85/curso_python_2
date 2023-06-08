from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

root = Tk()

# Ajustar el tamaño de la imagen y Crear un objeto Photoimagen
imagen = Image.open("printer.png")
imagen = imagen.resize((20, 20))
imagen = ImageTk.PhotoImage(imagen)

# Mostrar la imagen en el botón
Button(root, text='Imprimir', image=imagen, compound=LEFT).pack(side=TOP)

mainloop()