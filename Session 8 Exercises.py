#Exercise 1
prefixes = 'JKLMNOPQ'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        suffix = 'uack'
    else:
        suffix = 'ack'
    print(letter + suffix)

# Exercise 2
word = 'New England Patriots'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

team = 'New England Patriots'
index = team.find('a')
print(index)

# Exercise 4
import string
alphabet = string.ascii_lowercase()
def price_find(food):
    for i in alphabet:
        price[i] = (ord(i)) - 96
    sum(price)
food = 'bananas'
print(price_find(food))

# Exercise 5
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('food'))
print(any_lowercase1('Food'))
print(any_lowercase1('foOd'))
# checks if first letter is lower case

        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2('food'))
print(any_lowercase2('FoodtruCk'))
print(any_lowercase2('foOdtruck'))
checks if 'c' is lowercase. always True