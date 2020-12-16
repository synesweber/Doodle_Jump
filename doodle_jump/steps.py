from random import random

import pygame
import self as self


class Steps:
    def __init__(self, pos, color, speed):
        self.pos = pos
        self.color = color
        self.speed = speed

        self.color = (255, 0, 0)

    # def __pos__(self):
    #     pass


    def draw(self, win):
        pygame.draw.rect(win, self.color, (100, 100, 50, 50))
