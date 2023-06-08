from tkinter import *
from tkinter import messagebox

def isChecked():
    if seleccion.get() == 1:
        messagebox.showinfo('Cursos', 'Bienvenido a Programación Python!')
    elif seleccion.get()  == 2:
        messagebox.showinfo('Cursos', 'Bienvenido a Machine Learning!')
    elif seleccion.get()  == 3:
        messagebox.showinfo('Cursos', 'Bienvenido a AWS Lambda Functions!')


root = Tk()
root.geometry("300x200")

l_frame = LabelFrame(root, text='Seleccione sus Cursos')
l_frame.pack()

seleccion = IntVar(root, "0")


Button1 = Radiobutton(l_frame, text="Programación Python",
                      variable=seleccion,
                      value=1,
                      height=2,
                      padx=2,
                      command=isChecked)

Button2 = Radiobutton(l_frame, text="Machine Learning",
                      variable=seleccion,
                      value=2,
                      height=2,
                      padx=2,
                      command=isChecked)

Button3 = Radiobutton(l_frame, text="AWS Lambda Fuctions",
                      variable=seleccion,
                      value=3,
                      height=2,
                      padx=2,
                      command=isChecked)

Button1.pack()
Button2.pack()
Button3.pack()

mainloop()