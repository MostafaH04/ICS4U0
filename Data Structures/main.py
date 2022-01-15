#-----------------------------------------------------------------------------
# Name:        Tic-Tac-Toe | Data Structures Assignment 
# Purpose:     Implmenting datastructures in a meaningful way
#
# References: 	This program uses the python random and time libraries:
#               https://docs.python.org/3/library/random.html
#               https://docs.python.org/3/library/time.html
#               
#
# Author:      Mostafa Hussein
# Created:     19-Oct-2021
# Updated:     22-Oct-2021
#-----------------------------------------------------------------------------

#Imports
from game import Game
import os


# checks if this instance of the program is to connect to a prexisting session or create a new session
connecting = input("Are you creating a Session? (Y/N)")

# if this instance is a new game session, it requires a game session number for another user/player to connect
if connecting.lower() == "y":
    gameSessionNum = int(input("Create a game session: "))
    sender = True

# if this instance is not a new game session, it requires the number of the session they are connecting too
elif connecting.lower() == "n":
    gameSessionNum = int(input("What is the session number to connect?"))
    sender = False

else:
    print("wrong input")
    exit()

# Creates a game object to start the game
newGame = Game(gameSessionNum, sender)

# while loop to run the game until the game is over or a connection time out occurs
running = True
while running:
    # Retrives the move from the user / text connection file
    move = newGame.getMove()
    if move == None:
        running = False
        print("Restart Game")

    # After each move it checks if a player won the game
    if newGame.currentBoard.checkWinner():
        running = False
        print("Game OVER!")

    #Checks if user wants to change their symbol
    if newGame.currentTurn == newGame.currentBoard.playerNum and running:
        getNewSymbol = input("Do you want to get a new symbol? :) (Y/N) ")
        if getNewSymbol.lower() == 'y':
            newSymbol = input("Pick a new symbol (Please keep to one character)")
            if len(newSymbol) == 1:
                if newGame.currentBoard.localPlayer.changeSymbol(newSymbol):
                    print("Successful Change!")
                else:
                    print("Unsuccessful, try again later")
            else:
                print("Wrong length! Not changing symbol")

# Input function to keep terminal open for user to read Game OVER 
if sender:
    os.remove(f"{gameSessionNum}.txt")
input()


