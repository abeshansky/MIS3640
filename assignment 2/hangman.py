# # Hangman game
# #

# # -----------------------------------
# # Helper code
# # You don't need to understand this helper code,
# # but you will have to know how to use the functions
# # (so be sure to read the docstrings!)

# import random

# WORDLIST_FILENAME = "words.txt"


# def loadWords():
#     """
#     Returns a list of valid words. Words are strings of lowercase letters.

#     Depending on the size of the word list, this function may
#     take a while to finish.
#     """
#     print("Loading word list from file...")
#     # inFile: file
#     inFile = open(WORDLIST_FILENAME, 'r')
#     # line: string
#     line = inFile.readline()
#     # wordlist: list of strings
#     wordlist = line.split()
#     print("  ", len(wordlist), "words loaded.")
#     return wordlist


# def chooseWord(wordlist):
#     """
#     wordlist (list): list of words (strings)

#     Returns a word from wordlist at random
#     """
#     return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
## wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter in lettersGuessed:
            return True
        else:
            return False
# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(isWordGuessed(secretWord, lettersGuessed))

# Expected output:
# False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    return blanks

# When you've completed your function getGuessedWord, uncomment these three lines
# and run this file to test!

# secretWord = 'apple'
# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getGuessedWord(secretWord, lettersGuessed))

# Expected output:
# '_ pp_ e'


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Hint: You might consider using string.ascii_lowercase, which
    # is a string comprised of all lowercase letters.

    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
    return alphabet

# When you've completed your function getAvailableLetters, uncomment these two lines
# and run this file to test!

# lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(getAvailableLetters(lettersGuessed))

# Expected output:
# abcdfghjlmnoqtuvwxyz


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print ("Welcome to Hangman!")
    length = len(secretWord)
    print ("The secret word has %d letters!" % length)
    GuessRemain = 8
    lettersGuessed = []
    while GuessRemain >= 0:
        print("You have %d guesses left." % GuessRemain)
        print("The available letters are: %d." % getAvailableLetters)
        Guess = str(input("What is your guess?: "))
        if Guess in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(Guess)
            print(getGuessedWord(secretWord, lettersGuessed))
            GuessRemain =- 1
            if isWordGuessed == True:
                print("You Win! The word was %d" % secretWord)
        else:
            print("Guess again!")

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'baseball'
hangman(secretWord)