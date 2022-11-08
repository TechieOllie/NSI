import turtle as t

window = t.Screen()
window.setup (width=2000, height=2000, startx=0, starty=0)
window.title(" 1ere - Turtle ")

t.color("aqua")
t.bgcolor("black")
t.speed(0)
t.penup()
ypos = -400
xpos = 0
t.setposition(0,ypos)
t.pendown()



# taper votre code ci-dessous
t.colormode(255)
for i in range(255):
    t.pencolor(i, 255-i,i)
    t.circle(i+255)
    ypos = ypos + 1
    xpos = xpos + 1
    t.sety(ypos)
    t.setx(xpos)
    
   




# conserver pour la gestion de la fenêtre
window.exitonclick()
t.mainloop()
t.done()