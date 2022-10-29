"""
CS3B, Assignment #1, Tic Tac Toe
Copyright 2020 Zibin Yang
Starter code
"""

# import time
from enum import Enum


class GameBoardPlayer(Enum):
    """
    An enum that represents a player on a game board; it's used to denote:
    . which player occupies a space on the board (can be NONE if unoccupied)
    . which player is the winner of the game (can be DRAW)
    """
    NONE = 0
    X = 1
    O = 2
    DRAW = 3

    def __str__(self):

        if self.name != "NONE":
            ret_str = f"{self.name[0].upper()}"
        else:
            ret_str = f" "
        return ret_str

class ArrayGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols, grid=[]):
        if nrows <= 0 or ncols <= 0:
            raise ValueError
        self.nrows = nrows
        self.ncols = ncols
        self.grid = grid
        self.grid = [[GameBoardPlayer.NONE] * self.ncols] * self.nrows
        print(f"initiated grid: {self.grid}")

    def get_nrows(self):
        """ Return the number of rows of the board """
        return self.nrows

    def get_ncols(self):
        """ Return the number of columns of the board """
        return self.ncols

    def set(self, row, col, value):
        nrows = self.get_nrows()
        ncols = self.get_ncols()
        if row < 0 or col < 0 or row >= nrows or col >= ncols:
            raise IndexError
        for i in range(nrows):
            if i == row:
                self.grid[i][col] = value

    def get(self, row, col):
        if row < 0 or col < 0:
            raise IndexError
        return self.grid[row][col]

    def __str__(self):
        row = self.get_nrows()
        col = self.get_ncols()
        temp_string = ""
        for i in range(0, row):
            for j in range(0, col):
                if j != col - 1:
                    temp_string += f"{self.get(i, j)}|"
            temp_string += f"{self.grid[i][j]}"
            temp_string += f"\n"
            for j in range(0, row):
                if j != col - 1:
                    temp_string += f"-+"
            temp_string += f"-"
            temp_string += f"\n"
        return temp_string

    def get_winner(self):
        row = self.get_nrows()
        col = self.get_ncols()
        winner_exsit = False
        result = True
        """ Check whether there is a row wins """
        for i in range(0, row):
            winner_exsit = all(elem == self.grid[i][0] for elem in self.grid[i])
            if winner_exsit:
                if self.grid[i][0] == 1:
                    return "X"
                elif self.grid[i][0] == 2:
                    return "O"
        """ Check whether there is a col wins"""
        for j in range(0, row):
            for k in range(0, col):
                head = self.get(j, k)
                if self.get(j, k) != head:
                    result = False
            if result:
                if head == 1:
                    return "X"
                elif head == 2:
                    return "O"


class BitGameBoard:
    """A class that represents a rectangular game board"""

    def __init__(self, nrows, ncols):
        pass

    def get_nrows(self):
        pass

    def get_ncols(self):
        pass

    def set(self, row, col, player):
        pass

    def get(self, row, col):
        pass

    def __str__(self):
        return "(To be implemented)"

    def get_winner(self):
        return GameBoardPlayer.NONE


class TicTacToeBoard:
    """
    A class that represents a Tic Tac Toe game board.
    It's a thin wrapper around the actual game board
    """
    NROWS = 3
    NCOLS = 3

    def __init__(self):
        # The two game boards can be used interchangeably.
        self.board = ArrayGameBoard(self.NROWS, self.NCOLS)
        # self.board = BitGameBoard(self.NROWS, self.NCOLS)

    def set(self, row, col, value):
        if self.board.get(row, col) != GameBoardPlayer.NONE:
            raise ValueError(f"{row} {col} already has {self.board.get(row, col)}")
        self.board.set(row, col, value)

    def clear(self, row, col):
        self.board.set(row, col, GameBoardPlayer.NONE)

    def get(self, row, col):
        return self.board.get(row, col)

    def get_winner(self):
        return self.board.get_winner()

    def __str__(self):
        return self.board.__str__()


def test_game_board(gb):

    # Test 1: __str__()
    print("Test 1: __str__()")
    print(gb)

    print(f"winner of empty board is '{gb.get_winner()}'")

    gb.set(0, 0, GameBoardPlayer.X)
    gb.set(0, 1, GameBoardPlayer.X)
    gb.set(0, 2, GameBoardPlayer.X)
    print(f"after setting, grid: {gb.grid}")
    print("gb.get(0, 0) returns", gb.get(0, 0))
    print("gb.get(0, 1) returns", gb.get(0, 1))
    print("gb.get(0, 2) returns", gb.get(0, 2))

    try:
        gb.get(100, 100)
        print("gb.get(100, 100) fails to raise IndexError")
    except IndexError:
        print("gb.get(100, 100) correctly raises IndexError")

    print(f"winner of board with 1 row of X is '{gb.get_winner()}' \n")

    # TODO add other tests (GameBoardPlayer.O, different rows, columns, diagonal, etc)


if __name__ == '__main__':
    # The same tests should work for both types of *GameBoard
      test_game_board(ArrayGameBoard(3, 3))
    # test_game_board(BitGameBoard(3, 3))

"""
 There are no output from what I currently have. 
 I was stuck in the set() that the value doesn't set as expected.
 This the initiated grid:
 grid before: [[<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, 
 <GameBoardPlayer.NONE: 0>], [<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, 
 <GameBoardPlayer.NONE: 0>], [<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, 
 <GameBoardPlayer.NONE: 0>]]
 
 After running test_game_board(), and I only run gb.set(0, 0, GameBoardPlayer.X), 
 then it shows the result of grid like
 this:
 result after setting:  
grid after: [[<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, <GameBoardPlayer.X: 1>],
 [<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, <GameBoardPlayer.X: 1>], 
 [<GameBoardPlayer.NONE: 0>, <GameBoardPlayer.NONE: 0>, <GameBoardPlayer.X: 1>]]

So all the value in the same col change no matter which row. I suspect something wrong 
with the set() but I ran out of time...

I will keep working on it..

"""