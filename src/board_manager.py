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
    def __init__(self):
        self._covered = True
        self._flagged = False
        self._mine = False

    # Getters

    def isMine(self):
        return self._mine

    def isCovered(self):
        return self._covered

    def isFlagged(self):
        return self._flagged

    # Setters

    def uncover(self):
        self._covered = False

    def setMine(self):
        self._mine = True

    def setFlagged(self):
        self._flagged = True

    def unFlag(self):
        self._flagged = False

class BoardManager:
    def __init__(self):
        self.board = [[Cell() for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]