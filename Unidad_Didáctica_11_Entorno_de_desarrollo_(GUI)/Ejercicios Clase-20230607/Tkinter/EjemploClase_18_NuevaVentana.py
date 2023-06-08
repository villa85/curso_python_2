from tkinter import *
from tkinter.ttk import *

# Crear la ventana principal
root = Tk()
root.geometry("200x200")

# Function para crear una nueva ventana
def abrir_nueva_ventana():

    # Objeto de nivel superior que será tratado como una nueva ventana
    newWindow = Toplevel(root)
    newWindow.title("Nueva Ventana")  # título de la nueva ventana
    newWindow.geometry("200x200")

    # Crear una etiqueta en la nueva ventana
    Label(newWindow,
          text="Esta es una nueva Ventana").pack()

# Crear una etiqueta en la ventana principal
label = Label(root, text="Esta es la Ventana Principal")
label.pack(pady=10)

btn = Button(root,
             text="Nueva Ventana",
             command=abrir_nueva_ventana)
btn.pack(pady=10)

mainloop()
