import pygame
import math
from minimax.algorithm import *
from checkers.board import *
from checkers.constants import *
from checkers.game import *
from checkers.piece import *
from enhanced_terminal_widget import EnhancedTerminalWidget # Test terminal for game stats / monitoring

# Create a main loop that checks for user input (mouse, keyboard, etc) 
# Draw all the pieces, the board, etc.

FPS = 60 # References drawing the game
WINDOW_HEIGHT = HEIGHT + TERMINAL_HEIGHT
WINDOW = pygame.display.set_mode((WIDTH, WINDOW_HEIGHT))

# set caption for display here: shows up in top title bar
pygame.display.set_caption('Minimax AI Checkers with Alpha/Beta Pruning')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

# Main event loop for game
def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)
    terminal = EnhancedTerminalWidget(WINDOW, 0, HEIGHT, WIDTH, TERMINAL_HEIGHT)
    terminal.capture_print()

    print("Minimax AI Checkers - Alpha/Beta Pruning")
    print("You are RED. AI is WHITE. Good luck!")

    while run:
        clock.tick(FPS)

        if game.turn == WHITE: # Start AI HERE:
            # 5 = depth to traverse
            value, new_board = minimax(game.get_board(), 5, float('-inf'), float('inf'), True, game)
            game.ai_move(new_board)
    
        if game.winner() != None:
            winner = game.winner()
            if winner == WHITE:
                print(f'White AI Wins!!\n')
            elif winner == RED:
                print(f'RED Player Wins\n')
            print(f'Thanks for Playing! Goodbye!\n')
            run = False # Terminates the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Teminate Game

            if terminal.handle_event(event):
                continue  # Terminal handled it, don't process game event

            if event.type == pygame.MOUSEBUTTONDOWN: # Select game piece with mouse
                pos = pygame.mouse.get_pos()
                if pos[1] < HEIGHT: # Clicks in terminal area not sent to `game.select()` as coords.
                    row, col = get_row_col_from_mouse(pos)
                    game.select(row, col)

        game.update()
        terminal.draw()
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()