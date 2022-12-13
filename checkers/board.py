# board class: responsible for draing the board and pieces
import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE

class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12 # define the amount of red and black pieces each player begins with
        self.red_kings = self.white_kings = 0 # no one starts with king pieces

    def draw_squares(self, window):
        window.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2): # even indices are red, odd are black
                pygame.draw.rect(window, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))