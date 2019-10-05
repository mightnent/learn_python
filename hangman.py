# Hangman game
#

# -----------------------------------
#This is not exactly the same as what the edx grader accept. 
#however, the concept is correct

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
    
    # FILL IN YOUR CODE HERE...
    word = list(secretWord)
    counter = len(word)
    for i in word:
        if i in lettersGuessed:
            del i
            counter -= 1
    if counter == 0:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    guess = ""
    word = list(secretWord)
    for i in word:
        if i in lettersGuessed:
            guess += i
        else:
            guess += " _"
    return guess



import string
def getAvailableLetters(lettersGuessed=""):
    alphabet = list(string.ascii_lowercase)    
    for i in lettersGuessed:
        if i in alphabet:            
            alphabet.remove(i)
    return ''.join(alphabet)
    

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
    print("welcome to a game of hangman!!!")
    print("I am thinking of a word that is {} letters long".format(len(secretWord)))
    num_guess = 8
    lettersGuessed = ""
    while num_guess>=0:
      print("- - - - - - - - - - ")
      print("You have {} guesses left".format(num_guess))
      print("Available Letters: ",getAvailableLetters(lettersGuessed))
      userInput = input("Please guess a letter: ").lower()
      if userInput in lettersGuessed:
        print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord,lettersGuessed))
      else:
        lettersGuessed += userInput
        if isWordGuessed(secretWord,lettersGuessed)==True:
          print("Congratulations, you won!")
          break        
        else:
          if userInput in secretWord:
            print("Good guess: ", getGuessedWord(secretWord,lettersGuessed))
          else:
            print("Oops! That letter is not in my word: ", getGuessedWord(secretWord,lettersGuessed))
            num_guess -=1
    if(num_guess<0):
      print("Sorry, you ran out of guesses. The word was else." )


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
