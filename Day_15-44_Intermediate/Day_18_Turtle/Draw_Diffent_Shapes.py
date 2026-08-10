import random
from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')

colors = ['red', 'blue', 'orange', 'green', 'yellow','brown', 'grey']


def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)


for shape in range(3, 11):
    print(shape)
    color = random.choice(colors)
    turtle.pencolor(color)
    draw_shapes(shape)


screen = Screen()
screen.exitonclick()