from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')


"""
for _ in range(4):
    turtle.forward(100)
    turtle.left(90)
"""

for _ in range(15):
    turtle.forward(15)
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()




screen = Screen()
screen.exitonclick()