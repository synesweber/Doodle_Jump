import pygame

from doodle_jump.doodle import Doodle

pygame.init()

width = 600
height = 800
background_color = (255, 255, 255)

doodle1 = Doodle()

win = pygame.display.set_mode((width, height))
win.fill(background_color)
pygame.display.flip()

pygame.display.set_caption("Doodle Jump")

pygame.draw.rect(win, [red, green, blue], [left, top, width, 100], filled)
# win.fill([255, 255, 255])
# pygame.display.flip()

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



pygame.quit()

# doodle1 = Doodle(50,100)
