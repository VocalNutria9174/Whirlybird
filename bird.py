from pygame import draw, Rect, image, transform


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

        # imaage
        self.img = image.load("img/android.png")
        self.img = transform.scale(self.img, (self.r, self.r))

    def update(self):
        self.y += self.vy
        self.vy += self.gravity

    def up(self, num=10):
        self.vy = -num

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
        # draw.rect(self.scr, (100,100,100), Rect(self.x, self.y, self.r, self.r))
        self.scr.blit(self.img, (self.x, self.y))
