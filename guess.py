#-------------------------------------------------------------------------------
# Name:        guess.py
# Purpose:     Play a user-defined number of guessing games to guess the
#              randomly selected number for each game.
#
# Author:      arie claassens
#
# Created:     14/07/2019
# Copyright:   (c) arie_ 2019
# Licence:     GNU GPL v3
#-------------------------------------------------------------------------------
import random

#Global variables
countGames = 0
numberGames = -1
userTries = 0
guess = -1
tries = 0

#Get the number of games to play
while numberGames < 0:
    numberGames = input("How many games do you want to play?")
    try:
        numberGames = int(numberGames)
    except:
        print('Enter whole numbers only')

#Loop until the number of games matches the user selection
while countGames <= numberGames:
    #Start the game
    x = random.randint(0,25)
    #Let the user guess until guess matches x
    while guess != x:
        guess = input("Guess the number (0 - 25)")
        #Convert the user input
        try:
            guess = int(guess)
            tries +=1
        except:
            print('Enter whole numbers only')

        if guess == x:
            print("You used %s tries to find the correct number(s)" % tries)
            tries = 0
            countGames += 1 #Increase
            continue
        elif guess > x:
            print('Too high')
        elif guess < x:
            print('Too low')
    #increase game counter
    countGames += 1
print("Thank you for playing! See you again soon.")


