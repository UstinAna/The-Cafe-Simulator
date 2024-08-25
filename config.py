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

# Slider settings
slider_pos = [my_music.get_volume() if my_music else 0, my_sound.get_volume() if my_sound else 0]  # Slider position (0.0 to 1.0)
slider_width = WIDTH // 2
slider_height = 10
handle_width = 20
handle_height = 30
SLIDER_COLOR = (200, 200, 200)
HANDLE_COLOR = TITLE_COLOR
