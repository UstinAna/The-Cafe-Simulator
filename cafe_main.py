import pygame
import sys

# Initialize Pygame
pygame.init()

#Initialize the game and mouse
running = True
dragging = False

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafe Simulator")

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
menu_options = ["Start Game", "Exit", "Settings"]
selected_main = 0

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
    for i, option in enumerate(menu_options):
        color = SELECTED_COLOR if i == selected_main else UNSELECTED_COLOR
        option_surface = BUTTON_FONT.render(option, True, color)
        scaled_option = pygame.transform.scale(option_surface, 
                                               (option_surface.get_width() * PIXEL_SIZE, option_surface.get_height()
                                                 * PIXEL_SIZE))
        option_rect = scaled_option.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 80))
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip()

def main_menu():
    global selected_main
    global running

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_main = (selected_main - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_main = (selected_main + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_main == 0:  # Start Game selected
                        game()
                    elif selected_main == 1:  # Exit selected
                        running = False
                    elif selected_main == 2:  # Settings selected
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
    global selected_game
    global running

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_game()

# setting options
setting_options = ["Soundqwaejbgeskga"]
selected_setting = 0

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
        option_rect = scaled_option.get_rect(center=(len(option) * 20 + 30, HEIGHT // 2 + i * 80))
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip()

def setting():
    global selected_setting
    global running

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_setting()

def sound():
    pass

def start_game():
    main_menu()

if __name__ == "__main__":
    start_game()
