import random
from pygame import draw, Rect
from math import pow,sqrt

class Base:
    def __init__(self, scr, width, height):
        self.scr = scr
        self.width = width
        self.height = height

        self.w = 50
        self.h = 5
        self.x = random.randrange(0, self.width-self.w)
        self.y = random.randrange(0, self.height-self.h)

        # velocity
        self.vy = 5

        # move
        self.shift = True

    def move(self):
        if self.shift:
            self.y += self.vy

    def collide(self,bird):
        distance = sqrt(pow(bird.x-self.x,2)+pow(bird.y-self.y,2))
        return distance<bird.r and bird.x+bird.r>self.x and bird.x<self.x+self.w

    def update_pos(self):
        self.y = -15
        self.x = random.randrange(0, self.width-self.w)

    def show(self):
        draw.rect(self.scr, (100, 100, 100), Rect(self.x, self.y, self.w, self.h))
