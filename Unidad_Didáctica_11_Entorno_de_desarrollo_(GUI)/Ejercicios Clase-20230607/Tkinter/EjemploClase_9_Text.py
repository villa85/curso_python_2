from tkinter import *

root = Tk()
root.geometry("700x300")

# Create text widget and specify size.
T = Text(root, undo=True, maxundo=100,
         spacing1=10, spacing2=2,
         spacing3=5, height=5, wrap='char'
)

# Creatr una etiqueta
etiqueta = Label(root, text="Comentario")
etiqueta.config(font=("Courier", 14))

Comentario = """Es un producto de buena calidad...
la relación precio valor es excelente"""

# Crear botón Siguiente
boton_1 = Button(root, text="Siguiente...", )

# Crear botón Salir
boton_2 = Button(root, text="Salir",   command=root.destroy)

etiqueta.pack()
T.pack()
boton_1.pack()
boton_2.pack()

# Insertar Texto y la variable Comentario
T.insert(INSERT, "Comentario.....")
T.insert(END, Comentario)

# Obtener el contenido del texto
contents = T.get('1.0', 'end') # Extrae todo el texto
print(contents)

root.mainloop()
