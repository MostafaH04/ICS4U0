from player import Player
import random

class Xplayer(Player):
    '''
    This is the object for the x-player in a tic-tac-toe match, which is inherited from the Player object

    Attributes
    ----------
    playerNumber: int
        The number given to the player, used to identify them
    
    playerSymbol: str
        Holds the symbol that represents the "x" player in the game
        Initially set to "X"
    
    playerOrder: int
        The number that specifies the order at which X goes
        Initially set to 0, since X usually starts
    
    _winner: boolean
        States if the player won or did not win the game
        Initially set to False
    
    Methods
    -------
    selectMove(possibleMoves: int[][]) -> int[]
        Selects a move fro the current player by asking the player for their input

    useAbility(gameBoard: Board) -> int[]
        Allows the xPlayer to switch the opposing player's turn to their own
    
    changeSymbol(newSymbol: str) -> boolean
        Allows the xPlayer to switch their symbol
    '''

    def __init__(self, playerNum, _winner = False):
        '''
        Constructor to build an Xplayer object

        Parameters
        ----------
        playerNum: int
            The number given to the player, used to identify them
        
        winner: boolean, optional
            States if the player won or did not win the game
            Initially set to False          

        '''
        self.playerSymbol = "X"
        self.playerOrder = 0
        super().__init__(playerNum, _winner)
        print(self.playerNumber)
    
    def __str__(self):
        '''
        Sets the text that is returned when the player object is called

        Parameters
        ----------
        None

        Returns
        -------
        str
            Player information; player #, turns played, winner, symbol and order

        '''
        return f"{super().__str__()}, Symbol: {self.playerSymbol}, Order: {self.playerOrder}"
        
    
    def useAbility(self, gameBoard):
        '''
        Allows the xPlayer to randomly pick a random spot for the player

        gameBoard: Board
            The curret game's board which is used to access information about the spots

        Returns
        -------
        int[]
            The [y,x] position picked for their next move

        '''
        gameBoard = gameBoard.board
        possibleSpots = []
        for row in gameBoard:
            for currSpot in row:
                if not currSpot.occupied:
                    possibleSpots.append(currSpot.position)
        
        selectedPosition = possibleSpots[random.randint(0,len(possibleSpots)-1)]
        return selectedPosition

    def changeSymbol(self, newSymbol):
        '''
        Allows the x-player to switch their symbol

        Parameters
        ----------
        newSymbol: str
            The new symbol for the player

        Returns
        -------
        boolean
            Signifies if the symbol was changed

        '''
        if newSymbol != "O":
            self.playerSymbol = newSymbol
            return True
        
        else:
            return False