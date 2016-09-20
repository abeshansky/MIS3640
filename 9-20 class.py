print(2**38)

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

age = int(input('How old are you?'))
if age >= 21:
    print('Your age is {}.'.format(age))
    print('Your age is'+str(age)+'.')
    print('Yes, you can.')
elif age >=6:
    print ('Your age is ', age)
    print('You are a teenager. No, you cannot.')
else:
    print('our age is ',age)
    print('No, not allowed')

x = 1
y = 2
if x==y:
    print('x and y are equal.')
else:
    if x<y:
        print('x is less than y.')
    else:
        print('x is greater than y.')

print ('Welcome to the BMI Calculator')
weight = input('What is your weight in pounds?')
height = input('What is your height in inches?')
weight = float(weight)
height = float(height)
BMI = 703*(weight/(height**2))
if BMI <= 18.5:
    print ('Your BMI is %.1f. Eat some pizza.')
else:
    if BMI >18.5 and BMI <= 24.9:
        print ('You are gucci.')
    else:
        if BMI >25 and BMI <= 29.9:
            print ('you better watch be careful.')
        else:
            print ('LOSE SOME WEIGHT.')

def countdown(n):
        if n<=0:
            print('Blastoff!')
        else:
            print (n)
            countdown(n-1)

countdown(3)

def print_n(s, n):
    if n<=0:
        return
    print(s)
    print_n(s, n-1)
print_n('Hello.', 3)

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))

# do 2.3 and 2.4 for homework

input()