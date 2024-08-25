# cafe_game.py
import pygame
import sys
import config
import cafe_main

menu_options = [
    ("Weekly Purchase", "weekly_purchase"),
    ("Staffing & Hours", "staffing_hours"),
    ("Marketing", "marketing"),
    ("Special Decisions", "special_decisions"),
    ("Decision Summary", "decision_summary"),
    ("Exit", "exit_game")
]

def render_text_centered(text, font, color, center_pos):
    rendered_text = cafe_main.render_text(text, font, color, config.PIXEL_SIZE)
    rect = rendered_text.get_rect(center=center_pos)
    return rendered_text, rect

def draw_game():
    config.screen.fill(config.SCREEN_COLOR)

    title_text, title_rect = render_text_centered("GAME", config.TITLE_FONT, config.TITLE_COLOR, (config.WIDTH // 2, config.HEIGHT // 6))
    config.screen.blit(title_text, title_rect.topleft)

    # Add any additional game-specific drawing here

    pygame.display.flip()

def perform_action(action):
    if action == "weekly_purchase":
        weekly_purchase()
    elif action == "staffing_hours":
        staffing_hours()
    elif action == "marketing":
        marketing()
    elif action == "special_decisions":
        special_decisions()
    elif action == "decision_summary":
        decision_summary()
    elif action == "exit_game":
        pygame.quit()
        sys.exit()

def weekly_purchase():
    print("Weekly Purchase functionality goes here.")
    # Implement the weekly purchase functionality here
    pass

def staffing_hours():
    print("Staffing & Hours functionality goes here.")
    # Implement the staffing & hours functionality here
    pass

def marketing():
    print("Marketing functionality goes here.")
    # Implement the marketing functionality here
    pass

def special_decisions():
    print("Special Decisions functionality goes here.")
    # Implement the special decisions functionality here
    pass

def decision_summary():
    print("Decision Summary functionality goes here.")
    # Implement the decision summary functionality here
    pass

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_game()

if __name__ == "__main__":
    pygame.init()
    game()
