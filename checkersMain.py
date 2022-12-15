import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from checkers.game import Game

# Create a main loop that checks for user input (mouse, keyboard, etc) 
# Draw all the pieces, the board, etc.

FPS = 60 # do we need this in the constants file? No, only references drawing the game

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption for display here: shows up in top title bar
pygame.display.set_caption('AI Minimax a/B Pruning Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main (): ## define main event loop
    run = True
    clock = pygame.time.Clock()
    game = Game(WINDOW)

    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN: # Select game piece with mouse
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()

main()