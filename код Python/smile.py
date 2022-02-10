# -*- coding: utf-8 -*-

import random
import turtle
import time
import pyglet
import f1
from f2 import Player, Enemy, Particle


turtle.speed(0)
turtle.bgcolor("black")
turtle.bgpic("nebo.gif")
turtle.title("Sun-killer by Вагина Оксана,Серикова Дарья, Кушманов Евгений, Бурханов Руслан")
turtle.ht()  # скрывает черепаху
turtle.setundobuffer(1)  # буфер отмены действий
turtle.tracer(0)  # обновляет экран

# Дочерний класс Missile родительского класса Sprite. Наследует атрибуты родительского класса, создает свои значения для
# длины и ширины фигуры,скорости и статуса. А так же меняет расположение за края игрового поля
class Missile(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)
# Стрельба. С использованием библиотеки pyglet. Здесь значение расположения меняется на место Самолета и изменяется статус
    def fire(self):
        if self.status == "ready":
            audio = pyglet.media.load("sound2.mp3")
            audio.play()
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"
# Движение в случае столкновения с краем игрового поля. Пуля принимает изначальный статус и положение за границами игры
    def move(self):

        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor() < -290 or self.xcor() > 290 or \
                self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"

# Класс Game. Необходим для создания границы игры. Происходит рисунок линии на опрделенное расстояние,
# далее поврот на 90 градусов и так 4 раза
class Game():
    def __init__(self):
        self.pen = turtle.Turtle()

    def draw_border(self):

        self.pen.speed(0)
        self.pen.color("black")
        self.pen.pensize(2)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.goto(-290, -300)
        self.pen.write("Вагина Оксана, Серикова Дарья, Бурханов Руслан и Кушманов Евгений", move=False, align="left",
                       font=("Candara", 14, "normal"))


game = Game()
game.draw_border()

# Создание каждой из фигур на игровом поле
player = Player("triangle", "black", 0, 0)
enemy = Enemy("circle", "yellow", -100, 0)
missile = Missile("triangle", "orange", 0, 0)

particles = []
for i in range(20):
    particles.append(Particle("circle", "red", 0, 0))

# Повороты Самолета при нажатии клавиш
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()  # сбор инфы с клавиш на ключ

while True:
    turtle.update()
    player.move()
    enemy.move()
    missile.move()
    time.sleep(0.03)
# Действие солнца после столкновения - переход на новые рандомные координаты
    if player.is_collision(enemy):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        enemy.goto(x, y)
# Попадание пули в солнце. Появление лучей летящих в различные стороны от середины солнца.
    if missile.is_collision(enemy):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        enemy.goto(x, y)
        missile.status = "ready"
        for particle in particles:
            particle.goto(missile.xcor(), missile.ycor())
            particle.setheading(random.randint(0, 360))

    for particle in particles:
        particle.move()
