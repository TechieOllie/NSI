import turtle as t

window = t.Screen()
window.setup(width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("orangered")
t.speed(4)
t.penup()
t.setposition(-300, 200)
t.pendown()



# taper votre code ci-dessous

t.right(90)
t.forward(300)
t.back(150)
print(t.xcor())
t.penup()
t.setx(-450)
t.pendown()
t.left(90)
t.forward(300)
t.back(150)
t.left(45)
t.forward(75)
t.back(150)
t.forward(75)
t.right(90)
t.forward(75)
t.back(150)



# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()