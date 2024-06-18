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
    'buttons': pygame.font.SysFont("Arial", 19, True),
    'puzzle_digits': pygame.font.SysFont("Arial", 45, True),
    'solution_digits': pygame.font.SysFont("Arial", 45, False)
}

# Button dimensions
BUTTON_DIMENSIONS = {
    'action_btn': (160, 40),
    'return_to_main_menu_btn': (40, 40)
}

# Button positions
BUTTON_POSITIONS = {
    'sudoku_game_btn': (50, 65),
    'sudoku_solver_btn': (50, 145),
    'generate_btn': (70, 625),
    'solve_btn': (250, 625),
    'clear_btn': (430, 625),
    'new_game_btn': (250, 625),
    'return_to_main_menu_btn': (22, 672)
}

# Screen dimensions
SCREEN_DIMENSIONS = {
    'main_menu': (270, 252),
    'sudoku_screen': (660, 720)
}

# Sudoku Grid position and dimensions
GRID_CONFIG = {
    'position': (60, 60),
    'dimensions': (540, 540),
    'grid_side_length': 540,
    'cell_side_length': 60
}

