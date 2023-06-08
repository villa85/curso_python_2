from tkinter import *
from tkinter import messagebox

def isChecked():
    if Checkbutton1.get() == 1:
        messagebox.showinfo('Cursos', 'Bienvenido a Programación Python!')
    elif Checkbutton2.get() == 1:
        messagebox.showinfo('Cursos', 'Bienvenido a Machine Learning!')
    elif Checkbutton3.get() == 1:
        messagebox.showinfo('Cursos', 'Bienvenido a AWS Lambda Functions!')


root = Tk()
root.geometry("300x200")

l_frame = LabelFrame(root, text='Seleccione sus Cursos')
l_frame.pack()

Checkbutton1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

Button1 = Checkbutton(l_frame, text="Programación Python",
                      variable=Checkbutton1,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      padx=2,
                      command=isChecked)

Button2 = Checkbutton(l_frame, text="Machine Learning",
                      variable=Checkbutton2,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      padx=2,
                      command=isChecked)

Button3 = Checkbutton(l_frame, text="AWS Lambda Fuctions",
                      variable=Checkbutton3,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      padx=2,
                      command=isChecked)

Button1.pack()
Button2.pack()
Button3.pack()

mainloop()