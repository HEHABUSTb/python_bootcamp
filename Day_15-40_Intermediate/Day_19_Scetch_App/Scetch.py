from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def forward():
    turtle.forward(10)


def back():
    turtle.back(distance=10)


def left_turn():
    angle = turtle.heading()
    turtle.setheading(angle + 10)


def right_turn():
    angle = turtle.heading()
    turtle.setheading(angle - 10)


def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.setposition(x=0, y=0)
    turtle.setheading(to_angle=0)
    turtle.pendown()


screen.listen()
screen.onkey(key='w', fun=forward)
screen.onkey(key='s', fun=back)
screen.onkey(key='a', fun=left_turn)
screen.onkey(key='d', fun=right_turn)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
