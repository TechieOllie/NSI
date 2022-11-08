import turtle as t
import random as r

c = r.randint(10, 600)
a = 90


def line():
    t.forward(c / 2)
    t.left(a)
    t.forward(c)
    t.penup()
    t.left(a)
    t.forward(c / 2)
    t.left(90)
    t.forward(c / 2)
    t.left(90)
    t.pendown()
    t.forward(c)
