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
    def __init__(self, num_mines) -> None:
        self.board = board_manager.BoardManager()
        self.is_lost = False
        self.is_won = False
        self.num_mines = num_mines
        self.mine_count = self.num_mines # will be updated with by decreasing when flagging
        self.flags = 0
        self.cells_to_clear = board_manager.BOARD_SIZE ** 2 - self.num_mines
        self.populate_mines()

    def populate_mines(self) -> None:
        locations = [(row, col) for row in range(board_manager.BOARD_SIZE) for col in range(board_manager.BOARD_SIZE)]
        mine_locations = random.sample(locations, self.num_mines)
        self.board.set_mines(mine_locations)