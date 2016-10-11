print('FIND ALL THE FACTORS')
def prime_factors():
    x = int(input('Please input your number!'))
    factorlist = []
    number = 2
    if x == 1:
        return 1
    else:
        while number <= x:
            #will only check for numbers less than x
            while x%number == 0:
                factorlist.append(number)
                #will add the number to the list as a factor if it is evenly divisible
                x = x/number
            number +=1
            #increases number by 1 if it is no longer divisible
        return (factorlist)
        #returns the complete list of factors for x

print (prime_factors())

############################################

print('FIND THE PALINDROME')

# if word and reverse word are the same, then return True
inputStr = input("Enter a string:")
def isPalindrome(inputStr):
    i=0
    while i <= len(inputStr)/2:
        if inputStr[i] != inputStr[-i - 1]:
            return False
        i+=1
        #checks if first and last letter are the same, then second and second to last, etc.
        return True
   if True:
        print("That's a palindrome.")
   else:
        print("That isn't a palindrome")

print(isPalindrome('deed'))
print(isPalindrome('rotor'))
print(isPalindrome('aibohphobia'))
print(isPalindrome('hello'))

###################################################################

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

######################################################
