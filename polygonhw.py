import turtle

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

jude = turtle.Turtle()
polygon(jude, 150, 4)

jerry = turtle.Turtle()
square(jerry, 100)

teresa = turtle.Turtle()
square(teresa, 250)

import math
def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference/n
    polygon(t, n, length)

chris = turtle.Turtle()
circle(chris, 30)