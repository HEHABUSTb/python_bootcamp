import random
from turtle import Turtle
POSITIONS = [(-350, 0), (350, 0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddles()
        self.wall()
        self.speed = 25

    def create_paddles(self):
        for position in POSITIONS:
            paddle = Turtle(shape="square")
            paddle.shapesize(stretch_wid=3.5, stretch_len=0.08)
            paddle.color("white")
            paddle.penup()
            paddle.goto(position)
            self.paddles.append(paddle)

    def wall(self):
        wall = Turtle()
        wall.hideturtle()
        wall.color('white')
        wall.penup()
        wall.goto(x=300, y=300)
        wall.pendown()
        wall.goto(x=300, y=300)
        wall.goto(x=300, y=300)
        wall.goto(x=300, y=300)
        wall.goto(x=300, y=300)

    def move_left_paddle_down(self):
        new_x = self.paddles[0].xcor()
        new_y = self.paddles[0].ycor()
        if new_y > -260:
            new_y -= self.speed
        self.paddles[0].goto(x=new_x, y=new_y)

    def move_left_paddle_up(self):
        new_x = self.paddles[0].xcor()
        new_y = self.paddles[0].ycor()
        if new_y < 260:
            new_y += self.speed
        self.paddles[0].goto(x=new_x, y=new_y)

    def move_right_paddle_up(self):
        new_x = self.paddles[1].xcor()
        new_y = self.paddles[1].ycor() + self.speed
        self.paddles[1].goto(x=new_x, y=new_y)

    def move_right_paddle_down(self):
        new_x = self.paddles[1].xcor()
        new_y = self.paddles[1].ycor() - self.speed
        self.paddles[1].goto(x=new_x, y=new_y)

