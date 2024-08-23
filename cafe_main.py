import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 400, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Slider")

# Colors
TEXT_COLOR = (0, 0, 0)
SCREEN_COLOR = (255, 255, 255)
BAR_COLOR = (200, 200, 200)
HANDLE_COLOR = (0, 0, 255)

def create_slider(x, y, width, min_value, max_value, current_value):
    slider_rect = pygame.Rect(x, y, width, 10)
    handle_width = 20
    handle_height = 30
    handle_x = x + int((current_value - min_value) / (max_value - min_value) * (width - handle_width))
    handle_y = y - (handle_height // 2 - 5)
    handle_rect = pygame.Rect(handle_x, handle_y, handle_width, handle_height)
    return slider_rect, handle_rect, min_value, max_value, current_value

def draw_slider(window, slider_rect, handle_rect):
    pygame.draw.rect(window, BAR_COLOR, slider_rect)  # Draw slider bar
    pygame.draw.rect(window, HANDLE_COLOR, handle_rect)  # Draw handle

def update_slider(slider_rect, handle_rect, min_value, max_value):
    mouse_x, _ = pygame.mouse.get_pos()
    handle_rect.x = max(slider_rect.x, min(mouse_x - handle_rect.width // 2, slider_rect.x + slider_rect.width - handle_rect.width))
    value = min_value + (handle_rect.x - slider_rect.x) / (slider_rect.width - handle_rect.width) * (max_value - min_value)
    return value

# Running the game loop
running = True
dragging = False

# Create a slider
slider, handle, min_value, max_value, value = create_slider(50, height // 2, 300, 0, 100, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if handle.collidepoint(event.pos):
                dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                value = update_slider(slider, handle, min_value, max_value)

    # Drawing
    window.fill(SCREEN_COLOR)
    draw_slider(window, slider, handle)

    # Display value
    font = pygame.font.SysFont(None, 36)
    value_text = font.render(f"Value: {int(value)}", True, TEXT_COLOR)
    window.blit(value_text, (slider.x, slider.y + 50))

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
