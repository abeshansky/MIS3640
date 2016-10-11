# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            #checks to see if all letters in secretWord are in the list lettersGuessed
            return False
            #False - not all letters are there and the word is not guessed
    return True
    #True - all the letters are there and the word is guessed

# When you've completed your function isWordGuessed, uncomment these three lines
# and run this file to test!s

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
    blanks = '_' * len(secretWord)
    #stars out the word at blank spaces * the length of secretWord
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            #checks to see if the letters in secretWord are in the list lettersGuessed
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
            #inserts the letter in replace of the blank space if it is selected
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

    import string
    alphabet = string.ascii_lowercase
    #creates the string of the alphabet in lowercase
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
            #removes the letter if it is in the list lettersGuessed and replaces it with an empty space
    return alphabet
    #returns the updated alphabet (letters remaining)


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
    print ("Welcome to Hangman!")
    length = len(secretWord)
    print ("The secret word has %d letters!" % length)
    GuessRemain = 8
    #Game starts off at 8 guesses
    lettersGuessed = []
    #creates the list that stores the letters that are guessed
    while GuessRemain > 0:
        # will continue to run as long as you have at least one guess remaining
        print("You have %d guesses left." % GuessRemain)
        print("The available letters are: %s." % getAvailableLetters(lettersGuessed))
        Guess = str(input("What is your guess?: "))
        #asks for your guess
        if Guess in secretWord:
            lettersGuessed.append(Guess)
            #adds your guess to the list
            print(getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("You Win! The word was %s." % secretWord)
                #since all of the letters in secretWord were chosen, you win!
                return
        elif Guess in lettersGuessed:
            print(getGuessedWord(secretWord, lettersGuessed))
            print("You have already guessed that letter. Guess again!")
            #if the guess is already in the list, you have already guessed it and must choose another letter
        else:
            print(getGuessedWord(secretWord, lettersGuessed))
            print("That letter is not in my word. Guess again!")
            lettersGuessed.append(Guess)
            #the new incorrect guess is added to the list
            GuessRemain = GuessRemain - 1
            #you lose a turn
    print("You lose! The word was %s." % secretWord)
    #you ran out of GuessRemain (guesses remaining)
    return


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)