import time
from turtle import Screen
from Snake import Snake
from Food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.title('My Snake game!')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=snake.left, key='Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)

    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()

        score.score += 1
        score.update_score()

        snake.add_segment()




screen.exitonclick()
