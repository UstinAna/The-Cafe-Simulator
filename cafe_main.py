import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize the game and mouse
running = True

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafe Simulator")

# Set up sound and music
my_sound = pygame.mixer.Sound("asset/ordinary-loop-minimal-piano-182046.mp3")
my_sound.play(-1)
my_sound.set_volume(1)

# Set up fonts and colors
BASE_FONT_SIZE = 20
TITLE_COLOR = (255, 0, 255)
UNSELECTED_COLOR = (100, 100, 100)
SELECTED_COLOR = (255, 215, 0)
SCREEN_COLOR = (0, 0, 0)
TITLE_FONT = pygame.font.Font(None, BASE_FONT_SIZE)
BUTTON_FONT = pygame.font.Font(None, BASE_FONT_SIZE)

# Pixel size for the pixelated effect
PIXEL_SIZE = 5

# Menu options
menu_options = ["Start Game", "Settings", "Exit"]
menu_buttons = []

# Variable to track the currently selected (hovered) menu option
selected_main = -1

def draw_menu():
    screen.fill(SCREEN_COLOR)
    
    # Title
    title_text = "Cafe Simulator"
    title_surface = TITLE_FONT.render(title_text, True, TITLE_COLOR)
    scaled_title = pygame.transform.scale(title_surface, 
                                          (title_surface.get_width() * PIXEL_SIZE, title_surface.get_height() * PIXEL_SIZE))
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(scaled_title, title_rect.topleft)

    # Menu options
    menu_buttons.clear()  # Clear previous button rects
    for i, option in enumerate(menu_options):
        color = SELECTED_COLOR if i == selected_main else UNSELECTED_COLOR
        option_surface = BUTTON_FONT.render(option, True, color)
        scaled_option = pygame.transform.scale(option_surface, 
                                               (option_surface.get_width() * PIXEL_SIZE, option_surface.get_height()
                                                 * PIXEL_SIZE))
        option_rect = scaled_option.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 80))
        menu_buttons.append(option_rect)  # Store button rect
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip()

def main_menu():
    global selected_main
    global running

    while running:
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Update mouse position
        selected_main = -1  # Reset selected_main

        # Check if the mouse is hovering over any of the menu buttons
        for i, button in enumerate(menu_buttons):
            if button.collidepoint(mouse_x, mouse_y):
                selected_main = i
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selected_main == 0:  # Start Game selected
                    game()
                elif selected_main == 2:  # Exit selected
                    running = False
                    sys.exit()
                elif selected_main == 1:  # Settings selected
                    setting()

        draw_menu()

def draw_game():
    screen.fill(SCREEN_COLOR)
    title_text = "GAME"
    title_surface = TITLE_FONT.render(title_text, True, TITLE_COLOR)
    scaled_title = pygame.transform.scale(title_surface, 
                                          (title_surface.get_width() * PIXEL_SIZE, title_surface.get_height() * PIXEL_SIZE))
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(scaled_title, title_rect.topleft)

    pygame.display.flip()

def game():
    global running

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        draw_game()

# Setting options
setting_options = ["Sound"]

def draw_setting():
    screen.fill(SCREEN_COLOR)
    title_text = "SETTINGS"
    title_surface = TITLE_FONT.render(title_text, True, TITLE_COLOR)
    scaled_title = pygame.transform.scale(title_surface, 
                                          (title_surface.get_width() * PIXEL_SIZE, title_surface.get_height() * PIXEL_SIZE))
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(scaled_title, title_rect.topleft)

    # Setting options
    for i, option in enumerate(setting_options):
        color = TITLE_COLOR
        option_surface = BUTTON_FONT.render(option, True, color)
        scaled_option = pygame.transform.scale(option_surface, 
                                               (option_surface.get_width() * PIXEL_SIZE, option_surface.get_height()
                                                 * PIXEL_SIZE))
        option_rect = scaled_option.get_rect(center=(len(option) * BASE_FONT_SIZE + 30, HEIGHT // 2 + i * 80))
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip()

def setting():
    global running

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        draw_setting()

def start_game():
    main_menu()

if __name__ == "__main__":
    start_game()
