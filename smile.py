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


class Missile(f1.Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        f1.Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            audio = pyglet.media.load("sound2.mp3")
            audio.play()
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):

        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor() < -290 or self.xcor() > 290 or \
                self.ycor() < -290 or self.ycor() > 290:
            self.goto(-1000, 1000)
            self.status = "ready"


class Game():
    def __init__(self):
        self.pen = turtle.Turtle()

    def draw_border(self):
        # Draw border
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


game = Game()
game.draw_border()

# Create my sprites
player = Player("triangle", "black", 0, 0)
enemy = Enemy("circle", "yellow", -100, 0)
missile = Missile("triangle", "orange", 0, 0)

particles = []
for i in range(20):
    particles.append(Particle("circle", "red", 0, 0))

# Keyboard binds
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

    if player.is_collision(enemy):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        enemy.goto(x, y)

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
