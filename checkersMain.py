import pygame
from checkers.constants import WIDTH, HEIGHT
from checkers.board import Board

# Create a main loop that checks for user input (mouse, keyboard, etc) 
# Draw all the pieces, the board, etc.

FPS = 60 # do we need this in the constants file? No, only references drawing the game

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

# set caption for display here: shows up in top title bar
pygame.display.set_caption('AI Minimax a/B Pruning Checkers')

def main (): ## define main event loop
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw(WINDOW)
        pygame.display.update()

    pygame.quit()

main()