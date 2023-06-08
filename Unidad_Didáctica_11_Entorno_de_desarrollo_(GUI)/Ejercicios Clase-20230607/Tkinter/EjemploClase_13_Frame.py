from tkinter import *

root = Tk()
root.title('Mi GUI Python')
root.geometry('250x200')

# Crear el frame para las etiquetas
frame1 = Frame(root, padx=5, pady=5)
frame1.grid(row=0, column=1)

Label(frame1, text='Usuario: ', padx=5, pady=5).pack()
Label(frame1, text='Email: ', padx=5, pady=5).pack()
Label(frame1, text='Password: ', padx=5, pady=5).pack()

# Crear el frame para las entradas
frame2 = Frame(root, padx=5, pady=5)
frame2.grid(row=0, column=2)

Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)
Entry(frame2).pack(padx=5, pady=5)

Button(root, text='Guardar', padx=10).grid(row=1, columnspan=5, pady=5)

root.mainloop()