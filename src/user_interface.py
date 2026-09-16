"""
Module Name: user_interface.py
Description: Display the Minesweeper board using Python Arcade

Class Name: MinesweeperWindow
Description: Draw the board and pass user input to InputHandler

Inputs: Board state
Outputs: Game window
External Sources: ChatGPT
LLM AND GENERATIVE AI TOOLS:
A description of how and why AI was used: ChatGPT used for drafting and revising code with new, unfamiliar UI library
The specific prompts you entered: 
Vamos escribir el code en ingles para este proyecto sobre los minesweeper en una forma agile. Vamos seguir derechos de la proyecto y la forma de el code y nosotros implementacion solo necesita estar simlpe para este commit. Tambien nosotros usamos el bilbilitecha pyarcade por el UI y el input. Dame un Ui simple y un input handler simple para el proyecto pero, por favor, no implemente las caracteristicas por el juego todo, solo el UI y input handler por este generacion. Nosotros solomente neceistamos code corta y simple tabien. Por favor y gracias! Este es mi code y derechos por el proyecto: HINT: System Architecture 

Purpose: Describes the high-level structure to facilitate feature extensions by the Project 2 team

Components: 

Board Manager: Manages the 10x10 grid as a 2D array, tracking cell states (covered, flagged, uncovered, mine)

Game Logic: Handles gameplay rules, including mine placement, cell uncovering, recursive revealing, and win/loss detection

User Interface: Renders the grid, status indicators (e.g., mine count, game state), and user inputs (clicks for uncovering/flagging)

Input Handler: Processes user inputs (e.g., clicks, key presses) and communicates with Game Logic to update the Board

Data Flow: 

User input (click) → Input Handler validates and sends to Game Logic

Game Logic updates Board state (e.g., uncover cell, place flag)

Board state changes trigger UI updates (e.g., render number, flag, or mine)

Key Data Structures: 

2D array (10x10) for grid: stores cell states (0 = covered, 1 = flagged, 2 = uncovered number, 3 = mine)

Game state object: tracks mine count, flags remaining, and win/loss status


Assumptions: 

Fixed 10x10 grid size

Mine count user-specified (10–20) at game start

  
How you validated and revised the AI output: Proofreading, checking for sound logic, and testing, making sure it follows my original intentions and logic for a standard UI library
The challenges or limitations you faced while using AI: Validating logical execution of the UI code and ensuring that the UI functioned as intended took a significant amount of proofreading and testing.
Attributions: 
Authors: Kyler Russell, Blake Pennel
Creation Date: 9/15/2026
"""
import arcade
from game_logic import GameManager
import board_manager
from input_handler import InputHandler


CELL_SIZE = 50

BOARD_LEFT = 50
BOARD_BOTTOM = 50

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 650


class MinesweeperWindow(arcade.Window):
    """Simple Arcade UI for Minesweeper."""

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, "Minesweeper")

        self.game = GameManager(10)

        self.input_handler = InputHandler(
            self.game,
            CELL_SIZE,
            BOARD_LEFT,
            BOARD_BOTTOM
        )

    def on_draw(self):
        """Draw the current board."""
        self.clear(arcade.color.WHITE)

        for row in range(board_manager.BOARD_SIZE):
            for col in range(board_manager.BOARD_SIZE):

                left = BOARD_LEFT + col * CELL_SIZE
                bottom = BOARD_BOTTOM + row * CELL_SIZE

                if self.game.board.is_flagged(row, col):
                    color = arcade.color.YELLOW

                elif self.game.board.is_covered(row, col):
                    color = arcade.color.GRAY

                elif self.game.board.is_mine(row, col):
                    color = arcade.color.RED

                else:
                    color = arcade.color.LIGHT_GRAY

                arcade.draw_lbwh_rectangle_filled(
                    left + 1,
                    bottom + 1,
                    CELL_SIZE - 2,
                    CELL_SIZE - 2,
                    color
                )

        arcade.draw_text(
            f"Mines: {self.game.mine_count}",
            50,
            575,
            arcade.color.BLACK,
            18
        )

        if self.game.is_lost:
            arcade.draw_text(
                "Game Over",
                400,
                575,
                arcade.color.RED,
                18
            )

    def on_mouse_press(self, x, y, button, modifiers):
        """Send mouse input to the input handler."""
        self.input_handler.handle_click(x, y, button)


def main():
    MinesweeperWindow()
    arcade.run()


if __name__ == "__main__":
    main()