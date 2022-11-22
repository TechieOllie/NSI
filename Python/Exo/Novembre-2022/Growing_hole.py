import random as r
import turtle as t

window = t.Screen()
window.setup(width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("black")
t.speed(0)
t.penup()
t.setposition(0, -600)
t.pendown()


t.colormode(255)
d = -600
y = 100
# taper votre code ci-dessous

for i in range(255):
    a = r.randint(1, 255)
    b = r.randint(1, 255)
    c = r.randint(1, 255)
    t.pencolor(a, b, c)
    y = y + 10
    t.circle(y)
    d = d + 1
    t.sety(d)


# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()
