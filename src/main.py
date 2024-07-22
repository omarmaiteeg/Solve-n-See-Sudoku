import pygame
import sys
import config
import pygame_ui_utils as pui
import sudoku_utils as su

def display_sudoku_screen(mode='game'):
    """
    Displays the Sudoku screen based on the specified mode 
    ('game' or 'solver'). 
    
    Initializes the game or solver screen, draws necessary elements, and handles 
    user interactions.

    Parameters:
        mode (str): The mode of the screen, either 'game' for the
                    game screen or 'solver' for the solver screen. 
                    Default is 'game'.

    Returns:
        None
    """
    screen = pygame.display.set_mode(
                config.SCREEN_DIMENSIONS['sudoku_screen']
            )
    
    # Initialize grids
    grid = [[0]*9 for i in range(9)]
    user_grid = [[0]*9 for i in range(9)]
    puzzle_grid = [[0]*9 for i in range(9)]
    
    # Generate initial puzzle if in game mode
    if mode == 'game':
        su.generate_puzzle(grid)
        puzzle_grid = [row[:] for row in grid]
    
    run = True
    while run:
        
        screen.fill(config.COLORS['white'])
        
        # Draw Buttons based on mode either game or solver
        if mode == 'game':
            pui.draw_action_button(
                screen,
                config.BUTTON_POSITIONS['new_game_btn'],
                config.BUTTON_DIMENSIONS['action_btn'],
                "New Game"
            )
        
        else:
            pui.draw_action_button(
                screen,
                config.BUTTON_POSITIONS['generate_btn'],
                config.BUTTON_DIMENSIONS['action_btn'],
                "Generate"
            )
            pui.draw_action_button(
                screen,
                config.BUTTON_POSITIONS['solve_btn'],
                config.BUTTON_DIMENSIONS['action_btn'],
                "Solve"
            )
            pui.draw_action_button(
                screen,
                config.BUTTON_POSITIONS['clear_btn'],
                config.BUTTON_DIMENSIONS['action_btn'],
                "Clear"
            )
        
        # Draw buttons and grid found in both modes
        pui.draw_return_main_menu_button(
            screen,
            config.BUTTON_POSITIONS['return_to_main_menu_btn'],
            config.BUTTON_DIMENSIONS['return_to_main_menu_btn']
        )
        pui.draw_sudoku_grid(
            screen, config.GRID_CONFIG['position']
        )
        pui.draw_all_grid_numbers(
            screen, grid, puzzle_grid, user_grid
        )
        
        # Draw additional red circle feature for game mode
        if mode == 'game':
            pui.draw_red_circle_over_invalid_positions(
                screen, grid
            )
        
        for event in pygame.event.get():
            if mode == 'game':
                # Game screen button functionality
                if pui.is_button_pressed(
                    event,
                    config.BUTTON_POSITIONS['new_game_btn'],
                    config.BUTTON_DIMENSIONS['action_btn']
                ):
                    su.generate_puzzle(grid)
                    puzzle_grid = [row[:] for row in grid]
                    su.clear_sudoku_grid(user_grid)
            else:
                # Solver screen buttons' functionalities
                if pui.is_button_pressed(
                    event, config.BUTTON_POSITIONS['generate_btn'],
                    config.BUTTON_DIMENSIONS['action_btn']
                ):
                    su.generate_puzzle(grid)
                    puzzle_grid = [row[:] for row in grid]
                    su.clear_sudoku_grid(user_grid)
                if pui.is_button_pressed(
                    event, config.BUTTON_POSITIONS['solve_btn'],
                    config.BUTTON_DIMENSIONS['action_btn']
                ):
                    pui.solve_sudoku(screen, grid)
                if pui.is_button_pressed(
                    event, config.BUTTON_POSITIONS['clear_btn'],
                    config.BUTTON_DIMENSIONS['action_btn']
                ):
                    su.clear_sudoku_grid(grid)
                    su.clear_sudoku_grid(puzzle_grid)
                    su.clear_sudoku_grid(user_grid)

            # Handling grid clicks
            if pui.is_button_pressed(
                event, config.GRID_CONFIG['position'],
                config.GRID_CONFIG['dimensions']
            ):
                position = pui.get_mouse_position()
                if mode == 'game':
                    pui.handle_game_screen_input(
                        screen, 
                        position, 
                        grid, 
                        user_grid
                    )
                else:
                    pui.handle_solver_screen_input(
                        screen, 
                        position, 
                        grid, 
                        user_grid
                    )
                    
            
            # Return to main menu button functionality
            if pui.is_button_pressed(
                event,
                config.BUTTON_POSITIONS['return_to_main_menu_btn'],
                config.BUTTON_DIMENSIONS['return_to_main_menu_btn']
            ):
                main()
            
            # Quit event
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def main():
    """
    The main function to display the main menu screen of the Sudoku application.
    It initializes the main menu, draws the necessary buttons, and handles user 
    interactions to switch between the Sudoku game and solver screens.

    Returns:
        None
    """
    # Set window title
    pygame.display.set_caption('Solve\'n\'See Sudoku')


    main_menu_screen = pygame.display.set_mode(
        config.SCREEN_DIMENSIONS['main_menu']
        )

    


    run = True
    while run:
        main_menu_screen.fill(config.COLORS['white'])
        
        # Draw main menu buttons
        pui.draw_action_button(
            main_menu_screen,
            config.BUTTON_POSITIONS['sudoku_game_btn'],
            config.BUTTON_DIMENSIONS['action_btn'],
            "Sudoku Game"
        )
        pui.draw_action_button(
            main_menu_screen,
            config.BUTTON_POSITIONS['sudoku_solver_btn'],
            config.BUTTON_DIMENSIONS['action_btn'],
            "Sudoku Solver"
        )
        
        for event in pygame.event.get():
            # Swtich to game screen 
            if pui.is_button_pressed(
                event,
                config.BUTTON_POSITIONS['sudoku_solver_btn'],
                config.BUTTON_DIMENSIONS['action_btn']
            ):
                display_sudoku_screen(mode='solver')
            
            # Swtich to solver screen 
            if pui.is_button_pressed(
                event,
                config.BUTTON_POSITIONS['sudoku_game_btn'],
                config.BUTTON_DIMENSIONS['action_btn']
            ):
                display_sudoku_screen(mode='game')
            
            # Quit event
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    main()