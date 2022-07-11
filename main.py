import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

fps = 80

# Display configs
lg = 1024
al = 520
font1 = pygame.font.SysFont("arial", 32, True, False)
font2 = pygame.font.SysFont("arial", 20, True, False)
score = 0

# Enemy spaw status
x = lg / 2
y = al / 2
speed = 0
multiplier = 0

# Player status
laterals = 100
up_down = y
player_speed = 8

dspl = pygame.display.set_mode((lg, al))
pygame.display.set_caption("Sky attack")
clock = pygame.time.Clock()

while True:
    clock.tick(fps)
    dspl.fill((100, 100, 200))
    score_display = f"Score: {score}"

# Display configurations

    lose = font2.render("Game over!", True, (255, 0, 0))
    display_score = font1.render(score_display, True, (255, 255, 255))

# Quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

# Set controls

    if pygame.key.get_pressed()[K_a] and laterals >= 0:
        laterals = laterals - player_speed

    if pygame.key.get_pressed()[K_d] and laterals <= 980:
        laterals = laterals + player_speed

    if pygame.key.get_pressed()[K_w] and up_down >= 0:
        up_down = up_down - player_speed

    if pygame.key.get_pressed()[K_s] and up_down <= 479:
        up_down = up_down + player_speed

# Draw a floor

    pygame.draw.rect(dspl, (200, 100, 40), (0, 515, 1024, 20))

# Draw characters

    enemy = pygame.draw.rect(dspl, (255, 0, 255), (x, y, 50, 50))
    player = pygame.draw.rect(dspl, (255, 255, 0), (laterals, up_down, 35, 35))

# Game progression and mechanics

# Change position if enemy collide with floor
    if y >= 470:
        y = 0
        x = randint(20, 900)
        speed = randint(3, 5)
        score -= 1

# Configure if player scores

    if player.colliderect(enemy):
        x = randint(20, 900)
        multiplier = score / 5
        multiplier = int(multiplier)
        speed = randint(multiplier+3, multiplier+5)
        if speed >= 35:
            speed = 35

        y = 0
        score += 1

        if player_speed <= 20:
            if score % 10 == 2:
                player_speed += 1

# Sum score
    if score < 0:
        x = lg/2
        y = al/2
        dspl.blit(lose, (x, y))

    y = y + speed
    dspl.blit(display_score, (0, 0))

    pygame.display.update()
