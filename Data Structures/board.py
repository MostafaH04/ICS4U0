from oPlayer import Oplayer
from xPlayer import Xplayer

from spot import Spot 

class Board():
    '''
    A tic-tac-toe board object

    Attributes
    ----------
    dimensions: int[]
        Holds the y and x dimensions of the board
        Initially set to 3 by 3
    
    localPlayer: Player
        The Player object that is able to make moves on this board

    playerNum: int
        The number of the local player
    
    _rows: int
        The number of rows on the board
        Initially set to 3
    
    _columns: int
        The number of rows on the board
        Initially set to 3
    
    _board: Spot[][]
        2 dimensional Spot Object area which represents the board

    Methods
    -------
    draw() -> None
        Prints the physical reperesentation of the board to the terminal
    
    place(position: int[], playerNum: int, playerSymb: str) -> None
        Calls on the spot at a given position to occupy it
    
    checkTurn() -> int
        Checks who's turn it is in the game
    
    checkPossible() -> int[][]
        Checks the possible moves / empty spots on the board
    
    checkWinner() -> boolean
        Checks if a player has won the game

    '''
    def __init__(self, rows = 3, columns = 3, sender = True):
        '''
        Constructor to build a player object

        Paramaters
        ----------
        rows: int, optional
            The number of rows on the board
            Initially set to 3
        
        columns: int, optional
            The number of rows on the board
            Initially set to 3
        
        sender: boolean, optional
            The status of weather the user is a sender or reciever
            Initially set to True

        '''
        self.localPlayer = self._createPlayer(sender)
        self.playerNum = self.localPlayer.playerNumber
        self._rows = rows
        self._columns = columns
        self.dimensions = [rows, columns]

        self.board = self._createBoard()

    def draw(self):
        '''
        Prints the physical reperesentation of the board to the terminal

        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        currentBoard = self.board
        print(" " + "-"*(4*len(currentBoard[0])+1))
        for row in currentBoard:
            for currentSpot in row:
                print(" |", end = " ")
                symbol = currentSpot.playerSymbolOccupied
                print(symbol, end = "")
            print(" |\n " + "-"*(4*len(row)+1))

        return None

    def place(self, placeInfo):
        '''
        Calls on the spot at a given position to occupy it

        Parameters
        ----------
        placingInfo: dict
            dictionary with all the necessary information to place down a player's move

        Returns
        -------
        None

        '''
        y,x = placeInfo['position']
        spot = self.board[y][x]
        playerNum = placeInfo['number']
        playerSymb = placeInfo['symbol']
        spot.selectSpot(playerNum, playerSymb)

        return None

    def checkTurn(self):
        '''
        Checks who's turn it is in the game by checking who made the least moves

        Parameters
        ----------
        None

        Returns
        -------
        int
            The player number of the player with the current turn

        '''
        currentBoard = self.board
        countPlayers = {}
        players = []
        for row in currentBoard:
            for currentSpot in row:
                if not currentSpot.occupied:
                    continue
                
                occupyingPlayer = currentSpot.playerNumberOccupied
                players.append(occupyingPlayer)
                if occupyingPlayer not in countPlayers:
                    countPlayers[occupyingPlayer] = 0
                
                countPlayers[occupyingPlayer] += 1
        
        # Bypasses the case where only one player is on the board so far
        if len(players) == 1:
            if players[0] == 0:
                return 1
            else:
                return 0

        leastMovesPlayer = players[0]
        for player in players:
            if countPlayers[player] < countPlayers[leastMovesPlayer]:
                leastMovesPlayer = player
            elif countPlayers[player] == countPlayers[leastMovesPlayer]:
                if leastMovesPlayer > player:
                    leastMovesPlayer = player
        
        return leastMovesPlayer
    
    def checkPossible(self):
        '''
        Checks who's turn it is in the game by checking who made the least moves

        Parameters
        ----------
        None

        Returns
        -------
        int[][]
            List consisting of multiple lists including the y and x of possible spots

        '''
        possibleSpots = []
        currentBoard = self.board

        for row in currentBoard:
            for currentSpot in row:
                if not currentSpot.occupied:
                    possibleSpots.append(currentSpot.position)

        return possibleSpots
    
    def checkWinner(self):
        '''
        Checks if a player has won the game

        Parameters
        ----------
        None

        Returns
        -------
        boolean
            True or false status if a player has won the game

        '''
        currentBoard = self.board   
        
        # Checking Horizontal win
        for row in range(len(currentBoard)):
            initialRowOccupier = currentBoard[row][0].playerNumberOccupied
            matchingRow = True
            if initialRowOccupier == None and initialRowOccupier != 0:
                matchingRow = False
            for column in range(len(currentBoard)):
                if currentBoard[row][column].playerNumberOccupied != initialRowOccupier:
                    matchingRow = False
                    break

            if matchingRow:
                return True

        # Checking Veritcal win
        for column in range(len(currentBoard[0])):
            initialColOccupier = currentBoard[0][column].playerNumberOccupied
            matchingCol = True
            if initialColOccupier == None and initialColOccupier != 0:
                matchingCol = False
            for row in range(len(currentBoard)):
                if currentBoard[row][column].playerNumberOccupied != initialColOccupier:
                    matchingCol = False
                    break

            if matchingCol:
                return True
        
        # Checking Diagonal win
        initialSpot = currentBoard[0][0]
        initialOccupier = initialSpot.playerNumberOccupied
        matchingDiagonal = True
        if initialOccupier == None and initialOccupier != 0:
            matchingDiagonal = False
        for row in range(len(currentBoard)):
            if currentBoard[row][row].playerNumberOccupied != initialOccupier:
                matchingDiagonal = False
                break
        
        if matchingDiagonal:
            return True  

        initialSpot = currentBoard[-1][0]
        initialOccupier = initialSpot.playerNumberOccupied
        matchingDiagonal = True
        if initialOccupier == None and initialOccupier != 0:
            matchingDiagonal = False  
        for row in range(len(currentBoard)):
            maxPos = len(currentBoard)-1
            if currentBoard[maxPos-row][row].playerNumberOccupied != initialOccupier:
                matchingDiagonal = False
                break
        
        if matchingDiagonal:
            return True           

        #If all cases fail, returns false
        return False   
    
    def _createBoard(self):
        '''
        Creates the "board" it self using multiple spot objects

        Parameters
        ----------
        None

        Returns
        -------
        Spot[][]
            A 2 dimensional list of spot objects which represents the board

        '''
        rowNum = self.dimensions[0]
        columnNum = self.dimensions[1]
        newBoard = []
        for row in range(rowNum):
            newBoard.append([])
            for column in range(columnNum):
                newSpot = Spot([row, column])
                newBoard[row].append(newSpot)
        
        return newBoard
        
    def _createPlayer(self, sender):
        '''
        Creates the the player object of the player controlling this board

        Parameters
        ----------
        sender: boolean
            states if the new player is the person starting or not; starting is x otherwise its o

        Returns
        -------
        Player
            The object of the player controlling the board

        '''
        if sender:
            num = 0
            newPlayer = Xplayer(num)
        else:
            num = 1
            newPlayer = Oplayer(num)
            
        return newPlayer   