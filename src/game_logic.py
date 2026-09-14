"""
Module Name: game_logic.py
Description: Handle game logic and make calls to board_manager objects

Inputs:
Outputs:
External Sources:
Attributions:
Authors: Drew Medlock
Creation Date: 9/14/2026
"""

import board_manager
import random # Random is used to generate the mine locations

class GameManager:
    def __init__(self) -> None:
        self.board = board_manager.BoardManager()

    def populate_mines(self, num_mines: int) -> None:
        locations = [(row, col) for row in range(board_manager.BOARD_SIZE) for col in range(board_manager.BOARD_SIZE)]
        mine_locations = random.sample(locations, num_mines)
        self.board.set_mines(mine_locations)