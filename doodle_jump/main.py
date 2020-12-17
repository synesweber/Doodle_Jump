import pygame

import random

from pygame.time import delay

from doodle_jump.doodle import Doodle
from doodle_jump.steps import Step

pygame.init()

width = 600
height = 800
background_color = (255, 255, 255)
color = (255, 0, 0)

win = pygame.display.set_mode((width, height))
win.fill(background_color)
pygame.display.flip()

pygame.display.set_caption("Doodle Jump")
doodle1 = Doodle([int(300), int(700)])
steps1 = Step([int(300), int(600)], (255, 0, 0))


# for x in range(4):
#     x = random.randint(0, 525)
#     y = random.randint(0, 200)
#     pygame.draw.rect(win, color, [x, y, 75, 10], False)
#     pygame.display.flip()
#
# for x in range(4):
#     x = random.randint(0, 525)
#     y = random.randint(200, 400)
#     pygame.draw.rect(win, color, [x, y, 75, 10], False)
#     pygame.display.flip()
#
# for x in range(4):
#     x = random.randint(0, 525)
#     y = random.randint(400, 600)
#     pygame.draw.rect(win, color, [x, y, 75, 10], False)
#     pygame.display.flip()
#
# for x in range(4):
#     x = random.randint(0, 525)
#     y = random.randint(600, 800)
#     pygame.draw.rect(win, color, [x, y, 75, 10], False)
#     pygame.display.flip()


def check_keys():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and doodle1.pos[0] > -7:
        doodle1.pos[0] -= 1

    if keys[pygame.K_RIGHT] and doodle1.pos[0] < width - 32:
        doodle1.pos[0] += 1


run = True

while run:
    delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill(background_color)
    check_keys()
    doodle1.draw(win)
    doodle1.jump()
    steps1.draw(win)
    steps1.move(win)
    doodle1.checkcollision(steps1.steplist)

    pygame.display.update()

pygame.quit()
