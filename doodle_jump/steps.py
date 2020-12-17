import random
from turtle import speed

import pygame
from pygame import color


class Step:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        self.color = (255, 0, 0)
        self.y = 100
        self.y1 = 300
        self.y2 = 500
        self.y3 = 700
        self.speed = 1
        self.steplist = [[50, self.y, 75, 10], [200, self.y, 75, 10], [350, self.y, 75, 10], [500, self.y, 75, 10], [50, self.y1, 75, 10], [200, self.y1, 75, 10], [350, self.y1, 75, 10], [500, self.y1, 75, 10], [50, self.y2, 75, 10], [200, self.y2, 75, 10], [350, self.y2, 75, 10], [500, self.y2, 75, 10], [50, self.y3, 75, 10], [200, self.y3, 75, 10], [350, self.y3, 75, 10], [500, self.y3, 75, 10] ]

    def draw(self, win):
        #   y
        print(self.steplist)
        pygame.draw.rect(win, self.color, self.steplist[0], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[1], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[2], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[3], False)
        # pygame.display.flip()

        #   y1
        pygame.draw.rect(win, self.color, self.steplist[4], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[5], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[6], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[7], False)
        # pygame.display.flip()

        #   y2
        pygame.draw.rect(win, self.color, self.steplist[8], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[9], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[10], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[11], False)
        # pygame.display.flip()

        #   y3
        pygame.draw.rect(win, self.color, self.steplist[12], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[13], False)
        # pygame.display.flip()

        pygame.draw.rect(win, self.color, self.steplist[14], False)


        pygame.draw.rect(win, self.color, self.steplist[15], False)


    def move(self, win):

        for s in self.steplist:
            if 0 <= s[1] <= 800:
                s[1] = s[1] + self.speed

            elif s[1] > 800:
                s[1] = 0
        #
        # #   y
        # if 0 <= self.y <= 800:
        #     self.y = self.y + self.speed
        #
        # elif self.y > 800:
        #     self.y = 0
        #
        # #   y1
        # if 0 <= self.y1 <= 800:
        #     self.y1 = self.y1 + self.speed
        #
        # elif self.y1 > 800:
        #     self.y1 = 0
        #
        # #   y2
        # if 0 <= self.y2 <= 800:
        #     self.y2 = self.y2 + self.speed
        #
        # elif self.y2 > 800:
        #     self.y2 = 0
        #
        # #    y3
        # if 0 <= self.y3 <= 800:
        #     self.y3 = self.y3 + self.speed
        #
        # elif self.y3 > 800:
        #     self.y3 = 0