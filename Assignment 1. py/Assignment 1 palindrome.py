print('FIND THE PALINDROME')

# if word and reverse word are the same, then return True
def isPalindrome(s):
     i=0
     #creates a started point for the letter
     while i <= len(inputStr)/2:
         #checks to see if the letter is in the first half of the word
         if inputStr[i] != inputStr[-i - 1]:
             #checks if that letter is the same as the letter in its opposite place on the other side of the word
             print("That isn't a palindrome.")
             return False
         i+=1
         #checks if first and last letter are the same, then second and second to last, etc.
         print("That's a palindrome.")
         return True

inputStr = input("Enter a string: ")
#asks the user to enter a word to check
isPalindrome(inputStr)