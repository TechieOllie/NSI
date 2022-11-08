import turtle as t

window = t.Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("black")
t.speed(10)
t.penup()
t.setposition(-300,200)
t.pendown()



# taper votre code ci-dessous

t.hideturtle()
t.pendown()
for i in range(2):
    for i in range(4):
        t.forward(100)
        t.right(90)
    t.left(45)
    t.forward(50)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.left(135)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.penup()
    t.setx(10)
    t.pendown()




# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()