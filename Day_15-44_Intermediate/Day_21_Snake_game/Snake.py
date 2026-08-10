import time
from turtle import Turtle, Screen

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.wall()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position=position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def wall(self):
        wall = Turtle()
        wall.hideturtle()
        wall.color('white')
        wall.penup()
        wall.goto(x=-290, y=-290)
        wall.pendown()
        wall.goto(x=290, y=-290)
        wall.goto(x=290, y=290)
        wall.goto(x=-290, y=290)
        wall.goto(x=-290, y=-290)

    def extend(self):
        position = self.segments[-1].position()
        self.add_segment(position=position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].setposition(x=new_x, y=new_y)

        self.head.forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
