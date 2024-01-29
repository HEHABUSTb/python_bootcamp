import random
from turtle import Turtle
SPEED = [-3, -2, -1, 1, 2, 3]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')

        self.move_x = random.choice(SPEED)
        self.move_y = random.choice(SPEED)

    def random(self):
        self.move_x = random.choice(SPEED)
        self.move_y = random.choice(SPEED)

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)

    def bounce_from_wall(self):
        self.move_y *= -1

    def bounce_from_paddle(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.random()
