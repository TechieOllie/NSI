import turtle as t


t.pencolor("black")

t.penup()
t.goto(-200, -200)
t.pendown()
t.speed(8)
t.colormode(255)


a = 400
a2 = 2*a
# t.hideturtle()


def house():
    for i in range(2):
        t.forward(a)
        t.left(90)
        t.forward(a/3.5)
        t.left(90)
    t.forward(a/2)
    t.left(90)
    t.forward(a/3.5)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    t.right(90)
    t.forward(a/8)
    t.left(90)
    t.forward((a/3.8)-10)
    t.right(90)
    t.forward(a/3.8)
    t.right(90)
    t.forward((a/3.8)-10)
    t.right(180)
    for x in range(10):
        t.forward(a/46)
        t.left(90)
        t.forward((a/3.8))
        t.back((a/3.8))
        t.right(90)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    t.right(90)
    t.forward(a/2)
    t.forward(a/10)
    t.left(90)
    t.penup()
    t.forward(a/46)
    t.pendown()
    for y in range(2):
        t.forward(a/6)
        t.right(90)
        t.forward(a/16)
        t.right(90)
    t.left(180)
    t.penup()
    t.forward(a/46)
    t.pendown()
    t.left(90)
    t.forward(a/10)
    t.left(90)
    t.fillcolor(139, 69, 19)
    t.begin_fill()
    for n in range(2):
        t.forward(a/6)
        t.right(90)
        t.forward(a/12)
        t.right(90)
    t.end_fill()
    t.right(90)
    t.penup()
    t.forward(a/12)
    t.back(a/86)
    t.left(90)
    t.forward(a/12)
    t.pendown()
    t.fillcolor(255, 255, 255)
    t.begin_fill()
    t.circle(a/160)
    t.end_fill()
    t.penup()
    t.back(a/12)
    t.right(90)
    t.pendown()
    t.forward(a/86)
    t.forward(a/24)
    t.left(90)
    t.penup()
    t.forward(a / 46)
    t.pendown()
    for y in range(2):
        t.forward(a / 6)
        t.right(90)
        t.forward(a / 16)
        t.right(90)


if __name__ == "__main__":
    house()


t.exitonclick()
t.mainloop()
