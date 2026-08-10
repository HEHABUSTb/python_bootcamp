import random
import time
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape()

colors = ['red', 'blue', 'orange', 'green', 'yellow', 'brown', 'grey', 'purple', 'aquamarine', 'dark blue', 'medium purple']

turtle.speed(8)
turtle.pensize(15)

rotation = [0, 90, 180, 270]
for _ in range(0, 100):
    angle = random.choice(rotation)
    color = random.choice(colors)
    turtle.color(color)
    turtle.forward(20)
    turtle.setheading(angle)


screen = Screen()
screen.exitonclick()