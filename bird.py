from pygame import draw, Rect


class Bird:
    def __init__(self, scr, width, height, r):
        self.scr = scr
        self.width = width
        self.height = height

        self.x = self.width/2
        self.r = r
        self.y = self.height-self.r

        self.vy = 0
        self.gravity = 0.3

    def update(self):
        self.y += self.vy
        self.vy += self.gravity

    def up(self):
        self.vy = -10

    def move(self, num):
        self.x += num
        if self.x+self.r < 0:
            self.x = self.width-self.r
        elif self.x >= self.width:
            self.x = 0
        else:
            pass

    def constrain(self, var, minmum, maximum):
        if var <= minmum:
            return minmum
        elif var >= maximum:
            return maximum
        else:
            return var

    def show(self):
        self.y = self.constrain(self.y, 100, self.height-self.r)
        draw.rect(self.scr, (100,100,100), Rect(self.x, self.y, self.r, self.r))