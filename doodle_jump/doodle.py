import pygame


class Doodle:
    def __init__(self, pos):
        self.img = pygame.transform.scale(pygame.image.load("./images/penguin.png"), (40, 40))
        self.pos = pos


    def draw(self, win):
        win.blit(self.img, (self.pos[0], self.pos[1]))
