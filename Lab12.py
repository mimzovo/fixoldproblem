# -------------------------------------------------
#        Name: Mignote Tadesse, Oluwakemi Adebagbo
#    Filename: lab12.py
#        Date: July 25, 2019
#
# Description: Fibonacci and Fractals
# -------------------------------------------------

import turtle
import time
def draw_square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.color('green')
for i in range(360):
    draw_square()
    turtle.left(i)
