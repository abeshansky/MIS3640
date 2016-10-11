def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
            
def getGuessedWord(secretWord, lettersGuessed):
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    return blanks

def getAvailableLetters(lettersGuessed):
    import string
    alphabet = string.ascii_lowercase
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, "")
    return alphabet

def hangman(secretWord):
    print ("Welcome to Hangman!")
    length = len(secretWord)
    print ("The secret word has %d letters!" % length)
    GuessRemain = 8
    lettersGuessed = []
    while GuessRemain > 0:
        print("You have %d guesses left." % GuessRemain)
        print("The available letters are: %s." % getAvailableLetters(lettersGuessed))
        Guess = str(input("What is your guess?: "))
        if Guess in secretWord:
            lettersGuessed.append(Guess)
            print(getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("You Win! The word was %s." % secretWord)
                return
        elif Guess in lettersGuessed:
            print("You have already guessed that letter. Guess again!")
        else:
            print("That letter is not in my word. Guess again!")
            lettersGuessed.append(Guess)
            GuessRemain = GuessRemain - 1
    print("You lose!")
    return

secretWord = 'baseball'
hangman(secretWord)