#!/usr/bin/env python

#import sys

low = 0
high = 100

print("Please think of a number between 0 and 100!")

while True:
    guess = (high + low) // 2
    print("Is you secret number %i?" % guess)
    resp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if resp == "c":
        print("Game over. Your secret number was: %i" % guess)
        break
    elif resp == "h":
        high = guess
    elif resp == "l":
        low = guess
    else:
        print("Please read the instructions . . .")
