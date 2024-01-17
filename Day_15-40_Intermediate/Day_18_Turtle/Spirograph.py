import random
import time
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape()

colors = ['red', 'blue', 'orange', 'green', 'yellow', 'brown', 'grey', 'purple', 'aquamarine', 'dark blue', 'medium purple']
radius = 100
angle = 5
i = int(360 / angle)

turtle.speed(13)
turtle.pensize(4)


for _ in range(i):
    color = random.choice(colors)
    turtle.color(color)

    turtle.circle(radius)
    turtle.right(angle)








screen = Screen()
screen.exitonclick()