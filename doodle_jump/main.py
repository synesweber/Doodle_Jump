import pygame

import random

from doodle_jump.doodle import Doodle

pygame.init()

width = 600
height = 800
background_color = (255, 255, 255)
color = (255, 0, 0)
# x = random.randint(0, 600)
# y = random.randint(0, 800)


doodle1 = Doodle([int(width/2), int(height/2)])

win = pygame.display.set_mode((width, height))
win.fill(background_color)
pygame.display.flip()

pygame.display.set_caption("Doodle Jump")


def check_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and doodle1.pos[0] > 0:
        doodle1.pos[0] -= 1

    if keys[pygame.K_RIGHT] and doodle1.pos[0] < width:
        doodle1.pos[0] += 1

    if keys[pygame.K_UP] and doodle1.pos[1] > 0:
        doodle1.pos[1] -= 1

    if keys[pygame.K_DOWN] and doodle1.pos[1] < width:
        doodle1.pos[1] += 1


run = True

while run:
    for event in pygame.event.get():
        # pygame.draw.rect(win, color, [randint(0, 600), randint(0, 700), 75, 10], False)
        x = random.randint(0, 600)
        y = random.randint(0, 800)
        pygame.draw.rect(win, color, [x, y, 75, 10], False)
        pygame.display.flip()
        if event.type == pygame.QUIT:
            run = False

    check_keys()

pygame.quit()

# doodle1 = Doodle(50,100)
