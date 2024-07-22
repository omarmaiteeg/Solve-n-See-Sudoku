import pygame, config, time
import sudoku_utils as su
# Initialize Pygame 
pygame.init()




def draw_all_grid_numbers(screen, grid, puzzle_grid, user_grid):
    """
    Draws all non-zero numbers from the Sudoku grid onto a
    Pygame display surface, using different styles for numbers that
    are originally part of the puzzle versus those that are solutions
    added later or numbers inputted by the user. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                 the numbers will be drawn.
        grid (list[list[int]]): A 2D list representing the current state 
                                of the Sudoku grid, where each element 
                                is an integer from 0-9 (0 represents an 
                                empty cell).
        puzzle_grid (list[list[int]]): A 2D list representing the initial 
                                       puzzle setup representing the numbers
                                       originally provided in the puzzle.
        users_grid (list[list[int]]): A 2D list representing the numbers
                                      inputted by the user.
                                      
    Returns:
        None. This function draws directly on the specified surface but 
              does not return any value.
    """

    for row_index in range(9):  
        for column_index in range(9): 
             
            # Determine the font and color based on the cell's origin
            if grid[row_index][column_index] != 0:
                if not is_grid_empty(user_grid) and user_grid[row_index][column_index] != 0:
                    font = config.FONTS['puzzle_digits']
                    color = config.COLORS['black']
                elif puzzle_grid[row_index][column_index] != 0:
                    font = config.FONTS['puzzle_digits']
                    color = config.COLORS['black']
                else:
                    font = config.FONTS['solution_digits']
                    color = config.COLORS['black']
                
                position = row_index, column_index
                num = str(grid[row_index][column_index])
                
                # Draw the number in the cell
                draw_number_in_cell(screen, num, color, font, position)
    

def draw_sudoku_grid(screen, position):
    """
    Draws an empty 9x9 Sudoku grid on a Pygame display
    surface at a specified position. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the grid will be drawn.
        position (tuple): The (x, y) coordinates for the top-left corner 
                         of the grid on the display surface.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    x_coordinate = position[0]
    y_cooridinte = position[1]
    subgrid_thickness = 5
    grid_thickness = 1
    
    
    for i in range(10):  # There are 10 lines in a 9 cell by 9 cell grid.
        if i % 3 == 0:
            thickness = subgrid_thickness
        else:
            thickness = grid_thickness
        
        
        # Draw vertical lines
        pygame.draw.line(
            screen, 
            config.COLORS['black'], 
            (
                x_coordinate + config.GRID_CONFIG['cell_side_length'] * i, 
                y_cooridinte
            ), 
            (
                x_coordinate + config.GRID_CONFIG['cell_side_length'] * i, 
                y_cooridinte + config.GRID_CONFIG['grid_side_length']
            ), 
            thickness
        )
        
        # Draw horizontal lines
        # Extend the first and last horizontal lines for a
        # cleaner look at the borders
        padding = 2
        if i == 0 or i == 9: 
            pygame.draw.line(
                screen, 
                config.COLORS['black'], 
                (
                    x_coordinate - padding, 
                    y_cooridinte + config.GRID_CONFIG['cell_side_length'] * i), 
                (
                    x_coordinate + config.GRID_CONFIG['grid_side_length'] + padding, 
                    y_cooridinte + config.GRID_CONFIG['cell_side_length'] * i),  
                thickness
            )
        else:
            pygame.draw.line(
                screen, 
                config.COLORS['black'], 
                (
                    x_coordinate, 
                    y_cooridinte + config.GRID_CONFIG['cell_side_length'] * i
                ), 
                (
                    x_coordinate + config.GRID_CONFIG['grid_side_length'], 
                    y_cooridinte + config.GRID_CONFIG['cell_side_length'] *  i
                ), 
                thickness
                )


def draw_number_in_cell(screen, num, color, font, position):
    """
    Draws a given number in a specified cell of a Sudoku grid
    on a Pygame display surface.
    
    The function places the number at the center of the cell. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the number will be drawn.
        num (str): The number to be drawn within the Sudoku grid cell.
                   It should be a single character string.
        color (tuple): A tuple (R, G, B) representing the color of the
                       number to be drawn.
        font (pygame.font.Font): The Pygame font object used for
                                rendering the number.
        position (tuple): A tuple (x, y) representing the row and
                         column indices of the cell in the grid.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    
    x_coordinate, y_coordinate = position

    text = font.render(num, True, color)
    text_rect = text.get_rect()  

    # Calculate the position to center the text
    text_x_coordinate = ((
        (y_coordinate * config.GRID_CONFIG['cell_side_length'] +
        (config.GRID_CONFIG['cell_side_length'] - text_rect.width) // 2) + 
        config.GRID_CONFIG['cell_side_length'])
    )
    text_y_coordinate = (
        ((x_coordinate * config.GRID_CONFIG['cell_side_length']) +
        (config.GRID_CONFIG['cell_side_length'] - text_rect.height) // 2) + 
        config.GRID_CONFIG['cell_side_length'] - 20
    )

    
    screen.blit(text, (text_x_coordinate, text_y_coordinate))


def draw_focused_main_menu_button(screen, position, size):
    """
    Draws the return to main menu button with focused
    appearance on a Pygame display surface. 

    The function also places an icon image on the button, aligned
    within the button to represent its purpose. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                 the button will be drawn.
        position (tuple): A tuple (x, y) specifying the top-left
                          corner coordinates of the button on the
                          display surface.
        size (tuple): A tuple (width, height) for the dimensions of the 
        button.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    
    x_coordinate, y_coordinate = position
    button_width, button_height = size
    
    pygame.draw.rect(
        screen, 
        config.COLORS['white'], 
        (
            x_coordinate, 
            y_coordinate, 
            button_width, 
            button_height
        )
    )
    
    pygame.draw.rect(
        screen, 
        config.COLORS['grey'],
        (
            x_coordinate, 
            y_coordinate, 
            button_width, 
            button_height
        ),
        1, 
        2
    )
    return_menu_btn_icon_focused = pygame.image.load("../assets/return_icon_grey.png")
    image_rect = return_menu_btn_icon_focused.get_rect()
    

    # Calculate the position to center the icon
    icon_x_coordinate = (x_coordinate + (button_width - image_rect.width) // 2)
    icon_y_coordinate = y_coordinate + (button_height - image_rect.height) // 2
    
    screen.blit(
        return_menu_btn_icon_focused, 
        (
            icon_x_coordinate, 
            icon_y_coordinate
        )
    )


def draw_default_main_menu_button(screen, position, size):
    """
    Draws the return to main menu button with default
    appearance on a Pygame display surface. 

    The function also places an icon image on the button, aligned
    within the button to represent its purpose. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the button will be drawn.
        position (tuple): A tuple (x, y) specifying the top-left
                          corner coordinates of the button on the
                          display surface.
        size (tuple): A tuple (width, height) for the dimensions of 
                      the button.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """

    
    x_coordinate, y_coordinate = position
    button_width, button_height = size

    padding = 1 # Padding ensures that the filled rectangle is within the border

    pygame.draw.rect(
        screen, 
        config.COLORS['black'],
        (
            x_coordinate + padding, 
            y_coordinate + padding, 
            button_width - padding, 
            button_height - padding
        )
    )
    pygame.draw.rect(
        screen, config.COLORS['black'],
        (x_coordinate, y_coordinate, button_width, button_height),
        1, 2
    )
    return_menu_btn_icon_default = pygame.image.load("../assets/return_icon_grey.png")
    image_rect = return_menu_btn_icon_default.get_rect()
    
    icon_x_coordinate = x_coordinate + (button_width - image_rect.width) // 2
    icon_y_coordinate = y_coordinate + (button_height - image_rect.height) // 2
    
    screen.blit(return_menu_btn_icon_default, (icon_x_coordinate, icon_y_coordinate))
    
def draw_return_main_menu_button(screen, position, size):
    """
    Draws the return to main menu button on the specified Pygame
    display surface, with the appearance changing based on whether
    the mouse is hovering over it.
    
    The button represents a 'Return to Main Menu'  action

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which the 
                                 button will be drawn.
        position (tuple): A tuple (x, y) representing the top-left corner 
                         of the button on the display surface. 
        size (tuple): A tuple (width, height) representing the dimensions 
                      of the button.
    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    
    mouse_position = get_mouse_position() 
    x_coordinate, y_coordinate = position
    button_width, button_height = size
    
    mouse_over_button_condition = (
        x_coordinate < mouse_position[0] < x_coordinate + button_width
        and y_coordinate < mouse_position[1] < y_coordinate + button_height
    )

    if mouse_over_button_condition:
        draw_focused_main_menu_button(screen, position, size)
    else:
        draw_default_main_menu_button(screen, position, size)
        


def get_mouse_position():
    """
    Gets the current position of the mouse cursor within the screen.

    Returns:
        mouse_position (tuple): A tuple containing the x and y
                                coordinates of the mouse cursor.

    Examples:
        >>> get_mouse_position()
        (20, 150)

        >>> get_mouse_position()
        (60, 60)
    """
    mouse_position = pygame.mouse.get_pos()
    
    return mouse_position


def is_button_pressed(event, button_position, button_size):
    """
    Determines if a mouse button press occurs within the bounds of a
    specified button or area and returns True if the this condition is met.
    

    Parameters:
        event (pygame.event.Event): A Pygame event object.
        button_position (tuple): A tuple specifying the x and y
                                 coordinates of the top-left corner
                                 of the button.
        button_size (tuple): A tuple specifying the width and height
                             of the button.
    Returns:
        bool: True if the mouse button press occurs
            within the bouds of the specified button,
            otherwise, nothing is returned.
    """
    
    mouse_position = get_mouse_position()

    x_coordinate, y_coordinate = button_position
    button_width, button_height = button_size

    pressed_button_condition = (
        event.type == pygame.MOUSEBUTTONDOWN and
        event.button == 1 and 
        x_coordinate < mouse_position[0] < x_coordinate + button_width and 
        y_coordinate < mouse_position[1] < y_coordinate + button_height
    )
    
    if pressed_button_condition:
        return True


def draw_default_action_button(screen, position, size, text):
    """
    Draws a button with a default appearance on a Pygame display
    surface. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the button will be drawn.
        position (tuple): The (x, y) coordinates for the top-left
                          corner of the button on the display surface.
        size (tuple): The (width, height) dimensions of the button.
        text (str): The text to be displayed on the button.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    x_coordinate, y_coordinate = position
    button_width, button_height = size
    
    pygame.draw.rect(
        screen, 
        config.COLORS['black'],
        (
            x_coordinate + 2, 
            y_coordinate + 2, 
            button_width - 4, 
            button_height - 4
        )
    )
    pygame.draw.rect(
        screen, 
        config.COLORS['black'],
        (
            x_coordinate, 
            y_coordinate, 
            button_width, 
            button_height
        ),
        5, 
        2
    )
    
    text_surface = config.FONTS['buttons'].render(
        text, True, config.COLORS['white']
    )
    
    # Calculate the center position for the text
    text_x_coordinate = (
        x_coordinate + (button_width - text_surface.get_width())
        // 2
    )
    text_y_coordinate = (
        y_coordinate + (button_height - text_surface.get_height())
        // 2
    )
    
    screen.blit(text_surface, (text_x_coordinate, text_y_coordinate))
    
    
def draw_focused_action_button(screen, position, size, text):
    """
    Draws a button with a focused appearance on a Pygame display
    surface. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the button will be drawn.
        position (tuple): The (x, y) coordinates for the top-left
                          corner of the button on the display surface.
        size (tuple): The (width, height) dimensions of the button.
        text (str): The text to be displayed on the button.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    
    
    x_coordinate, y_coordinate = position
    button_width, button_height = size
    
    pygame.draw.rect(
        screen, 
        config.COLORS['white'],
        (
            x_coordinate, 
            y_coordinate, 
            button_width, 
            button_height
        )
    )
    pygame.draw.rect(
        screen, 
        config.COLORS['grey'],
        (
            x_coordinate, 
            y_coordinate, 
            button_width, 
            button_height
        ),
        1, 
        2
    )

    text_surface = config.FONTS['buttons'].render(
        text, True, config.COLORS['grey']
    )
    text_x_coordinate = (
        x_coordinate + (button_width - text_surface.get_width())
        // 2
    )
    text_y_coordinate = (
        y_coordinate + (button_height - text_surface.get_height())
        // 2
    )

    screen.blit(text_surface, (text_x_coordinate,text_y_coordinate))


def draw_action_button(screen, position, size, text):
    """
    Draws an action button on the specified Pygame display surface,
    with the appearance changing based on whether the mouse is
    hovering over it.

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                the button will  be drawn.
        position (tuple): The (x, y) coordinates for the top-left
                          corner of the button on the display surface.
        size (tuple): The (width, height) of the button.
        text (str): The text to be displayed on the button.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    mouse_position = get_mouse_position() 
    x_coordinate, y_coordinate = position
    button_width, button_height = size
    
    mouse_over_button_condition = (
        x_coordinate < mouse_position[0] < x_coordinate + button_width and 
        y_coordinate < mouse_position[1] < y_coordinate + button_height
    )
    
    if mouse_over_button_condition:
        draw_focused_action_button(screen, position, size, text)
    else:
        draw_default_action_button(screen, position, size, text)

       
def erase_cell_content(screen, position):
    """
    Erases the content of a specified cell in a Sudoku grid by
    filling it with a background color.
    
    This function is used to clear a cell before redrawing
    a number during the solving process or when resetting parts of the
    grid.
    
    It draws a smaller rectangle within the cell to
    overwrite any existing content with the background color.

    Parameters:
        screen (pygame.Surface): The Pygame display surface on which
                                 the grid is visualized.
        colour (tuple): A tuple (R, G, B) representing the color used
                        to fill the cell. This is the background color
                        of the grid.
        position (tuple): A tuple (row_index, column_index)
                          representing the grid coordinates of
                          the cell to be erased.

    Returns:
        None. This function draws directly on the specified
              surface but does not return any value.
    """
    
    row_index, column_index = position
    pygame.draw.rect(
        screen, 
        config.COLORS['white'], 
        (
            (column_index + 1) * config.GRID_CONFIG['cell_side_length'] + 3, 
            (row_index + 1) * config.GRID_CONFIG['cell_side_length'] + 3 - 20, 
            config.GRID_CONFIG['cell_side_length'] - 8, 
            config.GRID_CONFIG['cell_side_length'] - 8
        )

        )
    

def is_grid_empty(grid):
    """
    Checks if a given Sudoku grid is empty i.e. one 
    where all cells contain the value 0.

    Parameters:
        grid (list[list[int]]): A 2D list representing the Sudoku grid.

    Returns:
        bool: Returns True if all cells in the grid are 0, indicating
              the grid is empty. Returns False if any cell contains
              a non-zero value.

    Example:
        >>> grid = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        >>> is_grid_empty(grid)
        True

        >>> grid = [
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        >>> is_grid_empty(grid)
        False
    """
    for row_index in range(len(grid)):
        for column_index in range(len(grid)):
            if grid[row_index][column_index] != 0:
                return False
    return True


def solve_sudoku(screen, grid):
    """
    Attempts to solve a Sudoku puzzle using a backtracking algorithm.
    This function recursively places numbers in empty cells and
    visually updates the grid on the Pygame display surface.
    It visually represents each trial of number placements and
    backtracks if a placement does not lead to a solution.

    Parameters:
        screen (pygame.Surface): The Pygame display surface used for
                                 visualizing the Sudoku grid.
        grid (list[list[int]]): A 9x9 matrix representing the Sudoku
                                    puzzle, where 0 indicates an empty cell,
                                    and numbers 1 through 9 are placed
                                    according to Sudoku rules.

    Returns:
        bool: Returns True if the Sudoku puzzle is solved successfully,
             False otherwise. The grid is modified to reflect the
             solution if successful.
    """
    
    # Check if the grid is empty before solving
    if is_grid_empty(grid): 
        return
    
    # Check if the grid is empty before solving
    find = su.find_empty_cell(grid)
    
    if not find:
        # No empty cells found, puzzle is solved
        return True
    else:
        row_index, column_index = find

    for num in range(1, 10):
        
        # Check if the number can be placed in the empty cell found
        if su.is_position_valid(grid, num, (row_index, column_index)):
            grid[row_index][column_index] = num
            erase_cell_content(screen, (row_index, column_index))
            
            # Visual update
            draw_number_in_cell(
                screen, 
                str(num), 
                config.COLORS['black'], 
                config.FONTS['solution_digits'], 
                (row_index, column_index)
                )
            pygame.display.update()
            
            # Delay for visualization
            time.sleep(0.025) 
            
            # Recursively try to solve the grid with the current number placed
            if solve_sudoku(screen, grid):
                return True
            
            # If placing num doesn't lead to a solution, reset the cell and backtrack
            else:
                grid[row_index][column_index] = 0
            
    return False

    
def draw_red_circle_over_invalid_positions(screen, grid):
    """
    Draws red circles over invalid positions in the Sudoku grid.
    An invalid position is a cell that violates Sudoku rules.

    Parameters:
        screen (pygame.Surface): The Pygame display surface used for
                                 visualizing the Sudoku grid.
        grid (list of list of int): A 2D list representing the Sudoku grid.

    None. This function draws directly on the specified
              surface but does not return any value.
    """
    # List to store the coordinates of invalid cells
    coordinates_invalid_cells = []
    
    for row_index in range(9):
        for column_index in range(9):
            if grid[row_index][column_index] and not su.is_position_valid(grid, grid[row_index][column_index], (row_index, column_index)): 
                coordinates_invalid_cells.append((row_index, column_index))
    
    # Draw a red circle over each invalid cell
    for position in coordinates_invalid_cells:
        pygame.draw.circle(
            screen, 
            config.COLORS['red'], 
            (
                position[1] * config.GRID_CONFIG['cell_side_length'] + 110, 
                position[0] * config.GRID_CONFIG['cell_side_length'] + 110 - 20
            ), 
            4
        )
        
      
def highlight_clicked_cell(screen, position):
    """
    Draws a border around the clicked cell in the Sudoku grid.

    Parameters:
        screen (Surface): The Pygame display surface to draw the border on.
        position (tuple): The (x, y) coordinates of the clicked position in pixels.
    """
    
    column_index, row_index = (
        (position[1] // config.GRID_CONFIG['cell_side_length'] * 
        config.GRID_CONFIG['cell_side_length'] - 20), 
        (position[0]  // config.GRID_CONFIG['cell_side_length']) * 
        config.GRID_CONFIG['cell_side_length']
        )
    
    pygame.draw.rect(
        screen, 
        config.COLORS['black'], 
        (row_index, 
         column_index, 
         config.GRID_CONFIG['cell_side_length'], 
         config.GRID_CONFIG['cell_side_length']), 
        5)
    
    pygame.display.update()



def handle_solver_screen_input(screen, position, grid, user_grid):
    """
    Handles user input on the game screen, allowing users to insert digits 
    into the Sudoku grid. Highlights the clicked cell and waits for a key press 
    to insert the corresponding number into the grid. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface used for highlighting 
                                 the clicked cell.
        position (tuple): The (x, y) coordinates of the clicked position in pixels.
        grid (list of list of int): A 2D list representing the current state of 
                                    the Sudoku grid, where each element is an 
                                    integer from 0-9 (0 represents an empty cell).
        user_grid (list of list of int): A 2D list representing the numbers 
                                          inputted by the user.

     Returns:
        None. This function draws directly on the specified surface but 
              does not return any value.
    """
    # Convert from pixel position to grid cell indices
    row_index, column_index = (
        position[1] // config.GRID_CONFIG['cell_side_length'], 
        position[0] // config.GRID_CONFIG['cell_side_length']
        )
    
    while True:
        # Highlight the clicked cell
        highlight_clicked_cell(screen, position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                
                # If '0' is pressed, clear the cell and set it to 0 in the grid
                if event.key == 48: # ASCII code for '0'
                    grid[row_index - 1][column_index - 1] = 0
                    return
                
                # If a number between 1 and 9 is pressed and is a valid position, insert it
                if 0 < event.key - 48 < 10 and su.is_position_valid(grid, (event.key - 48), (row_index - 1, column_index - 1)):
                    grid[row_index - 1][column_index - 1] = event.key - 48
                    user_grid[row_index - 1][column_index - 1] = event.key - 48
                    
                return


def handle_game_screen_input(screen, position, grid, puzzle_grid):
    """
    Handles user input on the game screen, allowing users to insert digits 
    into the Sudoku grid. Highlights the clicked cell and waits for a key press 
    to insert the corresponding number into the grid. 

    Parameters:
        screen (pygame.Surface): The Pygame display surface used for 
                              highlighting the clicked cell.
        position (tuple): The (x, y) coordinates of the clicked position in 
                          pixels.
        grid (list of list of int): A 2D list representing the current state of 
                                    the Sudoku grid, where each element is an 
                                    integer from 0-9 (0 represents an empty cell).
        puzzle_grid (list of list of int): A 2D list representing the initial 
                                           puzzle setup, where non-zero values 
                                           are the numbers originally provided 
                                           in the puzzle.
     Returns:
        None. This function draws directly on the specified surface but 
              does not return any value.
    """
    
    # Convert from pixel position to grid cell indices
    row_index, column_index = (
        position[1] // config.GRID_CONFIG['cell_side_length'], 
        position[0] // config.GRID_CONFIG['cell_side_length']
        )
    
    while True:

        highlight_clicked_cell(screen, position)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                 
                # If '0' is pressed, clear the cell and set it to 0 in the grid
                if event.key == 48 and puzzle_grid[row_index - 1][column_index - 1] == 0 :
                    grid[row_index - 1][column_index - 1] = 0
                    return
                
                # If a number between 1 and 9 is pressed and the cell is not part of the initial puzzle, insert it
                if 0 < event.key - 48 < 10 and puzzle_grid[row_index - 1][column_index - 1] == 0:
                    grid[row_index - 1][column_index - 1] = event.key - 48
                return


