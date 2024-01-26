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
    time.sleep(0.15)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()

        score.score += 1
        score.update_score()

        snake.extend()

    # Detect collision with wall
    head_x = snake.head.xcor()
    head_y = snake.head.ycor()
    if head_x > 280 or head_x < -280 or head_y > 280 or head_y < -280:
        game_is_on = False
        score.game_over_message()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over_message()




screen.exitonclick()
