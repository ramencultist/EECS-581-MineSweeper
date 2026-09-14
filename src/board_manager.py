"""
Module Name: board_manager.py
Description: Hold and manage a 2D list of cells

Class Name: Cell
Description: Hold the states for each cell inside of the board

Class Name: BoardManager
Description: Hold the 10x10 grid of cells as a 2D list.

Inputs:
Outputs:
External Sources:
Attributions:
Authors: Drew Medlock
Creation Date: 9/9/2026
"""

BOARD_SIZE = 10

class Cell:
    """
    Cell class holds the states of each individual cell
    Code is original written by Drew Medlock
    """
    def __init__(self) -> None:
        self.covered = True
        self.flagged = False
        self.is_mine = False

class BoardManager:
    def __init__(self) -> None:
        self.board = [[Cell() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def is_mine(self, row: int, col: int) -> bool:
        return self.board[row][col].is_mine

    def is_covered(self, row: int, col: int) -> bool:
        return self.board[row][col].covered

    def is_flagged(self, row: int, col: int) -> bool:
        return self.board[row][col].flagged

    def uncover_cell(self, row: int, col: int) -> None:
        self.board[row][col].covered = False

    def set_mine(self, row: int, col: int) -> None:
        self.board[row][col].is_mine = True

    def set_flagged(self, row: int, col: int) -> None:
        self.board[row][col].flagged = True

    def remove_flag(self, row: int, col: int) -> None:
        self.board[row][col].flagged = False

    def set_mines(self, mines: list[tuple]) -> None:
        for mine_location in mines:
            self.set_mine(row=mine_location[0], col=mine_location[1])