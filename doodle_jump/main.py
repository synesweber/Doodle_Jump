import pygame

from doodle_jump.doodle import Doodle

pygame.init()

width = 600
height = 800

doodle1 = Doodle()

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Doodle Jump")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()

# doodle1 = Doodle(50,100)
