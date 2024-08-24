import pygame
import sys
import os

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafe Simulator")

# Constructing paths using os.path
base_path = os.path.dirname(__file__)  # Directory of the script
asset_path = os.path.join(base_path, 'asset')  # Path to the asset directory

# Load and set up sound and music
try:
    my_music = pygame.mixer.Sound(os.path.join(asset_path, "ordinary-loop-minimal-piano-182046.mp3"))
    my_music.play(-1)
    my_music.set_volume(1)
except FileNotFoundError:
    print("Music file not found. Please ensure 'ordinary-loop-minimal-piano-182046.mp3' is in the 'asset' folder.")
    my_music = None
except pygame.error as e:
    print(f"Error loading music file: {e}")
    my_music = None
    
try:
    my_sound = pygame.mixer.Sound(os.path.join(asset_path, "chinese-beat-190047.mp3"))
    my_sound.set_volume(1)
    my_sound.play(-1)
except FileNotFoundError:
    print("Sound file not found. Please ensure 'chinese-beat-190047.mp3' is in the 'asset' folder.")
    my_sound = None
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    my_sound = None

# Set up fonts and colors
BASE_FONT_SIZE = 18
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
setting_options = ["Music", "Sound"]
menu_buttons = []
selected_main = -1  # default selected option while mouse not hovering them

# Slider settings
slider_pos = [my_music.get_volume() if my_music else 0, my_sound.get_volume() if my_sound else 0]  # Slider position (0.0 to 1.0)
slider_x = [0, 0]
slider_y = [0, 0]
slider_width = 300
slider_height = 10
handle_width = 20
handle_height = 30
SLIDER_COLOR = (200, 200, 200)
HANDLE_COLOR = TITLE_COLOR

def render_text(text, font, color, scale_factor):
    surface = font.render(text, True, color)
    scaled_surface = pygame.transform.scale(surface, 
                                            (surface.get_width() * scale_factor, surface.get_height() * scale_factor))
    return scaled_surface

def draw_menu():
    screen.fill(SCREEN_COLOR)
    
    # Title
    title_text = "Cafe Simulator"
    scaled_title = render_text(title_text, TITLE_FONT, TITLE_COLOR, PIXEL_SIZE)
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 6))
    screen.blit(scaled_title, title_rect.topleft)

    # Menu options
    menu_buttons.clear()  # Clear previous button rects
    for i, option in enumerate(menu_options):
        color = SELECTED_COLOR if i == selected_main else UNSELECTED_COLOR
        scaled_option = render_text(option, BUTTON_FONT, color, PIXEL_SIZE)
        option_rect = scaled_option.get_rect(center=(WIDTH // 2, HEIGHT // 2 + i * 80))
        menu_buttons.append(option_rect)  # Store button rect
        screen.blit(scaled_option, option_rect.topleft)

    pygame.display.flip() 

def main_menu():
    global selected_main

    while True:
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Update mouse position
        selected_main = -1  # Reset selected_main

        # Check if the mouse is hovering over any of the menu buttons
        for i, button in enumerate(menu_buttons):
            if button.collidepoint(mouse_x, mouse_y):
                selected_main = i
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selected_main == 0:  # Start Game selected
                    game()  # This will transition to the game loop
                elif selected_main == 2:  # Exit selected
                    pygame.quit()
                    sys.exit()
                elif selected_main == 1:  # Settings selected
                    setting()  # Transition to settings

        draw_menu()

# Game loop
def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_game()

def draw_game():
    screen.fill(SCREEN_COLOR)
    scaled_title = render_text("GAME", TITLE_FONT, TITLE_COLOR, PIXEL_SIZE)
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 6))
    screen.blit(scaled_title, title_rect.topleft)

    pygame.display.flip()

# Setting menu
def draw_setting():
    screen.fill(SCREEN_COLOR)
    scaled_title = render_text("SETTINGS", TITLE_FONT, TITLE_COLOR, PIXEL_SIZE)
    title_rect = scaled_title.get_rect(center=(WIDTH // 2, HEIGHT // 6))
    screen.blit(scaled_title, title_rect.topleft)

    # Setting options
    for i, option in enumerate(setting_options):
        color = TITLE_COLOR
        hight = HEIGHT // 3
        option_text = f"{option}: {int(slider_pos[i] * 100)}"
        scaled_option = render_text(option_text, BUTTON_FONT, color, PIXEL_SIZE)
        option_rect = scaled_option.get_rect(topleft=(50, hight + i * 80))
        screen.blit(scaled_option, option_rect.topleft)
        
        # Draw slider
        option_rect2 = scaled_option.get_rect(topleft=(400, hight + i * 80 - 30 - slider_height // 2))
        slider_x[i] = option_rect2.bottomleft[0] + 10
        slider_y[i] = option_rect2.bottomleft[1] - handle_height // 2 + slider_height // 2
        pygame.draw.rect(screen, SLIDER_COLOR, (slider_x[i], slider_y[i] + 10, slider_width, slider_height))
        handle_x = slider_x[i] + slider_pos[i] * slider_width - handle_width // 2
        pygame.draw.rect(screen, HANDLE_COLOR, (handle_x, slider_y[i], handle_width, handle_height))

    pygame.display.flip()

def setting():
    global slider_pos
    adjusting = False  # Track if the user is adjusting the slider
    selected_slider = None  # Track which slider is being adjusted
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(setting_options)):
                    handle_x = slider_x[i] + slider_pos[i] * slider_width - handle_width // 2
                    if handle_x <= event.pos[0] <= handle_x + handle_width and slider_y[i] <= event.pos[1] <= slider_y[i] + handle_height:
                        adjusting = True
                        selected_slider = i
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                adjusting = False
                selected_slider = None
            elif event.type == pygame.MOUSEMOTION and adjusting:
                if selected_slider is not None:
                    new_pos = (event.pos[0] - slider_x[selected_slider]) / slider_width
                    slider_pos[selected_slider] = max(0, min(1, new_pos))  # Clamp value between 0 and 1
                    if selected_slider == 0 and my_music:
                        my_music.set_volume(slider_pos[selected_slider])
                    elif selected_slider == 1 and my_sound:
                        my_sound.set_volume(slider_pos[selected_slider])

        draw_setting()

def start_game():
    main_menu()  # Call main_menu() only once to start the game

if __name__ == "__main__":
    start_game()  # Ensure only this function is called at the start
