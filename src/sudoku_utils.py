from random import sample 
from pprint import pprint 

GRID_SIZE = 9 
BASE = 3 
SIDE = BASE * BASE
PERCENT_OF_CELLS_EMPTY = 50 # higher the percentage the harder the sudokus. 
row_base = range(BASE)


def is_position_valid(grid, num, position):
    """
    Determines if placing a given number in a specified position
    is valid within a Sudoku grid. Validity is assessed based on
    the number's absence from the given position's row, column,
    and 3x3 box.

    Parameters:
        grid (list[list[int]]): A 2D list representing the Sudoku grid.
        num (int): The number to be placed in the grid.
        position (tuple): A tuple (row_index, column_index) indicating the
        position in the grid where the number is to be placed.

    Returns:
        bool: Returns True if the number can be placed at the
              specified position without violating Sudoku rules,
              otherwise returns False.

    Examples:
    
    >>> grid = [[0, 3, 5, 8, 7, 1, 4, 9, 2],
                [1, 9, 2, 3, 5, 4, 6, 8, 7],
                [4, 8, 7, 9, 2, 6, 1, 3, 5],
                [9, 5, 4, 7, 6, 3, 8, 2, 1],
                [8, 2, 1, 5, 4, 9, 3, 7, 6],
                [3, 7, 6, 2, 1, 8, 9, 5, 4],
                [2, 1, 3, 4, 8, 5, 7, 6, 9],
                [7, 6, 9, 1, 3, 2, 5, 4, 8],
                [5, 4, 8, 6, 9, 7, 2, 1, 3]]
    
    >>> is_position_valid(grid, 3, (0,0))
    False
    >>> grid = [[7, 1, 3, 4, 0, 8, 0, 0, 0],
        [8, 0, 0, 5, 0, 2, 1, 0, 0],
        [2, 6, 5, 3, 0, 0, 9, 0, 0],
        [0, 0, 2, 7, 0, 0, 5, 0, 0],
        [0, 5, 0, 0, 0, 6, 0, 0, 0],
        [1, 4, 7, 0, 0, 9, 0, 0, 0],
        [3, 0, 0, 0, 8, 4, 0, 9, 0],
        [4, 0, 0, 0, 2, 0, 0, 0, 3],
        [0, 0, 9, 6, 0, 0, 0, 0, 4]]
    >>> is_position_valid(grid, 7, (0,6))
    False
    >>> is_position_valid(grid, 6, (1,8))
    True
    """
    
    # Check the row for the presence of the same number
    for row_index in range(len(grid)):
        if (grid[position[0]][row_index] == num and
            position[1] != row_index):
            return False

    # Check the column for the presence of the same number
    for column_index in range(len(grid)):
        if (grid[column_index][position[1]] == num and
            column_index != position[0]):
            return False

    # Check the 3 by 3 box for the presence of the same number
    box_x = position[1] // 3
    box_y = position[0] // 3
    
    for row_index in range(box_y * 3, box_y * 3 + 3):
        for column_index in range(box_x * 3, box_x * 3 + 3):
            if (grid[row_index][column_index] == num and
                (row_index, column_index) != position):
                return False

    return True

def shuffle(sequence):
    """
    Randomly shuffles the elements of the provided iterable sequence
    using the 'sample' function from the 'random' module.

    Parameters:
        sequence (iterable): The sequence (list, tuple, string, etc.)
                            whose elements are to be shuffled.

    Returns:
        shuffled_sequence (list): A new list containing the elements
                                from 'sequence' in a random order.

    Examples:
        Note: The output is random, and the following are only
                possible outcomes.

        >>> sequence = [1, 2, 3]
        >>> shuffle(sequence)
        [2, 3, 1]

        >>> shuffle('abcd')
        ['d', 'a', 'b', 'c']

        >>> shuffle(range(5))
        [4, 0, 2, 1, 3]
    """
    shuffled_sequence = sample(sequence, len(sequence))
    
    return shuffled_sequence

def pattern(row_index, column_index):
    """
    Calculates a unique number for each cell in a Sudoku grid
    based on its row and column indices.
    
    Ensures each number maintains Sudoku's row, column, and subgrid rules.
    
    Parameters:
        row_index (int): The index of the row in the Sudoku grid.
        column_index (int): The index of the column in the Sudoku grid.

    Returns:
        int: A computed integer that determines the position of a
            number in the grid's list of numbers. This value is used
            to index into a shuffled list of numbers from 1 to 9.

    Examples:
        Note: The output depends on the constants BASE and SIDE,
        and the examples assume BASE = 3, SIDE = 9.
        
        >>> pattern(0, 0)
        0
        >>> pattern(1, 2)
        5
        >>> pattern(8, 8)
        8
    """
    return (BASE * (row_index % BASE) + row_index // BASE + column_index) % SIDE



def generate_full_grid(grid):
    """
    Generates a complete, randomized 9x9 Sudoku grid. The function
    shuffles rows, columns, and numbers, then uses a mathematical
    pattern to place numbers in a valid Sudoku configuration.
    
    Parameters:
        grid (list[list[int]]): A 2D list representing the Sudoku grid
    
    Returns:
        None. The function fills the empty grid with a complete sudoku 
        puzzle. 
    
    Example:
        Note: The output is random, but it always adheres
            to the rules of Sudoku.
        >>> grid = [[0]*9 for i in range(9)]
        >>> generate_full_grid()
        [[5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    """

    row_indices = []
    
    # Generate a shuffled list of row indices
    for box_index in shuffle(row_base):
        for sub_row_index in shuffle(row_base):
            row_indices.append(box_index * BASE + sub_row_index)
    
    column_indices = []
    
    # Generate a shuffled list of column indices
    for box_index in shuffle(row_base):
        for sub_column_index in shuffle(row_base):
            column_indices.append(box_index * BASE + sub_column_index)
    
    # Shuffle numbers from 1 to 9
    shuffled_numbers = shuffle(range(1, BASE * BASE + 1))
    
    # Create the Sudoku board using the pattern function
    board = [[shuffled_numbers[pattern(row_index, column_index)] for
        column_index in column_indices] for row_index in row_indices]
    
    # Fill the input grid with the generated Sudoku board
    for i in range(SIDE):
        for j in range(SIDE):
            grid[i][j] = board[i][j]
            
    
def remove_cells_from_grid(grid):
    """
    Randomly removes a specified percentage of numbers from
    a completed Sudoku grid to create a puzzle. This is done by
    setting selected cells to zero to create empty spaces.

    Parameters:
        grid (list[list[int]]): A 2D list representing the 
                                complete/filled Sudoku grid
    Returns:
        None. The function modifies the grid by setting random cells to zero.
    
    Example:
        Note: The output is random.
        
        >>> grid = generate_full_grid()
        >>> pprint(grid)
        [[7, 2, 5, 9, 6, 8, 4, 1, 3],
         [3, 4, 1, 5, 7, 2, 8, 9, 6],
         [6, 8, 9, 1, 3, 4, 2, 5, 7],
         [8, 5, 7, 6, 4, 9, 1, 3, 2],
         [2, 1, 3, 7, 8, 5, 9, 6, 4],
         [4, 9, 6, 3, 2, 1, 5, 7, 8],
         [5, 3, 2, 8, 9, 7, 6, 4, 1],
         [9, 7, 8, 4, 1, 6, 3, 2, 5],
         [1, 6, 4, 2, 5, 3, 7, 8, 9]]
        >>> remove_cells_from_grid(grid)
        >>> pprint(grid)
        [[0, 0, 5, 0, 0, 0, 4, 1, 3],
        [3, 4, 1, 5, 0, 0, 0, 0, 0],
         [6, 0, 9, 1, 3, 0, 2, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 3, 2],
         [2, 1, 3, 0, 0, 0, 9, 0, 4],
         [4, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 8, 0, 7, 0, 4, 0],
         [9, 0, 8, 0, 0, 0, 0, 0, 0],
         [1, 6, 4, 0, 0, 0, 0, 8, 9]]
    """
    
    total_num_cells = GRID_SIZE * GRID_SIZE
    total_num_empty_cells = int(
        total_num_cells * (PERCENT_OF_CELLS_EMPTY / 100)
    )  
    
    # Randomly select cells to be emptied
    removed_cells_indices = sample(
        range(total_num_cells), total_num_empty_cells
    )
    
    for index in removed_cells_indices:
        # Convert the single index to row and column indices then set cell 
        # to zero
        row_index = index // GRID_SIZE
        column_index = index % GRID_SIZE
        grid[row_index][column_index] = 0


def find_empty_cell(grid):
    """
    Scans over a Sudoku grid to find the first empty cell, where
    empty cells are denoted by 0.

    Parameters:
        grid (list[list[int]]): A 2D list representing the unsolved Sudoku 
                                grid

    Returns:
        tuple or bool: Returns a tuple (row_index, column_index)
                       indicating the position of the first empty
                       cell found. If no empty cell is found,
                       returns False.

    Example:
        >>> grid = [[1, 6, 4, 3, 7, 5, 9, 8, 2],
                    [7, 5, 0, 6, 9, 2, 1, 4, 3],
                    [9, 3, 2, 8, 1, 4, 7, 6, 5],
                    [5, 4, 1, 7, 3, 8, 6, 2, 9],
                    [6, 2, 9, 4, 5, 1, 3, 7, 8],
                    [3, 8, 7, 2, 6, 9, 5, 1, 4],
                    [4, 9, 3, 1, 8, 6, 2, 5, 7],
                    [8, 1, 5, 9, 2, 7, 4, 3, 6],
                    [2, 7, 6, 5, 4, 3, 8, 9, 1]]
        >>> find_empty_cell(grid)
        (1, 2)
        >>> grid = [[9, 3, 4, 8, 1, 7, 6, 2, 5],
                    [8, 7, 1, 6, 5, 2, 9, 4, 3],
                    [6, 5, 2, 9, 3, 4, 8, 1, 7],
                    [2, 8, 7, 1, 6, 5, 4, 3, 9],
                    [1, 6, 3, 4, 7, 9, 2, 5, 8],
                    [4, 9, 5, 2, 8, 3, 1, 7, 6],
                    [3, 4, 6, 7, 9, 1, 5, 8, 2],
                    [7, 1, 9, 5, 2, 8, 3, 6, 4],
                    [5, 2, 8, 3, 4, 6, 7, 9, 1]]
        >>> find_empty_cell(grid)
        False
    """
    
    for row_index in range(len(grid)):
        for column_index in range(len(grid[0])):
            if grid[row_index][column_index] == 0:
                return (row_index, column_index)    
    return False



def clear_sudoku_grid(grid):
    """
    Clears a 9x9 Sudoku grid by setting all cells to zero. 

    Parameters:
        grid (list of lists): A 9x9 list of lists where each sublist 
                              represents a row in the Sudoku grid. Each 
                              element in the sublist represents a cell in 
                              the grid.

    Returns:
        None. The function modifies the grid, changing all the cell 
        values to 0.

    Example:
        >>> grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
        >>> clear_sudoku_grid(grid)
        >>> grid
        [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    """
    for row_index in range(9):
        for column_index in range(9):
            grid[row_index][column_index] = 0

def generate_puzzle(grid):
    """
    Generates a Sudoku puzzle by following these steps:
    1. Clears the existing Sudoku grid by calling 
       clear_sudoku_grid(grid)
    2. Generates a complete, filled 9x9 Sudoku grid by calling 
       generate_full_grid(grid)
    3. Removes a specified percentage of cells to create the puzzle by 
       calling remove_cells_from_grid(grid)

    Parameters:
        grid (list[list[int]]): A 2D list representing the Sudoku grid
   
   Returns:
        None. The function modifies the empty grid to create a sudoku 
        puzzle.                 
    Example:
        >>> grid = [[0]*9 for i in range(9)]
        >>> generate_puzzle(grid)
        >>> pprint(grid)
        [[0, 0, 5, 0, 0, 0, 4, 1, 3],
         [3, 4, 1, 5, 0, 0, 0, 0, 0],
         [6, 0, 9, 1, 3, 0, 2, 0, 0],
         [8, 0, 0, 0, 0, 0, 0, 3, 2],
         [2, 1, 3, 0, 0, 0, 9, 0, 4],
         [4, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 8, 0, 7, 0, 4, 0],
         [9, 0, 8, 0, 0, 0, 0, 0, 0],
         [1, 6, 4, 0, 0, 0, 0, 8, 9]]
    """
    clear_sudoku_grid(grid)
    generate_full_grid(grid)
    remove_cells_from_grid(grid)
    
