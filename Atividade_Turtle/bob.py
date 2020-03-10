import turtle
import math
bob = turtle.Turtle()

#Exercitando bob
def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
    turtle.mainloop()
    print(t)

def polygon(t, n, lenght):
    anglo = 360/n
    polyline(t, n, lenght, anglo)

def circle(t, r):
    arc(t, r, 360)

def arc(t, r, angle):
    tam_arco = 2 * math.pi * r * angle / 360
    n = int(tam_arco / 3) + 1
    step_tam = tam_arco / n
    step_anglo = float(angle) / n
    polyline(t, n, step_tam, step_anglo)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

#Flores
def petalas(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)

def flores(t, n, r, angle):
    for i in range(n):
        petalas(t, r, angle)
        t.lt(360/n)

#Tortas (Em revisão)
def torta(t, n, lenght):
    for i in range(n):
        polygon(t, 3, lenght)
        t.lt(360 / n)

torta(bob, 7, 60)

