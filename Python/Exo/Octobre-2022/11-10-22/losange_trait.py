import turtle as t

window = t.Screen()
window.setup(width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("orangered")
t.speed(10)
t.penup()
t.setposition(-300, 200)
t.pendown()

# taper votre code ci-dessous

t.forward(100)
t.right(45)


# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()
