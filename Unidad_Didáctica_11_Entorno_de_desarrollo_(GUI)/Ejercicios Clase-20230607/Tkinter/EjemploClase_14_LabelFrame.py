from tkinter import *

root = Tk()
root.geometry('300x300')

# Crear el Label Frame
labelframe_tk = LabelFrame(root, text="Titulo del Label Frame") #, width=200, height=200
labelframe_tk.pack(fill="both", expand="yes") #fill="both", expand="no"

# Insertar etiqueta
etiqueta = Label(labelframe_tk, text="Etiqueta")
etiqueta.pack()

root.mainloop()
