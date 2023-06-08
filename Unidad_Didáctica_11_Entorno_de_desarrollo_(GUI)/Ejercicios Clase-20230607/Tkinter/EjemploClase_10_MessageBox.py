from tkinter import *
from tkinter import messagebox

def pregunta():
    # Mensaje de Error
    messagebox.showerror("ERROR", "Disculpe, no hay preguntas disponibles")

def salir():
    # Mensaje Si o No
    if  messagebox.askyesno('Verificar', '¿Realmente quiere salir?'):
        # Mensaje de Alerta
        messagebox.showwarning('Si', 'No está implementado')
    else:
        # Mensaje de tipo información
        messagebox.showinfo('No', 'Salir fue cancelado')

root = Tk()
root.geometry("300x200")

messagebox.showinfo('Información', 'Bienvenido al sistema XYZ')
Button(text='Salir', command=salir).place(x=170, y=150)
Button(text='Pregunta', command=pregunta).place(x=210, y=150)

root.mainloop()