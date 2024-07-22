import pygame

# Initialize Pygame 
pygame.init()

# Colors
COLORS = {
    'grey': (204, 204, 204),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'red': (255, 75, 86)
}

# Fonts
FONTS = {
    'buttons': pygame.font.SysFont("Arial", 18, True),
    'puzzle_digits': pygame.font.SysFont("Arial", 45, True),
    'solution_digits': pygame.font.SysFont("Arial", 45, False)
}

# Button dimensions
BUTTON_DIMENSIONS = {
    'action_btn': (140, 40),
    'return_to_main_menu_btn': (36, 36)
}

# Button positions
BUTTON_POSITIONS = {
    'sudoku_game_btn': (50, 65),
    'sudoku_solver_btn': (50, 145),
    'generate_btn': (96, 600),
    'solve_btn': (260, 600),
    'clear_btn': (424, 600),
    'new_game_btn': (260, 600),
    'return_to_main_menu_btn': (16, 668)
}

# Screen dimensions
SCREEN_DIMENSIONS = {
    'main_menu': (270, 252),
    'sudoku_screen': (660, 720)
}

# Sudoku Grid position and dimensions
GRID_CONFIG = {
    'position': (60, 40),
    'dimensions': (540, 540),
    'grid_side_length': 540,
    'cell_side_length': 60
}

