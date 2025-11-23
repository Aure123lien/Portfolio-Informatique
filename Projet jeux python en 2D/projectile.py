import pygame

# Definir la classe pour configurer le projectile du personnage
class Projectile(pygame.sprite.Sprite):

     def __init__(self):
          super().__init__()
          self.velocity = 5
          self.image = pygame.image.load("Projet jeux python en 2D/assets/projectile.png")
          self.rect = self.image.get_rect()