from tkinter import *
from tkinter.ttk import *

def nueva_seleccion():
    Label(root, text=comboExample.get()).place(x=20, y=50)

root = Tk()
root.geometry('200x100')

labelTop = Label(root, text="Seleccione su mes de nacimiento")
labelTop.grid(column=0, row=0)

comboExample = Combobox(root,
                        values=[
                                "Enero", "Febrero", "Marzo",
                                "Abril", "Mayo", "Junio",
                                "Julio", "Agosto", "Septiembre",
                                "Octubre", "Noviembre", "Diciembre",
                            ])
comboExample.grid(column=0, row=1)
comboExample.current(0)

botonCalcular = Button(root, text="Selección")
botonCalcular.place(x=90, y=70)
botonCalcular.configure(command=nueva_seleccion)

root.mainloop()