class Spot():
    '''
    This is the class for a spot on the tic-tac-toe board

    Attributes
    ----------
    position: int[]
        The position of this spot on the grid

    occupied: boolean
        States if this spot is occupied
        Set to False initially
    
    playerNumberOccupied: int
        The player number for the player occupying the spot
        Initially set to None, since the spot starts unoccupied
    
    playerSymbolOccupied: str
        Holds the symbol of the player occupying the spot
        Initially set to " "(empty), since the spot starts unoccupied
    
    Methods
    -------
    selectSpot(playerNumber: int, playerSymbol: str) -> None
        Changes the spot's attributes when the spot is picked,
        filling in the player's general info and setting occupied
        variabel to True

    resetSpot() -> None
        Resets the given spot back to its original state 

    '''

    def __init__(self, position, occupied = False):
        '''
        Constructor to build a spot object

        Paramaters
        ----------
        position: int[]
            The position of the spot on the tic-tac-toe grid
        
        occupied: boolean, optional
            States if this spot is occupied
            Set to False initially           

        '''
        self.position = position
        self.occupied = occupied
        self.playerNumberOccupied = None
        self.playerSymbolOccupied = " "
    
    def selectSpot(self, playerNumber, playerSymbol):
        '''
        Changes the spot's attributes when the spot is picked,
        filling in the player's general info and setting occupied
        variabel to True

        Parameters
        ----------
        playerNumber: int
            The number of the player selecting this spot
        
        playerSymbol: str
            The symbol of the player selecting this spot

        Returns
        -------
        None

        '''
        self.playerNumberOccupied = playerNumber
        self.playerSymbolOccupied = playerSymbol

        self.occupied = True

        return None
    
    def resetSpot(self):
        '''
        Resets the given spot back to its original state

        Parameters
        ----------
        None

        Returns
        -------
        None

        '''
        self.playerSymbolOccupied = " "
        self.playerNumberOccupied = None
        self.occupied = False
        

        return None