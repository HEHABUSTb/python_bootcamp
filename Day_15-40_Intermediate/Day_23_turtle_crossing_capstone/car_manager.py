import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        i = random.randint(0, 4)
        if i == 0:
            color = random.choice(COLORS)
            random_y = random.randint(-300, 300)

            car = Turtle(shape='square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(color)
            car.goto(x=320, y=random_y)

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.back(self.move_distance)






    def speed_up(self):
        self.move_distance += MOVE_INCREMENT