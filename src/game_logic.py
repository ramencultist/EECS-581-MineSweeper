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

    def reveal_cell(self, row: int, col: int) -> None:
        # Being flagged prevents the cell from being uncovered
        if not self.board.is_flagged(row, col):
            self.board.uncover_cell(row, col)
            if self.board.is_mine(row, col):
                self.is_lost = True
            else:
                self.cells_to_clear -= 1

    def flag_cell(self, row: int, col: int) -> None:
        self.board.set_flagged(row, col)
        self.flags += 1
        # Check for preventing mine_count to going to negative if more than num_mines flags are placed
        if self.mine_count > 0:
            self.mine_count -= 1

    def unflag_cell(self, row: int, col: int) -> None:
        self.board.remove_flag(row, col)
        self.flags -= 1
        # If there are more flags than the number of mines, then the mine_count shouldn't be increased from 0
        # Ex: 16 flags and 15 mines, function is called. 16-1 = 15 flags and 15 mines, mine_count stays the same
        if self.flags < self.num_mines:
            self.mine_count += 1