from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle = self.create_player()

    def create_player(self):
        turtle = Turtle(shape='turtle')
        turtle.penup()
        turtle.color('black')
        turtle.setheading(to_angle=90)
        turtle.goto(STARTING_POSITION)

        return turtle

    def move_forward(self):
        self.turtle.forward(MOVE_DISTANCE)
