print('THE DRUNKARDS WALK')
import math
# import math to use sqrt function
import random
# import random to allow to choose a random direction
def Drunk_Walk():
    x = 0
    y = 0
    # creates the starting point (0,0)
    n = int(input('How many times would you like to move?'))
    # asks the user how many times to go through the simulation
    distance = 0
    # creates the initial distance as 0 from the starting point
    for i in range(n):
        a = random.randint(1,4)
        if a == 1:
            y = y + 1
            i =+1
        if a == 2:
            x = x + 1
            i =+1
        if a == 3:
            y = y - 1
            i =+1
        if a == 4:
            x = x - 1
            i =+ 1
    new_x = (x)^2
    new_y = (y)^2
    distance = math.sqrt(new_x + new_y)
    print("After the Drunkard has walked", n, "intersections, he is now", distance, "blocks from where he started.")
Drunk_Walk()