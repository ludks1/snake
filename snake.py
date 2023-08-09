import turtle
import time
import random

posponer = 0.1

# marcador
score = 0
high_score = 0

# se crea la pantalla donde se va a jugar
ventana = turtle.Screen()

ventana.title("Juego de la viborita")
ventana.bgcolor("black")
ventana.setup(width=600, height=600)
ventana.tracer(0)

# cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.color("white")
cabeza.direction = "stop"

# cuerpo de la serpiente
cuerpo = []

# comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0, 100)
comida.color("orange")

# Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Score: 0       High Score: 0", align="center",
            font=("Courtier", 24, "normal"))

# funciones


def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


# teclado
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")


def movimiento():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# acutualizacion de la ventana
while True:
    ventana.update()
    # colisiones borde
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"
        # eliminar cuerpo
        [i.hideturtle() for i in cuerpo]
        cuerpo.clear()
    # resetear marcador
        score = 0
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score),
        align="center", font=("Courtier", 24, "normal"))
    # colicion con la comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.speed(0)
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.color("grey")
        cuerpo.append(nuevo_cuerpo)

        # aumentar marcador
        score += 10
        if score > high_score:
            high_score = score
        texto.clear()
        texto.write("Score: {}       High Score: {}".format(score, high_score),
                    align="center", font=("Courtier", 24, "normal"))
    # cuerpo de la serpiente en movimiento
    total_cuerpo = len(cuerpo)
    for index in range(total_cuerpo - 1, 0, -1):
        x = cuerpo[index-1].xcor()
        y = cuerpo[index-1].ycor()
        cuerpo[index].goto(x, y)
    if total_cuerpo > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        cuerpo[0].goto(x, y)

    movimiento()
    # colision con el cuerpo
    for colision in cuerpo:
        if colision.distance(cabeza)<20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"
            # eliminar cuerpo
            [i.hideturtle() for i in cuerpo]
            cuerpo.clear()
        # resetear marcador
            score = 0
            texto.clear()
            texto.write("Score: {}       High Score: {}".format(score, high_score),
            align="center", font=("Courtier", 24, "normal"))

    time.sleep(posponer)
