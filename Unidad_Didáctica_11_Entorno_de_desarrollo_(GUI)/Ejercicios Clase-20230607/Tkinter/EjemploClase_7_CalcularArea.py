from tkinter import *
#from tkinter.ttk import *

def limpiar_label():
    label = Label(root, text="                                           ")
    label.place(x=50, y=30)

def saludar():
    limpiar_label()
    label = Label(root, text="Bienvenido")
    label.place(x=50, y=30)

def calcular():
    limpiar_label()
    a = base.get() * altura.get()
    label = Label(root, text=f"El área del triangulo es: {a} ")
    label.place(x=50, y=30)

if __name__ == '__main__':
    # Ventana principal
    root = Tk()
    root.geometry('400x200')
    root.resizable(False, False)
    root.title("Mi programa Python")

    # Variables
    base = IntVar(value=0)
    altura = IntVar(value=0)

    # Etiquetas y entradas
    etiqueta = Label(root, text="Calcular el área de un Triangulo!", font=('calibre', 14, 'bold')).pack()

    etiquetabase = Label(root, text="Base").place(x=40, y=60)
    entrada_base = Entry(root, textvariable=base, width=30).place(x=110, y=60)

    etiquetaaltura = Label(root, text="Altura").place(x=40, y=80)
    entrada_altura = Entry(root, textvariable=altura, width=30).place(x=110, y=100)

    # Botones
    botonSaludo = Button(root, text="Saludar")
    botonSaludo.place(x=110, y=150)

    botonCalcular = Button(root, text="Calcular")
    botonCalcular.place(x=170, y=150)

    botonCerrar = Button(root, text="Cerrar", command=root.quit)
    botonCerrar.place(x=230, y=150)

    botonCalcular.configure(command=calcular)
    botonSaludo.configure(command=saludar)

    root.mainloop()