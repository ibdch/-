import random
import turtle
import time
import pyglet

turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.bgpic("nebo.gif")
turtle.title("Sun-killer by Вагина Оксана,Серикова Дарья, Кушманов Евгений, Бурханов Руслан")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

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

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False


class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=2, stretch_len=2, outline=None)
        self.speed = 6
        self.setheading(random.randint(0, 360))


class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            audio = pyglet.media.load("sound.mp3")
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


class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.3, stretch_len=1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(10)


class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        # Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
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
turtle.listen()


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
