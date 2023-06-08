from tkinter import *

# Crear primer Panel
screen = PanedWindow(bg="red")
screen.pack(fill=BOTH, expand=1)

# Inserta etiqueta al primer panel
left = Label(screen, text="Panel Izquierdo" , bg="green")
screen.add(left)

# Crear segundo Panel
m2 = PanedWindow(screen, orient=VERTICAL) #HORIZONTAL
screen.add(m2)

# Insertar etiquetas
top = Label(m2, text="Panel superior")
m2.add(top)
top1 = Label(m2, text="Panel superior 2")
m2.add(top1)

# Crear tercer Panel
m3 = PanedWindow(screen,bg="blue" ,orient=HORIZONTAL) #HORIZONTAL
m2.add(m3)

# Insertar etiqueta
bottom = Label(m3, text="Panel inferior",bg="blue")
m3.add(bottom)

mainloop()