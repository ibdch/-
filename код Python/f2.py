import f1
import random

# Дочерний класс Player родительского класса Sprite. Он наследует атрибуты родительского класса,
# а так же принимает значения для размера фигур и скорости. Дальше расписаны повороты самолета
# на 45 градусов и изменение скорости при нажатии клавиши
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

# Дочерний класс Enemy родительского класса Sprite. Он так же наследует
# атрибуты с родительского класса и задает значения для формы фигуры, скорости и направления движения
class Enemy(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.speed = 1
        self.setheading(random.randint(0, 360))

# Дочерний класс Particle родительского класса Sprite. Он так же наследует
# атрибуты с родительского класса и задает значения для формы фигуры, скорости и направления движения.
# Данный класс определяет положение для фигуры и отмечает за пределами игрового поля, чтобы изначально его не было видно
class Particle(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0
# Взрыв. Частицы взрыва появляются в центре солнца и разлетаются в рандомном напрвлении
    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
# Движение частиц
    def move(self):
        self.fd(10)
