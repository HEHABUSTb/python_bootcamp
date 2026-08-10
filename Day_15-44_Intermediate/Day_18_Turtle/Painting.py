import random
from Extract_colors import extract_colors
import turtle as turtle_module


turtle_module.colormode(255)

colors = extract_colors()
turtle = turtle_module.Turtle()
turtle.speed(10)
turtle.hideturtle()

x = -250
y = -250

for _ in range(10):

    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for _ in range(10):
        color = random.choice(colors)
        turtle.dot(20, color)

        turtle.penup()
        turtle.forward(50)
        turtle.pendown()
    y += 50




screen = turtle_module.Screen()
screen.screensize(100, 100)
screen.exitonclick()