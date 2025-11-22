import pygame
pygame.init()

# on va generer la fenetre du jeux
pygame.display.set_caption("jeux de tir en 2D")
screen = pygame.display.set_mode((1080, 720))

# On va importer une image pour le mettre en arrire plan du jeu
background = pygame.image.load("Projet jeux python/assets/Background.jpg")

running = True

# On va creer une boucle pour la condition juste au dessus
while running:

    # appliquer l'arrière plan
    screen.blit(background, (0, 0))
    
    # Mettre a jour l'ecran
    pygame.display.flip()

    # On va vérifier si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # On va vérifier l'évenement est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False

# Quand on sort de la boucle
pygame.quit()
print("Le jeux se ferme")

