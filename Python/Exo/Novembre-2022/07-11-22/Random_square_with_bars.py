import turtle as t
import line_function

window = t.Screen()
window.setup(width=2000, height=2000, startx=0, starty=0)
window.title(" Turtle ")

t.color("aqua")
t.bgcolor("black")
t.speed(0)
t.penup()
t.setposition(-300, -300)
t.pendown()


# taper votre code ci-dessous
t.hideturtle()
for i in range(4):
    t.forward(line_function.c)
    t.left(line_function.a)
line_function.line()

# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()
