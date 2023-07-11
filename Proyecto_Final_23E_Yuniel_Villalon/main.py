# Proyecto Final 23E Yuniel Antonio Villalón Rosales
from tkinter import *
# Importar Librerias

#Importar modulos propios
from cargar_datos import cargar_datos_bbdd as bd
from GUI import funciones as fun
from GUI import main_screen as gu

# Programa principal
conexion = bd.conexion_bd("bbdd/video_juegos.db")

v_principal = Tk()
v_principal.title("Proyecto Final Yuniel Villalón")
v_principal.geometry(newGeometry='600x400')
v_principal.resizable(0, 0)
v_principal.iconbitmap('GUI\idea.ico')
menubar = Menu(v_principal)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Base de Datos', menu=file)
file.add_command(label='Carga Inicial', command=lambda :fun.carga_datos_inicial(conexion))
file.add_command(label='Borrar Datos', command=lambda :fun.eliminar_datos(conexion))
file.add_separator()
file.add_command(label='Salir', command=v_principal.destroy)
v_principal.config(menu=menubar)
VPrincipal = gu.Windows(v_principal)
v_principal.mainloop()