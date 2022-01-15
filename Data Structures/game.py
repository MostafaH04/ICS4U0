import time
from board import Board

class Game():
    '''
    A tic-tac-toe game object

    Attributes
    ----------
    sessionNumber: int
        The number given to connect to the current session
    
    currentBoard: Board
        The board for the current tic-tac-toe game

    currentTurn: int
        The player number of the player with the current Turn
    
    sender: boolean
        The status identifying whether this is a sending or recieving board 
        
    connectionTimeOut: int
        The number of seconds before the game times out while waiting for response
        Intially set to 60

    _latestSent: dict
        The latest sent data from this game object       

    Methods
    -------
    getMove() -> dict
        Gets a move from the user if its their turn, or waits for new data to be shared
        
    transmitData(latestMove:dict) -> None
        Writes to the file that shares the data with the other user (on another instance of the program)
            
    '''
    def __init__(self, sessionNumber, sender = True):
        '''
        Constructor to build a player object

        Paramaters
        ----------
        sessionNumber: int
            The number given to connect to the current session
        
        sender: boolean, optional
            The status identifying whether this is a sending or recieving board
            Initially set to True

        '''
        self.sessionNumber = sessionNumber
        self.sender = sender
        self.currentBoard = Board(sender = self.sender)
        self.currentBoard.draw()
        self.currentTurn = 0
        self.connectionTimeOut = 60
        self._latestSent = None
    
    def getMove(self):
        '''
        Gets a move from the user if its their turn, or waits for new data to be shared

        Paramaters
        ----------
        None

        Returns
        -------
        dict
            dictionary with the information of the latest move

        '''
        currentBoard = self.currentBoard
        localPlayer = currentBoard.localPlayer
        localPlayerNum = localPlayer.playerNumber

        if self.currentTurn == localPlayerNum:
            abilityUse = input("Do you want to use your ability? (Y/N)")
            if abilityUse.lower() == 'y':
                selectedPosition = localPlayer.useAbility(currentBoard)
            else:
                possibleMoves = currentBoard.checkPossible()
                selectedPosition = localPlayer.selectMove(possibleMoves)
            player = currentBoard.localPlayer
            playerNum = player.playerNumber 
            playerSymb = player.playerSymbol
            move = {
                    "number": localPlayerNum,
                    "position": selectedPosition,
                    "symbol": playerSymb
            }

            self.transmitData(move)
        
        else:
            move = self._recieveData()
            if move == None:
                print("Connection Timed Out")
                return None 
        
        currentBoard.place(move)
        self._latestSent = move
        currentBoard.draw()
        self.currentTurn = currentBoard.checkTurn()

        return move
    
    def transmitData(self, move):
        '''
        Writes to the file that shares the data with the other user (on another instance of the program)

        Paramaters
        ----------
        move: dict
            dictionary with the information of the latest move

        Returns
        -------
        None

        '''
        sessionNumber = self.sessionNumber
        with open(f"{sessionNumber}.txt", "w") as file:
            playerNum = move['number']
            position = move['position']
            symbol = move['symbol']

            data = f"{playerNum},{position[0]},{position[1]},{symbol}"
            file.write(data)
        
        return None
    
    def _recieveData(self):
        '''
        Recieves data from the other connected instantce of the program or the other player

        Paramaters
        ----------
        None

        Returns
        -------
        dict:
            dictonary with the received data from the other connected instantce

        '''
        currentBoard = self.currentBoard
        sessionNumber = self.sessionNumber
        dataRetrieved = False
        startingTime = time.time()
        while not dataRetrieved:
            try:
                with open(f"{sessionNumber}.txt", "r") as file:
                    currentTime = time.time()
                    if currentTime - startingTime > self.connectionTimeOut:
                        return None
                    
                    rawData = file.read().split(",")

                    playerNum = int(rawData[0])
                    if playerNum == 3:
                        playerNum = None
                    position = [int(rawData[1]),int(rawData[2])]
                    symbol = rawData[3]
                    data = {
                        "number": playerNum,
                        "position": position,
                        "symbol": symbol
                    }

                    if self._latestSent == None:
                        dataRetrieved = True
                    
                    if self._latestSent != data:
                        dataRetrieved = True
            except:
                # Error happened accessing the file
                continue

        return data
