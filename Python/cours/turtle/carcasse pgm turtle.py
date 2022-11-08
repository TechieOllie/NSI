# -*- coding): utf-8 -*-

# https://docs.python.org/3/library/turtle.html#turtle.Screen


import turtle as t

window = t.Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.speed(0)
t.penup()
t.setposition(-300,200)
t.pendown()



# taper votre code ci-dessous












# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()