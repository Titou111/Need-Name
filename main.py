import pygame
pygame.init()

getResolution = pygame.display.Info()
pygame.display.set_mode((getResolution.current_w, getResolution.current_h))

pygame.display.set_caption("Pas Encore De Nom ^^")
#pygame.display.set_mode((2560, 1440))

#UTILISER CETTE BOUCLE !!!!

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Jeu quitté")
