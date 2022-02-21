import pygame
pygame.init()

clock = pygame.time.Clock()
#Pour la création d'un fichier de réglage (FPS)
FPS = 144

getResolution = pygame.display.Info()
pygame.display.set_mode((getResolution.current_w, getResolution.current_h))

pygame.display.set_caption("Pas Encore De Nom ^^")
#pygame.display.set_mode((2560, 1440))

#UTILISER CETTE BOUCLE !!!!

running = True
while running:

    clock.tick(FPS)
    print(clock.get_fps())
    if 59 >= clock.get_fps():
        print("Fréquence d'image faible")


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Jeu quitté")
