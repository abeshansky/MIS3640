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