import pygame




class Doodle:
    def __init__(self, pos):
        self.pos = pos
        self.img = pygame.image.load("./images/penguin.png")
        self.img = pygame.transform.scale(pygame.image.load("./images/penguin.png"), (40, 40))
        self.count = 0
        self.j = True

    def draw(self, win):
        win.blit(self.img, (self.pos[0], self.pos[1]))

    def jump(self):
        print(self.j)
        if self.j:
            if self.count <= 100:
                self.pos[1] = self.pos[1] - 2
                self.count = self.count + 1

            elif self.pos[1] >= 752:
                self.j = False

            elif 100 <= self.count:
                self.pos[1] = self.pos[1] + 2
                self.count = self.count + 1

    def checkcollision(self, steplist):
        for s in steplist:
            if self.j == False:
                # print('check')
                # print(s[1], ' :', self.pos[1] + 40 , ' :', s[1] + s[3])

                if s[0] <= self.pos[0] + 40 <= s[0] + s[2] and s[1] <= self.pos[1] + 40 <= s[1] + s[3]: #and s[0] <= self.pos[0] + 40 <= s[0] + s[2]:
                    self.j = True
                    self.jump()

