from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)

def mostrar_grafico():
    fig = Figure(figsize=(5, 5), dpi=100)
    y = [i ** 2 for i in range(101)]
    plot1 = fig.add_subplot(111)
    plot1.plot(y)

    # Creamos el canvas o área donde se mostrara el gráfico
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

root = Tk()
root.title('Mostrar un gráfico con Tkinter')
root.geometry("500x500")

Label(root, text="Gráfico XYZ", font=('calibre',12, 'bold')).pack()

mostrar_grafico()
root.mainloop()