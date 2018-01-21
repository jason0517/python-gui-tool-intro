import pygame

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hello World")

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    #---Game logic code here---

    screen.fill((255, 255, 255))

    #---Drawing code here---
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Hello,World",True, (0, 0, 0))
    screen.blit(text, [300, 250])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()