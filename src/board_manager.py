"""
Module Name: board_manager.py
Description: Hold and manage a 2D list of cells

Class Name: Cell
Description: Hold the states for each cell inside of the board

Class Name: BoardManager
Description: Hold the 10x10 grid of cells as a 2D list. Contain methods for updating the cell states.

Update Description: Add adjacent_mines to count the mines in the up to eight cells around a given cell

Inputs: Mine locations and cell state changes from the game logic
Outputs: Cell state and adjacent mine count queries for the game logic and UI
External Sources: DeepSeek V4.1 Flash
Attributions:

Update 9/16/2026 - Carter Steenhard and DeepSeek V4.1 Flash:
A description of how and why AI was used: DeepSeek V4.1 Flash used to add the adjacent_mines method for the UI number display
How you validated and revised the AI output: Proofreading, logic tests checking every cell's count against a reference, and a scripted window test of the number display
The challenges or limitations you faced while using AI: Keeping the change minimal while matching the existing getter style
Authors: Drew Medlock, Carter Steenhard
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
    """
    Board Manager class initializes to a fresh board of cells of nxn where n is the board size
    Contains methods for reading from and updating the cells of the board.
    """
    def __init__(self) -> None: # Original code written by Drew Medlock
        self.board = [[Cell() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Getters

    def is_mine(self, row: int, col: int) -> bool: # Original code written by Drew Medlock
        return self.board[row][col].is_mine

    def is_covered(self, row: int, col: int) -> bool: # Original code written by Drew Medlock
        return self.board[row][col].covered

    def is_flagged(self, row: int, col: int) -> bool: # Original code written by Drew Medlock
        return self.board[row][col].flagged

    def adjacent_mines(self, row: int, col: int) -> int: # Original code written by Carter Steenhard and DeepSeek V4.1 Flash
        """Count the mines in the up to eight cells that surround the given cell."""
        count = 0
        for neighbor_row in range(row - 1, row + 2):
            for neighbor_col in range(col - 1, col + 2):
                if neighbor_row == row and neighbor_col == col:
                    continue
                # Skip neighbors that fall outside the board on the edges and corners
                if 0 <= neighbor_row < BOARD_SIZE and 0 <= neighbor_col < BOARD_SIZE:
                    if self.is_mine(neighbor_row, neighbor_col):
                        count += 1
        return count

    # Setters

    def uncover_cell(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board[row][col].covered = False

    def set_mine(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board[row][col].is_mine = True

    def set_flagged(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board[row][col].flagged = True

    def remove_flag(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board[row][col].flagged = False

    def set_mines(self, mines: list[tuple]) -> None: # Original code written by Drew Medlock
        for mine_location in mines:
            self.set_mine(row=mine_location[0], col=mine_location[1])