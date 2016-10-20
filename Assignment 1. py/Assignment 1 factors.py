print('FIND ALL THE FACTORS')
def prime_factors():
    x = int(input('Please input your number!'))
    #asks the user to input a number
    factorlist = []
    #creates the list which stores the factors
    number = 2
    #begins to see if number is divisible by 2
    if x == 1:
        return 1
    else:
        while number <= x:
            #factors must be less than the original number (x)
            while x%number == 0:
                #checks to see if x is divisible by the number
                factorlist.append(number)
                #will add the number to the factor list as a factor if it is evenly divisible
                x = x/number
                #x is then made smaller but the divisor of the factor
            number +=1
            #increases number by 1 if it is no longer divisible to move on to the next number
        return (factorlist)
        #returns the complete list of factors for x

print (prime_factors())