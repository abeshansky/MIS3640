import string

### DO NOT MODIFY THIS FUNCTION ###


def load_wordlist(file_name):
    '''
    '''
    print('Loading word list from file...')
    in_file = open(file_name, 'r')
    line = in_file.readline()
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###


def is_a_valid_word(word_list, word):
    '''    
    Returns: True if word is in word_list, False otherwise
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###


def get_joke_string():
    """
    Returns: an article in encrypted text.
    """
    f = open("joke.txt", "r")
    joke = str(f.read())
    f.close()
    return joke

WORDLIST_FILENAME = 'words.txt'


class Text(object):
    ### DO NOT MODIFY THIS METHOD ###

    def __init__(self, text):
        '''
        Initializes a Text object
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_text(self):
        '''
        Returns: self.text
        '''
        return self.text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
    
    def create_moved_dict(self, move):
        '''
        Creates a dictionary that maps every letter to a
        character moved down the alphabet by the input move. 
        move: an integer, 0 <= move < 26
        Returns: a dictionary
        Example: an_instance_of_Text.create_moved_dict(2) would generate
        {'a': 'c', 'b': 'd', 'c':'e', ...}  
        '''
        dict={}
        lowerend=lower[shift:]+lower[0:shift]
        upperend=upper[shift:]+upper[0:shift]
        for i in range(len(lower)):
            dict[lower[i]]=lowerend[i]
        for j in range(len(upper)):
            dict[upper[j]]=upperend[j]
        return dict

    def apply_move(self, move):
        '''
        Applies the cipher to self.text with the input move       
        move: an integer, 0 <= move < 26
        Returns: the text (string) in which every character is moved
             down the alphabet by the input move
        '''
        self.move = move
        encrypted_text = ""
        for i in range(len(text)):
            if text[i] in total:
                encrypted_text+=coder[text[i]]
            else:
                encrypted_text+=text[i]
        return encrypted_text

class PlainText(Text):

    def __init__(self, text, move):
        '''
        Initializes a PlainText object        
        text: a string
        move: an integer
        A PlainText object inherits from Text and has five attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
            self.move (integer, determined by input move)
            self.encrypting_dict (dictionary, built using move)
            self.encrypted_text (string, created using move)
        Note: you must use the parent class constructor(__init__ function) 
        so less code is repeated
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)
        self.move = move
        self.get_encrypting_dict = {}
        self.get_encrypted_text = ""

    def get_move(self):
        '''
        Used to safely access self.move outside of the class
        Returns: self.move
        '''
        return self.move

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        Returns: a COPY of self.encrypting_dict
        '''
        encrypting_dict_copy == self.encrypting_dict
        return encrypting_dict_copy

    def get_encrypted_text(self):
        '''
        Used to safely access self.encrypted_text outside of the class
        Returns: self.encrypted_text
        '''
        self.encrypted_text = get_joke_string()
        return self.encrypted_text

    def change_move(self, move):
        '''
        Changes self.move of the PlainText and updates other 
        attributes determined by move (ie. self.encrypting_dict and 
        encrypted_text).
        move: an integer, 0 <= move < 26
        Returns: nothing
        '''
        self.move = move

class CipherText(Text):

    def __init__(self, text):
        '''
        Initializes a CipherText object
        text: a string
        a CipherText object has two attributes:
            self.text (string, determined by input text)
            self.valid_words (list, determined using helper function load_wordlist)
        '''
        self.text = text
        self.valid_words = load_wordlist(WORDLIST_FILENAME)

    def decrypt_text(self):
        '''
        Decrypt self.text by trying every possible move value
        and find the "best" one. We will define "best" as the move that
        creates the maximum number of real words when we use apply_move(move)
        on the text. If s is the original move value used to encrypt
        the text, then we would expect 26 - s to be the best move value 
        for decrypting it.
        Returns: a tuple of the best move value used to decrypt the text
        and the decrypted  text using that move value. Check out the
        test case in main function below.
        '''
        self.move = 0
        while self.move <= 26:
            decrypted_text = self.text.apply_move(self,self.move)
            if decrypted_text in self.valid_words:
                return self.move, decrypted_text
            else: 
                self.move += 1

def decrypt_joke():
    joke = CipherText(get_joke_string())
    return joke.decrypt_text()


def main():
    # Example test case (PlainText)
    plaintext = PlainText('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_encrypted_text())

    # Example test case (CipherText)
    ciphertext = CipherText('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_text())

    print(decrypt_joke())

if __name__ == '__main__':
    main()