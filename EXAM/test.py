trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu','10':'shi', '100':'bai'}
def speak_Chinese(number):
    '''
    number: a integer, 0<=number<99
    Returns: a string that is the number in Chinese
    '''
if int(number) >= 20 and int(number) <= 99:
    count = 0
    a = int(number)
    while a - 10 > 0:
        a = a - 10
        count = count + 1
    ten = str(count)
    one = str(a)
if a != 0:
    return trans[ten] + " " + "shi" + " " + trans[one]
else:
    return trans[ten] + " " + "shi"

print(speak_Chinese('20'))