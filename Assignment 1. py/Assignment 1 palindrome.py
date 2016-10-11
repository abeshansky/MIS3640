print('FIND THE PALINDROME')

# if word and reverse word are the same, then return True
inputStr = str(input("Enter a string:"))
def isPalindrome(inputStr):
     i=0
     while i <= len(inputStr)/2:
         if inputStr[i] != inputStr[-i - 1]:
             print("That isn't a palindrome.")
             return False
         i+=1
         #checks if first and last letter are the same, then second and second to last, etc.
         print("That's a palindrome.")
         return True