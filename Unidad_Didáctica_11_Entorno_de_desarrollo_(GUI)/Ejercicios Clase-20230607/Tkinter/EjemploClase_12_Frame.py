from tkinter import *
from tkinter.ttk import *

# Crear la ventana principal
root = Tk()
root.geometry(newGeometry='800x600')
root.resizable(width=False, height=False)
root.title("Crear un Frame y un Botón")

# Definir un estilo para el frame
s = Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised'  ) #'sunken', background='red'

# Crear un frame en la ventana principal
frame = Frame(root, width=200, height=200, style='Danger.TFrame')
frame.grid()

# Agregar botones en el frame de root
button = Button(frame, text='Mi botón').place(x=40,y=80)

# Agregar etiqueta en el frame de root
etiqueta = Label(frame, text="Etiqueta")
etiqueta.place(x=40,y=60)

root.mainloop()