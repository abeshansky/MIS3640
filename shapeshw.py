import turtle
import math
alex = turtle.Turtle()

def polygon(t, length, n):
    t.speed("fastest")
    t.lt(60)
    t.fd(length)
    t.lt(120)
    t.fd(length)
    t.lt(120)
    t.fd(length)
    for i in range(n):
        t.lt(30)
        t.fd(length)
        t.lt(120)
        t.fd(length)
        t.lt(120)
        t.fd(length)

    radius = length/math.sqrt(3) #calculating the radius
    turtle.penup()
    turtle.goto(0,-120)
    turtle.pendown()
    turtle.circle(110)

# def circle(t, r):
#    circumference = 2 * math.pi * r
#    n = int(circumference / 3) + 1
#    length = circumference / n
#    polygon(t, n, length)


polygon(alex, 100, 3)
turtle.mainloop()