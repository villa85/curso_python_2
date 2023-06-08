from tkinter import *

# Crear la ventana principal
root = Tk()
root.geometry(newGeometry='800x600')
root.resizable(width=False, height=False)
root.title("Crear un Frame y un Botón")

# # Agregar botón con pack
button = Button(root, text='Mi botón', bd = '2')
# button.pack()
#
# # Agregar etiqueta con place
etiqueta = Label(root, text="Etiqueta con Place")
# etiqueta.place(x=40,y=60)

# Agregar controles con grid
titulo = Label(root, text=" Titulo ")
titulo.grid(columnspan=2)
button.grid(row=1,column=3)
etiqueta.grid(row=3,column=0)
etiqueta2 = Label(root, text=" Etiqueta ")
etiqueta2.grid(row=3, column=1)
etiqueta3 = Label(root, text=" Etiqueta mas grande ")
etiqueta3.grid(row=3, column=2)

# Tkinter event loop
root.mainloop()