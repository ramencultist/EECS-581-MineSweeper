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
    Cell class holds the states of each individual cell, and has functions for getting and setting these states.
    Code is original written by Drew Medlock
    """
    def __init__(self) -> None:
        self._covered = True
        self._flagged = False
        self._is_mine = False

    # Getters

    def is_mine(self) -> bool:
        return self._is_mine

    def is_covered(self) -> bool:
        return self._covered

    def is_flagged(self) -> bool:
        return self._flagged

    # Setters

    def uncover(self):
        self._covered = False

    def set_mine(self) -> None:
        self._is_mine = True

    def set_flagged(self) -> None:
        self._flagged = True

    def remove_flag(self) -> None:
        self._flagged = False

class BoardManager:
    def __init__(self) -> None:
        self.board = [[Cell() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def set_mines(self, mines: list[tuple]) -> None:
        for mine_location in mines:
            self.board[mine_location[0]][mine_location[1]].set_mine()