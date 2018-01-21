import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Some constants
SCREEN_WITH = 700
SCREEN_HEIGHT = 500

# Some variables
enemy_width = 25
enemy_height = 25

enemy_x = 10
enemy_y = 10

enemy__step = 5

player_width = 25
player_height = 25

player_x = SCREEN_WITH/2 - player_width
player_y = SCREEN_HEIGHT - player_height

x_player_speed = 0
y_player_speed = 0
player_speed_step = 5

score = 0
level = 1
pre_level = 1

pygame.init()

size = (SCREEN_WITH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My First Simple Game")

done = False
clock = pygame.time.Clock()


while not done:
    # --- Main event loop----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_player_speed = player_speed_step*(-1)
            elif event.key == pygame.K_RIGHT:
                x_player_speed = player_speed_step
            elif event.key == pygame.K_UP:
                y_player_speed = player_speed_step*(-1)
            elif event.key == pygame.K_DOWN:
                y_player_speed = player_speed_step

        # User let up on a key
        elif event.type == pygame.KEYUP:
            print "key up"
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_player_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_player_speed = 0

    # ---Game logic code here---
    if enemy_y < 575:
        enemy_y = enemy_y + enemy__step
    else:
        enemy_y = 10
        enemy_x = random.randint(10, 680)

    player_x += x_player_speed
    player_y += y_player_speed

    if abs(player_x-enemy_x) <= player_width and abs(player_y - enemy_y) <= player_height:
        print "collusion!"
        pygame.mixer.music.load("pop1.wav")
        pygame.mixer.music.play()
        enemy_y = 10
        enemy_x = random.randint(10, 680)
        score += 1
        if score % 10 == 0:
            level += 1
            enemy__step += 3


    screen.fill(BLACK)

    # ---Drawing code here---
    pygame.draw.rect(screen, (255, 0, 0), [enemy_x, enemy_y, 20, 25], 0)
    pygame.draw.rect(screen, (0, 255, 0), [player_x, player_y, 20, 25], 0)

    font = pygame.font.SysFont('Calibri', 18, True, False)
    text = font.render("Scores: "+str(score),True, WHITE)
    screen.blit(text, [15, SCREEN_HEIGHT-30])

    text1 = font.render("Level: "+str(level),True, WHITE)
    screen.blit(text1, [15, SCREEN_HEIGHT-60])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
