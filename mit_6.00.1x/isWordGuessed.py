#!/usr/bin/env python

import string
import sys

def isWordGuessed(secretWord, lettersGuessed):
  for c in secretWord:
    if c not in lettersGuessed:
      return False
  return True

def getGuessedWord(secretWord, lettersGuessed):
  assert isinstance(lettersGuessed) is list
  guessed_word = ''
  for c in secretWord:
    if c in lettersGuessed:
      guessed_word += c + ' '
    else:
      guessed_word += '_' + ' '
  return guessed_word
 
def getAvailableLetters(lettersGuessed):
  assert isinstance(lettersGuessed) is list
  lettersLeft = ''
  for l in string.ascii_lowercase:
    if l not in lettersGuessed:
      lettersLeft += l
  return lettersLeft

def hangman(secretWord):
  randomWord = secretWord
  lettersGuessed = []
  max_guesses = 8
  num_guesses = 0
  print("Welcome to the game, Hangman!")
  print("I am think of a word that is %i letters long." % len(randomWord))
  while 1:
   print("------------")
   if num_guesses == max_guesses:
     print("Sorry, you ran out of guesses.  The word was %s." % randomWord)   
     return
   if isWordGuessed(randomWord, lettersGuessed):
     print("Congratulations, you won!")
     return
   print("You have %i guesses left." % (max_guesses - num_guesses))
   print("Available letters: %s" % getAvailableLetters(lettersGuessed))
   guess = raw_input("Please guess a letter: ")
   if guess.lower() in lettersGuessed:
     print("Oops!  You've already guessed that letter: "), 
     print getGuessedWord(randomWord, lettersGuessed)
     num_guesses += 1
     continue
   lettersGuessed.append(guess.lower())
   if guess in randomWord:
     print("Good guess: "),
   else:
     print("Oops!  That letter is not in my word: "),
   num_guesses += 1
   print getGuessedWord(randomWord, lettersGuessed)
  
hangman("sea")
