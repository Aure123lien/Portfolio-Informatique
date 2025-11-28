import pygame
from ..configuration import *

pause_font = pygame.font.Font(FONT_PATH, PAUSE_FONT_SIZE)

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.pause_font = pygame.font.Font(FONT_PATH, PAUSE_FONT_SIZE)

    def draw(self, mouse_pos):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        pause_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - 250,
            SCREEN_HEIGHT // 2 - 150,
            500,
            300
        )
        pygame.draw.rect(self.screen, DARK_GRAY, pause_rect, border_radius=12)
        pygame.draw.rect(self.screen, WHITE, pause_rect, 3, border_radius=12)

        # Les paramètre du bouton pause
        continue_rect = pygame.Rect(pause_rect.x + 50, pause_rect.y + 30, 400, 50)
        continue_color = YELLOW if continue_rect.collidepoint(mouse_pos) else WHITE
        continue_text = self.pause_font.render("Continuer", True, continue_color)
        self.screen.blit(continue_text, continue_text.get_rect(center=(pause_rect.centerx, pause_rect.y + 55)))

        settings_rect = pygame.Rect(pause_rect.x + 50, pause_rect.y + 100, 400, 50)
        settings_color = YELLOW if settings_rect.collidepoint(mouse_pos) else WHITE
        settings_text = self.pause_font.render("Réglages", True, settings_color)
        self.screen.blit(settings_text, settings_text.get_rect(center=(pause_rect.centerx, pause_rect.y + 125)))

        quit_rect = pygame.Rect(pause_rect.x + 50, pause_rect.y + 170, 400, 50)
        quit_color = YELLOW if quit_rect.collidepoint(mouse_pos) else WHITE
        quit_text = self.pause_font.render("Quitter", True, quit_color)
        self.screen.blit(quit_text, quit_text.get_rect(center=(pause_rect.centerx, pause_rect.y + 195)))

        return continue_rect, settings_rect, quit_rect