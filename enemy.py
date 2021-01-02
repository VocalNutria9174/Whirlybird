import random
from pygame import draw, Rect, image, transform
from math import pow, sqrt


class Enemy:
    def __init__(self, scr, width, height):
        self.scr = scr
        self.width = width
        self.height = height

        self.r = 25
        self.x = self.width-self.r
        self.y = -random.randrange(15, 100)

        self.vx = -5

        # img
        self.img = image.load("img/enemy.png")
        self.img = transform.scale(self.img, (self.r, self.r))

    def move(self):
        self.x += self.vx
        if self.x <= 0:
            self.vx *= -1
        elif self.x >= self.width+self.r:
            self.vx *= -1
        else:
            pass

    def update_pos(self):
        self.y = -random.randrange(15, 100)

    def collide(self, bird):
        distance = sqrt(pow(bird.x-self.x, 2)+pow(bird.y-self.y, 2))
        return distance < bird.r

    def show(self):
        # draw.rect(self.scr, (100, 100, 100), Rect(self.x, self.y, self.r, self.r))
        self.scr.blit(self.img, (self.x, self.y))
