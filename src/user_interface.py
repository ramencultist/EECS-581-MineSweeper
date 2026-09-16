"""
Module Name: user_interface.py
Description: Handle users' view of the game through arcade 

Class Name: UIManager
Descrption: Renders the board, status indicators, and handles user input (does not process user input)

Inputs: width, height, title, game
Outputs: User Input directions to Input Handler
External Sources: api.arcade.academy for references to arcade drawing and input handling
Attributions: Skeleton created by Gemini, edited and verified by Kyler Russell
Authors: Kyler Russell, 
Creation Date: 9/15/2026
"""

import arcade
from board_manager import BoardManager, BOARD_SIZE
from game_logic import GameManager # TODO: Remove this and implement Input Handler

WINDOW_MARGIN = 10
HEADER_HEIGHT = 40
BORDER_THICKNESS = 2
"""
Set layout constants for the board, header, and game windows
"""

class UIManager(arcade.Window): 
    """
    Handles the user interface and drawing of the board.
    """
    def __init__(self, width: int, height: int, title: str, game: GameManager) -> None:
        """
        Initializes the ui manager.
        """
        super().__init__(width=width, height=height, title=title)
        self.background_color = arcade.color.GRAY
        self.game = game
        
        # Calculate bounding areas
        body_size = self.width - (2 * WINDOW_MARGIN)
        body_width = body_size
        body_height = body_size
        body_bottom = WINDOW_MARGIN

        header_bottom = body_bottom + body_height + WINDOW_MARGIN
        header_height = HEADER_HEIGHT
        
        # Initialize components
        self.header = HeaderUI(WINDOW_MARGIN, header_bottom, body_width, header_height)
        self.board_ui = BoardUI(WINDOW_MARGIN, body_bottom, body_width, body_height)
    
    def on_draw(self): 
        """
        Renders the entire game screen.
        """
        self.clear()
        self.header.draw(self.game)
        self.board_ui.draw(self.game.board)
    
class BoardUI:
    """
    Handles rendering of the game board body and cell grid.
    """
    def __init__(self, left: float, bottom: float, width: float, height: float) -> None:
        """
        Initializes the board ui.
        """
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height
        self.cell_size = width / BOARD_SIZE

    def draw(self, board: BoardManager): # Code written by Gemini, edited by Kyler Russell
        """
        Draws the board.
        """
        # Sets the color of the board
        arcade.draw_lbwh_rectangle_filled(
            left=self.left,
            bottom=self.bottom,
            width=self.width,
            height=self.height,
            color=arcade.color.LIGHT_GRAY
        )

        # Sets the color of the border
        arcade.draw_lbwh_rectangle_outline(
            left=self.left,
            bottom=self.bottom,
            width=self.width,
            height=self.height,
            color=arcade.color.BLACK,
            border_width=BORDER_THICKNESS
        )
        
        # Draw cell grid lines
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                cell_left = self.left + col * self.cell_size
                cell_bottom = self.bottom + (BOARD_SIZE - 1 - row) * self.cell_size
                
                # Draw cell grid lines
                arcade.draw_lbwh_rectangle_outline(
                    cell_left, cell_bottom, self.cell_size, self.cell_size,
                    arcade.color.DARK_GRAY, border_width=1
                )


class HeaderUI:
    """
    Handles the drawing of the header
    """
    def __init__(self, left: float, bottom: float, width: float, height: float) -> None:
        """
        Initializes the header ui.
        """
        self.left = left
        self.bottom = bottom
        self.width = width
        self.height = height

    def draw(self, game: GameManager) -> None: # Code written by Gemini, edited by Kyler Russell
        """
        Renders the entire game screen.
        """
        center_y = self.bottom + (self.height / 2)

        # draw mines left
        arcade.draw_text(
            text=f"Mines: {game.mine_count}", # - game.flag_count}",  TODO: Change to work with Input Handler rather than here. 
            x=self.left + 10,
            y=center_y,
            color=arcade.color.BLACK,
            font_size=16,
            bold=True,
            anchor_y="center"
        )

        # determine status
        if game.is_won:
            status_text = "Won!"
            status_color = arcade.color.DARK_GREEN
        elif game.is_lost:
            status_text = "Lost!"
            status_color = arcade.color.DARK_RED
        else:
            status_text = "Playing"
            status_color = arcade.color.BLACK

        # draw status
        arcade.draw_text(
            text=f"Status: {status_text}",
            x=self.left + 150,
            y=center_y,
            color=status_color,
            font_size=16,
            bold=True,
            anchor_y="center"
        )
        

# TEMP to test the UI, TODO: Delete before submission
if __name__ == "__main__":
    game = GameManager(num_mines=10)
    window = UIManager(width=500, height=580, title="Minesweeper", game=game)
    arcade.run()
