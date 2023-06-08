from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry('100x100')

# Crear un objeto Style
style = Style()

# Definir un estilo (TButton es utilizado por ttk.Button)
style.configure('W.TButton', font=('calibri', 10, 'bold'))

# Aplicar el estilo al botón
boton = Button(root, text='Salir', style='W.TButton', command=root.destroy)
boton.grid(row=0, column=3, padx=100)

root.mainloop()