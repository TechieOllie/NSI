import turtle as t
import random as r

window = t.Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("orangered")
t.speed(0)
t.penup()
t.setposition(-100, -200)
t.pendown()



# taper votre code ci-dessous
   
a =  r.randint(10, 600) 
for i in range(5):
    t.forward(a)
    t.left(90)
t.right(30)
t.forward(a/2)
t.left(30)
t.forward(a)
t.left(150)
t.forward(a/2)
t.back(a/2)
t.right(60)
t.forward(a)
t.left(60)
t.forward(a/2)
    




# conserver pour la gestion de la fenêtre

window.exitonclick()
t.mainloop()
t.done()