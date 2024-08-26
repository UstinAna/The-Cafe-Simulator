# config.py
import pygame
import os

# Screen dimensions and settings
WIDTH, HEIGHT = 1600, 800

# Initialize Pygame and create the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cafe Simulator")

# Constructing paths using os.path
base_path = os.path.dirname(__file__)  # Directory of the script
asset_path = os.path.join(base_path, 'asset')  # Path to the asset director

# bg music and sound effects
my_music = pygame.mixer.Sound(os.path.join(asset_path, "ordinary-loop-minimal-piano-182046.mp3"))
my_sound = pygame.mixer.Sound(os.path.join(asset_path, "chinese-beat-190047.mp3"))

# Set up fonts and colors
BASE_FONT_SIZE = 20
TEXT_DISTANCE = 80
PIXEL_SIZE = 5
TITLE_COLOR = (255, 0, 255)
UNSELECTED_COLOR = (100, 100, 100)
SELECTED_COLOR = (255, 215, 0)
SCREEN_COLOR = (0, 0, 0)
TITLE_FONT = pygame.font.Font(None, BASE_FONT_SIZE)
BUTTON_FONT = pygame.font.Font(None, BASE_FONT_SIZE)

# Slider settings
slider_pos = [my_music.get_volume() if my_music else 0, my_sound.get_volume() if my_sound else 0]  # Slider position (0.0 to 1.0)
slider_width = WIDTH // 2
slider_height = 10
handle_width = 20
handle_height = 30
SLIDER_COLOR = (200, 200, 200)
HANDLE_COLOR = TITLE_COLOR

# game ####
LEFTMENU_BG_COLOR = (80, 80, 80)
LEFTMENU_WIDTH = WIDTH // 5
LEFTMENU_HEIGHT = HEIGHT
BUTTON_FONT = pygame.font.SysFont('Arial', BASE_FONT_SIZE)
LEFTMENU_SELECTED_COLOR = SELECTED_COLOR
LEFTMENU_UNSELECTED_COLOR = (100, 20, 80)
LEFTMENU_CURRENT_COLOR = (40, 100, 100)
LEFTMENU_TEXT_y = 80
