import math
def quads():
    print('Let us run a quadratic equation')
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    c = int(input('enter c: '))
    print()
    if 4*a*c > b**2:
        return "FAIL"
    else:
        disc = (b**2) - (4*a*c)
        disc1 = sqrt(disc)
        answer1 = (-b+disc1)/(2*a)
        answer2 = (-b-disc1)/(2*a)
        print ('The answers are {0} and {1}'.format(answer1.answer2))