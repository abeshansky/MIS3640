def print_lyrics():
    print("Hey Jude. Don't make it bad.")
    print("Take a sad song and make it better.")

print(type(print_lyrics))
print_lyrics()

def repeat_lyrics():
    print_lyrics()
    print('Na - na - na - na - na, na - na - na - na')
    print_lyrics()

repeat_lyrics()


def print_twice(a):
        print(a)
        print(a)

my_name = 'Alex'
print_twice(my_name)

def my_abs(n):
    if n>=0:
        print(n)
    else:  
        print(-n)
my_abs(-23)

def my_abs(n):
    if isinstance(n, int) or isinstance(n, float):
        if n>=0:
            return(n)
        else:  
            return(-n)
    else:
        print('invalid value')
print (my_abs('jerry'))

def give_me_a_break():
    str1 = 'break'
    print('another break')
    return str1
print(give_me_a_break())

new_str= give_me_a_break()

print(give_me_a_break())



input()