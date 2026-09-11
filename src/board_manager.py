"""
Module Name: board_manager.py
Description: Hold and manage a 2D list of cells
Inputs:
Outputs:
External Sources:
Attributions:
Authors: Drew Medlock
Creation Date: 9/9/2026
"""

class Cell:
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