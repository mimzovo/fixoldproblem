# -------------------------------------------------
#        Name: Mignote Tadesse, Oluwakemi Adebagbo
#    Filename: lab12.py
#        Date: July 25, 2019
#
# Description: Fibonacci and Fractals
# -------------------------------------------------


# ------- START ATTRIBUTED CODE SECTION -------
# Code created with the help of Elliott Saslow
# https://blog.goodaudience.com/fractals-and-recursion-in-python-d11d87fcf9cd
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
for i in range(60):
    draw_square()
    turtle.left(i)
# --------- END ATTRIBUTED CODE SECTION --------
