import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
screen.listen()
screen.onkeypress(fun=turtle.move_forward, key='w')

cars = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create random cars
    cars.create_car()

    # move cars
    cars.move_cars()

    # Detect collision
    for car in cars.cars:
        if turtle.turtle.distance(car) < 20:
            print('game over')

    if turtle.turtle.ycor() > 280:
        turtle.turtle.goto((0, -280))
        print('Level UP')
