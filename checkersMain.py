import pygame
import math
import minimax.algorithm
import checkers.board, checkers.constants, checkers.game, checkers.piece
from minimax.algorithm import minimax
from checkers.constants import HEIGHT, WIDTH, WHITE, SQUARE_SIZE, RED
from checkers.game import Game

# Create a main loop that checks for user input (mouse, keyboard, etc) 
# Draw all the pieces, the board, etc.

FPS = 60 # References drawing the game
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption for display here: shows up in top title bar
pygame.display.set_caption('AI Minimax Checkers')

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

    while run:
        clock.tick(FPS)

        if game.turn == WHITE: # Start AI HERE:
            # 5 = depth to traverse
            value, new_board = minimax(game.get_board(), 5, float('-inf'), float('inf'), True, game)
            game.ai_move(new_board)
    
        if game.winner() != None:
            print(game.winner()) # prints red (255, 0, 0) or white (255, 255, 255) to the terminal
            run = False # Terminates the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False # Teminate Game

            if event.type == pygame.MOUSEBUTTONDOWN: # Select game piece with mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)
        
        game.update()
    
    pygame.quit()

main()