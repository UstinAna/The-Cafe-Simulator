import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafe Simulator")

# Set up fonts and colors
BASE_FONT_SIZE = 20
MENU_FONT = pygame.font.Font(None, BASE_FONT_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

# Menu options
menu_options = ["Start Game", "Exit", "Settings"]
selected_option = 0

# Pixel size for the pixelated effect
PIXEL_SIZE = 5

def draw_pixelated_text(text, x, y, color, pixel_size):
    for i, char in enumerate(text):
        char_surface = MENU_FONT.render(char, True, color)
        char_surface = pygame.transform.scale(char_surface, 
                                              (char_surface.get_width() * pixel_size, char_surface.get_height() * pixel_size))
        screen.blit(char_surface, (x + i * char_surface.get_width(), y))

def draw_menu():
    screen.fill(BLACK)
    
    # Title
    title_text = "Cafe Simulator"
    title_surface = MENU_FONT.render(title_text, True, WHITE)
    scaled_title = pygame.transform.scale(title_surface, 
                                          (title_surface.get_width() * PIXEL_SIZE, title_surface.get_height() * PIXEL_SIZE))
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(scaled_title, title_rect.topleft)

    # Menu options
    for i, option in enumerate(menu_options):
        color = WHITE if i == selected_option else GRAY
        option_surface = MENU_FONT.render(option, True, color)
        scaled_option = pygame.transform.scale(option_surface, 
                                               (option_surface.get_width() * PIXEL_SIZE, option_surface.get_height()
                                                 * PIXEL_SIZE))
        option_rect = scaled_option.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 80))
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip()

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game selected
                        start_game()
                    elif selected_option == 1:  # Exit selected
                        pygame.quit()
                        sys.exit()
                    elif selected_option == 2:  # Settings selected
                        setting()

        draw_menu()

def draw_game():
    screen.fill(BLACK)

def game():
    pass

def draw_setting():
    screen.fill(BLACK)
    title_text = "SETTINGS"
    title_surface = MENU_FONT.render(title_text, True, WHITE)
    scaled_title = pygame.transform.scale(title_surface, 
                                          (title_surface.get_width() * PIXEL_SIZE, title_surface.get_height() * PIXEL_SIZE))
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    screen.blit(scaled_title, title_rect.topleft)

def setting():
    pass

def start_game():
    print("Starting the game...")
    # Game logic goes here
    # Once the game is done, return to the main menu if needed
    main_menu()

if __name__ == "__main__":
    main_menu()
