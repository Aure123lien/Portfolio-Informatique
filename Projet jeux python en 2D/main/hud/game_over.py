import pygame
from ..configuration import *

title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

class GameOverScreen:
    def __init__(self, screen):
        self.screen = screen

        # Charger l'image de fin de partie
        self.game_over_img = pygame.image.load(GAME_OVER_IMG_PATH).convert_alpha()
        self.game_over_img = pygame.transform.scale(self.game_over_img, GAME_OVER_SCALE)

        # La polices d'écriture
        self.title_font = pygame.font.Font(FONT_PATH, TITLE_FONT_SIZE)
        self.text_font = pygame.font.Font(FONT_PATH, TEXT_FONT_SIZE)

        # Les différents boutons dessus
        self.restart_rect = pygame.Rect(
            int(SCREEN_WIDTH * RESTART_RECT[0]),
            int(SCREEN_HEIGHT * RESTART_RECT[1]),
            int(SCREEN_WIDTH * RESTART_RECT[2]),
            int(SCREEN_HEIGHT * RESTART_RECT[3])
        )
        self.menu_rect = pygame.Rect(
            int(SCREEN_WIDTH * MENU_RECT[0]),
            int(SCREEN_HEIGHT * MENU_RECT[1]),
            int(SCREEN_WIDTH * MENU_RECT[2]),
            int(SCREEN_HEIGHT * MENU_RECT[3])
        )

    def draw(self, mouse_pos):
        self.screen.blit(self.game_over_img, (0, 0))
        title = title_font.render("Vous avez péri", True, RED)
        self.screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, int(SCREEN_HEIGHT * 0.11))))

        # Bouton de redémarrage
        if self.restart_rect.collidepoint(mouse_pos):
            text = pygame.font.Font(FONT_PATH, RESTART_FONT_SIZE).render("Recommencer une nouvelle partie", True, YELLOW)
        else:
            text = text_font.render("Recommencer une nouvelle partie", True, WHITE)
        self.screen.blit(text, text.get_rect(center=self.restart_rect.center))

        # Bouton menu
        if self.menu_rect.collidepoint(mouse_pos):
            text = pygame.font.Font(FONT_PATH, RESTART_FONT_SIZE).render("Retour au menu principale", True, YELLOW)
        else:
            text = text_font.render("Retour au menu principale", True, WHITE)
        self.screen.blit(text, text.get_rect(center=self.menu_rect.center))

    def handle_click(self, pos):
        if self.restart_rect.collidepoint(pos):
            return "restart"
        elif self.menu_rect.collidepoint(pos):
            return "menu"
        return None