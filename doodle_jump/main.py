import pygame

from doodle_jump.doodle import Doodle

pygame.init()

width = 200
height = 500

doodle1 = Doodle()

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Doodle Jump")

run = True

#doodle1 = Doodle(50,100)



