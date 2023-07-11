import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pandastable import Table
from datetime import datetime

from cargar_datos import cargar_datos_bbdd as bd
from obtener_datos import consultar_datos as cd


FORMATO = "%Y-%m-%d"
hoy = datetime.today()
FECHA_P = hoy.strftime(FORMATO)

conexion = bd.conexion_bd("bbdd/video_juegos.db")

class TestApp(Frame):

    def __init__(self, parent = None, df = pd.DataFrame()):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('Consulta')
        f = Frame(self.main)
        f.pack(fill=BOTH, expand=True)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=False,
                                editable=False,
                                showstatusbar=True)
        pt.show()
        return

class Secondary_window(Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('GUI\idea.ico')
        self.config(width=300, height=200)
        self.title("Consulta")
        self.palabra_clave = StringVar()
        self.fecha_inicio = StringVar(value=cd.busca_fecha_menor_mensaje())
        self.fecha_final = StringVar(value=FECHA_P)

        self.etiqueta_palabra_clave = Label(self, text="Palabra Clave:").place(x=20, y=50)
        self.entrada_palabra_clave = Entry(self,  textvariable=self.palabra_clave).place(x=104, y=50)
        self.etiqueta_fecha_inicio = Label(self, text="Fecha Inicio:").place(x=20, y=80)
        self.entrada_fecha_inicio = Entry(self,  textvariable=self.fecha_inicio).place(x=104, y=80)
        self.etiqueta_fecha_final = Label(self, text="Fecha Final:").place(x=20, y=110)
        self.entrada_fecha_final = Entry(self,  textvariable=self.fecha_final).place(x=104, y=110)
        self.boton_enviar = Button(self, text="Enviar", command=self.consultar).place(x=90, y=150)
        self.boton_cerrar = Button(self, text="Cerrar", command=self.destroy).place(x=180, y=150)
        self.focus()
        self.grab_set()

    def consultar(self):
        clave = self.palabra_clave.get()
        f_inicio = self.fecha_inicio.get()
        f_final = self.fecha_final.get()
        df = cd.consultar_comentarios_fecha(conexion, clave, f_inicio, f_final)
        app = TestApp(self, df)
        app.mainloop()

class Secondary_window_2(Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('GUI\idea.ico')
        self.config(width=300, height=200)
        self.title("Cosulta")
        self.palabra_clave = StringVar()

        self.etiqueta_palabra_clave = Label(self, text="Palabra Clave:").place(x=20, y=50)
        self.entrada_palabra_clave = Entry(self,  textvariable=self.palabra_clave).place(x=104, y=50)
        self.boton_enviar = Button(self, text="Enviar", command=self.consultar).place(x=80, y=100)
        self.boton_cerrar = Button(self, text="Cerrar", command=self.destroy).place(x=180, y=100)
        self.focus()
        self.grab_set()

    def consultar(self):
        clave = self.palabra_clave.get()
        df = cd.consultar_comentarios_cantidad(conexion, clave)
        app = TestApp(self, df)
        app.mainloop()

class Secondary_window_3(Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('GUI\idea.ico')
        self.config(width=300, height=200)
        self.title("Cosulta")
        self.fecha_inicio = StringVar(value=cd.busca_fecha_menor_mensaje())
        self.fecha_final = StringVar(value=FECHA_P)

        self.etiqueta_fecha_inicio = Label(self, text="Fecha Inicio:").place(x=20, y=80)
        self.entrada_fecha_inicio = Entry(self,  textvariable=self.fecha_inicio).place(x=104, y=80)
        self.etiqueta_fecha_final = Label(self, text="Fecha Final:").place(x=20, y=110)
        self.entrada_fecha_final = Entry(self,  textvariable=self.fecha_final).place(x=104, y=110)
        self.boton_enviar = Button(self, text="Enviar", command=self.consultar).place(x=90, y=150)
        self.boton_cerrar = Button(self, text="Cerrar", command=self.destroy).place(x=180, y=150)
        self.focus()
        self.grab_set()

    def consultar(self):
        f_inicio = self.fecha_inicio.get()
        f_final = self.fecha_final.get()
        df = cd.consultar_media_mensajes(conexion, f_inicio, f_final)
        app = TestApp(self, df)
        app.mainloop()

class Secondary_window_4(Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.iconbitmap('GUI\idea.ico')
        self.config(width=300, height=200)
        self.title("Cosulta")
        self.palabra_clave = StringVar()

        self.etiqueta_palabra_clave = Label(self, text="Palabra Clave:").place(x=20, y=50)
        self.entrada_palabra_clave = Entry(self,  textvariable=self.palabra_clave).place(x=104, y=50)
        self.boton_enviar = Button(self, text="Enviar", command=self.consultar).place(x=80, y=100)
        self.boton_cerrar = Button(self, text="Cerrar", command=self.destroy).place(x=180, y=100)
        self.focus()
        self.grab_set()

    def consultar(self):
        clave = self.palabra_clave.get()
        df = cd.stadisticas_mensaje(conexion, clave)
        app = TestApp(self, df)
        app.mainloop()


class Windows:

    def __init__(self, principal):
        self.principal = principal
        self.opcion = IntVar(value=0)


        self.etiqueta = Label(principal, text="Elija opción",
                            font=('Arial 14 bold'))
        self.etiqueta.pack()
        self.etiqueta_opc1 = Label(principal, text="1. Consulta por palabra clave y por rango de fechas", font=('Arial 12')).place(x=40, y=60)
        self.etiqueta_opc2 = Label(principal, text="2. Consulta de comentarios por usuario", font=('Arial 12')).place(x=40, y=90)
        self.etiqueta_opc3 = Label(principal, text="3. Consulta de mensajes promedio por día", font=('Arial 12')).place(x=40, y=120)
        self.etiqueta_opc4 = Label(principal, text="4. Consulta de comentarios de un tema por red social", font=('Arial 12')).place(x=40, y=150)

        self.etiqueta_select = Label(principal, text="Introduzca su opción", font=('Arial 12 bold')). place(x=100, y=250)
        self.etiqueta_select2 = Entry(principal,textvariable=self.opcion, width=10).place(x=270, y=253)
        self.botonProcesar = Button(principal, text="Enviar")
        self.botonProcesar.place(x=180, y=300)
        self.botonCerrar = Button(principal, text="Cerrar", command=principal.quit)
        self.botonCerrar.place(x=280, y=300)
        self.botonProcesar.configure(command=self.procesar)

    def open_secondary_window(self):
        self.secondary_window = Secondary_window()

    def open_secondary_window_2(self):
        self.secondary_window = Secondary_window_2()

    def open_secondary_window_3(self):
        self.secondary_window = Secondary_window_3()

    def open_secondary_window_4(self):
        self.secondary_window = Secondary_window_4()

    def procesar(self):

        if self.opcion.get() in range(1,5):
            if self.opcion.get() == 1:
                self.open_secondary_window()
            elif self.opcion.get() == 2:
                self.open_secondary_window_2()
            elif self.opcion.get() == 3:
                self.open_secondary_window_3()
            elif self.opcion.get() == 4:
                self.open_secondary_window_4()
        else:
            messagebox.showerror("ERROR", "Solo valores válidos entre 1-4")