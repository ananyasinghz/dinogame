import pygame
pygame.init()

import os
import random
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Dino Hopping')

clock = pygame.time.Clock()

dino = pygame.image.load(os.path.join('images', 'dino.png'))
cactus = pygame.image.load(os.path.join('images', 'cactus.png'))
ground = pygame.image.load(os.path.join('images', 'ground.png'))

ground_height = 60
cactus_speed = 5

jump = False
score = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                jump = True

    screen.fill((0, 0, 0))

    if jump:
        dino_rect = dino.get_rect(topleft=(50, 350))
        jump = False
    else:
        dino_rect = dino.get_rect(topleft=(50, 370))

    screen.blit(ground, (0, 400 - ground_height))
    screen.blit(dino, dino_rect)

    cactus_x = random.randint(800, 1600)
    screen.blit(cactus, (cactus_x, 400 - ground_height))

    pygame.draw.line(screen, (255, 255, 255), (0, 400 - ground_height), (800, 400 - ground_height), 2)

    dino_rect.y += 5

    if dino_rect.colliderect(cactus.get_rect(topleft=(cactus_x, 400 - ground_height))):
        print('Game Over')
        pygame.quit()
        sys.exit()

    if dino_rect.bottom >= 400 - ground_height:
        dino_rect.bottom = 400 - ground_height

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
