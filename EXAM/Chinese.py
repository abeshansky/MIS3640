trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu','10':'shi', '100':'bai'}
def speak_Chinese(number):
    '''
    number: a integer, 0<=number<99
    Returns: a string that is the number in Chinese
    '''
    if int(number) <= 10:
        a = trans[number]
        return a
    if int(number) > 10 and int(number) < 20:
        a = str(int(number) - 10)
        b = trans[a]
        return "shi" + " " + b
    if int(number) >= 20 and int(number) <=99:
        count = 0
        a = int(number)
        while a - 10 >= 0:
            a = a - 10
            count = count + 1
        ten = str(count)
        one = str(a)
        if a != 0:
            return trans[ten] + " " + "shi" + " " + trans[one]
        else:
            return trans[ten] + " " + "shi"
    if int(number) % 100 == 0:
        count = 0
        a = int(number)
        while a - 100 >= 0:
            a = a - 100
            count = count + 1
        hundred = str(count)
        return trans[hundred] + " " + "bai"
    if int(number) >100 and int(number) <=999 and int(number) % 100 != 0:
        count_a = 0
        a = int(number)
        while a - 100 >= 0:
            a = a - 100
            count_a = count_a + 1
        hundred = str(count_a)
        b = int(number) - 100*count_a
        count_b = 0
        while b - 10 >= 0:
            b = b - 10
            count_b = count_b + 1
        ten = str(count_b)
        c = int(number) - count_a*100 - count_b*10
        one = str(c)
        if int(number[1]) != 0:
            return trans[hundred] + " " + "bai" + " " + trans[ten] + " " + "shi" + " " + trans[one]
        else:
            return trans[hundred] + " " + "bai" + " " + "ling" + " " + trans[one]
    if int(number) >100 and int(number) <=999 and int(number) % 100 != 0:
        count = 0
        a = int(number)
        if int(number[0]) != 0:
            return trans[hundred] + " " + "bai" + " " + trans[ten] + " " + "shi" + " " + trans[one]
        else:
            return trans[hundred] + " " + "bai" + " " + "ling" + " " + trans[one]   


# For testing
def main():
    print(speak_Chinese('36'))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese('20'))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese('16'))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese('109'))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese('999'))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()