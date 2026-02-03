# All constant values are stored in this folder.
import pygame
import os   # For PyInstaller
import sys  # For Pyinstaller

pygame.init()   # Initialize PyGame

WIDTH, HEIGHT = 800, 800 # 800 pixels high by 800 pixels wide
ROWS, COLS = 8, 8 # 8 rows by 8 columns = std checkers board
SQUARE_SIZE = WIDTH//COLS # defines the area of one square

# RGB Color Scheme for Pygame
RED = (255, 0, 0) # define red color for pygame
WHITE = (255, 255, 255) # define white
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

# Get correct path for assets (PyInstaller vs. Source code)
def resource_path(relative_path):
    try:
        # PyInstaller creates a temp filder, stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # If running as source, use normal path
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

CROWN = pygame.transform.scale(
    pygame.image.load('checkers/assets/crown.png'),
    (44, 25)
)