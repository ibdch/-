import turtle

# Создание первого класса  на который будут опираться дочерние.
# в нем отмечены все переменные, которые необходимы для создания фигур
#Конструктор класса – метод __init__() В объектно-ориентированном программировании конструктором
# класса называют метод, который автоматически вызывается при создании объектов.
class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1
# Движение фигур. Если фигура пересекает границу, то она меняет направление разворачиваясь на 60 градусов
    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)
# Столкновение. Если центры фигур находятся на расстоянии 20, то  это воспринимается как столкновение
    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False