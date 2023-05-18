import turtle

def dibuja_cuadrado(t, pasos):
    """La tortuga t dibujara un cuadrado con lados = pasos."""

    for i in range(4):
        t.forward(pasos)
        t.left(90) # angulo del giro

wn = turtle.Screen()       # define los atributos de la ventana

alex = turtle.Turtle()     # crea una tortuga llamada alex
alex.shape("turtle")
dibuja_cuadrado(alex, 150) # llama a la función pasando los argumentos alex y 150

wn.exitonclick() # cierra la ventana al hacer clic