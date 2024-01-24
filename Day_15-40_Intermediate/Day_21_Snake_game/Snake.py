import time
from turtle import Turtle, Screen

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        segment_1 = Turtle(shape='square')
        segment_1.color('white')
        segment_1.penup()
        self.segments.append(segment_1)

        for x_correction in 20, 40:
            segment = segment_1.clone()
            x = segment_1.xcor() - x_correction
            segment.setposition(x=x, y=segment_1.ycor())
            self.segments.append(segment)

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
