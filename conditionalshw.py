print('Exercise 2.1')
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

print('Exercise 2.2')
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(3))

print('Exercise 2.3')

def gcd(a, b):
    while b:
        c = a%b
        a = b
        b = c
    return a

print(gcd(88,230))

input()