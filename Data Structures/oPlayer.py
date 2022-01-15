from player import Player

class Oplayer(Player):
    '''
    This is the object for the o-player in a tic-tac-toe match, which is inherited from the Player object

    Attributes
    ----------
    playerNumber: int
        The number given to the player, used to identify them
    
    playerSymbol: str
        Holds the symbol that represents the "O" player in the game
        Initially set to "O"
    
    playerOrder: int
        The number that specifies the order at which O sgoes
        Initially set to 1, since O usually goes second
    
    _winner: boolean
        States if the player won or did not win the game
        Initially set to False
    
    Methods
    -------
    selectMove(possibleMoves: int[][]) -> int[]
        Selects a move fro the current player by asking the player for their input

    useAbility(gameBoard: Board) -> int[]
        Allows the oPlayer an already selected spot by the opposing player
    
    changeSymbol(newSymbol: str) -> boolean
        Allows the oPlayer to switch their symbol

    '''

    def __init__(self, playerNum, _winner = False):
        '''
        Constructor to build an Oplayer object

        Paramaters
        ----------
        playerNum: int
            The number given to the player, used to identify them
        
        _winner: boolean, optional
            States if the player won or did not win the game
            Initially set to False         

        '''
        self.playerSymbol = "O"
        self.playerOrder = 1
        super().__init__(playerNum, _winner)
    
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
        Allows the oPlayer an already selected spot by the opposing player

        Parameters
        ----------
        gameBoard: Board
            The curret game's board which is used to access information about the spots

        Returns
        -------
        int[]
            The [y,x] position picked for their next move

        '''
        gameBoard = gameBoard.board
        opposingPlayerSpots = []
        for row in gameBoard:
            for currSpot in row:
                if currSpot.occupied:
                    if currSpot.playerNumberOccupied != self.playerNumber:
                        opposingPlayerSpots.append(currSpot.position)

        return self.selectMove(opposingPlayerSpots)

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
            Signifies if the symbol was changed successfully

        '''
        if newSymbol != "X":
            self.playerSymbol = newSymbol
            return True
        
        else:
            return False