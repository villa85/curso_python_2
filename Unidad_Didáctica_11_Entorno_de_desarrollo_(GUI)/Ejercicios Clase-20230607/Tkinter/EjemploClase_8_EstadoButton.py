from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('400x200')
root.title("Mi programa Python")

etiqueta = Label(root, text="Estado Botones", font=('calibre', 14, 'bold')).pack()
botonSaludo = Button(root, text="Saludar")
botonSaludo.place(x=110, y=150)
botonSaludo.state(['disabled']) # Deshabilita el botón
print(botonSaludo.instate(['disabled']) )

botonCerrar = Button(root, text="Cerrar", command=root.quit)
botonCerrar.place(x=230, y=150)

root.mainloop()
