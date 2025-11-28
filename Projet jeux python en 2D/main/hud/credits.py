import pygame
import math
from ..configuration import *

credit_font = pygame.font.Font(FONT_PATH, CREDIT_FONT_SIZE)

class CreditsPopup:
    def __init__(self, screen):
        self.screen = screen
        self.credit_font = pygame.font.Font(FONT_PATH, CREDIT_FONT_SIZE)

        self.popup_width = int(SCREEN_WIDTH * POPUP_WIDTH_FACTOR)
        self.popup_height = int(SCREEN_HEIGHT * POPUP_HEIGHT_FACTOR)
        self.popup_rect = pygame.Rect(
            (SCREEN_WIDTH - self.popup_width) // 2,
            (SCREEN_HEIGHT - self.popup_height) // 2,
            self.popup_width,
            self.popup_height
        )
        self.close_btn_center = (self.popup_rect.right - 30, self.popup_rect.top + 30)

    def draw(self):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        pygame.draw.rect(self.screen, (240, 240, 240), self.popup_rect, border_radius=12)
        pygame.draw.rect(self.screen, BLACK, self.popup_rect, 3, border_radius=12)

        text1 = credit_font.render("Jeu créé et développé par", True, BLACK)
        text2 = credit_font.render("Aurélien Wins", True, BLACK)
        text1_rect = text1.get_rect(center=(self.popup_rect.centerx, self.popup_rect.top + self.popup_rect.height * 0.35))
        text2_rect = text2.get_rect(center=(self.popup_rect.centerx, self.popup_rect.top + self.popup_rect.height * 0.55))
        self.screen.blit(text1, text1_rect)
        self.screen.blit(text2, text2_rect)

        pygame.draw.circle(self.screen, RED, self.close_btn_center, 18)
        pygame.draw.line(self.screen, WHITE, (self.close_btn_center[0] - 8, self.close_btn_center[1] - 8),
                         (self.close_btn_center[0] + 8, self.close_btn_center[1] + 8), 3)
        pygame.draw.line(self.screen, WHITE, (self.close_btn_center[0] + 8, self.close_btn_center[1] - 8),
                         (self.close_btn_center[0] - 8, self.close_btn_center[1] + 8), 3)

    def handle_click(self, pos):
        mx, my = pos
        if math.hypot(mx - self.close_btn_center[0], my - self.close_btn_center[1]) <= 18:
            return "close"
        return None