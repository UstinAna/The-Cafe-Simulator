# cafe_main.py
import pygame
import sys
import config
import cafe_game

menu_options = ["Start Game", "Settings", "Exit"]
setting_options = ["Music", "Sound"]
menu_buttons = []
selected_main = -1  # default selected option while mouse not hovering them

# Slider positions and coordinates
slider_x = [0, 0]
slider_y = [0, 0]

def render_text(text, font, color, scale_factor):
    surface = font.render(text, True, color)
    scaled_surface = pygame.transform.scale(surface, 
                                            (surface.get_width() * scale_factor, surface.get_height() * scale_factor))
    return scaled_surface

def draw_menu():
    config.screen.fill(config.SCREEN_COLOR)
    
    # Title
    title_text = "Cafe Simulator"
    scaled_title = render_text(title_text, config.TITLE_FONT, config.TITLE_COLOR, config.PIXEL_SIZE)
    title_rect = scaled_title.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 6))
    config.screen.blit(scaled_title, title_rect.topleft)

    # Menu options
    menu_buttons.clear()  # Clear previous button rects
    for i, option in enumerate(menu_options):
        color = config.SELECTED_COLOR if i == selected_main else config.UNSELECTED_COLOR
        scaled_option = render_text(option, config.BUTTON_FONT, color, config.PIXEL_SIZE)
        option_rect = scaled_option.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 2 + i * 80))
        menu_buttons.append(option_rect)  # Store button rect
        config.screen.blit(scaled_option, option_rect.topleft)

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
                    cafe_game.game()  # Transition to game
                elif selected_main == 2:  # Exit selected
                    pygame.quit()
                    sys.exit()
                elif selected_main == 1:  # Settings selected
                    setting()  # Transition to settings

        draw_menu()

# Setting menu
def draw_setting():
    config.screen.fill(config.SCREEN_COLOR)
    scaled_title = render_text("SETTINGS", config.TITLE_FONT, config.TITLE_COLOR, config.PIXEL_SIZE)
    title_rect = scaled_title.get_rect(center=(config.WIDTH // 2, config.HEIGHT // 6))
    config.screen.blit(scaled_title, title_rect.topleft)

    # Setting options
    for i, option in enumerate(setting_options):
        color = config.TITLE_COLOR
        hight = config.HEIGHT // 3
        option_text = f"{option}: {int(config.slider_pos[i] * 100)}"
        scaled_option = render_text(option_text, config.BUTTON_FONT, color, config.PIXEL_SIZE)
        option_rect = scaled_option.get_rect(topleft=(50, hight + i * 80))
        config.screen.blit(scaled_option, option_rect.topleft)
        
        # Draw slider
        option_rect2 = scaled_option.get_rect(topleft=(400, hight + i * 80 - 30 - config.slider_height // 2))
        slider_x[i] = option_rect2.bottomleft[0] + 10
        slider_y[i] = option_rect2.bottomleft[1] - config.handle_height // 2 + config.slider_height // 2
        pygame.draw.rect(config.screen, config.SLIDER_COLOR, (slider_x[i], slider_y[i] + 10, config.slider_width, config.slider_height))
        handle_x = slider_x[i] + config.slider_pos[i] * config.slider_width - config.handle_width // 2
        pygame.draw.rect(config.screen, config.HANDLE_COLOR, (handle_x, slider_y[i], config.handle_width, config.handle_height))

    pygame.display.flip()

def setting():
    adjusting = False  # Track if the user is adjusting the slider
    selected_slider = None  # Track which slider is being adjusted
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press ESC to return to the main menu
                    return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(setting_options)):
                    handle_x = slider_x[i] + config.slider_pos[i] * config.slider_width - config.handle_width // 2
                    if handle_x <= event.pos[0] <= handle_x + config.handle_width and slider_y[i] <= event.pos[1] <= slider_y[i] + config.handle_height:
                        adjusting = True
                        selected_slider = i
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                adjusting = False
                selected_slider = None
            elif event.type == pygame.MOUSEMOTION and adjusting:
                if selected_slider is not None:
                    new_pos = (event.pos[0] - slider_x[selected_slider]) / config.slider_width
                    config.slider_pos[selected_slider] = max(0, min(1, new_pos))  # Clamp value between 0 and 1
                    if selected_slider == 0 and config.my_music:
                        config.my_music.set_volume(config.slider_pos[selected_slider])
                    elif selected_slider == 1 and config.my_sound:
                        config.my_sound.set_volume(config.slider_pos[selected_slider])

        draw_setting()

def main():
    main_menu()  # Call the main menu function

if __name__ == "__main__":
    main()  # Ensure this is only called once
