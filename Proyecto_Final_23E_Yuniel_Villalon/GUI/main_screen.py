# import pandas as pd
from tkinter import *
from tkinter.ttk import *



# class TestApp(Frame):

#     def __init__(self, parent = None, df = pd.DataFrame()):
#         self.parent = parent
#         Frame.__init__(self)
#         self.main = self.master
#         self.main.geometry('600x400+200+100')
#         self.main.title('Table app')
#         f = Frame(self.main)
#         f.pack(fill=BOTH, expand=True)
#         self.table = pt = Table(f, dataframe=df,
#                                 showtoolbar=True,
#                                 editable=False,
#                                 showstatusbar=True)
#         pt.show()
#         return

class Windows:

    def __init__(self, principal):
        self.principal = principal
        self.option = IntVar(value=0)
        self.principal.title("Proyecto Final Yuniel Villalón")
        self.principal.iconbitmap('GUI\idea.ico')
        self.menubar = Menu(principal)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Base de Datos', menu=self.file)
        self.file.add_command(label='Carga Inicial', command=None)
        self.file.add_command(label='Borrar Datos', command=None)
        self.file.add_separator()
        self.file.add_command(label='Salir', command=principal.destroy)
        self.principal.config(menu=self.menubar)

        self.etiqueta = Label(principal, text="Elija opción",
                            font=('Arial 14 bold'))
        self.etiqueta.pack()
        self.etiqueta_opc1 = Label(principal, text="1. Consulta por palabra clave y por rango de fechas", font=('Arial 12')).place(x=40, y=60)
        self.etiqueta_opc2 = Label(principal, text="2. Consulta de comentarios por usuario", font=('Arial 12')).place(x=40, y=90)
        self.etiqueta_opc3 = Label(principal, text="3. Consulta de mensajes promedio por día", font=('Arial 12')).place(x=40, y=120)
        self.etiqueta_opc4 = Label(principal, text="4. Consulta de comentarios de un tema por red social", font=('Arial 12')).place(x=40, y=150)

        # self.etiqueta_select =

if __name__ == '__main__':
    v_principal = Tk()
    v_principal.title('Mi App Python')
    v_principal.geometry(newGeometry='600x400')
    v_principal.resizable(0, 0)
    VPrincipal = Windows(v_principal)
    v_principal.mainloop()


# root = Tk()
# root.geometry(newGeometry='800x600')
# root.resizable(0, 0)

# root.title("Proyecto Final Yuniel Villalón")
# root.iconbitmap('GUI\idea.ico')

# # Crear la Barra de Menu
# menubar = Menu(root)

# # Creando el Menú File y sus opciones
# file = Menu(menubar, tearoff=0)
# menubar.add_cascade(label='Base de Datos', menu=file)
# file.add_command(label='Carga Inicial', command=None)
# file.add_command(label='Borrar Datos', command=None)
# file.add_separator()
# file.add_command(label='Salir', command=root.destroy)

# # Mostrar Menú
# root.config(menu=menubar)

# label = Label(root, text="¡Bienvenidos!").pack()

# root.mainloop()