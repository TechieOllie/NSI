import turtle as t

window = t.Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("orangered")
t.speed(10)
t.penup()
t.setposition(-300,200)
t.pendown()



# taper votre code ci-dessous

    
for a in range(4):
    t.right(90)
    t.forward(100)
t.forward(100)
for i in range(4):
    t.right(90)
    t.forward(100)
t.right(90)
t.forward(100)
for y in range(3):
    t.forward(100)
    t.right(90)
t.right(180)
for x in range(4):
    t.forward(100)
    t.right(-90)



# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()