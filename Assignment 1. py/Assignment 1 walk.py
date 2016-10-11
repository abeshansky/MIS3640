print('THE DRUNKARDS WALK')
import math
import random
def Drunk_Walk():
    x = 0
    y = 0
    n = 4
    distance = 0
    # sets starting point at (0,0)
    for i in range (1,n):
        i = 1
        a = random.randint(1,4)
        # randomly selects one of the four routes, four times
        if a == 1:
            x = x+0
            y = y+1
            i =+1
            # will move from the previous point and move on to the next round
        if a == 2:
            x = x+1
            y = y+0
            i =+1
        if a == 3:
            x = x+0
            y = y-1
            i =+1
        if a == 4:
            x = x-1
            y = y+0
            i =+1
    new_x = (x)^2
    new_y = (y)^2
    distance = math.sqrt(new_x + new_y)
    #solves for the diagonal distance from the starting point
    print(distance)
    return distance

Drunk_Walk()

import turtle
if a == 1:
    t.fd(100)
if a == 2:
    t.rt(90)
    t.fd(100)
if a == 3:
    t.bk(100)
else:
    t.lt(90)
    t.fd(100)

turtle.Turtle()
Drunk_Walk(AleX)