"""
Module Name: game_logic.py
Description: Handle game logic and make calls to board_manager objects

Class Name: GameManager
Descrption: Handle all of the hidden game state knowledge and set the states of the board, following the game logic

Update Description: Add the win condition and ignore already uncovered cells when revealing

Inputs:
Outputs:
External Sources: DeepSeek V4.1 Flash
Attributions:

Update 9/16/2026 - Carter Steenhard and DeepSeek V4.1 Flash:
A description of how and why AI was used: DeepSeek V4.1 Flash used to add the win condition and the guard against revealing an already uncovered cell
How you validated and revised the AI output: Proofreading, logic tests for win, loss, repeated reveals, and flag counting, and a scripted window test of the status indicator
The challenges or limitations you faced while using AI: Keeping the win condition accurate when a cell is revealed more than once and matching the existing style
Authors: Drew Medlock, Carter Steenhard
Creation Date: 9/14/2026
"""

import board_manager
import random # Random is used to generate the mine locations

class GameManager:
    """
    Game manager is responsiglve for interacting with the board to update it accordinging to the game logic.
    """
    def __init__(self, num_mines) -> None: # Original code written by Drew Medlock
        """
        Has states for the running of the game.
        Gets a board object
        is_lost and is_won are set to easily identify if the game has ended
        num_mines is the number of mines given from the user selection
        mine_count is the number of mines - the number of flags
        Cells to clear is the amount of cells that haven't been cleared/uncovered of the safe cells
        """
        self.board = board_manager.BoardManager()
        self.is_lost = False
        self.is_won = False
        self.num_mines = num_mines
        self.mine_count = self.num_mines # will be updated with by decreasing when flagging
        self.flags = 0
        self.cells_to_clear = board_manager.BOARD_SIZE ** 2 - self.num_mines
        self.populate_mines()

    def populate_mines(self) -> None: # Original code written by Drew Medlock
        """
        Generates a list of all the possible locations, then picks the mines from it
        """
        locations = [(row, col) for row in range(board_manager.BOARD_SIZE) for col in range(board_manager.BOARD_SIZE)]
        mine_locations = random.sample(locations, self.num_mines)
        self.board.set_mines(mine_locations)

    def reveal_cell(self, row: int, col: int) -> None: # Original code written by Drew Medlock, updated by Carter Steenhard and DeepSeek V4.1 Flash
        # Being flagged prevents the cell from being uncovered, and already uncovered cells are ignored
        if not self.board.is_flagged(row, col) and self.board.is_covered(row, col):
            self.board.uncover_cell(row, col)
            if self.board.is_mine(row, col):
                self.is_lost = True
            else:
                self.cells_to_clear -= 1
                # Win by uncovering every cell that does not contain a mine
                if self.cells_to_clear <= 0:
                    self.is_won = True

    def flag_cell(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board.set_flagged(row, col)
        self.flags += 1
        # Check for preventing mine_count to going to negative if more than num_mines flags are placed
        if self.mine_count > 0:
            self.mine_count -= 1

    def unflag_cell(self, row: int, col: int) -> None: # Original code written by Drew Medlock
        self.board.remove_flag(row, col)
        self.flags -= 1
        # If there are more flags than the number of mines, then the mine_count shouldn't be increased from 0
        # Ex: 16 flags and 15 mines, function is called. 16-1 = 15 flags and 15 mines, mine_count stays the same
        if self.flags < self.num_mines:
            self.mine_count += 1