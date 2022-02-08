import f1
import random


class Player(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Particle(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(10)
