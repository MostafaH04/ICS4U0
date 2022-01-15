from abc import abstractmethod

class Player():
    '''
    A tic-tac-toe player object that holds the player info; including player#,
    turns played and if they won the game

    Attributes
    ----------
    playerNumber: int
        The number given to the player, used to identify them
    
    _winner: boolean
        States if the player won or did not win the game
        Initially set to False

    Methods
    -------
    selectMove(possibleMoves: int[][]) -> int[]
        Selects a move fro the current player by asking the player for their input

    useAbility(gameBoard: Board) -> int[]
        Allows the player to use their special move

    '''

    def __init__(self, playerNum, _winner = False):
        '''
        Constructor to build a player object

        Paramaters
        ----------
        playerNum: int
            The number given to the player, used to identify them
        
        winner: boolean
            States if the player won or did not win the game
            Initially set to False

        '''
        self.playerNumber = playerNum
        self._winner = _winner
    
    def __str__(self):
        '''
        Sets the text that is returned when the player object is called

        Parameters
        ----------
        None

        Returns
        -------
        str
            Player information; player #, turns played and winner

        '''
        return f"Player #: {self.playerNumber}, Turns Played: {self.turnsPlayed}, Winner: {self._winner}"
    
    def selectMove(self, possibleMoves):
        '''
        Selects a move for the current player by asking the player for their input

        Parameters
        ----------
        possibleMoves: int[][]
            A 2D list, consiting of a list of 2 value lists which include possible
            [y,x] positions where the player can make their move

        Returns
        -------
        int[]
            The [y,x] position picked for their next move
        
        Raise
        -----
        TypeError
            Inputed by the player coordinates cannot be selected
        '''
        
        print("""
        Please Select an Avalaible Move
        Use the format:
        -> Y-coord
        -> X-coord
        """)
        positionSelected = False
        while not positionSelected:
            try:
                selectedYposition = int(input("Y-coord: "))
                selectedXposition = int(input("X-coord: "))
                selectedCoords = [selectedYposition, selectedXposition]
                
                if selectedCoords in possibleMoves:
                    print(f"Selected coordinates: {selectedCoords}")
                    positionSelected = True
                
                else:
                    raise TypeError("Inputed coordinates cannot be selected")
                
            except ValueError:
                print("Error -> Inputed values were not integers")
            
            except TypeError as errorMsg:
                print(f"Error -> {errorMsg}")

        return selectedCoords
    
    @abstractmethod
    def useAbility(self, gameBoard):
        pass

