import pygame
import sys
import config

def render_text(text, font, color, pos):
    """ Renders text on the screen at the specified position. """
    text_surface = font.render(text, True, color)
    config.screen.blit(text_surface, pos)

def draw_sidebar(selected_option=None, current_option=0):
    """ Draws the sidebar menu with options and highlights the selected and current options. """
    sidebar_options = [
        "Weekly Purchases", 
        "Staffing & Hours", 
        "Marketing", 
        "Special Decision", 
        "Decision Summary", 
        "Cash Budget Analysis", 
        "Break-Even Worksheet"
    ]
    
    # Draw Sidebar background
    pygame.draw.rect(config.screen, config.LEFTMENU_BG_COLOR, (0, 0, config.LEFTMENU_WIDTH, config.HEIGHT))
    
    for idx, option in enumerate(sidebar_options):
        # Background color based on current option
        bg_color = config.LEFTMENU_CURRENT_COLOR if idx == current_option else config.LEFTMENU_BG_COLOR
        
        # Draw the background for the current option
        pygame.draw.rect(config.screen, bg_color, (0, config.LEFTMENU_TEXT_y + idx * 60, config.LEFTMENU_WIDTH, 60), 0)

        # Text color based on selection
        text_color = config.LEFTMENU_SELECTED_COLOR if idx == selected_option else config.LEFTMENU_UNSELECTED_COLOR
        
        render_text(option, config.BUTTON_FONT, text_color, (20, config.LEFTMENU_TEXT_y + idx * 60 + 30))

def handle_option_selection(option_index):
    """ Handles the logic for when an option is selected. """
    if option_index == 0:
        print("Weekly Purchases selected")
        # Add logic to transition to the Weekly Purchases screen or view
    elif option_index == 1:
        print("Staffing & Hours selected")
        # Add logic for Staffing & Hours
    elif option_index == 2:
        print("Marketing selected")
        # Add logic for Marketing
    elif option_index == 3:
        print("Special Decision selected")
        # Add logic for Special Decision
    elif option_index == 4:
        print("Decision Summary selected")
        # Add logic for Decision Summary
    elif option_index == 5:
        print("Cash Budget Analysis selected")
        # Add logic for Cash Budget Analysis
    elif option_index == 6:
        print("Break-Even Worksheet selected")
        # Add logic for Break-Even Worksheet

def game():
    """ Main game loop handling the sidebar interaction and display. """
    selected_sidebar = None  # Assume nothing is selected by default
    current_option = 0  # Current always start with "Weekly Purchases"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for idx in range(7):
                    if 0 <= mouse_x <= config.LEFTMENU_WIDTH and config.LEFTMENU_TEXT_y + idx * 60 <= mouse_y <= 160 + idx * 60:
                        current_option = idx
                        selected_sidebar = idx  # Confirm selection
                        handle_option_selection(selected_sidebar)  # Handle selected option logic

        config.screen.fill(config.SCREEN_COLOR)  # Clear screen with background color

        # Draw the sidebar with highlighted selections
        draw_sidebar(selected_option=selected_sidebar, current_option=current_option)

        pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game()
